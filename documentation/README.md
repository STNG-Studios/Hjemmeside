# AI-dokumentation — STNG Studios Hjemmeside

## Til censor

Dette dokument giver overblik over al brug af AI (Claude Code) i dette projekt. Dokumentationen er designet til at fungere som en del af den afleverede ZIP-fil — du behøver ikke git eller andre værktøjer for at inspicere AI-brugen.

## Sådan sporer du AI-brugen (3 trin)

### 1. Inline-kommentarer i koden

Åbn en hvilken som helst kodefil (HTML, CSS, JS) og kig efter kommentarer med **"Lavet med AI"**. Hver kommentar beskriver hvad AI har lavet og refererer til en samtalefil:

```html
<!-- Responsiv navigation med hamburger-menu. Lavet med AI, kig i documentation/samtaler/session-002_2026-02-07.md -->
```

### 2. Samtaler — hvad blev diskuteret

Følg referencen i kommentaren til den tilhørende fil i `samtaler/`-mappen. Her kan du læse hele dialogen mellem Simon og Claude Code — hvad Simon bad om, og hvad AI svarede.

### 3. Kodeændringer — præcis hvad der blev ændret

For hver session findes der en ændringsfil i `ai-aendringer/`-mappen. Den beskriver:
- Hvilke filer der blev oprettet, redigeret eller slettet
- Detaljerede beskrivelser af ændringerne med linjenumre
- AI's rolle og beslutninger i sessionen

### Sporet visualiseret

```
Kode med kommentar       →  Samtalefil              →  Ændringsfil
─────────────────────        ──────────────────         ──────────────────
<!-- Nav menu.               Viser hvad Simon           Viser præcis
Lavet med AI, kig i          bad om og hvad             hvilke filer og linjer
session-002.md -->           Claude svarede             der blev ændret
```

## Mappestruktur

| Mappe/Fil | Indhold |
|-----------|---------|
| `samtaler/` | Eksporterede samtaler med Claude Code (Markdown) |
| `ai-aendringer/` | Beskrivelser af ændringer for hver AI-session |
| `oversigt.md` | Kronologisk changelog med kort beskrivelse af hver session |
| Denne fil | Overblik og vejledning til censor |

## AI-sessioner

| # | Dato | Beskrivelse | Samtale | Ændringer |
|---|------|-------------|---------|-----------|
| 001 | 2026-02-07 | Opsætning af dokumentationssystem | [samtale](samtaler/session-001_2026-02-07.md) | [ændringer](ai-aendringer/session-001_2026-02-07.md) |
| 002 | 2026-02-07 | Tilpasning af dokumentation til ZIP-aflevering + automatisering | [samtale](samtaler/session-002_2026-02-07.md) | [ændringer](ai-aendringer/session-002_2026-02-07.md) |
| 003 | 2026-02-07 | Oprettelse af `/eksporter`-slash-command + dokumentationsopdatering | [samtale](samtaler/session-003_2026-02-07.md) | [ændringer](ai-aendringer/session-003_2026-02-07.md) |
| 004 | 2026-02-07 | Oprettelse af komplet startside (index.html) med CSS, JS, OG tags, Schema markup | [samtale](samtaler/session-004_2026-02-07.md) | [ændringer](ai-aendringer/session-004_2026-02-07.md) |

## Værktøjer brugt

- **Claude Code** (CLI) — Anthropics AI-kodningsassistent
- **Model:** Claude Opus 4.6
- **Samtaler eksporteret med:** `/eksporter`-kommandoen i Claude Code (eller manuelt via `documentation/eksporter-samtale.py`)
- **Ændringsfiler:** Skrevet automatisk af Claude under sessionen
