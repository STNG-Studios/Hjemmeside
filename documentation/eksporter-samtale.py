#!/usr/bin/env python3
"""
Eksportér en Claude Code-samtale fra JSONL-logfil til læsbar Markdown.

Brug:
    python3 eksporter-samtale.py <session-id> <output-fil>

Eksempel:
    python3 eksporter-samtale.py 86fefbbf-93eb-4bb4-9bf8-4ff925b3b136 documentation/samtaler/session-001_2026-02-07.md

Session-ID'et finder du i filnavnet under:
    ~/.claude/projects/<projekt-sti>/<session-id>.jsonl
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime


def find_jsonl_file(session_id):
    """Find JSONL-filen for en given session."""
    claude_dir = Path.home() / ".claude" / "projects"
    if not claude_dir.exists():
        print(f"Fejl: Claude-projektmappe ikke fundet: {claude_dir}")
        sys.exit(1)

    # Søg i alle projektmapper
    for project_dir in claude_dir.iterdir():
        if project_dir.is_dir():
            jsonl_file = project_dir / f"{session_id}.jsonl"
            if jsonl_file.exists():
                return jsonl_file

    print(f"Fejl: Kunne ikke finde JSONL-fil for session {session_id}")
    print(f"Søgte i: {claude_dir}")
    sys.exit(1)


def extract_text_content(content):
    """Udtræk tekstindhold fra en besked."""
    if isinstance(content, str):
        return content

    parts = []
    if isinstance(content, list):
        for block in content:
            if isinstance(block, dict):
                if block.get("type") == "text":
                    text = block.get("text", "").strip()
                    if text:
                        parts.append(text)
                elif block.get("type") == "tool_use":
                    tool_name = block.get("name", "ukendt")
                    tool_input = block.get("input", {})
                    # Vis relevante tool-kald kortfattet
                    if tool_name == "Write":
                        path = tool_input.get("file_path", "")
                        parts.append(f"*[Opretter fil: `{path}`]*")
                    elif tool_name == "Edit":
                        path = tool_input.get("file_path", "")
                        parts.append(f"*[Redigerer fil: `{path}`]*")
                    elif tool_name == "Read":
                        path = tool_input.get("file_path", "")
                        parts.append(f"*[Læser fil: `{path}`]*")
                    elif tool_name == "Bash":
                        cmd = tool_input.get("command", "")
                        desc = tool_input.get("description", "")
                        label = desc if desc else cmd[:80]
                        parts.append(f"*[Kører kommando: `{label}`]*")
                    elif tool_name == "Glob":
                        pattern = tool_input.get("pattern", "")
                        parts.append(f"*[Søger efter filer: `{pattern}`]*")
                    elif tool_name == "Grep":
                        pattern = tool_input.get("pattern", "")
                        parts.append(f"*[Søger i kode: `{pattern}`]*")
                    elif tool_name == "Task":
                        desc = tool_input.get("description", "")
                        parts.append(f"*[Starter underopgave: {desc}]*")
                    else:
                        parts.append(f"*[Bruger værktøj: {tool_name}]*")
                elif block.get("type") == "tool_result":
                    # Spring tool-resultater over (for korthed)
                    pass
                elif block.get("type") == "thinking":
                    # Spring thinking-blokke over
                    pass
    return "\n\n".join(parts)


def parse_jsonl(jsonl_path):
    """Parse JSONL-fil og udtræk samtalen."""
    messages = []
    seen_content = set()

    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            entry_type = entry.get("type")

            # Spring progress-entries og snapshots over
            if entry_type in ("progress", "file-history-snapshot"):
                continue

            if entry_type == "user":
                msg = entry.get("message", {})
                content = msg.get("content", "")
                text = extract_text_content(content)
                if text and text not in seen_content:
                    seen_content.add(text)
                    timestamp = entry.get("timestamp", "")
                    messages.append({
                        "role": "bruger",
                        "content": text,
                        "timestamp": timestamp,
                    })

            elif entry_type == "assistant":
                msg = entry.get("message", {})
                content = msg.get("content", [])
                text = extract_text_content(content)
                if text and text not in seen_content:
                    seen_content.add(text)
                    timestamp = entry.get("timestamp", "")
                    messages.append({
                        "role": "assistent",
                        "content": text,
                        "timestamp": timestamp,
                    })

    return messages


def format_timestamp(ts):
    """Formatér ISO-timestamp til læsbar dansk tid."""
    if not ts:
        return ""
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return dt.strftime("%H:%M:%S")
    except (ValueError, AttributeError):
        return ""


def write_markdown(messages, output_path, session_id):
    """Skriv samtalen som Markdown."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Samtale — Session {session_id[:8]}...\n\n")
        f.write(f"**Eksporteret:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"**Fuld session-ID:** `{session_id}`\n\n")
        f.write("---\n\n")

        for msg in messages:
            time_str = format_timestamp(msg["timestamp"])
            time_label = f" ({time_str})" if time_str else ""

            if msg["role"] == "bruger":
                f.write(f"## Simon{time_label}\n\n")
            else:
                f.write(f"## Claude{time_label}\n\n")

            f.write(msg["content"])
            f.write("\n\n---\n\n")

    print(f"Samtale eksporteret til: {output_path}")
    print(f"Antal beskeder: {len(messages)}")


def main():
    if len(sys.argv) < 3:
        print("Brug: python3 eksporter-samtale.py <session-id> <output-fil>")
        print()
        print("Find session-ID'er med:")
        print("  ls ~/.claude/projects/*/")
        sys.exit(1)

    session_id = sys.argv[1]
    output_path = sys.argv[2]

    # Find JSONL-filen
    jsonl_path = find_jsonl_file(session_id)
    print(f"Fandt logfil: {jsonl_path}")

    # Parse samtalen
    messages = parse_jsonl(jsonl_path)
    if not messages:
        print("Advarsel: Ingen beskeder fundet i logfilen.")
        sys.exit(1)

    # Opret output-mappe hvis den ikke eksisterer
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    # Skriv Markdown
    write_markdown(messages, output_path, session_id)


if __name__ == "__main__":
    main()
