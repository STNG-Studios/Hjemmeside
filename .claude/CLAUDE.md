# STNG Studios Hjemmeside — Projektinstruktioner

## Commit-konventioner (VIGTIGT)

Alle commits lavet af Claude Code **SKAL** bruge `[AI]`-prefix i commit-beskeden.

Format:
```
[AI] Kort beskrivelse af ændringen

Detaljeret beskrivelse hvis nødvendigt.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

Eksempler:
- `[AI] Tilføj grundlæggende HTML-struktur til index.html`
- `[AI] Implementer responsiv navigation`
- `[AI] Fix styling-fejl i kontaktformular`

## Clarifying Questions (OBLIGATORISK)

Det er obligatorisk at stille afklarende spørgsmål ("clarifying questions") før implementering af nye features eller større ændringer. Dette sikrer:
- Ingen misforståelser mellem Simon og Claude
- At implementeringen følger best practice
- At det præcis er det ønskede resultat der leveres

Claude **skal** altid stille relevante spørgsmål om uklare krav, designvalg og tekniske detaljer **før** kodning begynder.

## Kontekst

Dette er et skoleprojekt for STNG Studios ApS. Al brug af AI skal dokumenteres, da censor skal kunne se præcis hvad AI har lavet og ændret.

- **`[AI]`-commits:** Lavet med hjælp fra Claude Code
- **`[MANUAL]`-commits:** Lavet af Simon uden AI

## Sprog

Projektet er på dansk. Commit-beskeder og kommentarer skrives på dansk.

## Session-nummer (VIGTIGT)

Ved starten af hver session **skal Simon oplyse session-nummer og dato** (f.eks. "Session 003, 2026-02-08"). Claude bruger dette til at generere korrekte filreferencer i inline-kommentarer.

Hvis Simon ikke har oplyst session-nummer, **spørg efter det** før du begynder at skrive kode.

## Inline-kommentarer i koden (VIGTIGT)

Projektet afleveres som en ZIP-fil — censor har **ikke** adgang til `git log` eller `git diff`. Derfor skal al AI-skrevet kode markeres med inline-kommentarer, så censor kan spore hvad AI har lavet.

### Regler

1. **Tilføj en kommentar ved toppen af hver logisk blok** som AI har skrevet eller ændret
2. Kommentaren skal indeholde en **kort beskrivelse** af hvad blokken gør + en **reference til samtalefilen**
3. Brug det korrekte kommentar-format for filtypen:

**HTML:**
```html
<!-- Beskrivelse. Lavet med AI, kig i documentation/samtaler/session-NNN_DATO.md -->
```

**CSS:**
```css
/* Beskrivelse. Lavet med AI, kig i documentation/samtaler/session-NNN_DATO.md */
```

**JavaScript:**
```js
// Beskrivelse. Lavet med AI, kig i documentation/samtaler/session-NNN_DATO.md
```

### Eksempler

```html
<!-- Responsiv navigation med hamburger-menu. Lavet med AI, kig i documentation/samtaler/session-002_2026-02-07.md -->
<nav class="main-nav">
  ...
</nav>
```

```css
/* Flexbox-layout til produktkort. Lavet med AI, kig i documentation/samtaler/session-003_2026-02-08.md */
.product-grid {
  display: flex;
  ...
}
```

### Hvornår kommentarer IKKE er nødvendige

- Rene whitespace-ændringer eller formatering
- Ændringer på én enkelt linje (f.eks. rettelse af en stavefejl)
- Filer i `documentation/`-mappen (de er selv dokumentation)

## Auto-dokumentation (VIGTIGT)

Projektet afleveres som ZIP-fil. Claude **skal automatisk** vedligeholde dokumentationen under hver session, så censor kan læse alt uden git.

### Ved sessionens START

1. Simon oplyser session-nummer og dato (f.eks. "Session 003, 2026-02-08")
2. Hvis Simon ikke oplyser det, **spørg efter det** før du begynder

### Løbende under sessionen

Hold styr på ALLE filer du opretter, redigerer eller sletter. Notér:
- Filnavn og handling (oprettet/redigeret/slettet)
- Kort beskrivelse af hvad der blev ændret
- Relevante linjenumre for større ændringer

### Ved sessionens SLUTNING (når Simon beder om det, eller før sidste commit)

Opdatér automatisk disse tre filer:

**1. Ændringsfil** — `documentation/ai-aendringer/session-NNN_DATO.md`:
```markdown
# AI-ændringer — Session NNN (DATO)

## Resumé
2-3 sætninger om formål og resultat.

## Ændrede filer
| Fil | Handling | Beskrivelse |
|-----|----------|-------------|
| `filnavn` | Oprettet/Redigeret/Slettet | Kort beskrivelse |

## Detaljerede ændringer
### `filnavn` (handling)
- Hvad der blev ændret (linje X-Y)
- Endnu en ændring

## AI's rolle
Hvad Simon bad om, og hvad Claude besluttede/implementerede.
```

**2. Sessionstabel** — tilføj en ny række i `documentation/README.md`:
```
| NNN | DATO | Kort beskrivelse | [samtale](samtaler/session-NNN_DATO.md) | [ændringer](ai-aendringer/session-NNN_DATO.md) |
```

**3. Oversigt** — tilføj en ny sessionsblok i `documentation/oversigt.md`:
```markdown
## Session NNN — DATO
**Formål:** ...
**Hvad blev lavet:** ...
**AI's rolle:** ...
```

### Hvad Claude IKKE kan gøre automatisk

**Samtale-eksport** — Simon kører slash-kommandoen `/eksporter` efter sessionen:
```
/eksporter NNN DATO
```
Kommandoen finder automatisk session-ID'et og kører eksport-scriptet. Simon committer manuelt bagefter.
