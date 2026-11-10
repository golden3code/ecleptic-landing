# -*- coding: utf-8 -*-
# Adaptation italienne des guides pour coachs, lot 1 (base : tools/en/coachs/batch_1.py).
# Droit, seuils et organismes : seulement tools/intl/_faits-ue.md et tools/intl/_faits-it.md.
# Aucune règle fiscale citée (alerte 2027 sans objet ici). Le PAR-Q+ n'est jamais reproduit.

ENTRIES = [
    {
        "fr": "fiche-client-coach-sportif",
        "slug": "scheda-cliente-personal-trainer",
        "title": "Scheda cliente per personal trainer: cosa deve contenere",
        "description": "Scheda cliente per personal trainer: le sezioni da prevedere, cosa conta come dato sulla salute, cosa evitare di scrivere e per quanto tempo conservarla.",
        "body": """
<p>La risposta breve: una <strong>scheda cliente per personal trainer</strong> sta in sette sezioni: contatti, logistica, obiettivo, esperienza sportiva, salute, misurazioni e monitoraggio. Appena contiene un infortunio, una patologia pregressa o le risposte a un questionario, contiene dati sulla salute, e in Italia questi dati sono protetti in modo particolare dal GDPR e dal Codice privacy. Annota solo ciò che ti serve, chiedi il consenso del cliente e tieni separata la parte sulla salute.</p>

<h2>Cosa deve contenere una scheda cliente?</h2>
<p>Ecco un esempio di struttura. L'ultima colonna indica come trattare ogni sezione, perché se un dato sia o no un dato sulla salute si valuta caso per caso.</p>
<div class="tablewrap"><table>
<caption>Sezioni proposte come esempio, con una lettura prudente del GDPR.</caption>
<thead><tr><th>Sezione</th><th>Cosa annoti</th><th>Tipo di dato</th></tr></thead>
<tbody>
<tr><td>Contatti</td><td>Nome, e-mail, telefono, persona da avvisare in caso di emergenza</td><td>Dato personale comune</td></tr>
<tr><td>Logistica</td><td>Orari, luogo, attrezzatura, pacchetto, data di inizio</td><td>Dato personale comune</td></tr>
<tr><td>Obiettivo</td><td>Le parole del cliente, scadenza, motivazione</td><td>Comune, salvo che riveli uno stato di salute</td></tr>
<tr><td>Esperienza sportiva</td><td>Attività attuale, passato sportivo, preferenze, intensità desiderata</td><td>Comune, da valutare caso per caso</td></tr>
<tr><td>Salute</td><td>Risposte al questionario, fastidi segnalati, parere medico richiesto</td><td>Dato sulla salute</td></tr>
<tr><td>Misurazioni</td><td>Peso, circonferenza vita, frequenza cardiaca, sonno</td><td>Da trattare come dato sulla salute</td></tr>
<tr><td>Monitoraggio</td><td>Test, sedute, carichi, sensazioni del cliente, decisioni prese</td><td>Sensibile appena incrociato con le misurazioni</td></tr>
</tbody>
</table></div>
<p>Per l'obiettivo, tieni le parole esatte del cliente. «Salire fino a casa senza fermarmi al secondo piano» ti servirà più di «cardio» quando sceglierai un test o misurerai un progresso.</p>

<h2>Quali dati della scheda cliente sono dati sulla salute?</h2>
<p>Nell'UE i dati relativi alla salute sono i dati personali sulla salute fisica o mentale di una persona che rivelano informazioni sul suo stato di salute, passato, presente o futuro, qualunque sia la fonte. Patologie pregresse, malattie, terapie e disabilità ne fanno parte per natura. Un infortunio che il cliente ti racconta rientra nella definizione, anche se l'informazione non arriva da un medico: archivialo con il resto. Tratta allo stesso modo le risposte a un <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">questionario sulla salute</a>.</p>
<p>Il peso dipende dal contesto. Un peso elevato può rivelare un'obesità, e il peso incrociato con il numero di passi o con le calorie assunte può diventare un dato sulla salute. Anche frequenza cardiaca, peso e altezza possono essere sensibili, soprattutto se arrivano da un dispositivo connesso. Il GDPR non dà un elenco chiuso: conta ciò che il dato rivela sullo stato di salute. Non ho trovato una classificazione scritta dei dati sul sonno, quindi per prudenza trattali come dati sulla salute. La tua scheda riunisce tutte queste misure nello stesso posto: applica all'insieme la regola più protettiva.</p>
<p>Nell'UE trattare dati relativi alla salute è vietato in linea di principio, salvo eccezioni; la prima è il consenso esplicito del tuo cliente per una o più finalità specifiche, che può revocare in qualsiasi momento, con la stessa facilità con cui l'ha dato. Chiedilo a parte rispetto alle condizioni generali, dopo avergli spiegato cosa raccogli e perché. In Italia al GDPR si aggiunge il Codice privacy (d.lgs. 196/2003): i dati sulla salute non possono essere diffusi, cioè mostrati a un pubblico indeterminato. L'autorità di controllo è il Garante per la protezione dei dati personali.</p>

<h2>Cosa evitare di scrivere nelle note sul cliente?</h2>
<ul>
<li><strong>Una diagnosi.</strong> Scrivi per esempio: «ginocchio destro dolorante sulle scale, segnalato il 12 gennaio, indirizzato al medico». Non aggiungere nomi di patologie di tua iniziativa. Non interpreti i dati sulla salute di un cliente: appena un segnale ti fa sorgere un dubbio, lo indirizzi al medico.</li>
<li><strong>Dettagli medici che non ti servono.</strong> Ti serve sapere che esiste un parere medico e quali limiti fissa. La copia di una ricetta o di un referto non ha posto nella tua scheda.</li>
<li><strong>Un giudizio sulla persona.</strong> Nell'UE, se un cliente ti chiede l'accesso ai suoi dati, devi rispondere senza ingiustificato ritardo e al più tardi entro un mese dal ricevimento della richiesta; se è complessa o le richieste sono numerose puoi prorogare il termine di due mesi, ma devi avvisarlo entro il primo mese spiegandogli il motivo. Scrivi ogni riga come se dovesse leggerla.</li>
<li><strong>Tutto ciò che non cambia niente nella seduta.</strong> Per ogni campo, chiediti cosa faresti di diverso con quell'informazione. Se non hai una risposta, elimina il campo.</li>
</ul>

<h2>Per quanto tempo conservare la scheda cliente, e dove?</h2>
<p>Stabilisci tu un periodo di conservazione, comunicalo al cliente e cancella la parte sulla salute quando non ti serve più, di norma alla fine del percorso. Le fatture seguono altre regole, quelle fiscali e contabili. Tieni quindi la parte amministrativa separata da quella sportiva: potrai cancellarne una senza toccare l'altra.</p>
<p>Nell'UE, anche se lavori da solo, l'esenzione dal registro delle attività di trattamento per chi ha meno di 250 dipendenti non vale se tratti dati in modo non occasionale o tratti dati relativi alla salute: in quel caso devi tenere il registro, almeno per quei trattamenti. Seguire i clienti con regolarità basta a far scattare l'obbligo, e lo stesso vale per i dati sulla salute.</p>
<p>Per l'archiviazione, devi proteggere i dati dei tuoi clienti con misure tecniche e organizzative adeguate al rischio, come la cifratura. Per dati sulla salute, una chat di WhatsApp o un file non protetto sono una scelta poco adatta.</p>

<h2>Come tenere aggiornata la scheda cliente?</h2>
<p>Aprila alla <a href="/coachs/bilan-forme-premier-rendez-vous.html">valutazione iniziale</a>, poi aggiungi tre cose dopo ogni seduta: cosa è stato fatto, come si è sentito il cliente, cosa cambierai la volta successiva. Annota anche i risultati dei <a href="/coachs/tests-physiques-nouveau-client.html">test fisici</a> insieme alle condizioni in cui si sono svolti.</p>
<p>Mostra questi numeri al cliente. Una meta-analisi di 138 studi sperimentali e 19.951 persone (Harkin, 2016) indica che monitorare i progressi aiuta a raggiungere gli obiettivi, con un effetto più forte quando il risultato viene annotato fisicamente o reso pubblico. Non riguarda solo l'esercizio fisico: prendila come un'indicazione.</p>
<p>Rileggi la sezione sulla salute ogni volta che la situazione cambia. Un dolore nuovo ti riporta alla stessa regola: annoti, non interpreti, indirizzi al medico.</p>
<p>Questa guida ha solo scopo informativo e non sostituisce il parere di un avvocato o di un responsabile della protezione dei dati (DPO).</p>

<h2>In sintesi</h2>
<ul>
<li>Sette sezioni bastano, e ogni campo deve cambiare qualcosa nella seduta.</li>
<li>Infortuni, patologie pregresse e risposte al questionario sono dati sulla salute. Per prudenza, tratta allo stesso modo peso e sonno.</li>
<li>Annota i fatti senza interpretarli, separa salute e fatturazione, stabilisci un periodo di conservazione.</li>
</ul>
""",
        "faq": [
            {"q": "Come si fa una scheda cliente da personal trainer?", "a": "Prevedi sette sezioni: contatti, logistica, obiettivo, esperienza sportiva, salute, misurazioni e monitoraggio. Annota solo ciò che ti serve e tieni separata la parte sulla salute, che il GDPR e il Codice privacy proteggono in modo particolare. Va bene un foglio di calcolo protetto o un software, purché l'accesso sia sicuro."},
            {"q": "La scheda cliente contiene dati sulla salute?", "a": "Quasi sempre. Infortuni, patologie pregresse e risposte a un questionario sono dati sulla salute, e anche peso e sonno possono esserlo, soprattutto se incrociati con altre misure. Nel dubbio trattali così e chiedi un consenso esplicito, separato dalle condizioni generali."},
            {"q": "Per quanto tempo conservare la scheda di un cliente?", "a": "Stabilisci tu il periodo, comunicalo al cliente e cancella la parte sulla salute quando non ti serve più, di norma alla fine del percorso. Le fatture seguono invece le regole fiscali e contabili sulla conservazione dei documenti."},
        ],
        "sources": [
            {"t": "Regolamento (UE) 2016/679 del Parlamento europeo e del Consiglio, del 27 aprile 2016 (regolamento generale sulla protezione dei dati). EUR-Lex. 2016.", "u": "https://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Article 29 Data Protection Working Party. Position Paper on the derogations from the obligation to maintain records of processing activities pursuant to Article 30(5) GDPR. 2018 (in inglese).", "u": "https://ec.europa.eu/newsroom/article29/items/624045"},
            {"t": "Decreto legislativo 30 giugno 2003, n. 196, Codice in materia di protezione dei dati personali, art. 2-septies. Normattiva, testo vigente al 9 novembre 2026.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-06-30;196~art2septies!vig=2026-11-09"},
            {"t": "Garante per la protezione dei dati personali. Sanità e Ricerca scientifica.", "u": "https://www.garanteprivacy.it/temi/sanita-e-ricerca-scientifica"},
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
        ],
    },
    {
        "fr": "bilan-forme-premier-rendez-vous",
        "slug": "valutazione-iniziale-primo-incontro-cliente",
        "title": "Valutazione iniziale: come condurre il primo incontro con un cliente",
        "seo_title": "Valutazione iniziale: come condurre il primo incontro",
        "description": "Valutazione iniziale per personal trainer: come prepararla, quali domande fare, cosa fare se emerge un problema di salute e come chiudere il primo incontro.",
        "body": """
<p>La risposta breve: una buona <strong>valutazione iniziale</strong> segue quattro passaggi: ascoltare l'obiettivo, individuare ciò che richiede un parere medico, misurare un punto di partenza semplice, poi proporre un piano chiaro. Non ho trovato nessuno standard che ne fissi contenuto o durata. Ti aiuta a decidere se puoi iniziare, a quale intensità e in quale direzione. Non fai nessuna diagnosi.</p>

<h2>Cosa preparare prima del primo incontro con un cliente?</h2>
<p>Tre cose inviate in anticipo ti evitano di perdere metà dell'incontro:</p>
<ul>
<li><strong>Il <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">questionario sulla salute</a></strong>, da compilare prima di venire, con una spiegazione di cosa fai dei dati e una richiesta di consenso.</li>
<li><strong>Le informazioni pratiche:</strong> luogo, abbigliamento, acqua, durata.</li>
<li><strong>La natura dell'incontro:</strong> gratuito o a pagamento, lo dici subito. La guida sulla <a href="/coachs/seance-essai-coach-sportif.html">lezione di prova</a> affronta questa domanda.</li>
</ul>
<p>Chiamala valutazione iniziale, mai «check-up» o «visita»: sono parole che creano un'aspettativa che non puoi soddisfare.</p>

<h2>Come si svolge una valutazione iniziale in un'ora?</h2>
<p>Non ho trovato nessuna raccomandazione che ne fissi la durata. Ecco un esempio di suddivisione in 60 minuti, da adattare:</p>
<ol>
<li><strong>5 minuti, l'introduzione.</strong> Spieghi cosa succederà e con cosa il cliente uscirà dall'incontro.</li>
<li><strong>20 minuti, l'ascolto.</strong> Obiettivo, storia sportiva, vincoli, preferenze.</li>
<li><strong>5 minuti, la sicurezza.</strong> Ripassate insieme il questionario.</li>
<li><strong>20 minuti, il movimento.</strong> Due o tre test semplici, con riscaldamento se il protocollo lo prevede.</li>
<li><strong>10 minuti, i passi successivi.</strong> Riassumi e fai la tua proposta.</li>
</ol>
<p>I <a href="/coachs/tests-physiques-nouveau-client.html">test fisici</a> fissano un punto di partenza. Aspettano se il questionario o la conversazione sollevano una domanda sulla salute. Al primo incontro tieni un margine: niente di massimale con una persona che hai appena conosciuto, e nessun test che spetta a un medico. La Haute Autorité de Santé (HAS), l'autorità sanitaria francese, ricorda che il test da sforzo con analisi dei gas si svolge in strutture specializzate, con medici formati.</p>

<h2>Quali domande fare a un nuovo cliente?</h2>
<p>Domande aperte, e un cliente che parla più di te:</p>
<ul>
<li><strong>«Cosa ti porta qui proprio adesso?»</strong> Il motivo del momento spesso dice più dell'obiettivo dichiarato.</li>
<li><strong>«Come capirai che ha funzionato?»</strong> Ottieni un criterio concreto, con le sue parole.</li>
<li><strong>«Cosa hai già provato, e cosa ti ha fatto smettere?»</strong> Individui gli ostacoli prima che si ripresentino.</li>
<li><strong>«Quante sedute ci stanno davvero nella tua settimana?»</strong> La scheda di allenamento si costruisce su questa risposta.</li>
<li><strong>«Cosa ti piace fare, e cosa ti rifiuterai di fare?»</strong> Il cliente mantiene il controllo su una parte delle scelte.</li>
</ul>
<p>Quest'ultimo punto conta. Una revisione di 66 studi (Teixeira, 2012) mostra un legame costante tra le forme autonome di motivazione e l'esercizio fisico, e la motivazione intrinseca predice meglio l'aderenza nel lungo periodo. La maggior parte di questi studi è descrittiva: stabilisce un legame, non una causa. La guida dell'HAS va nella stessa direzione per il colloquio motivazionale: individuare gli ostacoli e fissare obiettivi realistici insieme alla persona.</p>

<h2>Cosa fare se un cliente segnala un problema di salute?</h2>
<p>Dal 2015 lo screening dell'American College of Sports Medicine (ACSM) si basa su tre fattori: l'attività attuale, i segni o la presenza nota di una malattia cardiovascolare, metabolica o renale, e l'intensità desiderata. Quell'aggiornamento rispondeva a un eccesso: troppi invii dal medico non necessari, che possono scoraggiare le persone dal muoversi. Anche l'OMS ritiene in genere non necessario un via libera medico preventivo, in assenza di controindicazioni, per un'attività da leggera a moderata che non va oltre la camminata a passo svelto.</p>
<p>L'HAS indica come comportarsi in caso di dubbio:</p>
<ul>
<li><strong>Una risposta positiva al questionario:</strong> è raccomandato un parere medico prima di iniziare.</li>
<li><strong>Segni che fanno pensare a una malattia:</strong> la persona rimanda l'attività, qualunque sia l'intensità, e va dal suo medico.</li>
<li><strong>45 anni o più, nessuna attività intensa regolare e un programma vicino allo sforzo massimale:</strong> è consigliato un parere medico.</li>
</ul>
<p>In tutti e tre i casi non interpreti nulla. Ripeti ciò che hai sentito, spieghi che la decisione spetta a un medico, annoti la data e rimandi la parte di movimento. Se un cliente ha un dolore al petto o sviene davanti a te, chiama il 112, il numero unico di emergenza: è gratuito anche da un cellulare senza credito o senza SIM, e resta attivo anche il 118, il numero dell'emergenza sanitaria. La diagnosi spetta al medico: una frase come «sarà la pressione» non ha posto in una valutazione.</p>

<h2>Come chiudere la valutazione iniziale?</h2>
<p>Riassumi in tre frasi cosa hai capito, cosa hai misurato e cosa proponi. Poi indica un obiettivo con una data, il ritmo delle sedute e la data della prossima verifica. Metti per iscritto condizioni e prezzo prima di qualsiasi impegno.</p>
<p>Non promettere un risultato in numeri, perché non puoi né garantirlo né dimostrarlo. Spiega cosa misurerai, e quando. In Italia il titolo di chinesiologo richiede una laurea in scienze motorie, e in palestra i corsi a pagamento devono essere coordinati da un chinesiologo o da un istruttore qualificato da una federazione o da un ente di promozione sportiva riconosciuti; verifica anche le regole della tua regione. La sera stessa, riporta l'essenziale nella <a href="/coachs/fiche-client-coach-sportif.html">scheda cliente</a>, finché le parole esatte del cliente sono fresche.</p>

<h2>In sintesi</h2>
<ul>
<li>Invia il questionario prima dell'incontro e fai dell'ascolto la parte più lunga.</li>
<li>Al minimo segnale sulla salute, rimanda il movimento e indirizza al medico, senza interpretare.</li>
<li>Chiudi con un obiettivo datato e condizioni scritte, senza promettere risultati.</li>
</ul>
""",
        "faq": [
            {"q": "Cosa succede nella valutazione iniziale con un personal trainer?", "a": "Il personal trainer ascolta l'obiettivo e la storia sportiva, ripassa il questionario sulla salute, fa due o tre test semplici se nulla lo impedisce, poi propone un piano. Questo incontro valuta la forma fisica e non sostituisce una visita medica."},
            {"q": "Quanto dura una valutazione iniziale?", "a": "Non ho trovato nessuna raccomandazione che ne fissi la durata. Un'ora è un formato pratico: un terzo per l'ascolto, un terzo per il movimento, il resto per introduzione, sicurezza e passi successivi. Adattala al cliente e ai test che hai previsto."},
            {"q": "Cosa chiedere a un cliente al primo incontro?", "a": "Cosa lo porta da te adesso, come capirà che ha funzionato, cosa ha già provato, quanto tempo ha davvero, cosa gli piace e cosa si rifiuta di fare. Aggiungi il questionario sulla salute, e indirizzalo al medico appena una risposta lo richiede."},
        ],
        "sources": [
            {"t": "HAS. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022 (in francese).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Teixeira PJ, Carraça EV, Markland D, et al. Exercise, physical activity, and self-determination theory: a systematic review. <em>Int J Behav Nutr Phys Act</em>. 2012.", "u": "https://doi.org/10.1186/1479-5868-9-78"},
            {"t": "Decreto legislativo 28 febbraio 2021, n. 36, art. 41. Normattiva.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2021-02-28;36~art41"},
            {"t": "Decreto legislativo 28 febbraio 2021, n. 36, art. 42. Normattiva.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2021-02-28;36~art42"},
            {"t": "Ministero della Salute. Numero unico europeo per le emergenze (NUE) 112. 2024.", "u": "https://www.salute.gov.it/new/it/tema/112-118-e-pronto-soccorso/numero-unico-europeo-le-emergenze-nue-112/"},
            {"t": "Ministero della Salute. Le centrali 118 in Italia. 2022.", "u": "https://www.salute.gov.it/new/it/tema/112-118-e-pronto-soccorso/le-centrali-118-italia/"},
        ],
    },
    {
        "fr": "questionnaire-sante-avant-le-sport-client",
        "slug": "questionario-salute-attivita-fisica",
        "title": "Questionario sulla salute prima dell'attività fisica: cosa chiedere",
        "seo_title": "Questionario sulla salute: cosa chiedere al cliente",
        "description": "Questionario sulla salute prima dell'attività fisica: cosa chiedere al cliente, certificato medico, limiti del PAR-Q+ e cosa fare se risponde sì.",
        "body": """
<p>La risposta breve: un <strong>questionario sulla salute prima dell'attività fisica</strong> chiede dell'attività attuale, delle malattie note, dei sintomi nuovi e dell'intensità desiderata. Che sia obbligatorio dipende dal contesto in cui lavori, ma lo strumento è utile in ogni caso. La Haute Autorité de Santé (HAS), l'autorità sanitaria francese, raccomanda un questionario autosomministrato a chiunque voglia iniziare o aumentare un'attività di intensità almeno moderata, e indica che un professionista dell'attività fisica può proporlo. Se un cliente risponde sì, non interpreti: lo indirizzi al medico prima di iniziare.</p>

<h2>Il personal trainer deve chiedere un questionario o un certificato medico?</h2>
<p>In Italia, dal 2013, la legge non chiede più il certificato medico per l'attività ludico-motoria, cioè quella per il proprio benessere di chi non è tesserato con federazioni o enti sportivi, e nessuna norma nazionale ti obbliga a chiederlo a questi clienti. Il certificato non agonistico annuale serve invece a chi si allena nelle attività organizzate dal CONI o da società sportive affiliate. Come scelta pratica, puoi comunque chiedere un questionario o un certificato medico e scriverlo nel contratto con il cliente: sarà una tua condizione, non un obbligo di legge.</p>

<h2>PAR-Q+ o questionario tuo: quale usare?</h2>
<div class="tablewrap"><table>
<caption>Fonte: HAS 2022 e termini e condizioni del PAR-Q+, letti il 31 ottobre 2026.</caption>
<thead><tr><th>Opzione</th><th>Uso</th><th>Cosa sapere</th></tr></thead>
<tbody>
<tr><td>PAR-Q+</td><td>Screening prima dell'attività, dai 15 ai 69 anni</td><td>7 domande, testo protetto</td></tr>
<tr><td>Il tuo questionario</td><td>Ciò che cambia la tua seduta</td><td>Scrivilo tu, senza copiare il PAR-Q+</td></tr>
</tbody>
</table></div>
<p>Il PAR-Q+ richiede attenzione. I suoi termini chiedono un'autorizzazione scritta preventiva per modificarlo o per inserirlo in un'app, un sito, un software o un sondaggio online. Citare la fonte non vale come autorizzazione. Le versioni ufficiali non modificate sono attualmente gratuite per alcuni usi individuali, clinici, didattici e di ricerca non commerciale. I termini non nominano i personal trainer, anche se il sito offre risorse per i professionisti dell'esercizio fisico, e per l'uso commerciale possono essere previsti dei costi. Nel dubbio, scrivi al titolare dei diritti.</p>
<p>La via più semplice: invita il cliente a compilarlo da solo sul sito ufficiale, eparmedx.com. Trovare il testo ripubblicato altrove non ti autorizza a copiarlo nel tuo modulo.</p>

<h2>Cosa chiedere in un questionario prima dell'attività fisica?</h2>
<p>Per il tuo questionario, parti dalla logica dell'American College of Sports Medicine (ACSM), che si riduce a tre fattori, e aggiungi ciò che serve alla tua seduta:</p>
<ul>
<li><strong>L'attività attuale.</strong> Quante sedute a settimana, di che durata, a quale intensità.</li>
<li><strong>Ciò che è noto.</strong> Una malattia cardiovascolare, metabolica o renale diagnosticata. Basta un sì o un no.</li>
<li><strong>Ciò che è nuovo.</strong> Un segno insolito, a riposo o durante lo sforzo.</li>
<li><strong>L'intensità desiderata.</strong> Cosa vuole fare il cliente, e a quale livello.</li>
<li><strong>Ciò che limita il movimento.</strong> Fastidi, un intervento chirurgico recente, una gravidanza: tutto ciò che ti obbliga ad adattare un esercizio.</li>
</ul>
<p>Fai passare ogni domanda dallo stesso filtro: cosa cambi nella seduta se la risposta è sì? Se non cambia niente, eliminala.</p>
<p>L'HAS aggiunge due soglie di età. Dai 45 anni, senza un'attività intensa regolare e con un programma vicino allo sforzo massimale, è consigliato un parere medico. Dai 70 anni è raccomandato per un'attività di intensità almeno elevata.</p>

<h2>Cosa fare se il cliente risponde sì?</h2>
<p>L'HAS è chiara. Una risposta positiva: è raccomandato un parere medico prima di iniziare. Segni o sintomi che fanno pensare a una malattia: la persona rimanda e va dal suo medico. Tutte risposte negative: può diventare più attiva, con le precauzioni abituali.</p>
<p>Il tuo ruolo si ferma qui. Non giudichi la gravità e non rassicuri. Annoti la data, aspetti che il cliente ti confermi il parere ricevuto ed eventuali limiti, poi adatti. Ripeti il questionario ogni volta che la situazione cambia.</p>

<h2>Come gestire le risposte al questionario?</h2>
<p>In Italia ai dati sulla salute si applicano il GDPR e il Codice privacy (d.lgs. 196/2003), e le risposte a un questionario sulla salute sono dati di questo tipo. Non possono essere diffuse, cioè mostrate a un pubblico indeterminato, e l'autorità di controllo è il Garante per la protezione dei dati personali. Trattarle è vietato in linea di principio, salvo eccezioni: la prima è il consenso esplicito del cliente per una o più finalità specifiche, che può revocare in qualsiasi momento, con la stessa facilità con cui l'ha dato. Chiedilo a parte rispetto alle condizioni generali, dopo avergli spiegato cosa raccogli e perché. Resta un punto aperto: il consenso vale solo se la persona può davvero rifiutare, quindi non è chiaro se tu possa rifiutare un cliente che lascia il modulo in bianco. Conserva le risposte nella sezione salute della tua <a href="/coachs/fiche-client-coach-sportif.html">scheda cliente</a>.</p>
<p>Questa guida ha solo scopo informativo e non sostituisce il parere di un medico o di un avvocato.</p>

<h2>In sintesi</h2>
<ul>
<li>Per chi non è tesserato e si allena per il proprio benessere, la legge non chiede più il certificato medico dal 2013, ma l'HAS raccomanda un questionario prima di iniziare.</li>
<li>Il PAR-Q+ non si può copiare in un modulo senza autorizzazione scritta.</li>
<li>Quando un cliente risponde sì, non interpreti: lo indirizzi al medico prima di iniziare.</li>
</ul>
""",
        "faq": [
            {"q": "Il PAR-Q+ è obbligatorio?", "a": "Dipende dal contesto in cui lavori. La Haute Autorité de Santé, l'autorità sanitaria francese, raccomanda un questionario autosomministrato di questo tipo prima di iniziare o aumentare un'attività almeno moderata. I termini del PAR-Q+ vietano di modificarlo o di inserirlo in uno strumento online senza autorizzazione scritta."},
            {"q": "Il personal trainer può chiedere il certificato medico?", "a": "Come scelta pratica puoi chiederlo e scriverlo nel tuo contratto, ma sarà una tua condizione, non un obbligo di legge. Per l'attività ludico-motoria di chi non è tesserato la legge non lo chiede più dal 2013, mentre il certificato non agonistico annuale serve a chi si allena nelle attività organizzate dal CONI o da società sportive affiliate. Se le risposte del cliente richiedono un parere medico, aspettalo prima di iniziare."},
            {"q": "Cosa fare se un cliente risponde sì al questionario sulla salute?", "a": "Non interpretare la risposta e non rassicurare. È raccomandato un parere medico prima di iniziare, e un cliente con segni o sintomi che fanno pensare a una malattia rimanda l'attività e va dal suo medico. Annota la data, poi adatta la seduta quando il cliente ti conferma il parere ricevuto ed eventuali limiti."},
        ],
        "sources": [
            {"t": "HAS. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022 (in francese).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "PAR-Q+ Collaboration. Terms and Conditions. 2026.", "u": "https://eparmedx.com/terms-and-conditions/"},
            {"t": "Decreto-legge 21 giugno 2013, n. 69, art. 42-bis. Normattiva, testo vigente al 9 novembre 2026.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2013-06-21;69~art42bis!vig=2026-11-09"},
            {"t": "Decreto del Ministro della Salute 24 aprile 2013. <em>Gazzetta Ufficiale</em> n. 169 del 20 luglio 2013.", "u": "https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.dataPubblicazioneGazzetta=2013-07-20&atto.codiceRedazionale=13A06313"},
            {"t": "Regolamento (UE) 2016/679 del Parlamento europeo e del Consiglio, del 27 aprile 2016 (regolamento generale sulla protezione dei dati). EUR-Lex. 2016.", "u": "https://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Decreto legislativo 30 giugno 2003, n. 196, Codice in materia di protezione dei dati personali, art. 2-septies. Normattiva, testo vigente al 9 novembre 2026.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-06-30;196~art2septies!vig=2026-11-09"},
            {"t": "Garante per la protezione dei dati personali. Sanità e Ricerca scientifica.", "u": "https://www.garanteprivacy.it/temi/sanita-e-ricerca-scientifica"},
        ],
    },
    {
        "fr": "tests-physiques-nouveau-client",
        "slug": "test-fisici-nuovo-cliente",
        "title": "Test fisici per un nuovo cliente: quali scegliere?",
        "description": "Test fisici per un nuovo cliente: quali scegliere in base al profilo, come svolgerli bene, come leggere i risultati e cosa pensare del test di Ruffier.",
        "body": """
<p>La risposta breve: non ho trovato nessuna batteria di test ufficiale. Come <strong>test fisici per un nuovo cliente</strong>, scegline tre o quattro legati al suo obiettivo: uno per la resistenza, uno per la parte inferiore del corpo, uno per la parte superiore, e un test di equilibrio se il suo profilo lo richiede. Servono a confrontare il cliente con sé stesso. Non fanno nessuna diagnosi.</p>

<h2>Quali test fisici scegliere per ogni cliente?</h2>
<p>La Haute Autorité de Santé (HAS), l'autorità sanitaria francese, descrive nel dettaglio i test da campo più comuni e ricorda che nessun test misura da solo la forza o la flessibilità di tutto il corpo. La tabella unisce i suoi riferimenti ad alcuni studi.</p>
<div class="tablewrap"><table>
<caption>Fonte: HAS 2022; Holland 2014; Jones 1999; Penry 2011.</caption>
<thead><tr><th>Capacità</th><th>Test</th><th>Profilo</th><th>Cosa sapere</th></tr></thead>
<tbody>
<tr><td>Resistenza</td><td>Test del cammino in 6 minuti</td><td>Principiante, persona anziana, ripresa dell'attività</td><td>Validazione clinica, non sportiva</td></tr>
<tr><td>Resistenza</td><td>Corsa di 12 minuti (test di Cooper)</td><td>Giovane adulto già attivo</td><td>Sforzo intenso, stima del VO2max da prendere con cautela</td></tr>
<tr><td>Gambe</td><td>Alzate dalla sedia in 30 secondi</td><td>Persona anziana, principiante</td><td>Sedia senza braccioli, senza usare le mani. Validato dopo i 60 anni</td></tr>
<tr><td>Parte superiore</td><td>Piegamenti senza fermarsi</td><td>Adulto senza fastidi alla spalla</td><td>Mescola forza e resistenza</td></tr>
<tr><td>Forza</td><td>Massimale su 10-15 ripetizioni</td><td>Principiante, persona anziana, ripresa dell'attività</td><td>Specifico per ogni esercizio</td></tr>
<tr><td>Flessibilità</td><td>Sit and reach</td><td>Cliente senza mal di schiena</td><td>Soprattutto i muscoli posteriori della coscia</td></tr>
<tr><td>Equilibrio</td><td>Equilibrio su una gamba, a occhi chiusi</td><td>Persona anziana</td><td>Tre tentativi, il tempo migliore. Stagli accanto, vicino a un appoggio</td></tr>
</tbody>
</table></div>
<p>Due esempi di scelta. Per una persona sedentaria di 55 anni che riprende l'attività: cammino in 6 minuti, alzate dalla sedia, equilibrio su una gamba. Per una persona attiva di 30 anni che punta sulla forza: corsa di 12 minuti, piegamenti e un massimale su 8 ripetizioni in due esercizi che padroneggia, in due sedute.</p>
<p>Prima di qualsiasi test, rileggi il <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">questionario sulla salute</a>. Se richiede un parere medico, il test aspetta.</p>

<h2>Come svolgere i test fisici senza falsare i risultati?</h2>
<p>Un test vale qualcosa solo se puoi ripeterlo in modo identico. Lo standard tecnico della European Respiratory Society e dell'American Thoracic Society (ERS/ATS; Holland, 2014) considera i test del cammino validi, affidabili e sensibili al cambiamento nelle malattie respiratorie croniche, ma sottolinea quanto risentano di piccole differenze di metodo. Raccomanda due prove del test del cammino in 6 minuti, ad almeno 30 minuti di distanza, per fissare una base stabile.</p>
<ul>
<li><strong>Stesse condizioni.</strong> Stesso luogo, stesso percorso, stessa ora del giorno, stesse scarpe, stessa sedia. L'HAS descrive il test del cammino in 6 minuti attorno a due coni distanti 30 m. Lo standard ERS/ATS chiede una superficie piana e almeno 30 m: su un percorso più corto, lascia perdere i valori di riferimento.</li>
<li><strong>Stesse parole.</strong> Scrivi le istruzioni e leggile ad alta voce. Per il cammino, lo standard prevede una frase fissa ogni minuto, e nient'altro. Se il cliente si ferma, il cronometro continua a correre.</li>
<li><strong>Stessa preparazione.</strong> Per il cammino in 6 minuti, niente riscaldamento e nessuno sforzo intenso nelle 2 ore precedenti, secondo questo standard. Per gli altri test, mantieni lo stesso riscaldamento.</li>
<li><strong>Una traccia scritta.</strong> Annota le condizioni accanto al risultato, altrimenti finirai per confrontare due cose diverse.</li>
</ul>
<p>Se il cliente segnala dolore, una sensazione di svenimento, un fiato corto insolito o crampi, oppure se barcolla o impallidisce, interrompi il test e indirizzalo al medico. In caso di dolore al petto o di svenimento, fallo sedere o sdraiare e chiama il 112, il numero unico di emergenza, gratuito anche da un cellulare senza credito o senza SIM; resta attivo anche il 118, il numero dell'emergenza sanitaria.</p>

<h2>Un nuovo cliente può fare un test massimale?</h2>
<p>Non al primo incontro, salvo che sia un cliente allenato che conosce già il test. L'HAS descrive l'1RM come un indicatore affidabile della forza, e i test a 4RM o 8RM come una stima affidabile. Ritiene più sicuri i test su 10-15 ripetizioni massime per le persone anziane, decondizionate o con una malattia cronica. Anche a 4 o 8 ripetizioni, aspetta che la tecnica sia pulita. La corsa di 12 minuti richiede già uno sforzo sostenuto: riservala a un cliente abituato all'intensità.</p>
<p>Non confondere questi test con un test da sforzo clinico, che si svolge con monitoraggio dell'ECG e della pressione arteriosa in ambiente sanitario.</p>

<h2>Il test di Ruffier è affidabile?</h2>
<p>Resta un indicatore semplice, poco preciso per stimare la forma cardiorespiratoria. In uno studio su 81 adulti sani (Sartor, 2016), l'indice di Ruffier-Dickson aveva una correlazione di -0,40 con la forma misurata e spiegava il 15% della variabilità. Non compare nella tabella dei test dell'HAS. Se il tuo cliente ci tiene, confronta i suoi punteggi tra loro e non ricavarne un VO2max.</p>

<h2>Come leggere i risultati, e quando ripetere i test?</h2>
<p>Confronta il cliente con sé stesso: è il senso di una <a href="/methode/ligne-de-base.html">linea di base</a>. I valori di riferimento descrivono altre popolazioni. Per il cammino in 6 minuti, Enright (1998) ha trovato una mediana di 576 m negli uomini e 494 m nelle donne, su 290 adulti sani tra i 40 e gli 80 anni, e le equazioni spiegano circa il 40% della varianza. Per la corsa di 12 minuti, Penry (2011) riporta una buona affidabilità nei giovani adulti, ma invita alla cautela quando se ne ricava un VO2max.</p>
<p>Uno scarto da un valore di riferimento non ti permette di concludere nulla sulla salute del cliente. Se un risultato ti sorprende, indirizzalo al medico senza commentarlo. Il test della sedia, da parte sua, è stato validato su 76 adulti oltre i 60 anni (Jones, 1999): i suoi valori non valgono per un cliente di 30 anni.</p>
<p>Non ho trovato nessuna frequenza ufficiale per ripetere i test. La cosa più logica è ripeterli alla fine di un blocco della <a href="/coachs/creer-programme-personnalise-client.html">scheda di allenamento</a>, nelle stesse condizioni, poi mostrare l'evoluzione nel <a href="/coachs/bilan-mensuel-client-coaching.html">report mensile</a>.</p>

<h2>In sintesi</h2>
<ul>
<li>Bastano tre o quattro test legati all'obiettivo, scelti in base al profilo.</li>
<li>Usa ogni volta lo stesso protocollo, annota le condizioni e confronta il cliente con sé stesso.</li>
<li>Un test non fa diagnosi: al minimo segnale d'allarme, interrompi e indirizza al medico.</li>
</ul>
""",
        "faq": [
            {"q": "Quale test fisico far fare a un principiante?", "a": "Il test del cammino in 6 minuti per la resistenza, le alzate dalla sedia in 30 secondi per le gambe e, se serve, un massimale su 10-15 ripetizioni. Sono test facili da dosare. Rileggi sempre il questionario sulla salute prima di iniziare."},
            {"q": "Il test di Ruffier è affidabile?", "a": "È un indicatore semplice, poco preciso per stimare la forma cardiorespiratoria. In uno studio su 81 adulti sani spiegava il 15% della variabilità. Non compare nella tabella dei test della Haute Autorité de Santé, l'autorità sanitaria francese."},
            {"q": "Ogni quanto ripetere i test fisici a un cliente?", "a": "Non ho trovato nessuna frequenza ufficiale. La cosa più logica è ripeterli alla fine di un blocco di allenamento, nelle stesse condizioni, per confrontare il cliente con sé stesso."},
        ],
        "sources": [
            {"t": "HAS. Guide des connaissances sur l'activité physique et la sédentarité. 2022 (in francese).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2022-08/guide_connaissance_ap_sedentarite_vf.pdf"},
            {"t": "Holland AE, Spruit MA, Troosters T, et al. An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease. <em>Eur Respir J</em>. 2014.", "u": "https://doi.org/10.1183/09031936.00150314"},
            {"t": "Enright PL, Sherrill DL. Reference equations for the six-minute walk in healthy adults. <em>Am J Respir Crit Care Med</em>. 1998.", "u": "https://doi.org/10.1164/ajrccm.158.5.9710086"},
            {"t": "Jones CJ, Rikli RE, Beam WC. A 30-s chair-stand test as a measure of lower body strength in community-residing older adults. <em>Res Q Exerc Sport</em>. 1999.", "u": "https://doi.org/10.1080/02701367.1999.10608028"},
            {"t": "Penry JT, Wilcox AR, Yun J. Validity and reliability analysis of Cooper's 12-minute run and the multistage shuttle run in healthy adults. <em>J Strength Cond Res</em>. 2011.", "u": "https://doi.org/10.1519/JSC.0b013e3181cc2423"},
            {"t": "Sartor F, Bonato M, Papini G, et al. A 45-Second Self-Test for Cardiorespiratory Fitness: Heart Rate-Based Estimation in Healthy Individuals. <em>PLoS One</em>. 2016.", "u": "https://doi.org/10.1371/journal.pone.0168154"},
            {"t": "Ministero della Salute. Numero unico europeo per le emergenze (NUE) 112. 2024.", "u": "https://www.salute.gov.it/new/it/tema/112-118-e-pronto-soccorso/numero-unico-europeo-le-emergenze-nue-112/"},
            {"t": "Ministero della Salute. Le centrali 118 in Italia. 2022.", "u": "https://www.salute.gov.it/new/it/tema/112-118-e-pronto-soccorso/le-centrali-118-italia/"},
        ],
    },
    {
        "fr": "creer-programme-personnalise-client",
        "slug": "scheda-allenamento-personalizzata-cliente",
        "title": "Come creare una scheda di allenamento personalizzata: il metodo",
        "seo_title": "Scheda di allenamento personalizzata: come crearla",
        "description": "Scheda di allenamento personalizzata per un cliente: dalla valutazione iniziale alla progressione, con i riferimenti di OMS e ACSM per ogni obiettivo.",
        "body": """
<p>La risposta breve: una <strong>scheda di allenamento personalizzata</strong> parte dalla valutazione del cliente, mai da un modello. Comincia dal suo obiettivo, dal tempo che ha davvero a disposizione e dal suo livello. Fissa volume e intensità, scegli una suddivisione che riuscirà a rispettare, scrivi una regola di progressione, poi aggiusta in base a ciò che ti riferisce. La position stand dell'American College of Sports Medicine (ACSM) pubblicata nel 2026 mostra che poche variabili cambiano davvero i risultati: concentrati su quelle.</p>

<h2>Cosa sapere prima di creare una scheda di allenamento?</h2>
<p>Cinque informazioni decidono quasi tutto. Emergono dalla <a href="/coachs/bilan-forme-premier-rendez-vous.html">valutazione iniziale</a> e dai <a href="/coachs/tests-physiques-nouveau-client.html">test fisici</a>:</p>
<ul>
<li><strong>L'obiettivo</strong>, con le parole del cliente e una scadenza.</li>
<li><strong>Il tempo davvero disponibile:</strong> il numero di sedute che manterrà in una settimana piena di impegni.</li>
<li><strong>Il livello:</strong> cosa fa oggi, e cosa ha fatto in passato.</li>
<li><strong>Il luogo e l'attrezzatura.</strong></li>
<li><strong>I limiti:</strong> fastidi segnalati, un parere medico in attesa o limiti fissati da un medico.</li>
</ul>
<p>Se un parere medico è in attesa, anche la scheda aspetta. Se il cliente ha ricevuto dei limiti, applicali così come sono, senza reinterpretarli.</p>

<h2>Come impostare volume e intensità?</h2>
<p>Due riferimenti bastano per fissare i parametri: l'OMS per la salute e l'ACSM per l'allenamento della forza, con 137 revisioni sistematiche e più di 30.000 partecipanti, tutti adulti sani.</p>
<div class="tablewrap"><table>
<caption>Fonte: OMS 2020; ACSM 2026; Schoenfeld 2017. Adulti sani.</caption>
<thead><tr><th>Obiettivo</th><th>Riferimento</th><th>Fonte</th></tr></thead>
<tbody>
<tr><td>Salute, ripresa dell'attività</td><td>Da 150 a 300 min di attività moderata a settimana, o da 75 a 150 min di attività vigorosa, più esercizi di rafforzamento per tutti i grandi gruppi muscolari in 2 o più giorni</td><td>OMS</td></tr>
<tr><td>Anziani</td><td>All'interno di questo volume, attività varie centrate su equilibrio e forza, 3 o più giorni a settimana</td><td>OMS</td></tr>
<tr><td>Forza</td><td>80% dell'1RM o più, da 2 a 3 serie, 2 o più sedute a settimana</td><td>ACSM</td></tr>
<tr><td>Ipertrofia</td><td>10 o più serie a settimana per gruppo muscolare. Più volume, più guadagno (15 studi)</td><td>ACSM, Schoenfeld</td></tr>
<tr><td>Potenza</td><td>Dal 30 al 70% dell'1RM, fase di sollevamento veloce</td><td>ACSM</td></tr>
</tbody>
</table></div>
<p>Queste cifre descrivono la destinazione, ben oltre la prima settimana. L'OMS consiglia a chi ne è lontano di iniziare con poco, poi aumentare gradualmente frequenza, intensità e durata. Rispetto al non allenarsi, il lavoro di forza migliora già forza, massa muscolare ed equilibrio. Per un principiante basta una prima scheda semplice.</p>
<p>Altri parametri contano meno di quanto si pensi. Secondo l'ACSM, arrivare al cedimento muscolare o cambiare tipo di attrezzatura non ha cambiato i risultati in modo costante. Un cliente senza palestra può seguire una vera scheda, purché il carico o le ripetizioni possano aumentare.</p>

<h2>Come suddividere le sedute nella settimana?</h2>
<p>Scegli in base al calendario del cliente. Una meta-analisi di 14 studi e 392 persone (Ramos-Campo, 2024) non ha trovato differenze significative di forza o di massa muscolare tra full body e split a parità di volume. Gli autori concludono che la scelta può seguire le preferenze.</p>
<p>Ecco una logica di esempio, da adattare:</p>
<ul>
<li><strong>2 sedute:</strong> full body ogni volta.</li>
<li><strong>3 sedute:</strong> full body, oppure un'alternanza tra parte superiore e parte inferiore del corpo.</li>
<li><strong>4 sedute o più:</strong> lo split diventa possibile, se il cliente le mantiene davvero.</li>
</ul>
<p>Pensa alla settimana saltata: se salta una seduta, con uno split un gruppo muscolare resta indietro, con un full body no. Per un obiettivo di forza, metti l'esercizio prioritario all'inizio della seduta, come nota l'ACSM.</p>

<h2>Come far progredire una scheda di allenamento?</h2>
<p>Scrivi la regola nella scheda, così il cliente sa cosa fa scattare il passo successivo. Esempio: quando ogni serie arriva a 12 ripetizioni pulite, il carico sale e le ripetizioni tornano a 8.</p>
<p>Hai diverse leve. Uno studio su persone già allenate con i pesi (Plotkin, 2022, 43 all'inizio, 38 alla fine) mostra che aggiungere ripetizioni o aggiungere carico dà adattamenti paragonabili in 8 settimane, con un leggero vantaggio del carico per la forza massimale. È utile a casa, quando il carico disponibile arriva al limite. Lo studio è breve e riguarda solo quadricipiti e polpacci.</p>
<p>Cambia una variabile alla volta, così sai cosa ha prodotto cosa. Secondo l'ACSM la periodizzazione non ha cambiato i risultati in modo costante: tieni i piani complessi per un cliente avanzato, e ripassa <a href="/articles/periodisation-entrainement-bases.html">le basi della periodizzazione</a> se ti serve.</p>

<h2>Quando modificare la scheda, e dove finisce il tuo ruolo?</h2>
<p>Dopo ogni seduta, raccogli lo sforzo percepito, eventuali fastidi e ciò che è stato saltato. Se il cliente salta due volte di fila lo stesso tipo di seduta, cambia la scheda prima di parlare di motivazione.</p>
<p>Tre limiti non si spostano:</p>
<ul>
<li><strong>La salute.</strong> Secondo l'OMS, chi sviluppa nuovi sintomi mentre aumenta l'attività dovrebbe consultare un professionista sanitario. Ti fermi, indirizzi, non interpreti.</li>
<li><strong>L'alimentazione.</strong> Puoi condividere indicazioni generali. Più il consiglio è personale, più il rischio cresce, soprattutto in presenza di una condizione medica.</li>
<li><strong>Il quadro legale.</strong> In Italia il titolo di chinesiologo richiede una laurea in scienze motorie, e in palestra i corsi a pagamento devono essere coordinati da un chinesiologo o da un istruttore qualificato da una federazione o da un ente di promozione sportiva riconosciuti. Per l'allenamento a domicilio o online questa regola non dice nulla: non leggerci né un divieto né un via libera, e verifica anche le regole della tua regione.</li>
</ul>

<h2>In sintesi</h2>
<ul>
<li>La scheda nasce dalla valutazione: obiettivo, tempo reale, livello, attrezzatura, limiti.</li>
<li>Fissa poche variabili, con una regola di progressione scritta e una suddivisione che il cliente rispetterà.</li>
<li>Nuovi sintomi, alimentazione e regole sulla qualifica: questi limiti vengono prima della scheda.</li>
</ul>
""",
        "faq": [
            {"q": "Come creare una scheda di allenamento personalizzata per un cliente?", "a": "Parti dalla valutazione: obiettivo, tempo davvero disponibile, livello, attrezzatura e limiti. Poi fissa volume e intensità in base all'obiettivo, scegli una suddivisione che il cliente rispetterà, scrivi una regola di progressione e aggiusta in base ai suoi riscontri."},
            {"q": "Quante sedute a settimana deve prevedere una scheda?", "a": "L'OMS raccomanda esercizi di rafforzamento per tutti i grandi gruppi muscolari in 2 o più giorni a settimana, e l'ACSM 2 o più sedute per la forza. Per un principiante, due sedute full body sono un buon inizio. Il numero giusto è quello che il cliente mantiene in una settimana piena di impegni."},
            {"q": "Un personal trainer può inserire un piano alimentare nella scheda?", "a": "Puoi dare indicazioni generali, senza presentarti come dietista o nutrizionista. Il confine con il consiglio individuale non è netto: più il consiglio è personale, più il rischio cresce, soprattutto con una condizione medica. In quel caso indirizza il cliente a un medico o a un dietista."},
        ],
        "sources": [
            {"t": "Currier BS, D'Souza AC, Singh MAF, et al. American College of Sports Medicine Position Stand. Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults: An Overview of Reviews. <em>Med Sci Sports Exerc</em>. 2026.", "u": "https://doi.org/10.1249/MSS.0000000000003897"},
            {"t": "Schoenfeld BJ, Ogborn D, Krieger JW. Dose-response relationship between weekly resistance training volume and increases in muscle mass: A systematic review and meta-analysis. <em>J Sports Sci</em>. 2017.", "u": "https://doi.org/10.1080/02640414.2016.1210197"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Ramos-Campo DJ, Benito-Peinado PJ, Andreu-Caravaca L, et al. Efficacy of Split Versus Full-Body Resistance Training on Strength and Muscle Growth: A Systematic Review With Meta-Analysis. <em>J Strength Cond Res</em>. 2024.", "u": "https://doi.org/10.1519/JSC.0000000000004774"},
            {"t": "Plotkin D, Coleman M, Van Every D, et al. Progressive overload without progressing load? The effects of load or repetition progression on muscular adaptations. <em>PeerJ</em>. 2022.", "u": "https://doi.org/10.7717/peerj.14142"},
            {"t": "Decreto legislativo 28 febbraio 2021, n. 36, art. 41. Normattiva.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2021-02-28;36~art41"},
            {"t": "Decreto legislativo 28 febbraio 2021, n. 36, art. 42. Normattiva.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2021-02-28;36~art42"},
        ],
    },
    {
        "fr": "fideliser-clients-coaching-sportif",
        "slug": "fidelizzare-clienti-personal-trainer",
        "title": "Perché i clienti se ne vanno: come fidelizzarli da personal trainer",
        "seo_title": "Fidelizzare i clienti: perché lasciano il personal trainer",
        "description": "Fidelizzare i clienti da personal trainer: perché se ne vanno, cosa mostrano davvero gli studi sugli abbandoni e come calcolare il tuo tasso di fidelizzazione.",
        "body": """
<p>La risposta breve: per <strong>fidelizzare i clienti da personal trainer</strong>, comincia a misurare chi se ne va e per quale motivo: nessuna statistica lo farà al posto tuo. Non ho trovato nessun tasso di abbandono specifico per i personal trainer indipendenti. La ricerca sostiene soprattutto tre leve semplici: un obiettivo scritto, progressi registrati e riscontri regolari. Il resto è nel tuo elenco clienti.</p>

<h2>Quanti clienti abbandonano davvero?</h2>
<p>L'unico dato solido che ho tenuto viene da una sola palestra di Rio de Janeiro. Sperandei e colleghi hanno seguito 5.240 iscritti: il 63% aveva abbandonato prima del terzo mese, e meno del 4% ha superato i dodici mesi di attività continuativa. Lo studio, pubblicato nel 2016, riguarda una sola palestra, si basa sui suoi dati di iscrizione e si è svolto in un contesto senza supervisione, come dice il titolo. Non vale quindi né per tutte le palestre né per un cliente seguito da un personal trainer. Diffida delle percentuali di abbandono che circolano senza riferimento.</p>
<p>Il tuo numero reale si calcola in dieci minuti. Prendi i clienti attivi all'inizio di un trimestre e conta quanti ci sono ancora alla fine, senza aggiungere i nuovi. Esempio di calcolo: 12 clienti il 1° gennaio, 9 ancora attivi il 31 marzo, quindi 9 ÷ 12 = 75% di fidelizzazione su tre mesi. Con così pochi clienti, una sola partenza pesa più di 8 punti. Leggi questo tasso sull'anno, e guarda soprattutto i motivi.</p>

<h2>Perché i clienti lasciano il personal trainer?</h2>
<p>Nessuno degli studi citati qui risponde per il cliente di un personal trainer indipendente. La tua fonte migliore restano i tuoi ex clienti. Questa griglia di lavoro, senza valore statistico, ti aiuta a classificare ogni partenza:</p>
<ul>
<li><strong>Partenza prevista:</strong> l'obiettivo è raggiunto, o il cliente ora sa allenarsi da solo. È un successo, e forse un futuro passaparola.</li>
<li><strong>Partenza forzata:</strong> un trasloco, il budget, nuovi orari di lavoro, una nascita, la salute. A volte puoi proporre un formato più leggero o a distanza.</li>
<li><strong>Partenza evitabile:</strong> progressi invisibili, sedute tutte uguali, un obiettivo mai rivisto, un orario che non va più bene, un rapporto che si è spento.</li>
</ul>
<p>Fai tre domande a ogni cliente che se ne va: cosa ha fatto scattare la tua decisione, cosa ti avrebbe fatto restare, cosa diresti a chi pensa di iniziare? Annota le risposte parola per parola. «Non posso più permettermelo» può anche voler dire «non vedo più cosa ci guadagno». Se lo stesso motivo torna più volte in un anno, hai trovato la tua priorità.</p>

<h2>Cosa fa restare un cliente nel lungo periodo?</h2>
<p>Gli studi che ho selezionato non riguardano il personal training individuale da indipendente, ma danno una direzione.</p>
<ul>
<li><strong>Monitorare i progressi.</strong> La meta-analisi di Harkin e colleghi (2016, 138 studi sperimentali, 19.951 persone) trova un effetto medio di 0,40 sul raggiungimento degli obiettivi, più forte quando il risultato è registrato o condiviso. Non si limita all'esercizio fisico.</li>
<li><strong>Andare oltre l'automonitoraggio.</strong> Su 122 valutazioni e 44.747 persone, Michie e colleghi (2009) mostrano che gli interventi che lo combinano con un'altra tecnica della teoria del controllo raggiungono un effetto di 0,42, contro 0,26 per gli altri.</li>
<li><strong>Curare il contesto.</strong> La sintesi di 55 revisioni di Collado-Mateo (2021) elenca, tra gli altri, supervisione, riscontri, monitoraggio dei progressi, obiettivi, sostegno sociale e piacere. Riguarda pazienti con malattie croniche e anziani, non tutti i clienti di un personal trainer.</li>
</ul>
<p>In pratica: il cliente registra, tu rispondi, e rivedete insieme l'obiettivo. Un <a href="/coachs/bilan-mensuel-client-coaching.html">report mensile di una pagina</a> basta per dare questo ritmo.</p>

<h2>Quando intervenire per non perdere un cliente?</h2>
<p>Non aspettare che il cliente annunci che se ne va. Quattro momenti richiedono un'azione:</p>
<ul>
<li><strong>Le prime settimane.</strong> Nella palestra di Rio l'abbandono arrivava presto, e <a href="/articles/combien-de-temps-pour-prendre-une-habitude.html">un'abitudine richiede tempo per formarsi</a>. Prevedi un breve punto verso la terza settimana: cosa funziona, cosa no.</li>
<li><strong>La fine di un pacchetto.</strong> Parla del seguito due o tre sedute prima dell'ultima, report alla mano. Anche <a href="/coachs/packs-abonnement-seance-coach-sportif.html">la formula che proponi</a> conta in quel momento.</li>
<li><strong>Obiettivo raggiunto.</strong> Fissate insieme il successivo, o prepara un'uscita ordinata con ciò che gli serve per continuare da solo.</li>
<li><strong>Assenze ripetute.</strong> Applica <a href="/coachs/seance-annulee-regles-coach.html">le tue regole sulle sedute annullate</a>, poi chiedi cosa è cambiato nella sua settimana.</li>
</ul>
<p>Non contare sul contratto per trattenere qualcuno. Se il tuo abbonamento a tempo determinato si rinnova da solo, trenta giorni prima della scadenza devi dire al cliente entro quale data può disdire, per iscritto, via SMS o con il canale online che ha indicato: senza questo avviso, potrà recedere quando vuole, senza spese, fino alla scadenza successiva. Per inviare e-mail o SMS promozionali a un privato ti serve prima il suo consenso. Unica eccezione: puoi scrivere via e-mail a un tuo cliente, all'indirizzo che ti ha dato quando ha acquistato, per servizi simili, se lo hai informato e può opporsi in ogni momento, facilmente e gratis. Prima di scrivere a un ex cliente, quindi, controlla di poterlo fare, e in ogni messaggio dagli un modo semplice per dire di no.</p>

<h2>In sintesi</h2>
<ul>
<li>Nessun tasso di abbandono generale descrive la tua attività: calcola la fidelizzazione sui tuoi clienti e annota ogni motivo di partenza.</li>
<li>Obiettivo scritto, progressi registrati, riscontri regolari: sono le leve con il sostegno migliore, anche se gli studi non riguardano i personal trainer indipendenti.</li>
<li>Agisci prima della partenza: prime settimane, fine di un pacchetto, obiettivo raggiunto, assenze ripetute.</li>
</ul>
""",
        "faq": [
            {"q": "Come fidelizzare i clienti da personal trainer?", "a": "Fissa un obiettivo scritto, registra i progressi, fai verifiche regolari e parla del seguito prima che il pacchetto finisca. Chiedi anche a ogni cliente che se ne va cosa lo avrebbe fatto restare: i tuoi motivi di partenza ti insegneranno più di una statistica generale."},
            {"q": "Qual è il tasso di abbandono in palestra?", "a": "Non ho trovato un dato generale affidabile. In una palestra di Rio de Janeiro studiata su 5.240 iscritti, il 63% aveva abbandonato prima del terzo mese. Il risultato viene da una sola palestra in un contesto senza supervisione e non vale né per tutte le palestre né per un cliente seguito da un personal trainer."},
            {"q": "Come si calcola il tasso di fidelizzazione dei clienti?", "a": "Prendi i clienti attivi all'inizio di un trimestre e conta quanti ci sono ancora alla fine, senza aggiungere i nuovi. Per esempio, 12 clienti il 1° gennaio e 9 ancora attivi il 31 marzo danno 9 ÷ 12 = 75% su tre mesi. Con pochi clienti, leggi il tasso sull'anno."},
        ],
        "sources": [
            {"t": "Sperandei S, Vieira MC, Reis AC. Adherence to physical activity in an unsupervised setting: Explanatory variables for high attrition rates among fitness center members. <em>J Sci Med Sport</em>. 2016.", "u": "https://doi.org/10.1016/j.jsams.2015.12.522"},
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Michie S, Abraham C, Whittington C, McAteer J, Gupta S. Effective techniques in healthy eating and physical activity interventions: a meta-regression. <em>Health Psychol</em>. 2009.", "u": "https://doi.org/10.1037/a0016136"},
            {"t": "Collado-Mateo D, Lavín-Pérez AM, Peñacoba C, et al. Key Factors Associated with Adherence to Physical Exercise in Patients with Chronic Diseases and Older Adults: An Umbrella Review. <em>Int J Environ Res Public Health</em>. 2021.", "u": "https://doi.org/10.3390/ijerph18042023"},
            {"t": "Decreto legislativo 6 settembre 2005, n. 206, Codice del consumo, art. 65-bis. Normattiva, testo vigente al 9 novembre 2026.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206~art65bis!vig=2026-11-09"},
            {"t": "Decreto legislativo 30 giugno 2003, n. 196, Codice in materia di protezione dei dati personali, art. 130. Normattiva, testo vigente al 9 novembre 2026.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-06-30;196~art130!vig=2026-11-09"},
        ],
    },
    {
        "fr": "bilan-mensuel-client-coaching",
        "slug": "report-mensile-progressi-cliente",
        "title": "Report mensile dei progressi: cosa mostrare al cliente",
        "description": "Report mensile dei progressi del cliente: quali misure mostrare, come confrontarle, come condurre l'incontro e come gestire i dati sulla salute.",
        "body": """
<p>La risposta breve: un <strong>report mensile dei progressi</strong> sta in una pagina e risponde a quattro domande: a che punto è l'obiettivo, cosa avete fatto, cosa è cambiato, cosa cambi il mese prossimo. Mostra da tre a cinque misure, sempre confrontate con il cliente stesso, poi chiudi con una decisione scritta. Il ritmo mensile è una scelta pratica, che gli studi citati qui non fissano.</p>

<h2>Perché fare una verifica dei progressi ogni mese?</h2>
<p>Da una seduta all'altra, il cliente fa fatica a vedere i suoi progressi. Il report li rende visibili. La meta-analisi di Harkin e colleghi (2016, 138 studi sperimentali, 19.951 persone) mostra che monitorare i progressi aiuta a raggiungere gli obiettivi, con un effetto più forte quando il risultato è registrato o condiviso. Non si limita all'esercizio fisico, ma un report soddisfa entrambe le condizioni: è scritto, ed è condiviso con te.</p>
<p>Ti aiuta anche a prendere una decisione invece di riproporre la stessa scheda, e ti dà un appoggio per <a href="/coachs/fideliser-clients-coaching-sportif.html">fidelizzare un cliente nel lungo periodo</a>. Un mese ti dà già materiale su presenze e carichi. Un test da campo può aspettare due o tre mesi.</p>

<h2>Cosa mettere nel report mensile dei progressi?</h2>
<p>Scegli in base all'obiettivo del cliente. Questa griglia copre la maggior parte dei casi:</p>
<div class="tablewrap"><table>
<caption>Fonte: griglia di lavoro di questa guida, da adattare a ogni cliente.</caption>
<thead><tr><th>Misura</th><th>Cosa mostri</th><th>Precauzione</th></tr></thead>
<tbody>
<tr><td>Presenze</td><td>Sedute fatte su sedute previste</td><td>Separa le assenze inevitabili dalle altre</td></tr>
<tr><td>Carico</td><td>Sforzo percepito moltiplicato per la durata, settimana per settimana</td><td>Confronta con il cliente stesso, mai con qualcun altro</td></tr>
<tr><td>Prestazione</td><td>Due o tre esercizi di riferimento: carico, ripetizioni, tempo</td><td>Mantieni lo stesso esercizio e le stesse istruzioni</td></tr>
<tr><td>Test da campo</td><td>Un solo test, se serve all'obiettivo</td><td>Stesse condizioni ogni volta</td></tr>
<tr><td>Sensazioni</td><td>Energia, sonno, piacere, con un voto da 1 a 5</td><td>Orienta la conversazione e non diagnostica nulla</td></tr>
<tr><td>Peso, circonferenze</td><td>Solo se è il suo obiettivo e se è d'accordo</td><td>Mai l'unica misura del successo</td></tr>
</tbody>
</table></div>
<p>Per il carico, il metodo più semplice resta l'RPE di seduta: un voto di sforzo moltiplicato per la durata. Foster e colleghi lo hanno valutato nel 2001 rispetto a un metodo basato sulla frequenza cardiaca e lo hanno trovato valido su sforzi diversi. La scelta dei test è trattata nella nostra guida sui <a href="/coachs/tests-physiques-nouveau-client.html">test fisici per un nuovo cliente</a>.</p>

<h2>Come confrontare i risultati in modo corretto?</h2>
<p>L'unico confronto utile mette il cliente di fronte a sé stesso, a parità di condizioni: stesso esercizio, stesse istruzioni, stessa ora del giorno, stesso riscaldamento. Questo rigore conta. Per il test del cammino in 6 minuti, lo standard europeo e americano del 2014 nota che i risultati risentono di piccole differenze di metodo e raccomanda due prove. Il test è stato validato nelle malattie respiratorie croniche: con un cliente sano serve solo a confrontarlo con sé stesso.</p>
<p>Diffida anche dei test che promettono troppo. Nello studio di Sartor e colleghi (2016, 81 adulti sani), l'indice di Ruffier-Dickson spiega solo il 15% della variabilità della forma cardiorespiratoria. Tienilo come un indicatore semplice, e non ricavarne un VO2max. Leggi ogni scarto su più mesi: un singolo calo può venire da una settimana piena di impegni, da un viaggio o da un raffreddore.</p>

<h2>Come condurre la verifica mensile con il cliente?</h2>
<p>Bastano quindici o venti minuti, durante una seduta o in videochiamata. Un possibile svolgimento:</p>
<ol>
<li>Comincia chiedendo com'è andato il mese, prima di mostrare un solo numero.</li>
<li>Mostra cosa è migliorato, con accanto il numero di partenza.</li>
<li>Presenta ciò che si è fermato come un fatto: «6 sedute su 8», senza commenti sulla forza di volontà.</li>
<li>Cercate insieme la causa: orari, sonno, una scheda troppo ambiziosa, un obiettivo superato.</li>
<li>Decidete da una a tre modifiche e scrivete l'obiettivo del mese successivo.</li>
</ol>
<p>Tratta allo stesso modo un mese andato male. Se il cliente non riesce a mantenere tre sedute a settimana, adatta la scheda alla sua settimana reale. Non promettere nessun risultato per il mese successivo. Se parla di un sintomo nuovo, di una malattia o di un disturbo alimentare, non interpreti: lo indirizzi a un medico o a un dietista.</p>

<h2>Cosa fare con i dati del report?</h2>
<p>Un report contiene spesso dati sensibili, e in Italia ai dati sulla salute si applicano il GDPR e il Codice privacy (d.lgs. 196/2003). Patologie pregresse, malattie e terapie sono dati sulla salute per natura, e anche il peso può diventarlo, soprattutto se incrociato con i passi o con le calorie. Chiedi un consenso esplicito, separato dalle condizioni generali, e conserva questi documenti in uno spazio protetto. Questi dati non possono essere diffusi, cioè mostrati a un pubblico indeterminato, e l'autorità di controllo è il Garante per la protezione dei dati personali.</p>
<p>Il report resta tra te e il tuo cliente. Condividilo con un medico, un fisioterapista, un altro personal trainer o un familiare solo con il suo accordo. La cosa più semplice: consegnalo a lui, e sarà lui a condividerlo se vuole. Per pubblicare una foto prima e dopo in cui è riconoscibile ti serve il suo consenso: chiediglielo prima, meglio per iscritto, indicando mezzo, scopo e durata, perché accettare di essere fotografato non basta. Se poi la foto o la didascalia rivelano dati sulla salute, come il peso o una patologia, il Codice privacy ne vieta la diffusione e non prevede eccezioni espresse per il consenso.</p>

<h2>In sintesi</h2>
<ul>
<li>Una pagina, da tre a cinque misure, una decisione scritta: il report serve a cambiare qualcosa il mese successivo.</li>
<li>Confronta il cliente con sé stesso, a parità di condizioni, e leggi gli scarti su più mesi.</li>
<li>I dati del report appartengono al cliente: consenso esplicito, spazio protetto, nessuna condivisione senza il suo accordo.</li>
</ul>
""",
        "faq": [
            {"q": "Cosa mettere nel report mensile di un cliente?", "a": "L'obiettivo di partenza, le presenze, due o tre misure di prestazione, le sensazioni del cliente e le modifiche decise per il mese successivo. Basta una pagina. Confronta ogni numero con il cliente stesso, mai con una media o con un altro cliente."},
            {"q": "Bisogna pesare il cliente a ogni verifica?", "a": "Solo se il peso corrisponde al suo obiettivo e se è d'accordo. Questo numero non dovrebbe mai essere l'unica misura del successo e può essere un dato sulla salute. Se il cliente parla di un disturbo alimentare o di una malattia, indirizzalo a un medico o a un dietista."},
            {"q": "Il personal trainer può mandare il report al medico o al fisioterapista del cliente?", "a": "Solo con l'accordo del cliente. La cosa più semplice è consegnargli il report, così lo inoltra lui. Senza questo accordo non mandarlo a nessuno, nemmeno a un professionista sanitario."},
        ],
        "sources": [
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Foster C, Florhaug JA, Franklin J, et al. A new approach to monitoring exercise training. <em>J Strength Cond Res</em>. 2001.", "u": "https://pubmed.ncbi.nlm.nih.gov/11708692/"},
            {"t": "Holland AE, Spruit MA, Troosters T, et al. An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease. <em>Eur Respir J</em>. 2014.", "u": "https://doi.org/10.1183/09031936.00150314"},
            {"t": "Sartor F, Bonato M, Papini G, et al. A 45-Second Self-Test for Cardiorespiratory Fitness: Heart Rate-Based Estimation in Healthy Individuals. <em>PLoS One</em>. 2016.", "u": "https://doi.org/10.1371/journal.pone.0168154"},
            {"t": "Regolamento (UE) 2016/679 del Parlamento europeo e del Consiglio, del 27 aprile 2016 (regolamento generale sulla protezione dei dati). EUR-Lex. 2016.", "u": "https://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Decreto legislativo 30 giugno 2003, n. 196, Codice in materia di protezione dei dati personali, art. 2-septies. Normattiva, testo vigente al 9 novembre 2026.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-06-30;196~art2septies!vig=2026-11-09"},
            {"t": "Garante per la protezione dei dati personali. Sanità e Ricerca scientifica.", "u": "https://www.garanteprivacy.it/temi/sanita-e-ricerca-scientifica"},
            {"t": "Legge 22 aprile 1941, n. 633, Protezione del diritto d'autore e di altri diritti connessi al suo esercizio, art. 96. Normattiva, testo vigente al 9 novembre 2026.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1941-04-22;633~art96!vig=2026-11-09"},
        ],
    },
    {
        "fr": "lire-etat-de-forme-client",
        "slug": "valutare-stato-di-forma-cliente",
        "title": "Sonno, fatica, carico: come valutare un cliente prima della seduta",
        "seo_title": "Stato di forma del cliente: come valutarlo prima di iniziare",
        "description": "Stato di forma del cliente: cosa chiedere prima della seduta, cosa cambia una notte corta, come monitorare il carico e cosa dicono davvero smartwatch e HRV.",
        "body": """
<p>La risposta breve: per valutare lo <strong>stato di forma del cliente</strong>, fai tre domande prima del riscaldamento, confronta le risposte con ciò che è normale per quel cliente, poi adatta la seduta quando più segnali vanno nella stessa direzione. Nessun indicatore basta da solo: né il sonno, né la variabilità della frequenza cardiaca, né il punteggio di uno smartwatch. Queste misure ti aiutano a dosare uno sforzo. Non fanno nessuna diagnosi.</p>

<h2>Cosa chiedere a un cliente prima della seduta?</h2>
<p>Bastano due minuti. Mantieni le stesse domande e la stessa scala da 1 a 5:</p>
<ul>
<li>Come hai dormito rispetto al solito?</li>
<li>Quanta energia hai oggi, stress compreso?</li>
<li>Hai un dolore o un fastidio nuovo?</li>
</ul>
<p>La revisione di Saw e colleghi (2016, 56 studi) mostra che le misure soggettive e quelle oggettive concordano poco, e che quelle soggettive riflettono meglio il carico di allenamento. Riguarda atleti, quindi applicala con cautela. Registra ogni risposta, perché conta solo lo scarto rispetto al suo normale. Un 2 da un cliente che risponde sempre 4 pesa più di un 2 da uno che risponde spesso 2.</p>

<h2>Una notte dormita male deve cambiare la seduta?</h2>
<p>Non per forza. La meta-analisi di Craven e colleghi (2022, 69 pubblicazioni, 959 partecipanti, per l'89% uomini) trova una prestazione in calo in media del 7,56% dopo 6 ore di sonno o meno, con un'eterogeneità molto alta tra gli studi. Due sfumature aiutano nella pratica:</p>
<ul>
<li><strong>Il tipo di notte.</strong> Gli effetti erano costanti solo dopo una notte in bianco o una sveglia anticipata, non dopo essere andati a letto tardi. Il calo arrivava allora a circa lo 0,4% per ogni ora di veglia prima dello sforzo.</li>
<li><strong>L'ora della seduta.</strong> Gli sforzi del pomeriggio e della sera ne risentivano, quelli del mattino molto poco.</li>
</ul>
<p>Un cliente che si è alzato alle 5 e arriva alle 19 è in una situazione diversa da uno che è andato a letto tardi e arriva alle 8. Queste medie comunque non prevedono la sua seduta: guarda come risponde al riscaldamento prima di cambiare qualcosa.</p>

<h2>Come monitorare il carico di allenamento senza strumenti?</h2>
<p>Fai valutare al cliente il suo sforzo da 0 a 10 dopo la seduta e moltiplica il voto per la durata: è l'RPE di seduta. Esempio di calcolo: 60 minuti valutati 7 danno 420 unità. Foster e colleghi lo hanno valutato nel 2001 rispetto a un metodo basato sulla frequenza cardiaca e lo hanno trovato valido su sforzi diversi. Somma le sedute, compreso l'esercizio fatto senza di te, poi confronta le settimane tra loro.</p>
<p>Questo punteggio descrive come il cliente ha percepito lo sforzo. I tuoi carichi, le serie e le distanze descrivono cosa ha fatto. A parità di lavoro, uno sforzo percepito che sale per più sedute merita una domanda. Lascia invece da parte il rapporto tra carico acuto e cronico per prevenire gli infortuni: Impellizzeri e colleghi hanno concluso nel 2020 che nessuna prova sostiene questo uso.</p>

<h2>Quanto sono affidabili smartwatch e HRV?</h2>
<p>Leggili come tendenze, con limiti noti.</p>
<ul>
<li><strong>Sonno.</strong> In Chinoy e colleghi (2021), sette dispositivi commerciali dell'epoca, indossati o posizionati vicino al letto e confrontati con la polisonnografia in 34 giovani adulti sani, rilevavano bene il sonno (sensibilità di almeno 0,93) e meno bene la veglia (specificità da 0,18 a 0,54). Le fasi del sonno erano incoerenti, e le notti disturbate erano misurate peggio. Ignora il dato di «sonno profondo» di una singola notte.</li>
<li><strong>Variabilità della frequenza cardiaca.</strong> Secondo la meta-analisi di Bellenger e colleghi (2016, 27 studi), aumenta a riposo quando l'adattamento è positivo e cambia poco con l'overreaching. Un valore basso non prova il sovrallenamento, e un valore normale non lo esclude. Questi studi riguardano atleti di resistenza, lontani dal cliente medio.</li>
<li><strong>Misurazione.</strong> La <a href="/methode/variabilite-cardiaque.html">variabilità della frequenza cardiaca</a> dipende dal sensore, da come si indossa l'orologio, dai battiti irregolari o da un farmaco che rallenta il cuore. Non puoi confrontarla da un dispositivo all'altro.</li>
<li><strong>Punto di riferimento.</strong> Ha senso solo la <a href="/methode/ligne-de-base.html">linea di base</a> del cliente stesso, costruita in più settimane. Mostra se si sta allontanando dalle sue abitudini, senza dire se quelle abitudini sono buone, e una deriva lenta può sfuggirle.</li>
<li><strong>Punteggi di recupero.</strong> Riassumono questi segnali, limiti compresi. Un punteggio basso non vieta niente, e uno alto non autorizza niente.</li>
</ul>
<p>Questi dati appartengono al cliente. Te li mostra se vuole, con il suo consenso esplicito, e tu non li passi a nessuno senza di lui. Non far mai dipendere la seduta da questa condivisione. In Italia ai dati sulla salute si applicano il GDPR e il Codice privacy (d.lgs. 196/2003): non possono essere diffusi, cioè mostrati a un pubblico indeterminato, e l'autorità di controllo è il Garante per la protezione dei dati personali.</p>

<h2>Quando adattare la seduta, e quando indirizzare al medico?</h2>
<p>Cerca la convergenza: un segnale da solo lo osservi, quando sono diversi agisci.</p>
<div class="tablewrap"><table>
<caption>Fonte: riferimenti prudenti di questa guida, senza valore diagnostico.</caption>
<thead><tr><th>Cosa osservi</th><th>Decisione possibile</th></tr></thead>
<tbody>
<tr><td>Notte corta, energia discreta, buon riscaldamento</td><td>Seduta prevista</td></tr>
<tr><td>Notte corta ed energia bassa, seduta di pomeriggio o di sera</td><td>Meno volume, nessun carico massimale</td></tr>
<tr><td>Sforzo percepito in aumento per più sedute</td><td>Settimana più leggera, cerca la causa con il cliente</td></tr>
<tr><td>Dolore che cambia il movimento</td><td>Togli l'esercizio, parere medico se persiste</td></tr>
<tr><td>Stanchezza insolita che dura nonostante un carico più leggero</td><td>Indirizza al medico</td></tr>
<tr><td>Sensazione di svenimento, dolore al petto, fiato corto anomalo, palpitazioni</td><td>Stop immediato, consulto medico e, in caso di emergenza, chiama il 112, il numero unico di emergenza (resta attivo anche il 118, per l'emergenza sanitaria)</td></tr>
</tbody>
</table></div>
<p>Non devi dare un nome a ciò che succede. «Sovrallenamento» e «carenza» sono conclusioni mediche. Descrivi ciò che osservi, suggerisci un consulto, e riporta le tendenze nel tuo <a href="/coachs/bilan-mensuel-client-coaching.html">report mensile</a>.</p>

<h2>In sintesi</h2>
<ul>
<li>Tre domande con un voto a ogni seduta ti danno già l'essenziale: lo scarto dal normale del cliente.</li>
<li>Sonno, carico, smartwatch e variabilità della frequenza cardiaca si leggono insieme e come tendenze. Nessuno basta da solo.</li>
<li>Adatti la seduta e non fai diagnosi: un sintomo nuovo o una stanchezza che dura sono affare del medico.</li>
</ul>
""",
        "faq": [
            {"q": "Come capire se un cliente è troppo stanco per allenarsi?", "a": "Chiedi come ha dormito, quanta energia ha e se ha un dolore nuovo, poi guarda come risponde al riscaldamento. Se più segnali calano, alleggerisci la seduta. Se la stanchezza dura o si accompagna a sintomi, indirizzalo al medico."},
            {"q": "Bisogna annullare la seduta dopo una notte dormita male?", "a": "Non per forza. Una notte corta abbassa in media la prestazione, soprattutto il pomeriggio o la sera e dopo una sveglia anticipata, ma la risposta varia da persona a persona. Mantieni la seduta se il cliente risponde bene al riscaldamento, altrimenti riduci volume o intensità."},
            {"q": "Un HRV basso significa sovrallenamento?", "a": "No. I risultati sono contraddittori e, secondo una meta-analisi del 2016 su atleti di resistenza, l'HRV a riposo cambia poco con l'overreaching. Un singolo calo può venire da una brutta notte o da una misurazione meno pulita: leggi la tendenza, insieme alle sensazioni del cliente."},
        ],
        "sources": [
            {"t": "Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures: a systematic review. <em>Br J Sports Med</em>. 2016.", "u": "https://doi.org/10.1136/bjsports-2015-094758"},
            {"t": "Craven J, McCartney D, Desbrow B, et al. Effects of Acute Sleep Loss on Physical Performance: A Systematic and Meta-Analytical Review. <em>Sports Med</em>. 2022.", "u": "https://doi.org/10.1007/s40279-022-01706-y"},
            {"t": "Foster C, Florhaug JA, Franklin J, et al. A new approach to monitoring exercise training. <em>J Strength Cond Res</em>. 2001.", "u": "https://pubmed.ncbi.nlm.nih.gov/11708692/"},
            {"t": "Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:Chronic Workload Ratio: Conceptual Issues and Fundamental Pitfalls. <em>Int J Sports Physiol Perform</em>. 2020.", "u": "https://doi.org/10.1123/ijspp.2019-0864"},
            {"t": "Chinoy ED, Cuellar JA, Huwa KE, et al. Performance of seven consumer sleep-tracking devices compared with polysomnography. <em>Sleep</em>. 2021.", "u": "https://doi.org/10.1093/sleep/zsaa291"},
            {"t": "Bellenger CR, Fuller JT, Thomson RL, et al. Monitoring Athletic Training Status Through Autonomic Heart Rate Regulation: A Systematic Review and Meta-Analysis. <em>Sports Med</em>. 2016.", "u": "https://doi.org/10.1007/s40279-016-0484-2"},
            {"t": "Decreto legislativo 30 giugno 2003, n. 196, Codice in materia di protezione dei dati personali, art. 2-septies. Normattiva, testo vigente al 9 novembre 2026.", "u": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-06-30;196~art2septies!vig=2026-11-09"},
            {"t": "Ministero della Salute. Numero unico europeo per le emergenze (NUE) 112. 2024.", "u": "https://www.salute.gov.it/new/it/tema/112-118-e-pronto-soccorso/numero-unico-europeo-le-emergenze-nue-112/"},
        ],
    },
]
