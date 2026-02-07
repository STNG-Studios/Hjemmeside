# AI-dokumentation — STNG Studios Hjemmeside

## Til censor

Dette dokument giver overblik over al brug af AI (Claude Code) i dette projekt. Al kode lavet eller ændret af AI er sporbar via git-historik og samtalelogfiler.

## Sådan er dokumentationen opbygget

| Mappe/Fil | Indhold |
|-----------|---------|
| `samtaler/` | Eksporterede samtaler med Claude Code (Markdown) |
| `ai-aendringer/` | Git-diffs og opsummeringer for hver AI-session |
| `oversigt.md` | Løbende changelog med kort beskrivelse af hver session |
| Denne fil | Overblik og vejledning til censor |

## AI-sessioner

| # | Dato | Beskrivelse | Samtale | Diff |
|---|------|-------------|---------|------|
| 001 | 2026-02-07 | Opsætning af dokumentationssystem | [samtale](samtaler/session-001_2026-02-07.md) | [diff](ai-aendringer/session-001_2026-02-07.md) |

## Git-kommandoer til inspektion

Censor kan bruge følgende kommandoer til at inspicere ændringer:

```bash
# Se alle commits
git log --oneline

# Se kun AI-commits
git log --oneline --grep="\[AI\]"

# Se kun manuelle commits
git log --oneline --grep="\[MANUAL\]"

# Se fuld diff for én commit
git show <commit-hash>

# Se hvad AI har ændret mellem to commits
git diff <start-commit>..<slut-commit>

# Statistik: antal linjer ændret af AI
git log --grep="\[AI\]" --shortstat

# Statistik: antal linjer ændret manuelt
git log --grep="\[MANUAL\]" --shortstat
```

## Værktøjer brugt

- **Claude Code** (CLI) — Anthropics AI-kodningsassistent
- **Model:** Claude Opus 4.6
- **Samtaler eksporteret med:** `documentation/eksporter-samtale.py`
- **Diffs genereret med:** `documentation/eksporter-diff.sh`
