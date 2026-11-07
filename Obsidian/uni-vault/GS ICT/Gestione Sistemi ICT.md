# Lezione 2 — Fondamenti dei sistemi informativi

## Che cos'è un sistema informativo
Il corso si colloca nell'ambito della **gestione dei sistemi ICT** (*Information and Communication Technology*), che riunisce due mondi storicamente distinti: l'**IT** (*Information Technology*, l'elaborazione dei dati) e le **TLC** (*Telecommunications*, la trasmissione). La definizione cardine da cui parte tutto è la seguente: ==un **sistema informativo** è l'insieme delle *procedure* e delle *infrastrutture* che definiscono e supportano il fluire delle *informazioni* all'interno di una struttura organizzativa==. È importante coglierne subito la natura ==non puramente tecnologica==: il sistema informativo non è "il computer" o "il software", ma l'intreccio organizzato di regole, strumenti e flussi che permette a un'azienda di trasformare dati grezzi in conoscenza utile e di farla arrivare alle persone giuste.
Concettualmente il sistema informativo ==vive fra tre poli==: le **infrastrutture** (i mezzi fisici), le **procedure** (le regole dinamiche) e le **informazioni / conoscenza** (il risultato che si vuole produrre). ==Il suo scopo è== duplice e va tenuto sempre presente perché orienta ogni scelta progettuale:
- **Guidare** l'esecuzione dei processi aziendali, cioè ==accompagnare l'operatore== passo passo nelle attività.
- **Presentare** le ==informazioni alle persone *nel momento in cui servono*==, né prima né dopo.
Per raggiungere questi obiettivi si definiscono procedure che svolgono due funzioni complementari: la **raccolta** dei dati in archivi organizzati e la loro **elaborazione** per trasformarli in informazioni. Il ciclo logico completo è quindi *raccolta dei dati → elaborazione dei dati → presentazione delle informazioni → guida dei processi*: i dati entrano, vengono lavorati, escono come informazioni e queste a loro volta indirizzano l'azione.

### Esempi che chiariscono la differenza dato/procedura/informazione
Due esempi rendono concreta l'astrazione. Nell'**acquisizione di un ordine cliente** la *procedura* guida l'operatore nell'inserimento: propone valori predefiniti, verifica l'ammissibilità dei dati e controlla che siano stati compilati tutti i campi necessari — qui la procedura "guida". Nella **gestione del magazzino**, invece, ogni prelievo o versamento di materiale viene memorizzato in un *archivio* (dati); quando serve conoscere la disponibilità di un articolo (*informazione*), una procedura calcola la giacenza in deposito partendo dai movimenti registrati — qui si vede la trasformazione dato→informazione. La lezione da trarre è che l'informazione non è un dato, ma il *risultato dell'elaborazione* dei dati.

## Le componenti del sistema informativo
Un sistema informativo è composto da tre famiglie di elementi: **dati**, **procedure** e **mezzi/strumenti**.
I **dati** sono la base del sistema: vanno strutturati e organizzati proprio per poterne estrarre informazioni. Si distinguono per natura in quattro tipi:
- **Di configurazione** — definiscono il contesto di funzionamento (es. l'esercizio corrente, la moneta d'esercizio).
- **Operativi** — registrano l'avanzamento delle attività (es. lo stato di avanzamento di una lavorazione).
- **Di supporto** — accompagnano il dato principale con informazioni accessorie (es. il nome del server Web tramite cui è arrivato l'ordine).
- **Di stato** — fotografano una grandezza a un certo istante (es. il fatturato aziendale alla data odierna).
Le **procedure** sono la porzione *dinamica* del sistema: specificano e attuano azioni, trasformano i dati, controllano, calcolano e distribuiscono le informazioni; sono ciò che "fa accadere le cose" (es. le procedure di acquisizione dati e di elaborazione delle informazioni). I **mezzi e strumenti** sono gli apparati per il trasferimento e il trattamento delle informazioni — gli apparati elettronici per acquisire dati, eseguire le procedure e distribuire i risultati. La distinzione fra questi tre piani non è accademica: confondere un dato con un'informazione o uno strumento con una procedura porta a progettare male il sistema.

## Le proprietà garantite: accessibilità e correttezza
Un buon sistema informativo deve garantire due proprietà fondamentali, che sono di fatto il suo metro di valutazione:
- **Accessibilità** all'informazione *nelle forme e nei tempi opportuni* — non basta che il dato esista, deve essere raggiungibile dalla persona giusta nel formato giusto al momento giusto.
- **Correttezza** del flusso delle informazioni — il dato deve transitare senza errori, duplicazioni o disallineamenti lungo tutto il percorso.
Queste due proprietà tornano costantemente: quasi tutti i problemi reali di un sistema informativo si possono ricondurre a una carenza di accessibilità (informazione frammentata, non reperibile in tempo) o di correttezza (errori, ridondanze, dati non sincroni).

## Il sistema informativo è dinamico
Un punto concettuale spesso sottovalutato: il sistema informativo **evolve nel tempo**, e la sua *complessità* tende a crescere. Non è un oggetto da progettare una volta e dimenticare. Le evoluzioni strutturali sono provocate da due categorie di fattori:
- **Fattori interni** all'azienda — la spinta a migliorare le prestazioni e a ottimizzare i processi.
- **Fattori esterni** all'azienda — vincoli imposti dall'esterno, come l'obbligo di trasferire dati in formato digitale richiesto dalle grandi aziende ai propri subfornitori.
La regola d'oro è che l'evoluzione deve avvenire in modo **armonico**, sviluppando al massimo la *complementarietà* e l'*integrazione* fra i diversi componenti: un sistema che cresce per aggiunte scoordinate diventa rapidamente ingestibile.

## Informatica aziendale: le macro aree di influenza
Con *informatica aziendale* si intende l'utilizzo concreto dei sistemi informativi in azienda. L'informatica influisce su quattro **macro aree**, che è utile vedere come quattro livelli crescenti di impatto, dall'operatività quotidiana fino alla strategia.
- **Di aiuto e guida operativi** — sostituisce la carta con strumenti elettronici e definisce procedure che guidano e facilitano i compiti esecutivi. In concreto introduce controlli sui flussi che guidano l'operatore, avvia controlli interattivi sui dati digitati e facilita la ricerca di informazioni su banche dati centralizzate. È il livello più "vicino al lavoro manuale".
- **Organizzativa** — influenza l'organizzazione del lavoro, dei processi e del fluire delle informazioni. Libera risorse da attività automatizzabili, richiede risorse con competenze diverse e spesso impone nuovi metodi di ottimizzazione dei flussi e nuove esigenze gestionali. Qui l'informatica non si limita a velocizzare, ma *ridisegna* come si lavora.
- **Di controllo** — tiene sotto controllo gli eventi aziendali in tempo reale analizzando i dati raccolti, con analisi quantitative sull'andamento dell'attività per attuare politiche di controllo e favorire il processo decisionale suggerendo azioni tempestive.
- **Strategica** — è il "sistema nervoso aziendale": memorizza i dati, supporta i processi di trasformazione e comunicazione e favorisce le opportunità legate a innovazioni di prodotto e di processo.
Il filo che lega le quattro aree è una progressione: si parte dall'automatizzare il singolo compito, si passa a riorganizzare il lavoro, poi a controllarlo in tempo reale, e infine a usarlo come leva strategica.

## Impatto: conoscenza dei fenomeni aziendali
Le persone che operano in azienda hanno bisogni di conoscenza *diversi*, e questa è una delle idee più importanti del capitolo: non esiste "l'informazione giusta" in assoluto, esiste quella giusta *per quel ruolo, in quel momento*. Le esigenze si differenziano lungo tre dimensioni.
- **Livello di astrazione** — il grado di sintesi delle informazioni. Possono essere *analitiche* (la composizione di un singolo ordine) oppure *sintetiche*, ottenute dall'elaborazione dei dati (il fatturato della società). Un operatore vuole il dettaglio, un dirigente vuole la sintesi.
- **Tempestività** — la velocità con cui le informazioni transitano. Si può aver bisogno di conoscere gli eventi *nel momento in cui si verificano* (l'insoluto di un cliente, per bloccare nuove spedizioni) oppure *su richiesta*, quando servono (l'analisi delle vendite a fine mese).
- **Livello di copertura** — la quantità di fenomeni analizzati e l'estensione temporale. Si va da una conoscenza su un *periodo ristretto* (l'operatore di produzione conosce solo i piani della giornata) a una *visione estesa e articolata su un periodo ampio* (il responsabile della pianificazione della produzione).

### I due flussi dell'informazione
L'informazione in azienda fluisce in due direzioni complementari, e capire entrambe è essenziale per progettare i flussi:
- **Orizzontalmente** — fra le varie aree aziendali, per definire e sincronizzare i processi operativi (es. definire la produzione in base agli ordini clienti aperti). È il coordinamento "tra pari".
- **Verticalmente** — lungo la scala dell'organigramma, per organizzare ed elaborare i dati operativi estraendone informazioni che servono a controllare l'andamento aziendale. È il flusso che "sale" dal dettaglio operativo verso la sintesi direzionale e "scende" come indirizzo.

## I processi classici trattati dai sistemi informativi
Storicamente i sistemi informativi aziendali si sono occupati di tre processi, che rappresentano anche tre obiettivi di valore crescente.
- **Sviluppo delle funzioni operative** — l'informatizzazione dei flussi operativi, che porta a ridurre il costo del lavoro (meccanizzazione, automazione), migliorare i processi (maggior definizione e omogeneità), *cambiare* i processi e aumentare la quantità e la qualità dei dati.
- **Pianificazione** — l'uso dei dati per una migliore definizione degli obiettivi, la conoscenza dello stato attuale dell'azienda e la visione della sua evoluzione temporale.
- **Controllo** — maggior tempestività nella rilevazione delle anomalie e feedback immediati sulle azioni (monitorando l'attività produttiva si capisce subito se il piano di produzione è in ritardo).

## Tecnologia come veicolo di cambiamento e il BPR
Il messaggio strategico del capitolo è che la tecnologia non è solo uno strumento per fare meglio le stesse cose, ma un **veicolo di cambiamento e innovazione** che agisce su quattro fronti: l'*organizzazione*, i *flussi*, le *modalità di trattamento dei dati* e la *comunicazione*. Da qui nasce il concetto di **Business Process Reengineering (BPR)**: l'idea che, *integrando l'innovazione tecnologica con l'innovazione organizzativa*, si ottenga un miglioramento delle performance. Il punto cruciale, e controintuitivo, è il "se non… altrimenti": se si introduce la tecnologia *senza* ripensare l'organizzazione, si automatizza l'inefficienza esistente e i benefici sono modesti; è solo combinando i due piani che si ottiene un salto di prestazioni.

## Evoluzione storica e cambiamenti organizzativi
L'evoluzione tecnologica dell'IT ha generato cambiamenti organizzativi profondi, distinguibili in due piani.
Sul piano dell'**organizzazione interna**:
- Riduzione dei ruoli impiegatizi, sostituiti da procedure automatiche.
- Riqualificazione di tutti i ruoli aziendali e riduzione dei ruoli di supporto.
- Revisione dei processi di front office.
- Revisione del modello organizzativo, con il passaggio chiave *da un'organizzazione per funzioni a una per processi*.
- Reperimento dettagliato delle informazioni su clienti e mercato.
Sul piano dell'**organizzazione esterna**:
- Contenimento delle dimensioni dell'azienda.
- Adozione di strutture reticolari, terziarizzazione e *outsourcing*.
Il passaggio "per funzioni → per processi" è la chiave di volta che prepara i capitoli successivi: i sistemi informativi moderni (e gli ERP in particolare) hanno senso proprio perché supportano una visione *per processi* trasversale alle funzioni aziendali.

## Esercizi applicativi
### Esercizio 1 — Classificare gli elementi del sistema informativo
L'esercizio chiede di assegnare ciascun elemento a una delle quattro categorie *dato / informazione / procedura / mezzo-strumento*, e serve proprio a fissare le distinzioni viste sopra. I criteri guida emersi dalle soluzioni sono: un **dato** è la registrazione di un evento elementare o un valore puntuale (ordine cliente n. 4587, prezzo unitario del prodotto A, data di consegna prevista, archivio anagrafico fornitori come base dati strutturata); un'**informazione** è il frutto di un'aggregazione o elaborazione (fatturato totale di marzo, report vendite per area, dashboard KPI); una **procedura** è una sequenza che guida, trasforma o controlla (procedura di inserimento cliente, regola di blocco spedizione, calcolo automatico IVA, procedura di backup); un **mezzo/strumento** è l'infrastruttura o l'applicazione tecnologica (server ERP, database MySQL, software di gestione magazzino). Il caso più istruttivo è "quantità disponibile = 12": è un **dato** (di stato), anche se calcolato a partire dai movimenti — il punto è che rappresenta lo *stato puntuale*, non un'aggregazione interpretativa.

### Esercizio 2 — Analisi di un sistema informativo aziendale
Il caso *Alfa Srl* (PMI commerciale di componenti elettronici) descrive una situazione tipicamente "non integrata": gli ordini arrivano via email, un impiegato li reinserisce a mano su un Excel condiviso, il magazzino aggiorna le giacenze su un *altro* Excel, la contabilità registra le fatture a fine mese con un software separato, e non esiste alcun sistema integrato — con la conseguenza di disallineamenti vendite/magazzino, errori di fatturazione, ritardi nelle consegne e difficoltà nel calcolare la marginalità mensile.
Scomponendo il caso secondo le componenti viste: i **dati** sono ordini clienti, giacenze, fatture, prezzi di vendita e costi dei prodotti; le **procedure** sono l'inserimento manuale degli ordini su Excel, l'aggiornamento manuale delle giacenze e la registrazione delle fatture a fine mese; i **mezzi/strumenti** sono email, file Excel condivisi, software contabile separato, PC e rete aziendale.
I **problemi** si leggono perfettamente attraverso le due proprietà fondamentali. Sull'*accessibilità*: informazioni distribuite su più strumenti, nessuna base dati unica, difficoltà a reperire dati aggiornati in tempo reale, nessuna visione integrata. Sulla *correttezza del flusso*: doppio inserimento dei dati, elevato rischio di errore umano, disallineamento vendite/magazzino, aggiornamento non sincrono e informazioni disponibili solo a posteriori (a fine mese).
Quanto ai **benefici** che l'informatica potrebbe portare, essi si distribuiscono sulle macro aree: sul piano *operativo* automazione dell'inserimento ordini, aggiornamento automatico delle giacenze e riduzione degli errori manuali; sul piano *organizzativo* integrazione tra reparti, definizione di flussi strutturati ed eliminazione della ridondanza informativa; sul piano *di controllo* report in tempo reale, monitoraggio dei ritardi e controllo della marginalità; e, indirettamente, sul piano *strategico* una migliore pianificazione e decisioni basate su dati affidabili. È il caso-scuola che motiva l'introduzione di un sistema integrato (l'ERP), tema dei capitoli successivi.

---
# Lezione 3 — Struttura dell'azienda e del suo sistema informativo

## Il concetto di esigenza informativa
La funzione primaria del sistema informativo è **aiutare e guidare chi fa funzionare l'azienda** attraverso la propria attività. Ma questo aiuto serve in aree diverse e con un *livello di astrazione che sale man mano che aumenta il livello decisionale*: l'idea centrale del capitolo è che non esiste un'unica "esigenza informativa", perché essa dipende dal tipo di attività da compiere. In particolare:
- I **livelli operativi** hanno bisogno di informazione *dettagliata e attuale*, perché agiscono nell'immediato sul singolo evento.
- I **livelli decisionali** hanno bisogno di informazione *sintetica*, perché ragionano su tendenze e aggregati.
Questo principio — più si sale nella scala decisionale, più l'informazione si sintetizza — è la chiave di lettura di tutta la lezione e prepara il modello che segue.

## La piramide di Anthony
Il successo di un'azienda poggia su tre pilastri: la **definizione degli obiettivi strategici**, la loro **traduzione in azioni concrete** e infine la loro **attuazione**. A questi tre pilastri corrispondono i tre livelli della **piramide di Anthony**, che ordina l'azienda dal vertice alla base e governa di conseguenza i flussi informativi: salendo si va verso informazioni *sintetiche*, scendendo verso informazioni *dettagliate*.

### Livello strategico
È il vertice: ha il ruolo di definire visione e strategia aziendali, pianificare nel lungo termine (investimenti, espansione, posizionamento competitivo) e monitorare le performance complessive. Vi operano figure come l'Amministratore Delegato (CEO), i Direttori Generali e il Consiglio di Amministrazione. Lavora con informazioni *molto sintetiche*.

### Livello tattico
È il livello intermedio: traduce le strategie aziendali in *piani operativi*, gestisce team e risorse per ottimizzare l'efficienza e monitora l'andamento delle attività riferendo ai vertici. Vi operano i Manager di Dipartimento, i Responsabili di area, i Supervisori e i coordinatori. È la "cerniera" che trasforma la strategia in operatività.

### Livello operativo
È la base: esegue le attività quotidiane, segue le procedure definite dai manager e raccoglie dati e feedback. Vi operano operai, tecnici, addetti a produzione/logistica/customer service/vendite dirette e impiegati operativi. Lavora con informazioni *analitiche e attuali*.
Un esempio rende viva la piramide: il livello strategico *decide di investire in nuove tecnologie* per aumentare la produzione; il tattico *pianifica l'acquisto dei macchinari, forma il personale e organizza i turni*; l'operativo *utilizza i macchinari, segue le nuove procedure e segnala i problemi*. Lo stesso schema vale per "ridurre i costi di produzione" o "decidere se cambiare strategia": ogni livello fa la sua parte sullo stesso obiettivo, a granularità diversa.

### Lo scambio di informazioni nella piramide
Il punto importante è che l'informazione non scorre in un solo verso, ma in *tre* direzioni.
- **Discendente (dall'alto verso il basso)** — il top management comunica obiettivi, strategie e direttive; i manager intermedi le trasformano in piani operativi dettagliati; gli operatori ricevono istruzioni precise su *cosa* fare e *come* eseguire i compiti.
- **Ascendente (dal basso verso l'alto)** — gli operatori segnalano problemi, inefficienze e suggerimenti ai manager intermedi; questi filtrano e strutturano le informazioni; il top management le usa per prendere decisioni strategiche basate su *feedback reali*. È il meccanismo per cui l'esempio "ridurre i costi" si chiude: l'operativo segnala nuovi problemi, il tattico valuta e riferisce, lo strategico decide se cambiare strategia.
- **Orizzontale** — fra manager di diversi dipartimenti e fra operatori di reparti diversi, che devono collaborare per garantire efficienza.

### I sistemi informativi associati a ciascun livello
A ogni livello della piramide corrispondono tipici sistemi informativi, e notare quali si ripetono aiuta a capire la trasversalità di alcuni strumenti.
- **Livello strategico** — DSS (*Decision Support Systems*), BI (*Business Intelligence*), ERP (*Enterprise Resource Planning*).
- **Livello tattico** — MIS (*Management Information Systems*), ERP, CRM (*Customer Relationship Management*).
- **Livello operativo** — TPS (*Transaction Processing Systems*), MES (*Manufacturing Execution Systems*), SCM (*Supply Chain Management*), ERP.
L'**ERP compare a tutti e tre i livelli**: è questo il segnale che si tratta del sistema "spina dorsale" che attraversa l'intera piramide, tema centrale dei capitoli successivi.

## I profili informativi
Incrociando i livelli di Anthony con le caratteristiche dell'informazione si ottengono i **profili informativi**, descritti su quattro dimensioni: la *frequenza* con cui serve l'informazione, il *tipo di dati*, la loro *provenienza* (interna o esterna all'azienda) e i *volumi*.
- **Livello direzionale strategico** — frequenza *sporadica*, dati *molto sintetici*, provenienza *interna ed esterna*, volumi *bassi*. Il vertice guarda raramente ma in profondità, e ha bisogno anche di dati che vengono da fuori (mercato, concorrenza).
- **Livello direzionale tattico** — frequenza *prefissata*, dati *sintetici e analitici*, provenienza *interna*, volumi *medi*. Il livello intermedio lavora a cadenze regolari su un mix di sintesi e dettaglio.
- **Livello operativo** — frequenza *continua*, dati *analitici*, provenienza *interna*, volumi *elevati*. La base macina di continuo grandi quantità di dati di dettaglio interni.
La logica è coerente con tutto il resto: più si sale, più rara è la consultazione, più sintetico il dato, più rilevante la fonte esterna e più piccolo il volume; più si scende, più tutto si inverte.

## La scomposizione del sistema informativo
Il sistema informativo aziendale si scompone in due grandi sottosistemi, in corrispondenza diretta con la piramide di Anthony.
- Il **sistema operazionale** è di supporto alle *attività* — copre funzioni come servizio clienti, acquisti, controllo qualità, magazzino, contabilità. Sta alla base (livello operativo) e produce *dati*.
- Il **sistema informazionale** è di supporto alle *decisioni* — aiuta nella ricerca di soluzioni a *problemi non strutturati*, cioè quelli per cui non è possibile fissare a priori una sequenza di passaggi elementari. Sta in cima (livello strategico) e si nutre anche di *dati da fonti esterne*.
I due sottosistemi sono collegati da un flusso a doppio senso: il sistema operazionale fornisce *dati* a quello informazionale, e quest'ultimo restituisce *direttive e piani* a quello operazionale. È la traduzione informatica dello scambio ascendente/discendente di Anthony.

## Sistemi operazionali e informazionali a confronto
### Sistemi operazionali
Le loro **funzioni principali** sono l'automazione di attività procedurali, la definizione di nuovi processi, l'aiuto nelle attività aziendali, la raccolta di dati per il controllo dell'attività operativa e la guida per l'operatore. Le **azioni sui dati** che li caratterizzano sono l'*accesso interattivo*, l'*elaborazione di informazioni attuali* e l'*aggregazione*. Le **componenti fondamentali** sono una *base di dati operazionale* e le *funzioni operative*.

### Sistemi informazionali
Le loro **funzioni principali** sono la facilitazione del processo decisionale, la presentazione dei dati e il confronto tra indicatori. Le **azioni sui dati** sono l'*accesso in sola lettura*, l'*aggregazione di dati*, le *ricerche per aree/temi*, la *profondità temporale* e la *multidimensionalità*. Le **componenti fondamentali** sono una *base di dati di tipo Data Warehouse*, gli *strumenti di analisi* e le *procedure di alimentazione* (che caricano il Data Warehouse a partire dai sistemi operazionali).

### Comparazione sistematica
Il confronto diretto fra i due tipi di sistema è il cuore concettuale del capitolo, perché spiega *perché* servono due sistemi distinti e non uno solo.
- **Finalità** — l'operazionale supporta l'*operatività*, l'informazionale supporta il *processo decisionale*.
- **Utenti** — molti e operativi nell'operazionale, pochi e direzionali nell'informazionale.
- **Dati** — analitici nell'operazionale (l'ordine x del cliente y), sintetici e solitamente numerici nell'informazionale (il fatturato mensile per categoria di cliente).
- **Modalità di utilizzo** — guidata, per processi e stati successivi, nell'operazionale; interrogazioni *ad hoc* nell'informazionale.
- **Quantità di dati per attività elementare** — bassa nell'operazionale (centinaia di record per transazione), alta nell'informazionale (milioni di record per ogni query).
- **Orientamento** — per processo/applicazione nell'operazionale, per area/tema nell'informazionale.
- **Frequenza di aggiornamento** — continua e tramite azioni nell'operazionale, sporadica e tramite funzioni esplicite nell'informazionale.
- **Copertura temporale** — dati correnti nell'operazionale, dati storici nell'informazionale.
- **Ottimizzazione** — questo è il punto tecnico più rilevante: l'operazionale è ottimizzato per accessi in *lettura e scrittura* su una *porzione* della base di dati, con un *modello normalizzato*; l'informazionale è ottimizzato per accessi in *lettura* e interrogazioni di *aggregazione su tutta* la base di dati, con un *modello denormalizzato e multidimensionale*. La differenza di modello dati (normalizzato vs denormalizzato/multidimensionale) è la ragione tecnica profonda per cui un unico database non può servire bene entrambi gli scopi.

## L'ERP come sistema duale
L'ERP è interessante proprio perché incarna *entrambe* le nature. Come **sistema operazionale** include moduli che automatizzano e gestiscono le operazioni quotidiane: gestione della produzione e della supply chain (SCM), contabilità e finanza, gestione del magazzino (WMS) e logistica, risorse umane e paghe (HRM). Come **sistema informazionale** raccoglie quei dati e fornisce informazioni utili al decision-making: genera report e dashboard per il management, analizza vendite e produttività e supporta la pianificazione strategica. È questa doppia anima a renderlo lo strumento "trasversale" che compare a ogni livello della piramide.

## La piramide DIKW
Per classificare la conoscenza si usa la **piramide DIKW**, che dispone su quattro livelli *Data → Information → Knowledge → Wisdom*, in ordine crescente di valore e di astrazione.
- **Data (dato)** — informazioni in forma di testo, numeri o simboli che possono essere usati da un computer. È la materia prima grezza.
- **Information (informazione)** — il dato viene elaborato e messo a confronto con altri dati, traendone conclusioni e dando un primo significato ai dati raccolti.
- **Knowledge (conoscenza)** — la comprensione delle *relazioni* tra le informazioni, che permette di prendere decisioni.
- **Wisdom (saggezza)** — l'abilità di usare conoscenza ed esperienza per raggiungere obiettivi e prendere decisioni *efficaci*.

### Gli strumenti che fanno salire la piramide
A ogni passaggio di livello corrisponde una tecnologia che "trasforma" il livello inferiore in quello superiore, ed è qui che la piramide diventa operativa:
- Dal **Data** si parte con i *database*: il sistema operativo e il DB che raccolgono i dati grezzi.
- Per passare a **Information** si usa la *Business Intelligence*: aggregare e contestualizzare i dati per trasformarli in informazioni.
- Per passare a **Knowledge** si usa l'*analisi dei dati*.
- Per raggiungere **Wisdom** si usa l'*analisi predittiva*: algoritmi di machine learning che "imparano" dai dati immagazzinati in passato e riescono a prevedere gli andamenti futuri.
L'obiettivo finale è l'azienda **data driven**, cioè che usa i dati per prendere le decisioni aziendali.

### Il legame DIKW ↔ sistemi operazionali/informazionali
La piramide DIKW si sovrappone perfettamente alla scomposizione vista prima: il **sistema operazionale** presidia il livello *Data* (genera e gestisce i dati grezzi dell'operatività), mentre il **sistema informazionale** presidia i livelli *Information, Knowledge e Wisdom* (li trasforma in informazione, conoscenza e capacità decisionale). È la sintesi finale del capitolo: i due sottosistemi non sono in concorrenza ma in *successione*, l'uno fornisce la base dati che l'altro innalza verso la decisione.

---
# Lezione 4 — Sistemi operazionali

## Funzioni, azioni e componenti
Il **sistema operazionale** è il sottosistema che supporta l'operatività quotidiana dell'azienda, e va inquadrato a partire da tre piani già introdotti. Le sue **funzioni principali** sono l'automazione delle attività procedurali, la definizione di nuovi processi, l'aiuto nelle attività aziendali, la raccolta di dati per il controllo dell'attività operativa e la guida per l'operatore. Le **azioni sui dati** che lo caratterizzano sono l'*accesso interattivo*, l'*elaborazione di informazioni attuali* e l'*aggregazione*. Le **componenti fondamentali** sono una *base di dati operazionale* e le *funzioni operative*. Tutto il capitolo approfondisce queste tre dimensioni, scendendo nel dettaglio di *cosa* fa un sistema operazionale (le finalità), *come* è fatta l'informazione che tratta e *come* la realtà viene modellata nei dati e nei processi.

## Le finalità dei sistemi operazionali
Le finalità si articolano in quattro grandi compiti, concatenati fra loro: la *registrazione delle transazioni*, la *pianificazione e controllo delle operazioni*, l'*acquisizione e organizzazione della conoscenza* e l'*elaborazione delle situazioni aziendali*.

### Registrazione delle transazioni
Una **transazione** è un'operazione elementare (un evento) che si manifesta in un dato momento e che l'azienda ha interesse a *tracciare*. Esempi: ordini cliente e fornitore; eventi che modificano lo stato interno (prelievo da magazzino, spedizione della merce, produzione di un oggetto, pagamento di una fattura); aggiornamenti anagrafici (inserimento di un prodotto a listino, classificazione di un nuovo fornitore). Le transazioni si distinguono in due tipi, ed è una distinzione importante per capire come si propagano gli effetti nel sistema:
- **Semplice** — registrata con un *singolo dato* (es. una movimentazione di magazzino).
- **Complessa** — una *serie di registrazioni elementari connesse* tra loro (es. una spedizione), che può generare transazioni *a cascata*: una spedizione, per esempio, produce tanti movimenti di magazzino quanti sono gli articoli spediti. Il punto chiave è che una transazione complessa scatena automaticamente altre transazioni, ed è questo che rende il sistema "vivo".

### Pianificazione e controllo delle operazioni
Poiché i processi aziendali sono *concatenati*, il sistema usa i dati dei processi a monte per pianificare l'attività di quelli a valle. L'esempio canonico è il **piano di produzione**, che si costruisce combinando due tipi di informazione:
- **Informazioni da processi diversi** — gli ordini cliente aperti, lo stato del magazzino, ecc.
- **Informazioni di struttura del processo** — le strutture dei prodotti, i centri di lavoro, le fasi di lavoro.
Dalla loro combinazione nasce un piano che, per ciascun articolo, specifica quantità, centro di lavoro, persona, istruzioni aggiuntive, fase e durata di lavorazione. Il concetto generale è che *piano di produzione = informazioni da processi diversi + informazioni di struttura del processo*: la pianificazione non è un atto isolato ma l'incrocio fra lo stato corrente e la struttura stabile dell'azienda.

### Organizzazione della conoscenza
Il sistema operazionale costruisce **basi di conoscenza aziendale** con due obiettivi: la *centralizzazione* delle informazioni e il loro mantenimento *sempre aggiornato*. Le informazioni organizzate sono di due nature complementari:
- **Registrazioni delle transazioni** — la traccia degli eventi.
- **Anagrafiche** — le informazioni che definiscono le *relazioni* tra le anagrafiche stesse.
Le caratteristiche di queste informazioni organizzate sono di essere *strutturate* e *correlate*: non bastano dati centralizzati, devono avere una struttura e dei legami che li rendano interrogabili.

### Elaborazione delle situazioni aziendali
Questa è l'idea più profonda del capitolo: il sistema informativo è un **sistema dinamico che modella l'azienda**, esattamente come una macchina a stati. La conoscenza dello *stato corrente* permette di "pilotare" il sistema tramite opportuni *eventi* (piani di produzione, approvvigionamenti) per portarlo nella *condizione desiderata*. Il ciclo è: si parte da uno stato A, arriva un *evento* in ingresso, l'*elaborazione delle transazioni* lo registra contro lo *stato corrente* (struttura + archivio), l'*elaborazione delle informazioni di stato* aggiorna le grandezze, e si arriva a un nuovo stato B. Esempi di indicatori di stato sono le giacenze di magazzino, gli ordini inevasi, il fatturato. La metafora della macchina a stati spiega *perché* il sistema operazionale è centrale: non si limita a memorizzare, ma fa evolvere l'azienda da uno stato all'altro attraverso gli eventi.

## L'informazione operativa
L'informazione operativa è organizzata all'interno di un **archivio virtualmente unitario**: anche se fisicamente distribuita, dev'essere concettualmente unica e coerente. Si classifica in quattro **categorie di informazione**:
- **Movimenti** — le registrazioni degli eventi.
- **Documenti di processo** — strutturati in *testa* (i dati comuni del documento) e *righe* (le voci di dettaglio).
- **Informazioni di stato** — distinte in *puntuali* (un valore diretto) e *derivate* (calcolate da altri dati).
- **Informazioni anagrafiche** — i dati di base stabili.

### Qualità dei dati
La **qualità dei dati** è definita (norma ISO 8402-1995) come "il possesso della totalità delle caratteristiche che portano al soddisfacimento delle esigenze, esplicite o implicite, dell'utente". È una definizione *centrata sull'utente*: un dato è di qualità non in assoluto, ma se soddisfa i bisogni di chi lo usa.

### Caratteristiche strutturali
L'informazione operativa si descrive lungo tre **caratteristiche strutturali**:
- **Aggregazione** — può essere *analitica* (il singolo dato) o *aggregata* (una sintesi).
- **Tempificazione** — può essere *puntuale* (riferita a un istante) o *cumulativa* (accumulata nel tempo).
- **Dimensionalità** — il numero di dimensioni lungo cui il dato è organizzato.
Incrociando queste caratteristiche con le categorie di informazione si ottiene un profilo per ciascuna:
- **Informazioni anagrafiche** — aggregazione *analitica*, tempificazione *puntuale*, dimensionalità *unitaria*.
- **Movimenti e documenti** — aggregazione *analitica*, tempificazione *puntuale*, dimensionalità *contenuta*.
- **Informazioni di stato** — aggregazione *analitica o aggregata*, tempificazione *puntuale o cumulata*, dimensionalità *contenuta*. Le informazioni di stato sono le più "flessibili" perché possono assumere entrambe le forme su due delle tre caratteristiche.

### Caratteristiche funzionali
Oltre a quelle strutturali, l'informazione operativa deve possedere cinque **caratteristiche funzionali**, che ne definiscono la bontà d'uso:
- **Completezza** — non mancano dati necessari.
- **Correttezza** — i dati sono esatti.
- **Precisione** — il livello di dettaglio è adeguato.
- **Omogeneità** — i dati sono coerenti fra loro nei formati e nelle convenzioni.
- **Fruibilità** — l'informazione è effettivamente utilizzabile.

## La rappresentazione della realtà
Per costruire un sistema operazionale bisogna *rappresentare la realtà aziendale*, e lo si fa su due fronti distinti:
- **Modellazione dei dati** — tramite *modelli concettuali* (E-R, UML) e *modelli logici* (relazionali, a oggetti).
- **Modellazione dei processi** — tramite *modelli concettuali* (DFD, SADT), che differiscono per gli aspetti della dinamica rappresentati e per il livello di formalizzazione.
La distinzione concettuale/logico è essenziale: il modello *concettuale* descrive la realtà a un livello vicino al dominio (cosa esiste e come si lega), il modello *logico* la descrive nei termini della struttura di memorizzazione (le tabelle).

## Modellazione dei dati
### Il diagramma Entità-Relazione (E-R)
Il modello **concettuale** per eccellenza è il diagramma **Entità-Relazione**, una rappresentazione grafica delle caratteristiche delle entità gestite dal sistema e delle relazioni tra esse. I suoi costrutti di base sono:
- **Entità** — una classe di oggetti con proprietà comuni ed esistenza autonoma.
- **Relazione** — un legame logico fra entità, collegate alla relazione tramite un *connettore*.
- **Attributo** — una caratteristica (di entità o di relazione) di interesse per il sistema.
- **Cardinalità** — un attributo del connettore: il numero *minimo* e *massimo* di istanze della relazione a cui un'istanza dell'entità può partecipare. Le combinazioni tipiche sono:
	- `(0,1)` relazione unaria opzionale,
	- `(0,N)` relazione ennaria opzionale,
	- `(1,1)` relazione unaria obbligatoria,
	- `(1,N)` relazione ennaria obbligatoria.
Le relazioni possono essere **binarie** (es. un *Listino* "contiene" un *Articolo*) o **ricorsive**, cioè che legano un'entità a sé stessa (es. un Articolo "composto da" altri Articoli). La ricorsività serve a modellare strutture gerarchiche come la distinta base di un prodotto.

### Il modello relazionale
Il modello **logico** più usato è il modello **relazionale**, che descrive i dati tramite la struttura delle *tabelle* e le relazioni fra esse. I due concetti fondamentali sono:
- **Schema** — l'insieme degli attributi (colonne) che definiscono il numero e il dominio dei dati ospitati; è la "forma" della tabella.
- **Istanza** — il singolo elemento (riga); descrive una singola entità o un singolo evento.
Le relazioni fra elementi memorizzati su tabelle diverse si definiscono tramite il valore contenuto in alcuni campi, le **chiavi esterne**. Per esempio, una tabella *Movimenti di Magazzino* lega ogni movimento a un *Articolo* e a un *Deposito* tramite i rispettivi codici, che fungono da chiavi esterne verso le tabelle *Articoli* e *Depositi*: è così che i dati restano collegati senza essere duplicati.

### Dal diagramma E-R al modello relazionale
La traduzione dal concettuale al logico segue regole precise:
- Ogni **entità** diventa una *tabella* (le colonne sono gli attributi dell'entità).
- Ogni **relazione** ha una rappresentazione logica *dipendente dalla cardinalità*:
	- si crea una *tabella dedicata* se la cardinalità è ennaria per tutte le entità coinvolte, oppure se la relazione non è obbligatoria e ha attributi propri;
	- si usano invece *colonne dedicate* sullo schema dell'entità se la relazione è unaria.
Le basi di dati costruite sul modello relazionale hanno caratteristiche pregiate, che spiegano la loro diffusione: memorizzano la sola informazione necessaria limitando la *ridondanza*; sono poco soggette a *errori accidentali* in popolamento; sono *efficienti* in inserimento e modifica; implementano *controlli nativi* sui dati e sulla congruenza dei legami fra tabelle; e rendono efficienti le ricerche tramite *indici*. Si noti il legame con la lezione precedente: questo è il modello *normalizzato*, ottimizzato per la scrittura e tipico dei sistemi operazionali (in contrasto col modello denormalizzato/multidimensionale dei sistemi informazionali).

## Modellazione dei processi
Per rappresentare i processi si usa il **Data Flow Diagram (DFD)**, che descrive formalmente il *flusso dei dati* tra i processi. I suoi costrutti di base sono:
- **Agente** — un elemento che *produce o consuma* dati nel sistema (la sorgente o la destinazione).
- **Deposito di dati** — l'informazione che il sistema *mantiene*, su cui i processi agiscono in lettura o scrittura.
- **Processo** — la porzione di sistema che *trasforma* i dati.
- **Flusso** — la linea attraverso cui l'informazione si *propaga*.
Componendo questi elementi si descrivono situazioni tipiche: un *agente sorgente* che invia dati a un processo (flusso A), un *accesso ai dati in lettura/scrittura* fra un processo e un deposito (flusso B), un *flusso di dati tra processi* (flusso C). A differenza dell'E-R, che fotografa la *struttura statica* dei dati, il DFD descrive la loro *dinamica*, cioè come si muovono e si trasformano.

## La potenzialità informatica
Il capitolo si chiude con un criterio per decidere *quanto* convenga informatizzare un'azienda: la **potenzialità informatica**, che dipende da due fattori più la disposizione del management.
- L'**intensità informativa** è la necessità di informazioni *proprie* dell'azienda; dipende dal mercato in cui opera e dalla complessità della struttura. Si scompone a sua volta in *intensità informativa di prodotto* e *intensità informativa di processo*, entrambe legate alla complessità.
- L'**attrattiva informatica** è correlata alle *caratteristiche dei processi* aziendali, ed è tanto più elevata quanto più i processi sono adatti a essere automatizzati. In particolare:
	- **alta proceduralità** → elevata attrattiva (processi ben definiti si automatizzano bene);
	- **bassa complessità** → elevata attrattiva (processi semplici sono più facili da informatizzare);
	- **alta ripetitività** → elevata attrattiva (conviene automatizzare ciò che si ripete);
	- **alti volumi** → elevata attrattiva (l'automazione rende su grandi numeri).
Il terzo elemento, che fa da moltiplicatore, è la **propensione del manager all'investimento** in infrastruttura informatica e all'uso della tecnologia a supporto delle attività: anche con alta intensità e attrattiva, senza la volontà decisionale del management l'informatizzazione non parte. La sintesi è che conviene informatizzare dove c'è *bisogno* di informazione (intensità), dove i processi sono *automatizzabili* (attrattiva) e dove c'è la *volontà* di investire.

---
# Lezione 5 — ERP e ODOO

## La composizione dei sistemi operazionali
I sistemi operazionali sono composti da **diversi sottosistemi**, ma il punto di partenza del capitolo è una constatazione importante: *non esiste una classificazione standard* dei sottosistemi operazionali. Il motivo è duplice. Da un lato c'è una forte eterogeneità tra le aziende — per esempio, nelle industrie manifatturiere la casistica è estremamente varia, e modalità come la gestione di commesse o la produzione a ciclo continuo sono applicabili ad alcune aziende e ad altre no. Dall'altro, oltre a questa "parcellizzazione", i criteri di classificazione stessi si diversificano a seconda dell'aspetto che si privilegia: si può classificare *per funzione, per processo, per architettura*, e così via. Questa premessa spiega perché non si possa dare un elenco rigido e perché si ricorra invece a categorie più ampie come il portafoglio applicativo.

## Il portafoglio applicativo
Le applicazioni informatiche aziendali si raggruppano in due **portafogli**, la cui distinzione è cruciale perché determina quanto un'applicazione sia *specifica* o *standardizzabile*.
- Il **portafoglio operativo** raccoglie le applicazioni legate ai processi *market driven*, cioè quelli che dipendono dal mercato e dal core business. È caratterizzato da elevata specializzazione settoriale, ampia variabilità tra settori merceologici diversi e, persino nello stesso settore, ampia variabilità tra aziende di dimensione o processi produttivi diversi. È frequente trovarvi software fortemente *verticalizzato*, costruito su misura per un settore.
- Il **portafoglio istituzionale** raccoglie le applicazioni che trattano le attività di *sostegno* a quelle primarie. È caratterizzato da elevata attrattiva informatica, alta proceduralità e ripetitività, bassa complessità di elaborazione, elevata omogeneità al variare del settore e *invarianza* rispetto alla natura del prodotto o servizio. Proprio per questo sul mercato esistono numerose soluzioni *standardizzate*.
La logica sottostante (collegata alla "potenzialità informatica" della lezione precedente) è che il portafoglio istituzionale — procedurale, ripetitivo, uguale per tutti — si presta a soluzioni standard, mentre quello operativo, legato alle specificità del business, richiede soluzioni verticalizzate.

## Dal sistema gestionale classico al sistema ERP
### Il sistema gestionale classico: le isole informatiche
Il modello "antico" è quello del **sistema gestionale classico**, fatto di *isole informatiche autonome e specializzate*: produzione, logistica, acquisti, vendite, amministrazione, ognuna con il *proprio archivio* separato (archivio produzione/magazzino, archivio vendite, archivio amministrazione…). Le cause di questa frammentazione sono storiche e organizzative: lo sviluppo *incrementale* del sistema informativo (si aggiunge un pezzo per volta), la rigidità delle organizzazioni aziendali e la specializzazione dei produttori di software. I problemi che ne derivano sono però gravi e ricorrenti:
- **eterogeneità** dei dati e dei formati,
- **ridondanza** dei dati (lo stesso dato replicato in più archivi),
- **discrepanze** tra le copie dello stesso dato,
- **difficoltà di avere visioni d'insieme** dell'azienda.
Sono esattamente i problemi di *accessibilità* e *correttezza* visti nella lezione 2, qui causati dalla mancanza di integrazione.

### Il sistema ERP
L'**ERP (Enterprise Resource Planning)** è la risposta a quei problemi: un sistema informativo operazionale **nativamente integrato**. Le sue due caratteristiche fondanti sono:
- una **base di dati unica** — un solo archivio condiviso da tutti i moduli, che elimina ridondanza e discrepanze;
- **processi interagenti e cooperanti** — i moduli non sono isole ma collaborano.
Il suo **obiettivo primario** è la trattazione *ottimale* di tutte le risorse utilizzate e la gestione e il controllo dei processi aziendali. L'ERP è inoltre un sistema **flessibile**, capace di assecondare l'azienda nei suoi processi di evoluzione e crescita, e *altamente configurabile* rispetto all'organizzazione aziendale e all'architettura sistemistica. Il passaggio dal gestionale classico all'ERP si può leggere come una sostituzione che mantiene i tre strati (organizzazione aziendale, procedure gestionali, piattaforma tecnologica) ma li *integra*: dove prima c'erano tante piattaforme scollegate, ora c'è un'unica piattaforma ERP configurabile. La parola chiave è "nativamente integrato": l'integrazione non è aggiunta dopo, ma è il principio costitutivo del sistema.

## Gli ambiti applicativi dell'ERP
Un ERP è composto da **moduli indipendenti**, ognuno dei quali copre uno specifico ambito aziendale. Nato per le aziende manifatturiere, grazie alle sue caratteristiche di *modularità, configurabilità e forte orientamento ai processi* è applicabile con successo anche in ambiti molto diversi: servizi finanziari, grande e piccola distribuzione, trasporti, telecomunicazioni, sanità, pubblica amministrazione. I **flussi di base** coperti sono cinque.
- **Amministrativo** — è l'ambito di *prima applicazione* delle procedure informatiche, con vincoli legislativi molto stretti e procedure ben definite e articolate; è il *cuore del portafoglio istituzionale*. Si è evoluto ampliando sia le funzioni avanzate di controllo e gestione, sia le interfacce per l'integrazione con altri flussi, interni o esterni all'azienda.
- **Logistico** — si occupa del trattamento dei *materiali*: la loro definizione, la movimentazione all'interno dell'azienda, l'analisi dei costi e delle valorizzazioni a essi riconducibili. Fa parte del *portafoglio operativo*.
- **Attivo (vendite)** — costruisce la catena di processi per interagire con il *cliente*: la presentazione dell'offerta, l'acquisizione dell'ordine, la sua evasione, la fatturazione.
- **Passivo (acquisti)** — costituisce la catena di processi per interagire con i *fornitori*, per l'approvvigionamento di materiali o la richiesta di lavorazioni e servizi.
- **Produttivo** — è uno dei sottosistemi *più articolati*, fortemente dipendente dal settore merceologico e dalle modalità produttive adottate. Proprio per ridurre la complessità che un prodotto unico avrebbe, i produttori di ERP forniscono spesso sottosistemi di produzione *verticalizzati* per tipologie aziendali (in linea con la natura "operativa" e specifica di quest'area).

## I sistemi operazionali complementari
Oltre al nucleo ERP esistono **sistemi complementari**, raggruppati in quattro famiglie a seconda del ruolo che svolgono.
- I **sistemi di supporto primario all'ERP** sviluppano flussi abbastanza standardizzati, adottati da un numero relativamente ridotto di imprese, che non fanno *nativamente* parte della proposta ERP — per esempio Controllo Qualità, Ricerca e Sviluppo, Manutenzione degli impianti, Risorse Umane, Tesoreria.
- Le **estensioni dell'ERP** permettono al sistema di *scambiare dati col mondo esterno*: per esempio il CRM (*Customer Relationship Management*), l'E-commerce o i dispositivi IoT (*Internet of Things*).
- I **sistemi tecnici** risolvono processi di natura tecnica specifica, come la schedulazione della produzione o la progettazione assistita dal computer (CAD, *computer aided design*).
- I **sistemi di dematerializzazione documenti e organizzazione d'ufficio** trattano il lavoro degli uffici e facilitano l'organizzazione interna: strumenti di *office automation* (scrittura testi, elaborazione tabelle), archiviazione e trattazione di documenti elettronici, strumenti di *document flow* (flusso documentale) e di *workflow* (flusso di lavoro), procedure per la comunicazione a distanza e il lavoro collaborativo.

## ODOO
**ODOO** (acronimo di *On Demand Open Project*) è una piattaforma ERP **open source**, con **architettura modulare**, che offre una vasta raccolta di applicazioni aziendali: CRM, gestione delle vendite, eCommerce, gestione del magazzino, gestione degli acquisti, suite di contabilità, gestione della produzione e risorse umane. La sua filosofia è di *dare al cliente potere nell'implementazione*, cioè la possibilità di comporre il sistema scegliendo i moduli.

### I moduli principali di ODOO
ODOO si compone di moduli attivabili in base alle esigenze. I principali e ciò che fanno:
- **Vendite** — semplifica le trattative con la *firma elettronica* (i clienti rivedono e firmano i preventivi online), invia avvisi personalizzati, conserva automaticamente i record delle negoziazioni e facilita l'*upselling* proponendo opzioni e accessori extra, trigger di chiusura e sconti.
- **Contabilità** — si collega direttamente al conto bancario o PayPal con transazioni sincronizzate ogni ora, semplifica la creazione e l'invio delle fatture, dà visibilità sulla situazione finanziaria e gestisce le spese dei dipendenti.
- **Magazzino & MRP** — supporta produzione e catena di approvvigionamento; automatizza gli acquisti con regole su prodotti *made-to-order*, scorte minime o piano principale di produzione; controlla i tempi di elaborazione, organizza il magazzino, gestisce spedizioni e proposte d'ordine in base alle previsioni, traccia le scadenze e crea codici a barre personalizzati.
- **eCommerce** — realizza e gestisce il negozio online, imposta i termini di pagamento, definisce promozioni e integra una *live chat* per rispondere ai clienti in tempo reale.
- **Email Marketing / Marketing** — crea campagne automatiche e mirate segmentando i prospect, struttura email accattivanti, gestisce campagne SMS e social media aziendali.
- **Risorse Umane** — crea i profili dei dipendenti, gestisce contratti, presenze (ferie e malattia) e schede di attività; crea un social network aziendale con chat e integra una funzione di *gamification* (sfide, obiettivi, ricompense) per stimolare il coinvolgimento.
- **Pianificazione** — gestisce la giornata lavorativa (appuntamenti, assegnazione task, tracciamento dei tempi) come sistema multi-progetto pensato per i manager.
- **Discuss** — migliora la comunicazione interna con gruppi, discussioni e notifiche, e gestisce le richieste dei dipendenti tramite una dashboard di approvazione.

### Le fasi di implementazione di ODOO
L'introduzione di un ERP come ODOO segue sei fasi, da capire come un percorso ordinato in cui ogni fase poggia sulla precedente.
1. **Analisi preliminare e definizione dei requisiti** — si analizzano in dettaglio le necessità aziendali, si identificano i processi chiave da supportare e si definiscono moduli, personalizzazioni e integrazioni necessarie. È la fase fondamentale per allineare il sistema finale agli obiettivi aziendali.
2. **Progettazione e personalizzazione** — si configurano i moduli scelti e si personalizza il sistema (workflow, formulari, report, dashboard), curando che sia non solo adeguato alle esigenze immediate ma anche *scalabile e flessibile* per il futuro.
3. **Implementazione e integrazione** — si installa e configura il sistema nell'ambiente operativo e lo si *integra* con gli altri software in uso (contabilità, CRM, HR) non sostituiti dai moduli ODOO, per ottenere un flusso di lavoro *seamless* e minimizzare la duplicazione dei dati.
4. **Formazione degli utenti** — si addestrano i dipendenti all'uso efficace del sistema; l'*adozione da parte degli utenti* è spesso uno dei maggiori indicatori del successo di un'implementazione ERP.
5. **Test e messa in opera** — si eseguono test funzionali, di performance e di sicurezza; confermata la stabilità, il sistema va in produzione.
6. **Supporto post-implementazione** — il supporto continuo risolve i problemi che emergono nell'uso reale, con eventuali revisioni periodiche per ottimizzare le funzionalità man mano che l'azienda cresce.

### Criteri di scelta di un ERP (ODOO vs SAP/Oracle)
La scelta di un ERP si valuta su sette aspetti, ed è istruttivo vedere come ODOO si posiziona rispetto ai grandi nomi (SAP, Oracle, Microsoft Dynamics).
- **Flessibilità e facilità d'uso** — ODOO ha interfaccia intuitiva e struttura modulare (si aggiungono/rimuovono moduli a piacere); SAP e Oracle sono percepiti come più rigidi e complessi, richiedendo interventi IT significativi.
- **Personalizzazione** — ODOO eccelle grazie al *codice open source* modificabile; SAP e Oracle personalizzano ma a costo e complessità maggiori.
- **Costi** — ODOO è più economico, vantaggio significativo per le PMI; i grandi ERP richiedono investimenti iniziali e di manutenzione elevati.
- **Scalabilità** — ODOO è adatto sia a piccole sia a grandi imprese grazie alla modularità; SAP e Microsoft Dynamics sono tradizionalmente visti come più adatti a grandi organizzazioni con enormi volumi di dati.
- **Settore di mercato** — ODOO è popolare tra start-up e PMI; SAP e Oracle sono scelti da grandi corporazioni (manifattura, finanza) che richiedono reporting e conformità normativa sofisticati.
- **Supporto e comunità** — ODOO ha una comunità open source molto attiva con molte risorse online; SAP e Oracle offrono supporto professionale e consulenza, critici per grandi implementazioni.
- **Innovazione e aggiornamenti** — ODOO è più agile grazie all'approccio open source; SAP e Oracle, pur innovativi, hanno cicli di rilascio più lunghi per via della scala e complessità dei prodotti.
La sintesi è che ODOO è la scelta tipica per PMI che cercano flessibilità e costi contenuti, mentre i grandi ERP restano lo standard delle grandi organizzazioni con esigenze di robustezza e conformità.

---
# Lezione 6 — Esercizi ODOO: i processi di acquisto e vendita

## Inquadramento
Questa lezione è di natura pratica: si lavora "a mano" su ODOO per vedere all'opera i moduli dell'ERP. Sul piano operativo l'esercizio prevede di creare un database di prova sul sito ODOO (anteponendo `edu-` al nome per usarlo in modalità completa per 24 mesi, e ricordando di *attivarlo* per non perderlo), di abilitare la *modalità sviluppatore* dalle Impostazioni e di installare i moduli di lavoro — **Inventory** (Magazzino), **Purchase** (Acquisti), **Manufacturing** (Produzione) e **Accounting** (Contabilità). Sul piano concettuale, però, il valore di studio sta nei **processi di business** che ODOO modella: il ciclo *passivo* (acquisto), il ciclo *attivo* (vendita di beni) e la vendita di *servizi*. Capire questi processi è ciò che permette poi di usare sensatamente l'ERP, perché ogni passo del processo corrisponde a una funzione del sistema e a un cambiamento di stato dei dati (ordini, magazzino, contabilità).

## Il processo di acquisto (ciclo passivo)
Il **processo di acquisto** è la catena che permette all'azienda di interagire con i fornitori. Si articola in sette fasi consecutive, ciascuna delle quali produce un documento o un cambiamento di stato nell'ERP.
- **Identificazione del fabbisogno** — l'azienda rileva la necessità di acquistare materie prime, beni o servizi. La necessità può nascere dal raggiungimento delle *scorte minime*, da *ordini di vendita* da soddisfare o da *richieste interne*. È il punto in cui il magazzino o la produzione "chiamano" l'approvvigionamento.
- **Creazione della richiesta d'acquisto (RFQ — Request for Quotation)** — il reparto acquisti invia una *richiesta di preventivo* ai fornitori per ottenere offerte sui prodotti necessari. La RFQ è ancora una domanda, non un impegno.
- **Selezione del fornitore** — si valutano i preventivi ricevuti in base a *prezzo, tempi di consegna e qualità* e si sceglie il fornitore più adatto. È il momento decisionale del processo.
- **Emissione dell'ordine di acquisto (PO — Purchase Order)** — selezionato il fornitore, si genera un ordine d'acquisto *ufficiale*. Qui la RFQ si trasforma in un impegno contrattuale.
- **Ricevimento della merce e controllo qualità** — la merce arriva in magazzino e viene verificata in *quantità e qualità*; eventuali non conformità possono generare resi o richieste di sostituzione. È il controllo che protegge l'azienda da forniture errate.
- **Registrazione della fattura e pagamento** — il fornitore invia la fattura, l'azienda ne verifica la *conformità con l'ordine* (il classico controllo a tre vie ordine-merce-fattura) e procede al pagamento.
- **Aggiornamento dell'inventario** — se l'acquisto riguarda prodotti da stoccare, il magazzino viene aggiornato *automaticamente* nel sistema ERP. È il punto in cui l'integrazione nativa dell'ERP si vede all'opera: l'arrivo della merce muove da solo le giacenze.

## Il processo di vendita di beni (ciclo attivo)
Il **processo di vendita** è la catena speculare che permette all'azienda di interagire con il cliente. Anch'esso si articola in sette fasi.
- **Ricezione della richiesta o dell'ordine cliente** — il cliente invia una richiesta d'offerta o un ordine di acquisto. È l'innesco del ciclo attivo.
- **Generazione del preventivo** — il reparto vendite prepara un'*offerta commerciale* con prezzi e condizioni di vendita. È il corrispettivo, lato vendite, della RFQ.
- **Conferma dell'ordine di vendita (SO — Sales Order)** — se il cliente accetta il preventivo, l'ordine di vendita viene confermato. Qui il preventivo diventa impegno (l'analogo del Purchase Order, ma dal lato venditore).
- **Gestione della logistica e spedizione** — il magazzino *preleva* i prodotti e li prepara per la spedizione, emettendo il documento di trasporto (DDT) o la bolla di consegna. È la fase fisica che muove la merce verso il cliente.
- **Fatturazione al cliente** — dopo la spedizione viene emessa la *fattura di vendita*.
- **Ricezione del pagamento** — il cliente paga secondo le modalità concordate (bonifico, carta di credito, ecc.).
- **Aggiornamento dell'inventario e analisi post-vendita** — l'inventario viene aggiornato e il reparto vendite può *analizzare le performance* delle vendite e la soddisfazione del cliente. Anche qui l'aggiornamento del magazzino è automatico, e si aggiunge la dimensione *informazionale* (l'analisi post-vendita).
La simmetria fra ciclo passivo e attivo è la chiave di lettura: RFQ ↔ preventivo, Purchase Order ↔ Sales Order, ricevimento merce ↔ spedizione, fattura passiva ↔ fattura attiva. Entrambi convergono sul *magazzino* e sulla *contabilità*, che sono i due punti dove i due cicli si incontrano e dove l'integrazione dell'ERP evita disallineamenti.

## Il processo di vendita di servizi
La vendita di **servizi** (consulenza, manutenzione, formazione, assistenza tecnica) segue una catena simile a quella dei beni, ma con una differenza fondamentale: *non c'è una merce fisica da spedire*, bensì una prestazione da erogare e spesso da *tracciare a tempo*. Si articola in cinque fasi.
- **Creazione dell'offerta e preventivo** — il cliente richiede un servizio, il team vendite crea un preventivo con dettagli su servizio, tempi e costi, e lo invia per approvazione.
- **Conferma dell'ordine di servizio** — accettato il preventivo, si genera un ordine di vendita (SO); l'ERP assegna *automaticamente* il servizio ai responsabili (tecnici, consulenti). Questo automatismo di assegnazione è la specificità del ciclo servizi.
- **Erogazione del servizio** — il servizio viene svolto secondo tempi e modalità stabilite; se necessario si *tracciano le ore di lavoro* (per consulenze o assistenza) e il cliente può ricevere aggiornamenti o documenti di consegna (es. rapporti di intervento). Il "magazzino" qui è sostituito dal *tempo* e dalle competenze.
- **Fatturazione automatica** — erogato il servizio, si genera la fattura, che può essere creata manualmente o *in automatico in base alle ore lavorate* o all'ordine confermato. La fatturazione "a consuntivo" sulle ore è tipica dei servizi.
- **Pagamento e contabilità** — il cliente paga (bonifico, carta, PayPal, ecc.) e il sistema ERP aggiorna *automaticamente* la contabilità.
Il confronto con la vendita di beni chiarisce il concetto: dove per i beni il valore passa per il *magazzino* e la *spedizione fisica*, per i servizi passa per l'*erogazione* e il *tracciamento delle ore*, e la fatturazione tende a essere automatica e legata al lavoro effettivamente svolto. In entrambi i casi, però, è l'ERP integrato a far sì che ordine, erogazione, fattura e contabilità restino coerenti senza reinserimenti manuali.

---
# Lezione 7 — Enterprise Architecture: Zachman e TOGAF

## Che cos'è l'Enterprise Architecture
Il problema che l'Enterprise Architecture (EA) risolve si capisce da un caso tipico: un'azienda retail con vendite gestite dal CRM, marketing su Excel, logistica su un sistema separato e amministrazione su un ERP, *ognuno con database diversi*. Le conseguenze sono dati duplicati (lo stesso cliente in più sistemi), informazioni incoerenti, difficoltà di integrazione, errori decisionali e inefficienze operative. La **definizione** è: l'Enterprise Architecture è *un insieme coerente di principi, metodi e modelli usati nella progettazione e realizzazione della struttura organizzativa, dei processi aziendali, dei sistemi informativi e dell'infrastruttura di un'impresa*. È una *disciplina* che guida in modo olistico e proattivo le risposte dell'azienda agli eventi dirompenti, identificando come attuare il cambiamento verso la visione desiderata, e crea valore offrendo ai leader suggerimenti per adeguare politiche e progetti agli obiettivi di business.
L'EA agisce su **tre pilastri** fondamentali dell'azienda:
- i **processi di business**,
- le **informazioni strategiche**,
- gli **elementi tecnologici (IT)**.

### I quattro livelli architetturali
L'EA *scompone l'azienda nei suoi singoli elementi*, in modo da gestirli e riorganizzarli efficientemente restando coerenti con la visione d'insieme. I livelli, dal più alto al più basso, sono:
- **Business Architecture** — definisce strategia, governance, organizzazione e processi chiave; è il livello più alto, stabilisce *cosa* fa l'azienda e *perché*.
- **Data Architecture** — descrive come sono gestite le risorse di dati (modelli logici e fisici, gestione dei dati).
- **Application Architecture** — fornisce il progetto dei singoli sistemi applicativi, le loro interazioni e le relazioni con i processi di business.
- **Technology Architecture** — descrive le infrastrutture software e hardware necessarie (server, reti, sistemi operativi).
Per fissare la classificazione: un *processo "gestione ordini"* e un *responsabile vendite* sono Business; *SAP ERP* è Application; un *server cloud* e un *database clienti* sono Technology.

### Perché adottare l'EA e cosa cambia concretamente
I benefici dell'EA sono decisioni migliori, processi più efficienti, maggiore adattabilità e supporto alla trasformazione. In concreto: migliora il supporto decisionale, facilita la percezione delle risorse IT necessarie a breve/medio/lungo termine, ottimizza i processi IT (utile in fusioni e accorpamenti), supporta riorganizzazione e modernizzazione, dà capacità di adattarsi più agilmente ai cambiamenti di mercato e migliora la gestione delle risorse umane. Sul piano operativo elimina processi obsoleti e ridondanti, ottimizza l'impiego degli asset, rende gli aspetti IT comprensibili alle figure decisionali non specialistiche (manager, CdA) e ai team finanziari (che li traducono in voci di bilancio), e agevola la comunicazione fra reparti. Il *vero beneficio principale* quando i dati sono duplicati e i sistemi non integrati è **migliorare l'integrazione dei dati** (non ridurre l'hardware o sostituire l'ERP), e l'EA serve *davvero* soprattutto nei contesti complessi — una multinazionale con 50 sistemi o un'azienda in fusione — più che in una startup di 3 persone o una PMI con 2 software.

### I framework principali e il ruolo dell'Enterprise Architect
Esistono diversi **framework** di EA, da adattare al caso specifico: **Zachman** (pionieristico, schema di classificazione bidimensionale), **TOGAF** (The Open Group Architectural Framework, ampiamente usato, con metodo dettagliato e strumenti), **UAF** (Unified Architecture Framework), **Agile EA**, **FEAF** (governo federale USA), framework di **SAP** e di **Gartner**, e quello dell'**ESA** per i sistemi spaziali. L'**Enterprise Architect** è la figura che assicura il rispetto di alcune best practice: stabilire un set standardizzato di attività, procedere in modo *progressivo* (prima i processi prioritari), usare tecnologie di *data visualization* per illustrare ai decisori come l'EA risolve problemi concreti, *parlare la lingua dell'interlocutore* (più tecnica con sviluppatori, più di business con i manager), integrare fonti di dati automatizzate, mantenere alta la *data quality*, redigere report regolari per gli stakeholder e coinvolgere referenti per ciascuna linea di business (LoB). Per le PMI, che faticano a implementarla, esiste l'**EAaaS** (*Enterprise Architecture as a Service*), in cui un fornitore centralizza pianificazione, analisi e gestione dell'architettura.

## Il framework di Zachman
Introdotto da John Zachman (IBM) nel 1987, il framework di Zachman è ancora oggi usato su piccoli progetti. La distinzione concettuale fondamentale è che **è un'ontologia, NON una metodologia**:
- come **ontologia** definisce concetti e relazioni all'interno di un dominio, organizzando gli artefatti architetturali (documenti, specifiche, modelli) tramite una *matrice bidimensionale*;
- *non* è una metodologia perché non fornisce i passaggi per passare da uno stato all'altro, né implica un metodo specifico per raccogliere o usare le informazioni.
La matrice incrocia due dimensioni: le **prospettive** (le righe) e gli **interrogativi** (le colonne).

### Le prospettive (righe)
Le sei prospettive corrispondono a chi guarda l'azienda e a quale livello di dettaglio:
- **Executive** — visione d'insieme dell'azienda (diagrammi di alto livello), utile ai dirigenti per comprendere portata e obiettivi.
- **Business** — modelli di business che descrivono come l'azienda opera quotidianamente, utili a proprietari e manager per i processi e le funzioni.
- **Architect** — modelli *logici* dei sistemi, che rappresentano come i sistemi informativi supportano i processi; utili agli architetti di sistema.
- **Engineer** — modelli *tecnologici* con specifiche tecniche e limitazioni; utili agli ingegneri che implementano.
- **Technical** — rappresentazioni dettagliate dei componenti e delle configurazioni; utili a tecnici e sviluppatori.

### Gli interrogativi (colonne)
Le sei colonne rispondono alle domande fondamentali su qualunque sistema:
- **WHAT** — dati e informazioni,
- **HOW** — funzionalità e processi,
- **WHERE** — rete e localizzazione (dove accadono le cose),
- **WHO** — persone e responsabilità,
- **WHEN** — tempistica e cicli,
- **WHY** — motivazioni e obiettivi.
Ogni cella della matrice (prospettiva × interrogativo) contiene un artefatto specifico. Salendo lungo le prospettive si va dal generale al dettagliato: per esempio la colonna **WHAT** passa dalle *entità importanti per l'azienda* (Executive) alle *entità di sistema come applicazioni e database* (Architect) fino agli *script di database* (Technical); la colonna **WHERE** va dalle *sedi fisiche* (Executive) all'*architettura di sistema distribuita* (Architect) fino alle *configurazioni di rete dettagliate* (Technical). L'esempio dell'implementazione di un ERP mostra come riempire ogni cella: a livello Executive il WHY sono gli obiettivi strategici (es. aumentare le vendite online), a livello Business il WHAT è un diagramma E-R, a livello Architect il WHERE è l'architettura di rete, e così via fino al livello Technical con script di database, codice sorgente e configurazioni.

### Integrazione con UML/BPMN/ERD
Il framework di Zachman si può applicare insieme ad altri linguaggi per evidenziare i processi:
- **UML/SysML** — l'*Unified Modeling Language* (per software) e il *System Modeling Language* (per sistemi) per specificare, costruire e documentare.
- **BPMN** — *Business Process Model and Notation*, metodo per delineare un processo aziendale.
- **ERD** — *Entity-Relationship Diagram*, per illustrare come le entità si relazionano in un sistema.
Nella matrice, tipicamente la colonna WHAT usa ERD/Data model, la colonna HOW usa BPMN/UML, la colonna WHO usa organigrammi e use case, ecc., a granularità crescente per prospettiva.

## TOGAF
**TOGAF** è un framework di architettura che fornisce metodi e strumenti per assistere accettazione, produzione, uso e manutenzione di un'EA. Si basa su un *modello di processo iterativo* supportato da best practice e da un insieme riutilizzabile di risorse architettoniche, riflette le esigenze degli stakeholder e applica i principi del **Deming cycle** (PDCA: *Plan–Do–Check–Act*, cioè Pianificare–Fare–Verificare–Agire). Definisce l'*architettura* come "la struttura dei componenti, le loro inter-relazioni e i principi e le linee guida che ne governano la progettazione ed evoluzione nel tempo".

### Architecture Transformation
Il cuore di TOGAF è la **trasformazione** da una **Baseline Architecture** (lo stato attuale, AS-IS) a una **Target Architecture** (lo stato desiderato, TO-BE). La trasformazione risponde a quattro domande operative — *quali percorsi seguire? come organizzarsi? come comunicare? quali rischi e come ridurli?* — riassumibili in: sapere da dove veniamo, determinare dove vogliamo andare, scegliere il percorso migliore e completare la trasformazione con successo.

### Architecture Abstraction: la doppia classificazione
TOGAF classifica l'architettura su due dimensioni incrociate. La prima è la **tipologia di architettura** (i quattro livelli già visti): **Business** (persone, processi, organizzazione, servizi), **Data** (informazioni trattate), **Application** (software e funzioni applicative), **Technology** (infrastruttura tecnica). La seconda è il **livello di astrazione**:
- **Contextual (WHY)** — contesto, obiettivi, motivazioni.
- **Conceptual (WHAT)** — cosa serve, senza ancora una soluzione dettagliata.
- **Logical (HOW)** — come si organizza logicamente la soluzione.
- **Physical (WITH WHAT)** — con quali tecnologie e componenti concreti si implementa.
Incrociando le due dimensioni si ottiene una matrice 4×4. L'esempio dell'università che digitalizza la gestione degli esami la riempie passo passo: nel dominio **Business**, il Contextual è "gli studenti faticano a prenotarsi, la segreteria perde tempo", il Conceptual è "prenotazione esami, pubblicazione appelli, verbalizzazione", il Logical è il processo "la segreteria apre l'appello → lo studente si prenota → il docente vede gli iscritti → inserisce i voti", il Physical sono l'ufficio segreteria reale, i docenti, il regolamento. Nel dominio **Data** si va dai "dati studente/corso/appello" (Contextual) al modello E-R (Logical) fino al "DB PostgreSQL con tabelle STUDENTI, APPELLI, PRENOTAZIONI, ESITI" (Physical). Nel dominio **Application** dai "bisogni di supporto applicativo" ai "Portale Studenti, Portale Docenti, Servizio Gestione Appelli" fino a "Esse3, portale Angular, backend Java, API REST". Nel dominio **Technology** dai "bisogni di accesso web e sicurezza" ai "web server, application server, database server" fino a "Linux, Nginx, PostgreSQL, Azure, firewall Fortinet".

### Principi, interoperabilità e prodotti del lavoro
I **principi architetturali** sono regole e linee guida generali, destinate a durare nel tempo, che informano come l'organizzazione realizza la propria missione; si distinguono in *Enterprise Principles* (base decisionale per tutta l'azienda) e *Architecture Principles* (governano il processo di architettura). L'**interoperabilità** si declina su più piani — operativa/di business, delle informazioni, tecnica — e dal punto di vista IT in integrazione della *presentazione*, delle *informazioni*, delle *applicazioni* e *tecnica*. I **prodotti del lavoro architetturale** sono di tre tipi, da non confondere:
- **Deliverable** — l'output formale e contrattuale (es. il documento di architettura del sistema esami).
- **Artifact** — un singolo prodotto descrittivo (es. un diagramma di processo, una matrice attori-funzioni).
- **Building Block** — un componente riutilizzabile, che può essere *Architecture Building Block (ABB)*, più astratto, o *Solution Building Block (SBB)*, concreto (es. il sistema di gestione esami, dall'ABB all'SBB).
Tutti questi output sono memorizzati nell'**Architecture Repository** a diversi livelli di astrazione, all'interno dell'**Enterprise Continuum**.

## L'Architecture Development Method (ADM)
L'**ADM** è il processo testato e ripetibile di TOGAF per sviluppare architetture. Ogni sua fase si descrive secondo un *contenuto* fatto di obiettivi, approccio, input/output e ripartizione del lavoro. Le fasi sono nove, più la gestione trasversale dei requisiti.

### Preliminary Phase
Prepara l'organizzazione a "fare EA": ne è obiettivo definire *regole, ruoli e strumenti*. Le attività principali sono identificare stakeholder e organizzazione, definire ruoli e responsabilità, definire i principi architetturali, *adattare TOGAF al contesto* aziendale e definire strumenti e repository. Gli output sono il modello organizzativo EA, i principi architetturali, il framework personalizzato e l'Architecture Repository iniziale. *(Esempio università: si identificano Direzione ICT, segreteria, docenti, studenti; si definiscono principi come "dati studenti unificati" e "rispetto GDPR"; si scelgono strumenti come Archi/draw.io e SharePoint.)*

### Phase A: Architecture Vision
Definisce *cosa si vuole ottenere*, identifica stakeholder e bisogni e stabilisce lo scopo. Le attività si raggruppano in identificazione iniziale (stakeholder, problemi, obiettivi e driver di business), analisi organizzativa (valutare capability e *readiness al cambiamento*), definizione del perimetro (lo *scope*, cosa è incluso/escluso, baseline e target) e costruzione della visione (Architecture Vision, proposta di valore, KPI, rischi). Output: Architecture Vision, *Statement of Architecture Work*, principi confermati, bozza di *Architecture Definition Document* e piano di comunicazione. *(Esempio: scope incluso = prenotazione esami e verbalizzazione, escluso = gestione lezioni e tasse; baseline = processi manuali, target = sistema digitale unico con dati integrati; KPI = tempo di prenotazione, numero errori, soddisfazione; rischi = resistenza dei docenti, budget limitato.)*

### Phase B: Business Architecture
Modella processi e attività, identifica le *capability* e definisce come creare valore. Le tecniche di scomposizione dell'azienda sono: **Business Capability Mapping**, **Organization Map**, **Value Stream Mapping**, **Activity/Business Process Model**, **Use-Case Models** e **Logical Data Model**. Il lavoro procede per iterazioni a partire da un **Business Scenario** — usato nelle fasi Preliminary, A e B — che deve essere *specifico, misurabile, realistico, azionabile e limitato nel tempo*. Output: Business Architecture (baseline + target), Architecture Definition Document aggiornato, Architecture Roadmap e requisiti architetturali. *(Esempio: capability map "Gestione esami → prenotazione, gestione appelli, verbalizzazione"; value stream "creazione appello → prenotazione → esame → verbalizzazione"; gap analysis AS-IS prenotazione manuale vs TO-BE online; trade-off tra soluzione semplice e completa.)*

#### I diagrammi dei casi d'uso (UML)
All'interno della Business Architecture si usano i **casi d'uso UML**, che esprimono le aspettative degli stakeholder e rispondono a tre domande: *cosa* viene descritto (il **sistema**), *chi* interagisce (gli **attori**) e *cosa* possono fare (i **casi d'uso**). Un **caso d'uso** descrive una funzionalità prevista dal sistema che porta un beneficio tangibile a uno o più attori; l'insieme di tutti i casi d'uso documenta la funzionalità complessiva. Un **attore** rappresenta un *ruolo* adottato dagli utenti (un utente può ricoprire più ruoli), sta *fuori* dai confini del sistema e si collega ai casi d'uso tramite *associazioni* (linee continue, sempre binarie, con possibili molteplicità); ogni attore comunica con almeno un caso d'uso. Gli attori si classificano in:
- **umano** (studente, professore) o **non-umano** (un server);
- **primario** (esegue il caso d'uso, ne riceve beneficio) o **secondario** (non riceve beneficio diretto);
- **attivo** (avvia l'esecuzione) o **passivo** (fornisce funzionalità per l'esecuzione).
La **descrizione strutturata** di un caso d'uso comprende: nome, breve descrizione, *precondizione* (prerequisito per la corretta esecuzione), *postcondizione* (stato del sistema dopo l'esecuzione), situazioni di errore e relativo stato del sistema, attori coinvolti, *trigger* (eventi che avviano il caso d'uso), *processo standard* (i singoli passi) e *processi alternativi*. *(Esempio: sistema di amministrazione studenti, attore Professore, casi d'uso "interrogazione dati studenti", "emissione certificato", "annunciare l'esame".)*

### Phase C: Information Systems Architectures
Definisce *quali dati* e *quali applicazioni* servono, allineando l'IT al business; si divide in due sotto-architetture. La **Data Architecture** definisce i dati necessari e come sono strutturati, gestiti e condivisi, con l'obiettivo di garantire dati corretti, coerenti e disponibili; le sue attività coprono modellazione dati (entità e relazioni, modelli), gestione dati (proprietà, qualità, sicurezza, accesso) e integrazione dati (condivisione, *evitare duplicazioni*). Qui è centrale la distinzione fra **requisiti funzionali (WHAT)** — cosa il sistema deve fare sui dati: creare, aggiornare, consultare, eliminare — e **requisiti non funzionali (HOW)** — come i dati devono essere gestiti: sicurezza (accessi, privacy, GDPR), qualità (accuratezza, completezza), disponibilità, integrità. La **Application Architecture** definisce le applicazioni necessarie, come sono strutturate e come interagiscono, con l'obiettivo di garantire integrazione ed *evitare duplicazioni di funzionalità*; le attività coprono modellazione applicativa (applicazioni, componenti, servizi), interazione tra applicazioni (comunicazione, flussi di dati) e supporto al business (allineamento ai processi, copertura dei requisiti). *(Esempio: il "portale studenti" comunica col "sistema esami", che a sua volta riusa il "sistema studenti" già esistente per non duplicare i dati anagrafici.)*

### Phase D: Technology Architecture
Identifica le tecnologie necessarie e definisce come supportano applicazioni e dati, garantendo affidabilità, sicurezza e disponibilità e preparando la base tecnica per l'implementazione. Le attività coprono modellazione tecnologica (tecnologie, componenti, servizi), infrastruttura (architettura, reti, ambienti on-premise/cloud), supporto alle applicazioni (esecuzione, gestione dati, integrazione tecnica) e qualità/sicurezza (sicurezza, disponibilità, performance, affidabilità). *(Esempio: architettura a 3 livelli frontend/application/database, server on-premise, backup e ridondanza per l'affidabilità.)*

### Phase E: Opportunities & Solutions
Conduce la pianificazione iniziale dell'implementazione: identifica le possibili soluzioni, le raggruppa in *progetti* e costruisce una prima roadmap. Le attività coprono identificazione soluzioni (valutare alternative *make/buy*, identificare building block), definizione progetti (*work packages*, prioritizzazione), pianificazione (roadmap, sequenza, dipendenze) e valutazione (costi-benefici, rischi). Output: soluzioni identificate, work package e progetti, Architecture Roadmap, analisi costi-benefici e rischi. *(Esempio: scelta "buy + personalizzazione" del sistema esami, riuso di autenticazione e database studenti esistenti, progetti separati per sistema/integrazione/portale.)*

### Phase F: Migration Planning
Affronta il passaggio dalla baseline al target, finalizzando un *piano dettagliato di implementazione e migrazione*. Le attività coprono pianificazione migrazione (ordinare i progetti nel tempo, priorità, dipendenze), consolidamento roadmap, valutazione (costi, rischi, ottimizzazione sequenza) e preparazione implementazione (piano, coordinamento, validazione con stakeholder). Output: *Implementation & Migration Plan*, Architecture Roadmap aggiornata, sequenza dei progetti, analisi costi/benefici/rischi. *(Esempio: prima il database studenti centralizzato, poi il sistema esami, poi l'integrazione col portale, infine il rilascio.)*

### Phase G: Implementation Governance
L'architettura definita viene *implementata e controllata*. L'obiettivo è garantire che l'implementazione rispetti l'architettura definita, controllare i progetti durante la realizzazione e assicurare coerenza tra soluzione e architettura. Le attività coprono implementation governance (monitorare, verificare conformità, gestire deviazioni), supporto ai progetti (linee guida, supporto ai team, problemi architetturali), controllo qualità (verifica qualità, validazione deliverable, rispetto standard) e gestione cambiamenti. Output: soluzioni validate, deliverable approvati, *Architecture Compliance Reports*, architettura aggiornata. *(Esempio: si verifica che il sistema esami usi il database centrale e non ne crei di duplicati, bloccando le implementazioni non conformi.)*

### Phase H: Architecture Change Management
Stabilisce le procedure per *gestire le modifiche* alla nuova architettura, con l'obiettivo del miglioramento continuo. Le attività coprono gestione cambiamenti (identificare richieste, valutare impatti, *classificare in minori/maggiori*), decisione e pianificazione (decidere, aggiornare l'architettura, eventualmente *attivare un nuovo ciclo ADM*), monitoraggio (evoluzione del sistema, allineamento col business, nuove esigenze) e miglioramento continuo. Output: *Change Requests*, architettura aggiornata, decisioni sui cambiamenti, avvio di nuovi cicli ADM. Il principio chiave è che i cambiamenti *minori* si implementano subito, mentre quelli *maggiori* (es. una nuova app mobile, nuove normative GDPR) fanno ripartire l'intero ciclo ADM. *(Esempio: richiesta di app mobile → cambiamento maggiore → nuova fase progettuale.)*

### Requirements Management (gestione trasversale)
È il processo *al centro* dell'ADM, che gestisce i requisiti per *tutte* le fasi: li raccoglie, li mantiene aggiornati, garantisce coerenza tra fasi e supporta le decisioni. Le attività coprono gestione requisiti (identificare, documentare, classificare in funzionali/non funzionali), evoluzione requisiti (aggiornare, gestire modifiche, *tracciare*) e supporto all'ADM (fornire input alle fasi, verificare coerenza, validare). Output: *Architecture Requirements Specification*, *Requirements Repository*, requisiti aggiornati. La *tracciabilità* è l'aspetto più potente: lo stesso requisito "prenotazione esame" si segue dalla Phase B (processo) alla Phase C (dato "prenotazione" e applicazione "portale studenti") alla Phase D (tecnologia web) alle Phase E/F (progetto di sviluppo), garantendo che ogni bisogno sia coperto end-to-end.

### Il flusso dei deliverable tra le fasi
Un aspetto che lega tutto l'ADM è che ogni deliverable è *output* di alcune fasi e *input* di altre, creando un flusso coerente. Per esempio l'*Architecture Vision* è prodotta in Phase A ed E e alimenta tutte le fasi successive da B a H più il Requirements Management; l'*Architecture Definition Document* è prodotto e raffinato lungo le fasi A–F e usato fino alla G/H; i *Solution Building Block* prodotti in G diventano input per le fasi A–G di cicli successivi; lo *Statement of Architecture Work* prodotto in Phase A accompagna tutte le fasi. Questo intreccio input/output è ciò che rende l'ADM un processo *iterativo e tracciabile*, in cui nessuna fase è isolata e ogni artefatto ha un ruolo lungo l'intero ciclo di vita dell'architettura.

---
# Lezione 8 — ArchiMate: introduzione

## Che cos'è ArchiMate
**ArchiMate** è un *linguaggio per la modellazione dell'Enterprise Architecture*: una notazione visuale che potenzia la pratica di EA e aiuta a descrivere e comprendere sistemi complessi. È usato principalmente per descrivere i *building block* (i mattoni dell'architettura), è *estensibile* ed è mantenuto da **The Open Group** — lo stesso ente di TOGAF, il che spiega la loro stretta complementarità. Mentre TOGAF dà il *metodo* (l'ADM) per costruire l'architettura, ArchiMate dà il *linguaggio grafico* per rappresentarla.

### A cosa serve una descrizione di architettura
Una descrizione di architettura ha molteplici usi pratici, ed è utile averli presenti perché motivano la disciplina:
- come base per le attività di *progettazione e sviluppo* del sistema;
- come base per *analizzare e valutare* implementazioni alternative e architetture alternative;
- come *documentazione* di sviluppo e manutenzione;
- per *comunicare* tra le parti coinvolte (sviluppo, produzione, deployment, operatività, manutenzione);
- per pianificare la *transizione* da un'architettura legacy a una nuova.

## Gli elementi di interesse
ArchiMate (in linea con lo standard ISO/IEC/IEEE 42010) ruota attorno a cinque elementi concettuali: **stakeholder, concern, view, viewpoint, model**. Capirne le relazioni è la chiave dell'intero linguaggio.

### Stakeholder e concern
Uno **stakeholder** è chi ha un *interesse* nel sistema che si sta architettando: utenti, operatori, proprietari, fornitori, sviluppatori, manutentori. Un **concern** (preoccupazione/interesse) è un interesse verso il sistema rilevante per uno o più stakeholder, per esempio:
- gli *scopi* del sistema;
- l'*idoneità* dell'architettura a raggiungere quegli scopi;
- la *fattibilità* di costruzione e deployment;
- i *rischi e impatti* potenziali sugli stakeholder durante il ciclo di vita;
- la *manutenibilità ed evolvibilità* del sistema.
La lista di possibili concern è vastissima (funzionalità, fattibilità, usabilità, performance, affidabilità, sicurezza, privacy, conformità normativa, costo, tempistiche, flessibilità, modularità, ecc.): di fatto qualunque proprietà del sistema può essere un concern per qualcuno.

### Viewpoint e view
La distinzione fra viewpoint e view è il punto concettuale più importante.
- Un **viewpoint** stabilisce le *convenzioni* per costruire, interpretare e usare le viste che inquadrano determinati concern. È *"dove stai guardando"* (il punto di osservazione).
- Una **view** (vista) cattura la *prospettiva* di uno stakeholder nei termini dei suoi concern. È *"ciò che vedi"*. Una descrizione di architettura include una o più viste, e ogni vista affronta uno o più concern.
L'esempio del traffico aereo chiarisce tutto. Il **pilota** ha un viewpoint ("come specificare posizione e direzione del *mio* aereo") e la corrispondente vista è "dove sono e in che direzione va il mio aereo". Il **controllore di volo** ha un viewpoint diverso ("come specificare posizioni e direzioni di *tutti* gli aerei nello spazio aereo") e la sua vista è "la situazione complessiva come somma delle posizioni e direzioni di tutti gli aerei". *Stessa realtà, viewpoint diversi, viste diverse*: ciascuno vede ciò che gli serve.

### Model
Un **architecture model** è una *rappresentazione* di un soggetto di interesse, in scala ridotta, semplificata e/o astratta. È l'astrazione che permette di ragionare sul sistema senza la sua complessità reale.

## Cosa fornisce ArchiMate
ArchiMate mette a disposizione cinque cose: un *linguaggio* con concetti per descrivere le architetture, un *framework* per organizzare questi concetti, una *notazione grafica*, una *visione sulle visualizzazioni* per i diversi stakeholder, e uno *standard aperto* mantenuto da The Open Group. Nel corso non si copre tutto il linguaggio, ma ci si concentra su tre layer e sulle viste che ne derivano:
- il **Technology layer** per modellare l'infrastruttura,
- l'**Application layer** per modellare le applicazioni usate dall'organizzazione,
- il **Business layer** per modellare i processi principali.
I risultati della modellazione saranno l'*Implementation and Deployment view*, la *Technology view* e la *Technology usage view*.

## Il CORE framework di ArchiMate
Il framework "core" di ArchiMate organizza i concetti lungo due dimensioni: i **layer** (le righe) e gli **aspect** (le colonne).

### I tre layer
I layer rappresentano i livelli dell'azienda, con una logica di *servizio dall'alto verso il basso*:
- **Business layer** — offre prodotti e servizi ai clienti esterni.
- **Application layer** — *supporta* il business layer con servizi applicativi, realizzati da applicazioni software.
- **Technology layer** — offre i servizi infrastrutturali necessari a far girare le applicazioni, realizzati da computer e comunicazione.
La logica di fondo è quella del "servire": la tecnologia serve le applicazioni, che servono il business. È la stessa stratificazione dei livelli architetturali vista in TOGAF, qui resa in un linguaggio grafico.

### I tre aspect
Gli aspect rappresentano la natura degli elementi, ed è una distinzione che ritorna in ogni layer:
- **Active structure** — gli elementi *strutturali* che mostrano comportamento: i "soggetti" dell'attività (attori di business, componenti applicativi, dispositivi). Sono il *chi/cosa* agisce.
- **Behavior** — il *comportamento* svolto dagli attori (processi, funzioni, eventi, servizi); gli elementi strutturali sono *assegnati* a quelli comportamentali per mostrare chi mostra quel comportamento. È il *cosa si fa*.
- **Passive structure** — gli *oggetti* su cui il comportamento è esercitato: tipicamente *information object* nel Business layer e *data object* nell'Application layer, ma anche oggetti fisici. È il *su cosa* si agisce.
La tripletta active-behavior-passive è la grammatica di base: un soggetto (active) compie un'azione (behavior) su un oggetto (passive), in ciascuno dei tre layer.

## Le relazioni di ArchiMate (cheatsheet)
ArchiMate definisce un insieme di **relazioni** che collegano gli elementi, ed è essenziale conoscerle perché sono il "verbo" del linguaggio. Le principali:
- **composition** (composizione) — un elemento è composto da altri (legame forte, le parti non esistono senza il tutto).
- **aggregation** (aggregazione) — un elemento raggruppa altri (legame più debole).
- **assignment** (assegnazione) — collega un elemento *active structure* al comportamento che esegue (chi fa cosa).
- **realization** (realizzazione) — un elemento più concreto *realizza* uno più astratto.
- **serving** (servizio) — un elemento *serve* un altro fornendogli funzionalità.
- **triggering** (innesco) — una relazione temporale/causale tra comportamenti (uno scatena l'altro).
- **flow** (flusso) — il trasferimento di informazione o valore tra elementi.
- **association** (associazione) — una relazione generica non specificata.
Incrociando layer, aspect e relazioni si ottiene la *cheatsheet* di ArchiMate: una matrice in cui ogni cella (es. Business × Active structure, Application × Behavior) ha i propri simboli grafici, collegati dalle relazioni viste.

## Relazione con altri standard
ArchiMate non vive isolato ma si *mappa* su altri standard, e capire questi ponti aiuta a collocarlo.
- **TOGAF** — ArchiMate fornisce la notazione per rappresentare le architetture che TOGAF costruisce con l'ADM; i suoi layer si mappano sui livelli architetturali di TOGAF.
- **Zachman** — gli elementi di ArchiMate si possono collocare nelle celle della matrice di Zachman.
- **BPMN** — entrambi modellano processi di business, ma con livelli di dettaglio opposti e complementari: ArchiMate è usato per i processi *ad alto livello* e le loro relazioni con il contesto enterprise, mentre BPMN supporta la modellazione *dettagliata* di sotto-processi e task fino a specifiche eseguibili, ma *manca* del contesto enterprise più ampio (non modella i servizi applicativi che supportano un processo o gli obiettivi che deve soddisfare).
- **UML** — ArchiMate deriva diversi concetti da UML: nel Business layer il *business process* si mappa sugli *activity diagram* UML e *business actor/role* sugli *actor* UML; nell'Application layer l'*application component* corrisponde al *component* UML, l'*application function* agli *activity diagram* e l'*application service* allo *use-case diagram*; il Technology layer corrisponde direttamente a UML. Molte relazioni di ArchiMate hanno legami stretti con UML.
Lo strumento raccomandato per modellare è **Archi** (gratuito), con in alternativa gli stencil per Microsoft Visio.

---
# Lezione 9 — ArchiMate Business Layer

## Inquadramento
Il **Business layer** di ArchiMate modella i processi e l'organizzazione che offrono prodotti e servizi ai clienti esterni. Come tutti i layer di ArchiMate, i suoi elementi si dividono nei tre **aspect** già visti — *active structure* (chi agisce), *behavior* (cosa si fa), *passive structure* (su cosa si agisce) — più l'elemento di *grouping*. Tutta la potenza espressiva sta poi nelle **relazioni** che collegano questi elementi, che sono il vero cuore del capitolo.

## Elementi active structure (i "soggetti")
Sono gli elementi strutturali interni che mostrano comportamento:
- **Business actor** — un'entità aziendale in grado di eseguire comportamenti (una persona, un'unità organizzativa).
- **Business role** — la *responsabilità* di eseguire un comportamento specifico, ovvero il *ruolo* che un attore svolge in una particolare azione o evento. La distinzione attore/ruolo è importante: lo stesso attore può ricoprire ruoli diversi.
- **Business collaboration** — un'aggregazione di due o più elementi di struttura attiva che *lavorano insieme* per eseguire un comportamento collettivo.
- **Business interface** — un punto di accesso tramite cui un servizio aziendale è messo a disposizione dell'ambiente.
L'esempio canonico è il *Contact Center di ArchiSurance*: composto da tre dipendenti (Greg, Joan, Larry), serve i clienti tramite tre interfacce (Telefono, E-mail, Web Chat). Greg è "analista sinistri viaggio", Joan "specialista prodotti casa", Larry "rappresentante servizio clienti"; i primi due sono *specializzazioni* di un ruolo "Specialista", e "Aggiudicazione sinistri ad alto rischio" è una *collaborazione* fra "Specialista" e "Rappresentante del Servizio Clienti".

## Elementi behavior (il "cosa si fa")
- **Business process** — una *sequenza* di comportamenti che produce un risultato specifico (un insieme definito di prodotti o servizi). È orientato al risultato.
- **Business function** — una raccolta di comportamenti basata su criteri scelti (tipicamente risorse e competenze richieste), allineata all'organizzazione ma non necessariamente governata esplicitamente da essa. A differenza del processo (orientato al *risultato*), la funzione è orientata alle *competenze/risorse*.
- **Business interaction** — un'unità di comportamento *collettivo* eseguita da due o più attori, ruoli o collaborazioni.
- **Business service** — un comportamento *esposto* esplicitamente che un ruolo/attore/collaborazione mette a disposizione del proprio ambiente.
- **Business event** — rappresenta una *modifica dello stato* dell'organizzazione (qualcosa che accade e innesca comportamento).
L'esempio della *Gestione dei sinistri* lega tutti questi concetti: è una *business function* composta da più *processi* e da un'*interaction*, che realizza il *servizio* "Elaborazione dei reclami". L'*evento* "Reclamo depositato" attiva il processo "Accetta reclamo", che attiva "Assegna reclamo"; secondo il tipo, si esegue il processo "Aggiudica reclamo standard" *oppure* l'*interaction* "Aggiudica reclamo ad alto rischio" — è un'interaction proprio perché la politica aziendale vuole *due persone* coinvolte per ridurre il rischio di frode. Dopo l'aggiudicazione, "Notifica al cliente" e "Pagamento reclamo" girano in *parallelo*, e al termine di entrambi si attiva "Chiudi reclamo".

## Elementi passive structure (il "su cosa")
- **Business object** — un concetto usato all'interno di un particolare dominio aziendale (es. una polizza, un sinistro).
- **Representation** — la *forma percettibile* dell'informazione fornita da un business object (es. una fattura cartacea che rappresenta i dati di fatturazione).
- **Contract** — una specificazione (formale o informale) di un *accordo* tra fornitore e consumatore, che fissa diritti, obblighi e parametri funzionali e non funzionali dell'interazione.
- **Product** — un insieme di servizi e/o elementi di struttura passiva, accompagnato da un contratto/insieme di accordi, offerto *nel suo insieme* ai clienti.
L'esempio del *trading* (vendita di beni ricondizionati) mostra il *Product* "Refurbished goods" che aggrega la "Auction page description", la garanzia "1-month warranty" e i "Goods", offerto tramite il contratto "Trading partnership" fra "Seller" e "Buyer".

## Grouping
L'elemento di **grouping** aggrega o compone un gruppo *arbitrario* di concetti — elementi e/o relazioni, dello stesso tipo o di tipi diversi. Serve a raccogliere visivamente elementi correlati che non condividono necessariamente un legame strutturale predefinito.

## Le relazioni di ArchiMate
Le relazioni sono il "verbo" del linguaggio e si dividono in quattro categorie: *strutturali*, *di dipendenza*, *dinamiche* e *altre*, più i *connettori*.

### Relazioni strutturali
Modellano la costruzione statica o la composizione di concetti.
- **Composition (composizione)** — un elemento *è costituito da* uno o più altri concetti; è un legame *forte*, con dipendenza di esistenza: se si elimina il composto, si eliminano anche le parti. *(Es. "Financial Processing" è composto da Contabilità, Pagamento, Fatturazione.)*
- **Aggregation (aggregazione)** — un elemento *combina* uno o più concetti, *senza* dipendenza di esistenza; è un legame *debole*. *(Es. il "File cliente" aggrega una "Polizza" e un "Sinistro".)*
- **Assignment (assegnazione)** — rappresenta l'allocazione di *responsabilità*, l'esecuzione di un comportamento, l'archiviazione o l'esecuzione; collega tipicamente un elemento active structure al comportamento che esegue. *(Es. il componente "Finanza" è assegnato alla funzione "Elaborazione transazioni"; un "cliente" assegnato al ruolo "assicurato".)*
- **Realization (realizzazione)** — un elemento *più concreto* ("come"/"fisico") realizza uno *più astratto* ("cosa"/"logico"): un processo realizza un servizio, un data object realizza un business object, un artefatto realizza un componente applicativo. *(Es. la funzione "Elaborazione transazioni" realizza il "Servizio di fatturazione".)*
La distinzione **aggregation vs composition** è frequente: l'aggregazione è un'associazione *debole* (gli oggetti possono esistere indipendentemente, eliminarne uno non tocca l'altro), la composizione è *forte* (gli oggetti sono fortemente dipendenti, eliminarne uno influisce sull'altro).

### Relazioni di dipendenza
Modellano come un elemento *supporta* un altro.
- **Serving (servizio)** — un elemento *fornisce la propria funzionalità* a un altro; descrive come servizi/interfacce servono le entità dell'ambiente. *(Es. l'"Interfaccia di pagamento" serve il "Cliente", il "Servizio di pagamento" serve il processo "Paga fatture".)*
- **Access (accesso)** — la capacità di un comportamento o di un elemento active structure di *osservare o agire* su un elemento passive structure; la punta della freccia indica creazione, modifica o utilizzo. *(Es. "Crea fattura" scrive il business object "Fattura", "Invia fattura" lo legge.)*
- **Influence (influenza)** — un elemento *influenza* l'implementazione o il raggiungimento di un elemento motivazionale (è la forma "debole" della realizzazione verso le motivazioni).
- **Association (associazione)** — una relazione *non specificata*, o non rappresentata da altre relazioni ArchiMate; utile nei primi modelli di alto livello, da raffinare poi in relazioni più specifiche. *(Es. un contratto assicurativo associato al profilo cliente e all'oggetto assicurato.)*

### Relazioni dinamiche
Modellano le dipendenze *comportamentali* nel tempo.
- **Triggering (innesco)** — una relazione *temporale o causale*: parte dell'elemento sorgente deve *completarsi* prima che l'elemento destinazione possa iniziare. È la relazione che dà l'ordine ai processi.
- **Flow (flusso)** — il *trasferimento* da un elemento all'altro di informazioni, beni o denaro tra elementi comportamentali. *(Es. "Valutazione dei sinistri" inoltra le decisioni a "Liquidazione dei sinistri".)*
La differenza fra triggering e flow è sottile ma importante: il *triggering* esprime la *sequenza* (cosa viene prima/dopo), il *flow* esprime il *passaggio di qualcosa* (informazione, valore) da un elemento all'altro.

### Altre relazioni e connettori
- **Specialization (specializzazione)** — un elemento è un *tipo particolare* di un altro. *(Es. "Stipulare assicurazione di viaggio" e "Stipulare assicurazione bagaglio" sono specializzazioni di "Stipulare un'assicurazione".)*
- **Junction (giunzione)** — non è una relazione vera, ma un *connettore* che collega relazioni dello *stesso tipo*. Serve a esprimere combinazioni logiche: una giunzione *AND* indica che più elementi realizzano *insieme* un servizio (es. "Vendite" e "Finanza" realizzano insieme "Fatturazione"), una giunzione *OR* indica un'alternativa (es. "Valutare la richiesta" può essere "Accettato" o "Rifiutato").

## Esercizi (viste organizzative e di processo)
Gli esercizi del capitolo chiedono di costruire **viste organizzative** e **viste di processo** in ArchiMate a partire da descrizioni testuali; servono ad applicare elementi e relazioni viste sopra.
- **Speedy (delivery company)** — modellare un nuovo servizio di reportistica per il top management: in una variante offerto tramite *interfaccia Web* (il manager seleziona area geografica, analizza i prodotti, crea il report), in un'altra tramite *interazione con un dipendente* analista che crea il report su richiesta. Mette a confronto un servizio esposto via *interface* vs via *interaction*.
- **IC (compagnia assicurativa)** — modellare un servizio di assicurazione online per piccoli oggetti (<2000) per clienti affidabili: arriva la richiesta, si controllano credenziali e cronologia, se il cliente è affidabile carica foto e dettagli, un addetto stima il prezzo; se <2000 si produce il contratto firmato (in una variante via sistema, in un'altra via *interaction* fra cliente e legale rappresentante), se >2000 il sistema invia le condizioni. Esercita *triggering*, scelte (junction OR) e *interaction*.
- **RedBrake (manifattura freni)** — generare la *vista dell'organizzazione*: stabilimenti produttivi in Brasile, Vietnam, Cina e sede centrale in Svizzera dove si gestiscono HR, amministrazione, raccolta ordini e reclami. Esercita la modellazione di attori/ruoli e unità organizzative distribuite.
- **Retail attrezzature sportive** — modellare il processo di aggiornamento del catalogo *assegnato* al team marketing: aggiornare lista attrezzature → prezzi attrezzature → prezzi servizi → (in una variante, se il totale servizi supera 2000 coinvolgere il Responsabile marketing per l'*approvazione*) → stile del catalogo → creazione nuovo catalogo. Esercita *assignment*, *triggering* sequenziale e *junction* condizionale.
- **Palestra** — modellare l'iscrizione di un nuovo cliente: il prezzo si può negoziare con *intermediari* o con l'*amministrazione*, formalizzata la richiesta si crea il contratto, che le parti discutono e, se tutte soddisfatte, firmano. Esercita *collaboration*, alternative e il ciclo di negoziazione/firma del contratto.

---
# Lezione 10 — ArchiMate Application Layer

## Inquadramento
L'**Application layer** di ArchiMate modella le *applicazioni software* usate dall'organizzazione, che *supportano* il Business layer con servizi applicativi. Come ogni layer, i suoi elementi seguono i tre aspect — *active structure*, *behavior*, *passive structure* — e usano lo *stesso insieme di relazioni* del Business layer (composition, aggregation, assignment, realization, serving, access, influence, association, triggering, flow, specialization, junction). La novità qui è terminologica e di dominio: si passa dagli attori e processi *aziendali* ai componenti e funzioni *applicativi*.

## Elementi active structure
- **Application component** — un *incapsulamento* delle funzionalità dell'applicazione, allineato alla struttura di implementazione, *modulare e sostituibile*. È il mattone del software (es. il "CRM system", il "Back-office system").
- **Application collaboration** — un'aggregazione di due o più componenti che *interagiscono* per eseguire un comportamento collettivo.
- **Application interface** — il punto di accesso tramite cui un servizio applicativo è reso disponibile a un utente, a un altro componente o a un nodo (es. "Web interface", "Application API", "Character interface").

## Elementi behavior
- **Application process** — una *sequenza* di comportamenti dell'applicazione che produce un risultato specifico.
- **Application function** — comportamento *automatizzato* eseguibile da un componente (es. "Customer relation management", "Manage claims", "Claim payments").
- **Application interaction** — unità di comportamento *collettivo* eseguita da due o più componenti.
- **Application service** — comportamento *esposto* esplicitamente (es. "Client registration", "Claim handling", "Payments").
- **Application event** — elemento di comportamento che indica una *modifica dello stato*.

## Struttura vs comportamento: chi esegue e cosa esegue
ArchiMate distingue sempre fra elementi *strutturali* (i componenti, nell'application layer) ed elementi *comportamentali* (le funzioni). Proprio in questo layer è spesso difficile distinguere fra *chi* sta eseguendo (l'elemento attivo, cioè il componente) e *cosa* viene eseguito (l'elemento comportamentale, cioè la funzione o il processo); tenerli separati è la disciplina chiave. Alcune regole guida:
- funzioni e processi sono svolti da un *unico ruolo*; se sono coinvolti più ruoli, si usa un *nodo* o un'*interaction* (eseguita da una collaboration) per renderlo esplicito;
- funzioni e processi possono essere *composti* da altri elementi comportamentali;
- si usa una **function** quando gli elementi che la compongono hanno *qualcosa in comune* (es. lo stesso ruolo, le stesse risorse);
- si usa un **process** quando gli elementi che lo compongono *raggiungono collettivamente lo stesso obiettivo*.
La distinzione function/process è dunque la stessa del Business layer: la *function* aggrega per affinità di risorse/competenze, il *process* aggrega per obiettivo comune.

## Elementi passive structure
- **Data object** — *dati strutturati* per l'elaborazione automatizzata (es. "Customer data", "Policy data", "Claim data"). È l'equivalente applicativo del *business object*: dove il business object è un concetto del dominio, il data object è la sua forma elaborabile dal software.

## Il modello applicativo di base e l'allineamento con il business
Componendo gli elementi si ottiene un **modello applicativo di base**: per esempio il componente "CRM system" realizza il servizio "Client registration" tramite la "Web interface", esegue la funzione "Customer relation management", accede al data object "Customer data" e *serve* (relazione *serving*) il componente "Back-office system". L'aspetto più importante è però l'**allineamento tra Application e Business layer**: i servizi applicativi *servono* i processi di business. Nell'esempio della gestione sinistri, il processo di business "Handle claim" (con i suoi passi Register → Accept/Reject → Adjudicate → Pay) è *supportato* dai servizi applicativi "Client registration", "Claim handling", "Payments", a loro volta realizzati dai componenti CRM e Back-office. Questo allineamento verticale è il cuore di ArchiMate: mostra *come l'IT supporta il business*, rendendo esplicito quale servizio applicativo sostiene quale processo aziendale — esattamente la visione integrata che mancava nelle "isole informatiche".

## Esercizi
- **Esercizio 1 — Speedy (delivery)**: modellare a livello applicativo il nuovo servizio di reportistica offerto via interfaccia Web (selezione area geografica → analisi prodotti → creazione report). Speedy si appoggia a un *sistema ERP* (recupera info su zone e prodotti) e a un *data warehouse* che legge periodicamente dall'ERP via *API* per creare un *data mart*; un *modulo di reportistica* interagisce col data mart per abilitare le attività dell'utente. Esercita componenti applicativi, interfacce, *serving* e flussi di dati fra applicazioni.
- **Esercizio 2 — IC (assicurazione)**: modellare il sistema informatico a supporto del servizio assicurativo online (<2000$). È composto da un *sistema CRM* (gestisce le info clienti e ne verifica l'affidabilità), un programma ad-hoc "estimator" esposto al dipendente tramite *interfaccia desktop* per stimare il prezzo, e un'*applicazione web* a supporto della finalizzazione del contratto. Esercita la mappatura fra i passi del processo di business e i componenti/servizi applicativi che li supportano.

---
# Lezione 11 — ArchiMate Technology Layer

## Inquadramento
Il **Technology layer** di ArchiMate modella l'*infrastruttura* — hardware, software di sistema, reti — che offre i servizi necessari a far girare le applicazioni. È il livello più basso della catena del "servire": la tecnologia serve le applicazioni, che servono il business. Anche qui valgono i tre aspect e lo *stesso insieme di relazioni* dei layer precedenti; cambia il vocabolario, che diventa quello dei sistemi computazionali.

## Elementi active structure
Il Technology layer ha l'insieme di elementi attivi più ricco, perché distingue le diverse risorse fisiche e di rete:
- **Node** — una risorsa computazionale o fisica che *ospita, manipola o interagisce* con altre risorse (es. "CRM Server", "Database server", "Legacy system"). È l'elemento attivo principale del layer.
- **Technology collaboration** — un aggregato di due o più nodi che lavorano insieme per un comportamento collettivo.
- **Technology interface** — il punto di accesso tramite cui un servizio tecnologico offerto da un nodo è reso accessibile (es. "Win32 API", "OCI", "RPG ILE").
- **Device** — una risorsa IT *fisica* su cui si distribuiscono software di sistema ed elementi (es. "X86-64 server", "SPARC server", "AS/400").
- **System software** — software che fornisce un *ambiente* per archiviazione, esecuzione e utilizzo di software e dati (es. "Windows Server 2008 R2", "Oracle 10g R2", "OS/400 V7R1").
- **Communication network** — un insieme di strutture che collegano i sistemi per *trasmettere, instradare e ricevere* dati (es. "Corporate network").
- **Path** — un collegamento tra due o più nodi attraverso cui essi *scambiano dati*.
La distinzione *node / device / system software* è la più importante: un nodo è spesso *composto* da un device (l'hardware fisico) e da un system software (il sistema operativo o il middleware che ci gira sopra). Per esempio un "CRM Server" (nodo) è composto da un "X86-64 server" (device) e da "Windows Server 2008 R2" (system software).

## Elementi behavior
- **Technology process** — una *sequenza* di comportamenti tecnologici che raggiunge un risultato specifico.
- **Technology function** — elemento che raggruppa il comportamento *infrastrutturale* eseguibile da un nodo.
- **Technology interaction** — unità di comportamento *collettivo* eseguita da due o più nodi.
- **Technology service** — unità di funzionalità *visibile esternamente*, fornita da uno o più nodi ed esposta tramite interfacce ben definite (es. "CRM execution service", "CRM data service", "Backoffice data service").
- **Technology event** — elemento che denota una *modifica dello stato*.
L'esempio del backup illustra un processo tecnologico: l'evento "1st day of week" innesca "Perform incremental Backup", poi "Verify backup", che porta agli eventi "Backup succeeded" o "Backup failed".

## Elementi passive structure
- **Artifact** — un *dato* (un file, un eseguibile, una libreria) usato o prodotto in un processo di sviluppo software, o dalla distribuzione e dal funzionamento di un sistema. È l'equivalente, a livello tecnologico, del data object applicativo: rappresenta la forma *fisica/deployabile* del software e dei dati.

## Il modello tecnologico di base e l'allineamento con l'applicazione
Il **modello tecnologico di base** compone questi elementi: i nodi (CRM Server, Database server, Legacy system) ospitano system software, espongono servizi tecnologici tramite interfacce e sono collegati dalla *Corporate network* (con relazioni di *association*). L'aspetto centrale è di nuovo l'**allineamento**, stavolta tra Application e Technology layer: i servizi tecnologici *servono* i componenti applicativi. Nell'esempio, il "CRM execution service" e il "CRM data service" (offerti dal CRM Server e dal Database server) *supportano* il componente applicativo "CRM system", mentre il "Backoffice data service" supporta il "Back-office system"; i data object applicativi ("Customer data", "Policy data", "Claim data") sono *realizzati* da artifact concreti memorizzati nei database fisici ("Customer database", "Policy database", "Claim database"). Mettendo insieme i tre layer si ottiene la **vista completa** dell'architettura — dal processo di business "Handle claim", giù attraverso i servizi e componenti applicativi, fino ai server e alle reti che li eseguono — che è esattamente l'obiettivo di ArchiMate: rendere visibile in un unico modello *come l'infrastruttura tecnologica supporta le applicazioni, che a loro volta supportano i processi di business*.

---
# Lezione 12 — ArchiMate: elementi compositi

## Raggruppamento
Quando un modello cresce, serve **aggregare** elementi correlati per leggibilità. ArchiMate offre l'elemento di **grouping**, che raccoglie insieme concetti correlati. Una prassi tipica è raggruppare gli elementi appartenenti a una *stessa organizzazione esterna*: si raggruppano le organizzazioni esterne, mentre di solito *non* si raggruppa l'organizzazione *target* (quella che stiamo modellando) per non appesantire il diagramma. L'esempio mostra due organizzazioni distinte (Organization 1 e Organization 2), ciascuna col proprio gruppo di nodi, collegate da una rete: il raggruppamento rende immediato capire "chi appartiene a chi".

## Relazioni derivate
ArchiMate distingue fra relazioni *"standard"* (quelle esplicite viste finora) e **relazioni derivate**, che rappresentano lo *stesso modello sottostante* in forma sintetica. L'idea è che, data una catena di relazioni standard fra elementi (per esempio A serve B che serve C), si può *derivare* una relazione diretta equivalente (A serve C) senza disegnare tutti i passaggi intermedi. Le relazioni derivate servono a produrre viste più astratte e leggibili a partire da un modello dettagliato, mantenendo la coerenza con il modello completo.

## L'annidamento (nesting)
L'**annidamento** è la tecnica per *contenere* graficamente elementi figli dentro elementi genitori, riducendo la complessità visiva. Il principio è che le relazioni di **assignment** e **realization** consentono di annidare gli elementi figli all'interno dei genitori: invece di disegnare un nodo, il suo device, il suo system software e i loro collegamenti come elementi separati con frecce, si introduce un *nodo astratto* (es. "Database Server") che *aggrega* device, system software e gli elementi del sistema, mostrandoli annidati al suo interno. In questo modo *tutta l'infrastruttura si riduce a un unico nodo*: si parte da una vista in cui ogni elemento è mostrato con tutte le sue relazioni, e si arriva a una vista compatta in cui i dettagli sono "ripiegati" dentro il contenitore. È lo stesso principio delle relazioni derivate, applicato alla disposizione grafica.

## Le viste della tecnologia
Dal modello si producono due viste complementari del Technology layer:
- la **Technology view** (visualizzazione del livello tecnologico) — mostra l'infrastruttura in sé (nodi, device, software, reti);
- la **Technology usage view** (visualizzazione dell'utilizzo della tecnologia) — mostra *come* applicazioni e business *usano* quell'infrastruttura.
La distinzione è utile: la prima descrive *cosa c'è*, la seconda descrive *a cosa serve*, cioè il legame fra l'infrastruttura e ciò che la consuma.

## Definizione dell'architettura: on-premises vs cloud
Un'applicazione frequente di questi concetti è modellare *dove* risiede l'ERP aziendale.
- Nell'architettura **on-premises tradizionale** tutto è interno all'azienda: gli utenti interni e i negozi (shops) accedono via WEB SERVER all'**ERP**, che ospita i moduli (Accounting, Administration). L'infrastruttura è interamente di proprietà e gestione aziendale. Si possono modellare casi come "il modulo di contabilità gira sull'Operating System" o "un soggetto esterno accede al sistema informativo aziendale".
- Nell'architettura **Cloud ERP** parte dell'infrastruttura è esternalizzata: alcuni moduli o servizi (es. CAD/Design) risiedono su provider cloud, mentre utenti interni e negozi accedono comunque all'ERP. Il cloud sposta la responsabilità dell'infrastruttura dal cliente al fornitore.

## I livelli del cloud: SaaS, PaaS, IaaS
La distinzione fondamentale del capitolo è fra i tre **modelli di servizio cloud**, che differiscono per *quanto* il fornitore gestisce e *quanto* resta al cliente.
- **IaaS (Infrastructure as a Service)** — il provider offre l'*infrastruttura* virtualizzata: server virtuali, rete virtuale, virtual appliance. Il cliente gestisce tutto ciò che ci sta sopra (sistema operativo, middleware, applicazioni). È il livello più "basso" e flessibile.
- **PaaS (Platform as a Service)** — il provider offre una *piattaforma* di esecuzione (es. esecuzione di applicazioni J2EE/EJB, custom function): il cliente sviluppa e rilascia le proprie applicazioni senza gestire l'infrastruttura sottostante.
- **SaaS (Software as a Service)** — il provider offre direttamente il *software* pronto all'uso (es. word processing, web interface): il cliente lo usa senza preoccuparsi né di piattaforma né di infrastruttura. È il livello più "alto" e meno gestito dal cliente.
La progressione IaaS → PaaS → SaaS corrisponde a una *delega crescente* al fornitore: più si sale, meno il cliente gestisce, meno controllo ha ma meno responsabilità si assume. ArchiMate permette di modellare esplicitamente a quale livello (SaaS/PaaS/IaaS provider) è affidato ciascun pezzo dell'architettura.

## Architetture client-server: i tier
Il capitolo richiama le architetture a livelli (*tier*), modellabili in ArchiMate:
- **Client a 2 livelli (2-tier)** — il client comunica direttamente con un server; può esporre uno o più servizi.
- **Architettura a 3 livelli (3-tier)** — separa tre strati, tipicamente *presentazione (P), applicazione (A) e dati (D)*, con un server intermedio fra client e database.
La scelta del numero di tier riflette quanto si separano presentazione, logica e dati: più tier significa maggiore modularità e scalabilità, ma anche maggiore complessità.

## Virtualizzazione: bare metal vs hosted
Infine, la **virtualizzazione** dei server si presenta in due modalità:
- **Bare metal** — l'hypervisor gira *direttamente sul server fisico*, senza un sistema operativo ospite sottostante; i server virtualizzati stanno sopra l'hypervisor che controlla l'hardware nudo. È più efficiente e tipico dei data center.
- **Hosted** — l'hypervisor gira *sopra un sistema operativo ospite* installato sul server fisico; i server virtualizzati stanno sopra l'hypervisor che a sua volta sta sopra l'OS. È più semplice da installare ma meno efficiente.
La differenza chiave è *cosa* sta sotto l'hypervisor: l'hardware nudo (bare metal) o un sistema operativo (hosted). Modellare questa distinzione in ArchiMate aiuta a documentare scelte infrastrutturali con impatto su prestazioni e gestione.

---
# Lezione 13 — ArchiMate: esercizi di modellazione

## Inquadramento
Questa lezione è interamente costituita da **esercizi di modellazione completa** in ArchiMate, in cui da una descrizione testuale si deve costruire un modello che attraversa i tre layer (Business, Application, Technology). Sono la sintesi applicata di tutto il percorso: per ciascun caso si individuano gli *elementi* (attori, processi, componenti, nodi) e le *relazioni* (serving, assignment, triggering, realization, ecc.), e si producono le viste di allineamento fra i livelli. Di seguito i tre casi con le caratteristiche di modellazione da cogliere.

## Esercizio 1 — BIM (catalogo prodotti)
**Scenario.** BIM raccoglie informazioni sui prodotti dai produttori e le presenta ai potenziali acquirenti. I *produttori* inseriscono i prodotti secondo uno schema predefinito (selezionare categoria → tipologia → dettagli → salvare) e possono modificarli; usano un'applicazione di *gestione del prodotto* che offre modifica, salvataggio, import ed export. L'applicazione gira *su cloud* ed è supportata da un *database relazionale* (campi strutturati), un *file system* (file associati, es. foto) e un *graph database* (esplorazione); inoltre si appoggia all'*infrastruttura BIM aziendale* per le funzionalità di import/export, esposte tramite un *servizio tecnologico*. Gli *acquirenti* cercano i prodotti (ricerca per categorie → affinamento → selezione) tramite un'applicazione interattiva sull'infrastruttura BIM, supportata anch'essa dal software di gestione prodotto che fornisce i dati. Il responsabile dei processi è il *BIM manager*.
**Cosa esercita.** È il caso più completo: una stessa componente applicativa (il software di gestione prodotto) poggia su *due infrastrutture diverse* — cloud e infrastruttura BIM aziendale — esercitando l'allineamento application↔technology su due fronti. Si modellano: l'azienda e il BIM manager (Business), i processi di inserimento e di ricerca, l'acquirente che agisce tramite un'applicazione, e i tre tipi di storage tecnologico (relazionale, file system, graph) più il servizio tecnologico di import/export.

## Esercizio 2 — POSH (e-sales con clienti privati e aziendali)
**Scenario.** Perfect Office Solutions House (POSH) vende soluzioni complete per l'ufficio (dai quaderni ai set completi) più consulenza, con clienti *privati* e *aziendali*. Apre un canale web di e-sales che deve gestire le *differenze* fra i due tipi di cliente: entrambi inseriscono l'ordine, fanno il checkout e pagano, ma in modo diverso — i clienti *commerciali* fanno login all'inizio, inseriscono l'ordine, fanno checkout e pagano la *fattura*; i clienti *privati* inseriscono i dati, fanno checkout ed effettuano il *pagamento*. Dopo il pagamento, conferma ordine, gestione ordine e consegna sono *uguali per tutti*. Il processo è supportato da un *ERP* (gestione ordini, gestione pagamenti, movimentazione merci, pubblicità); un'*applicazione di amministrazione* fornisce i dati all'ERP tramite un protocollo ad hoc a livello applicativo. ERP e applicazione amministrativa risiedono su *due server diversi*, ciascuno con il proprio *database relazionale*, collegati da una *LAN*.
**Cosa esercita.** La modellazione di un processo con *rami differenziati* per tipo di cliente (che converge poi in fasi comuni) — esercita le *specialization* o le scelte/junction sul percorso del processo — e l'allineamento con un'architettura applicativa/tecnologica fatta di due componenti (ERP + amministrazione) su due nodi distinti collegati in rete.

## Esercizio 3 — IKAO (servizio di reso e integrazione legacy/CRM)
**Scenario.** IKAO vende mobili e offre un *servizio di reso*: si verifica l'ammissibilità della richiesta e l'eventuale presenza di difetti per accettarla o rifiutarla; se accettata, il prodotto viene ritirato presso il cliente, si avvisa quando arriva in azienda, e poi viene *riparato o rimborsato*; altrimenti la richiesta è respinta. Un *ERP* gestisce il servizio con le sue funzioni (contabilità, gestione ordini, gestione pagamenti, movimentazione merci, pubblicità). La funzione *contabile* dell'ERP necessita di dati dal *sistema legacy* (con database legacy esposto tramite un *servizio legacy*); inoltre, per tracciare i clienti fra le diverse funzioni, l'ERP necessita di dati dal *CRM*. L'ERP risiede sull'infrastruttura aziendale (un server con il suo database); il sistema legacy sta su un *server separato* con il proprio database, connesso all'ERP via *LAN*; la gestione dell'infrastruttura del CRM è in *outsourcing* e comunica con i server locali via *Internet* (l'applicazione CRM accede all'infrastruttura cloud del provider tramite un servizio tecnologico).
**Cosa esercita.** L'integrazione fra sistemi *eterogenei e distribuiti*: ERP interno, sistema legacy su server separato (collegato in LAN, con l'integrazione ERP↔legacy da rinviare in futuro) e CRM in cloud outsourced (collegato via Internet). Esercita la modellazione di servizi tecnologici esposti (servizio legacy, servizio tecnologico del provider cloud) e i *flussi di dati* fra le funzioni dell'ERP e le fonti esterne (legacy e CRM), cioè proprio quei problemi di *integrazione dei dati* che l'Enterprise Architecture e ArchiMate servono a rendere visibili e governabili.

## Conclusione del percorso GSICT
Questi esercizi chiudono il corso ricongiungendo tutti i fili: dai *fondamenti dei sistemi informativi* (dato/informazione/procedura, accessibilità e correttezza) alla *struttura aziendale* (piramide di Anthony, operazionale vs informazionale), ai *sistemi operazionali* e all'*ERP* (integrazione nativa contro le isole informatiche), fino all'*Enterprise Architecture* (Zachman, TOGAF/ADM) e al suo linguaggio di modellazione *ArchiMate* (Business, Application e Technology layer). Modellare un caso reale in ArchiMate è l'atto finale che dimostra di saper rappresentare *come l'IT supporta il business* in modo integrato e coerente — l'obiettivo ultimo della gestione dei sistemi ICT.
