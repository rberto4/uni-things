#### Algoritmi e problemi computazionali
Gli algoritmi forniscono una strategia risolutiva per giungere alla soluzione di un dato problema computazionale (o di calcolo)
- NON DEDUCIBILI -> es. Halting problem
```java
boolean halts(A, d) // true se, su input finito d, la funzione termina
```
- DEDUCIBILI 
	- TRATTABILI -> Costo polinomiale (quelli che trattiamo noi)
	- NON TRATTABILI -> Costo esponenziale

Quelli trattabili con costo polinomiale sono, ad esempio: 
Ordinamento -> Disporre dati in un certo ordine
Calendario -> Calcolare una data a partire da un numero di giorni
Ricerca -> Cercare uno studente in un DB data la matricola
Duplicati

DEF (ALGORITMO) -> Una sequenza finita di operazioni non ambigue ed effettivamente calcolabili che, una volta eseguite, producono un risultato in una quantità finita di tempo.

PROPRIETÀ 
1. Finitezza -> la sequenza di istruzioni deve essere finita
2. Non ambiguità -> Istruzioni espresse in modo chiaro
3. Realizzabilità -> devono essere eseguibili
4. Efficacia -> devono portare ad un risultato
5. Efficenza -> devono ponderare l'uso delle risorse (tempo, memoria ..)

#### Ciclo di sviluppo di codice algoritmico 
![[Pasted image 20261107181738.png]]
Due fasi
- Fase progettuale -> design in piccolo
- Fase realizzativa

#### 1 Analisi dei requisiti
Definire il problema di calcolo identificando : 
- Requisiti di ingresso e requisiti di uscita (I/O)
Identificare una metodologia di progettazione
- Es. DIVIDI ET IMPERA -> separazione del problema complesso in moduli, in sotto problemi meno complessi
#### 2 Valutazione delle difficoltà 
Vogliamo algoritmi che minimizzano risorse spazio/tempo utilizzate 
-> Per ogni problema, esiste un limite inferiore di costo computazionale, alla quantità di risorse necessarie

#### 3 Progetto di un algoritmo risolutivo
Usiamo lo pseudo-codice per descrivere i passi dell'algoritmo 

#### 4 Analisi di correttezza
Producano risultati CORRETTI in modo EFFICIENTE
- Verifica formale -> Prova che i requisiti sui dati prodotti dall'algoritmo siano soddisfatti 
Altrimenti si torna alla fase 3 Progettuale

#### 5 Analisi prestazioni 
L'analisi teorica >> analisi sperimentale 
permette di scegliere una via per implementare un algoritmo e predire le prestazioni che avrà.

Consideriamo un modello mono-processore + RAM, senza concorrenza e parallelismo
Analisi teorica con :
- Modello di calcolo -> come Von neumann e Touring
- Modello di costo teorico ->
	- A costo uniforme -> indipendente dalla dimensione degli operandi
	- A costo logaritmico -> complicato, dipende dalla dimensione degli operandi
#### A costo uniforme
Ogni istruzione consuma una unità di tempo e richiede una unità di spazio
E' un approccio semplice ma poco efficiente e veritiero.
La complessità è proporzionale al numero di bit dell'operando e l'accesso è proporzionale al numero di bit dell'indirizzo