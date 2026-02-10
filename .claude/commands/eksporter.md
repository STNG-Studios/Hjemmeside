Eksportér den aktuelle samtale til Markdown-fil til dokumentation.

Argumenter (valgfrit): $ARGUMENTS

## Instruktioner

1. **Parse argumenter:** Hvis `$ARGUMENTS` indeholder to værdier (f.eks. `003 2026-02-08`), brug dem som session-nummer og dato. Hvis `$ARGUMENTS` er tomt, spørg Simon om session-nummer og dato.

2. **Find den nyeste JSONL-fil:** Kør denne kommando for at finde session-ID'et (UUID) for den nyeste samtale:
   ```
   ls -t ~/.claude/projects/-Users-simontrinderup-STNG-Studios-Hjemmeside/*.jsonl | head -1
   ```
   Udtræk UUID'et fra filnavnet (alt før `.jsonl`).

3. **Kør eksport-scriptet:** Brug Bash til at køre:
   ```
   python3 documentation/eksporter-samtale.py <UUID> documentation/samtaler/session-<NNN>_<DATO>.md
   ```
   Hvor `<NNN>` er session-nummeret (med ledende nuller, f.eks. `003`) og `<DATO>` er datoen.

4. **Vis resultatet:** Fortæl Simon at eksporten er færdig, og mind ham om at committe manuelt:
   ```
   git add documentation/samtaler/session-<NNN>_<DATO>.md
   git commit -m "[MANUAL] Dokumentation: tilføj samtale for session <NNN>"
   ```

## Vigtigt
- Brug ALTID det nyeste JSONL-fil som session-ID — det er den aktuelle samtale.
- Commit IKKE automatisk — Simon gør det selv med `[MANUAL]`-prefix.
