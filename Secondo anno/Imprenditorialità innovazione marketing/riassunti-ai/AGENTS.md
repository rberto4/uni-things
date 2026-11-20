# AGENTS

## Obiettivo del repository
- Preparare riassunti per l’esame di *Imprenditorialità, innovazione e marketing*.
- Fonte unica e vincolante: `libro.pdf`.
- Non usare fonti esterne o conoscenza non verificabile dal PDF.

## Regole non negoziabili
- Riassumere **solo** i capitoli/pagine richiesti.
- Scrivere in italiano, stile accademico, chiaro/concisione/completezza.
- Non inventare contenuti, esempi, definizioni, dati o citazioni.
- Ogni sezione deve essere MOLTO BEN argomentata e completa, non indicarmi solo i punti salienti in forma di lista. DEVE ESSERE UN VERO E PROPRIO RIASSUNTO, NON UN ELENCO PUNTATO. (Esempio, se ci sono 3 punti da trattare, non fare 3 elenchi puntati, ma fai 3 paragrafi ben argomentati e completi)
- Scrivere in forma assertiva e autoriale, senza meta-riferimenti al supporto di studio: evitare formule come "nel capitolo", "nel testo", "nel libro c'e scritto"; esporre direttamente i contenuti (es. "L'imprenditorialita presenta...").
- Coprire esplicitamente i riferimenti istituzionali e di policy citati nelle pagine assegnate (es. OCSE/OECD, DTI, UE, report e programmi), indicando la loro tesi/contributo sostanziale.
- Nei case study non limitarsi alla menzione: riportare in modo argomentato contesto, attori, strategia, passaggi causali, dati numerici rilevanti ed esito.
- Prima di consegnare ogni riassunto, fare un controllo copertura rispetto a "Contents" e sottosezioni del range assegnato, per evitare omissioni di concetti, attori o riferimenti chiave.
- Non è una mera traduzione ma devi cercare di mantenere almeno il 80% del contenuto originale, quindi non parafrasare troppo.
- Quando si indicano definizioni formali o spiegazioni tecniche, assicurati di riportarle correttamente.
- Quando si usa un inglesismo, un modo di dire o un termine tecnico, assicurati di riportarlo correttamente con la propria traduzione italiana e spiegazione tra parentesi.
- Se ci sono formule matematiche, assicurati di riportarle correttamente in LaTeX.
- Salvare i riassunti in markdown dentro `riassunti/`.
- Il file markdown deve essere ottimizzato per l'uso su Obsidian o Notion.
- Dopo ogni capitolo completato, aggiornare `TODO.md` (capitoli/pagine completate e rimanenti).

## Capitoli e pagine autorizzate
- Capitolo 1 — *Introduction: Context, issues and case study selection*
  - Libro: 1-13
  - PDF: 28-40
- Capitolo 2 — *Contributions of entrepreneurial firms*
  - Libro: 15-29
  - PDF: 41-56
- Capitolo 5 — *‘Types’ of entrepreneurs I: Habitual entrepreneurs*
  - Libro: 75-94
  - PDF: 102-121
- Capitolo 6 — *‘Types’ of entrepreneurs II: High technology and academic entrepreneurs*
  - Libro: 95-111
  - PDF: 122-138
- Capitolo 7 — *‘Types’ of organisations I: Family firms*
  - Libro: 113-132
  - PDF: 140-159
- Capitolo 8 — *‘Types’ of organisations II: Corporate entrepreneurship*
  - Libro: 134-147
  - PDF: 161-174
- Capitolo 11 - External environmental context: Drivers and barriers
  - Libro: 175-193
  - PDF: 202-220
- Capitolo 12 - Entrepreneurial finance
  - Libro: 195-217
  - PDF: 222-244

## Workflow operativo (default)
1. Leggere da `libro.pdf` solo il range PDF del capitolo richiesto.
2. Produrre il riassunto in `riassunti/` (markdown, italiano accademico).
3. Aggiornare subito `TODO.md` al termine del capitolo.

## Quality gate obbligatorio (prima della consegna)
- Eseguire un controllo copertura 1:1 tra `Contents` del range e sezioni del riassunto: nessuna sottosezione deve restare implicita o assente.
- Verificare che riferimenti istituzionali/policy presenti nel range (es. OCSE/OECD, DTI, UE, report, programmi) siano esplicitati con sigla, nome esteso e contributo sostanziale.
- Verificare che ogni case study citato nel range sia trattato con: contesto, attori, strategia, passaggi causali, dati numerici rilevanti, esito e implicazioni.
- Verificare che il testo resti autoriale: eliminare formule meta-testuali ("nel capitolo", "nel testo", "il libro dice").
- Verificare che i termini tecnici in inglese siano accompagnati da traduzione/spiegazione in parentesi alla prima occorrenza.
- Verificare assenza di omissioni su blocchi comparativi e tabelle (es. contributi positivi vs barriere negative, pro vs contro, vantaggi vs svantaggi).
- Verificare coerenza fattuale: non introdurre inferenze non supportate dal range; se un dato non e nel range, non aggiungerlo.
- Se il capitolo risulta troppo sintetico per lo studio, ampliare prima i nessi causali e le parti applicative (casi/policy), non le frasi introduttive.

## Tool/skill da preferire
- Skill: `pdf`, `writing-plans`, `obsidian-markdown`.
- Dare priorità alle istruzioni verificabili nel repository rispetto a convenzioni generiche.

## Stato repository (as-is)
- File chiave: `AGENTS.md`, `TODO.md`, `libro.pdf`.
- Directory output: `riassunti/` (può partire vuota).
- Nessuna pipeline build/test/lint configurata nel repository.
