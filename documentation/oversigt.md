# Oversigt over AI-brug — STNG Studios Hjemmeside

Denne fil indeholder en kort, kronologisk beskrivelse af hver AI-session.

---

## Session 001 — 2026-02-07

**Formål:** Opsætning af AI-dokumentationssystem

**Hvad blev lavet:**
- Initialiseret git-repo med .gitignore og .gitattributes
- Oprettet commit-konventioner ([AI] og [MANUAL] prefix)
- Oprettet dokumentationsstruktur (denne mappe)
- Oprettet scripts til eksport af samtaler og diffs
- Oprettet README.md til censor med vejledning

**AI's rolle:** Claude Code opsatte hele dokumentationssystemet efter instruktion fra Simon.

---

## Session 002 — 2026-02-07

**Formål:** Tilpasning af dokumentationssystem til ZIP-aflevering + automatisering

**Hvad blev lavet:**
- Tilføjet regler for inline-kommentarer i `.claude/CLAUDE.md` så al AI-kode markeres med kommentarer der peger på samtalefiler
- Tilføjet regel om at Simon skal oplyse session-nummer ved start af hver session
- Tilføjet auto-dokumentationsregler i `.claude/CLAUDE.md` så Claude automatisk skriver ændringsfiler og opdaterer README/oversigt
- Omskrevet `documentation/README.md` så den guider censor uden at antage git-adgang
- Omdøbt "Diff"-kolonne til "Ændringer" i sessionstabellen
- Slettet `documentation/eksporter-diff.sh` (erstattet af Claudes auto-dokumentation)
- Slettet tom `session-001_2026-02-07.diff`-fil
- Erstattet tom session-001 ændringsfil med reel beskrivelse i nyt format
- Forenklet workflow i MEMORY.md fra 5 til 2 manuelle trin
- Oprettet ændringsfil for session 002

**AI's rolle:** Claude Code tilpassede hele dokumentationssystemet efter instruktion fra Simon. Systemet blev ændret fra git-baseret (kræver `git log`/`git diff`) til et selvstændigt system hvor Claude selv skriver ændringsfiler under sessionen. Det eneste manuelle trin der er tilbage er samtale-eksport (nu forenklet med `/eksporter`-kommandoen).

---

## Session 003 — 2026-02-07

**Formål:** Oprettelse af `/eksporter`-slash-command og opdatering af tilhørende dokumentation

**Hvad blev lavet:**
- Oprettet `.claude/commands/eksporter.md` — slash command der automatisk finder session-UUID og eksporterer samtalen
- Opdateret `.claude/CLAUDE.md` med reference til `/eksporter`-kommandoen
- Omskrevet `documentation/VEJLEDNING.md` med nye eksport-trin, eksempel og tjekliste
- Opdateret `documentation/README.md` værktøjsbeskrivelse
- Opdateret `documentation/oversigt.md` session 002-tekst
- Opdateret `MEMORY.md` workflow-trin

**AI's rolle:** Claude Code designede og implementerede `/eksporter`-kommandoen efter instruktion fra Simon, samt opdaterede al dokumentation der refererede til det gamle manuelle eksport-workflow.

---

## Session 004 — 2026-02-07

**Formål:** Oprettelse af komplet startside (index.html) for STNG Studios

**Hvad blev lavet:**
- Oprettet `index.html` med semantisk HTML5 (header, hero, app-sektion, founder's note, footer)
- Oprettet `css/style.css` med mobile-first dark theme baseret på brand-farver
- Oprettet `js/main.js` med jQuery-baseret interaktivitet (sticky navbar, hamburger-menu, auto-karrusel, scroll-animationer)
- Implementeret Open Graph meta tags og Schema markup (JSON-LD Organization)
- Tilføjet obligatorisk regel om clarifying questions i `.claude/CLAUDE.md`

**AI's rolle:** Claude Code stillede afklarende spørgsmål om design, karrusel-opførsel, navbar-stil og kontaktinfo. Derefter implementerede Claude hele startsiden inkl. responsive layout, billedkarrusel med auto-rotation, scroll-animationer (kun desktop) og SEO-optimering.

---

## Session 006 — 2026-02-08

**Formål:** Oprettelse af servicevilkår-side (vilkår for brug og privatlivspolitik)

**Hvad blev lavet:**
- Udfyldt `servicevilkår.html` (var tom fil) med komplet indhold: 8 vilkårs-sektioner i individuelle bokse
- Tilføjet nye `.terms-*` CSS-klasser i `css/style.css` med responsive overrides
- Layout ligner FAQ-siden men uden expand/collapse — alle bokse er altid synlige
- Punkt 5 (Databeskyttelse og Cookies) har underpunkter med bullet-liste

**AI's rolle:** Claude Code planlagde implementeringen og oprettede nye CSS-klasser for at undgå kobling til FAQ-klasserne. Alt indhold blev leveret af Simon og placeret i semantisk HTML5-struktur med korrekte ARIA-labels.

---

## Session 008 — 2026-02-08

**Formål:** Oprettelse af produkter-side (produkter.html) med app deep-dive showcase

**Hvad blev lavet:**
- Oprettet `produkter.html` med hero-sektion (placeholder til custom "exploding phone"-billede), tre feature-sektioner med eksisterende app-screenshots i alternerende layout, CTA-sektion og footer
- Tilføjet nye `.product-hero`, `.feature-row`, `.product-cta`, `.cta-button` CSS-klasser i `css/style.css` med responsive breakpoints
- Genbrugt designmønstre fra om-os (alternerende layout, wave-divider, scroll-animationer)
- Ingen ændringer nødvendige i JavaScript — eksisterende kode virker automatisk

**AI's rolle:** Claude Code brainstormede tre layout-tilgange med Simon og stillede afklarende spørgsmål om hero-design, billeder og CTA. Simon valgte "Apple Product Page"-stilen. Claude implementerede hele siden.

---

## Session 010 — 2026-02-09

**Formål:** Oprettelse af kontaktside (kontakt.html)

**Hvad blev lavet:**
- Oprettet `kontakt.html` med hero-sektion, generel kontaktinfo (email + sociale medier), team-kort (polaroid-stil) og footer
- Tilføjet nye `.contact-*` CSS-klasser i `css/style.css` med responsive breakpoints
- Genbrugt polaroid-kort design fra om-os.html og bølge-dividere fra øvrige sider
- Ingen ny JavaScript — eksisterende scroll-animationer og hamburger-menu virker automatisk

**AI's rolle:** Simon var i tvivl om hvad kontaktsiden skulle indeholde for ikke at se tom ud. Claude foreslog flere tilgange, og Simon valgte en løsning med generel kontaktinfo (email + SoMe) og polaroid-kort for co-founders — uden kontaktformular. Claude implementerede hele siden.
