# Vejledning — Sådan bruger du AI-dokumentationssystemet

Denne fil er til dig, Simon. Den forklarer præcis hvad du skal gøre for at dokumentationen bliver komplet efter hver AI-session.

---

## Overblik

| Hvem | Hvad | Hvornår |
|------|------|---------|
| **Simon** | Oplyser session-nummer og dato | Før sessionen |
| **Claude** | Skriver ændringsfil, opdaterer README og oversigt | Automatisk under sessionen |
| **Simon** | Eksporterer samtalen med `/eksporter` | Efter sessionen |
| **Simon** | Committer samtale-filen | Efter eksport |

Claude gør det meste automatisk. Du har **kun ét manuelt trin**: eksportér samtalen.

---

## Før sessionen

Når du starter en ny Claude Code-session, skal det **første du skriver** være:

```
Session NNN, DATO
```

Eksempel:
```
Session 005, 2026-02-10
```

Claude bruger dette til at navngive filer korrekt og referere til den rigtige samtalefil i inline-kommentarer. Hvis du glemmer det, vil Claude spørge dig.

**Husk:** Session-nummeret er det næste i rækken. Tjek `documentation/README.md` for at se hvad det seneste nummer var.

---

## Under sessionen

Du behøver ikke gøre noget. Claude håndterer automatisk:

1. **Inline-kommentarer** i al kode Claude skriver/ændrer
2. **Ændringsfil** i `documentation/ai-aendringer/session-NNN_DATO.md`
3. **Ny række** i sessionstabellen i `documentation/README.md`
4. **Ny blok** i `documentation/oversigt.md`

Hvis Claude glemmer noget af dette, kan du minde den om det ved at sige: "Husk at opdatere dokumentationen."

---

## Efter sessionen (det ene manuelle trin)

### Trin 1: Eksportér samtalen med `/eksporter`

Start en ny Claude Code-session (eller brug den samme) og skriv:

```
/eksporter NNN DATO
```

Eksempel:
```
/eksporter 005 2026-02-10
```

Claude finder automatisk session-ID'et (UUID) og kører eksport-scriptet for dig. Du behøver ikke selv finde UUID'et.

Hvis du bare skriver `/eksporter` uden argumenter, spørger Claude om session-nummer og dato.

### Trin 2: Commit

```bash
git add documentation/samtaler/session-NNN_DATO.md
git commit -m "[MANUAL] Dokumentation: tilføj samtale for session NNN"
```

### Alternativ: Manuel eksport

Hvis `/eksporter` ikke virker, kan du stadig køre scriptet manuelt:

```bash
# Find nyeste session-ID
ls -lt ~/.claude/projects/-Users-simontrinderup-STNG-Studions-Hjemmeside/*.jsonl | head -1

# Kør eksport med UUID'et fra kommandoen ovenfor
python3 documentation/eksporter-samtale.py SESSION_UUID documentation/samtaler/session-NNN_DATO.md
```

---

## Komplet eksempel: Session 005

Her er et komplet eksempel med en fiktiv session 005.

### 1. Start sessionen

Åbn Claude Code og skriv:
```
Session 005, 2026-02-10. Jeg vil have en responsiv navigation med hamburger-menu.
```

### 2. Arbejd med Claude

Claude implementerer navigationen og gør automatisk:
- Tilføjer inline-kommentarer i koden med reference til `session-005_2026-02-10.md`
- Skriver `documentation/ai-aendringer/session-005_2026-02-10.md`
- Opdaterer tabellen i `documentation/README.md`
- Opdaterer `documentation/oversigt.md`

### 3. Sessionen er slut — eksportér samtalen

Skriv i Claude Code:
```
/eksporter 005 2026-02-10
```

Claude finder automatisk session-ID'et og eksporterer samtalen til `documentation/samtaler/session-005_2026-02-10.md`.

### 4. Commit

```bash
git add documentation/samtaler/session-005_2026-02-10.md
git commit -m "[MANUAL] Dokumentation: tilføj samtale for session 005"
```

Færdig! Dokumentationen for session 005 er nu komplet.

---

## Tjekliste (brug denne efter hver session)

- [ ] Kørte jeg `/eksporter NNN DATO` i Claude Code?
- [ ] Committede jeg samtale-filen? (`git commit -m "[MANUAL] ..."`)
- [ ] Tjek: ligger samtale-filen i `documentation/samtaler/`?
- [ ] Tjek: har Claude opdateret `documentation/ai-aendringer/`?
- [ ] Tjek: er sessionstabellen i `documentation/README.md` opdateret?

---

## Hvor filerne ligger

```
documentation/
├── README.md                              ← Censors indgang (auto-opdateret)
├── oversigt.md                            ← Kronologisk log (auto-opdateret)
├── VEJLEDNING.md                          ← Denne fil (til dig)
├── eksporter-samtale.py                   ← Script til samtale-eksport
├── samtaler/
│   ├── session-001_2026-02-07.md          ← Eksporteret samtale
│   └── session-NNN_DATO.md               ← ...en fil per session
└── ai-aendringer/
    ├── session-001_2026-02-07.md          ← Ændringsbeskrivelse (auto)
    └── session-NNN_DATO.md               ← ...en fil per session
```

---

## Aktuel status

| Session | Samtale eksporteret? | Ændringsfil skrevet? |
|---------|---------------------|---------------------|
| 001 | Ja | Ja |
| 002 | **Nej — mangler!** | Ja |

**For at eksportere session 002:**
```bash
python3 documentation/eksporter-samtale.py ee949c35-bf88-4d72-85de-3480e44d9e4b documentation/samtaler/session-002_2026-02-07.md
git add documentation/samtaler/session-002_2026-02-07.md
git commit -m "[MANUAL] Dokumentation: tilføj samtale for session 002"
```
