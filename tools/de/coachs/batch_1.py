# -*- coding: utf-8 -*-
# Adaptation allemande du lot 1 des guides coachs (Allemagne ; Autriche et Suisse seulement là
# où la fiche donne une différence vérifiée). Base : tools/en/coachs/batch_1.py.
# Faits : tools/intl/_faits-ue.md et tools/intl/_faits-de.md. Le PAR-Q+ n'est jamais reproduit.

ENTRIES = [
    {
        "fr": "fiche-client-coach-sportif",
        "slug": "kundenakte-personal-trainer",
        "title": "Kundenakte für Personal Trainer: Was gehört hinein?",
        "description": "Kundenakte für Personal Trainer: welche Bereiche hineingehören, was als Gesundheitsdaten zählt, was du besser nicht notierst und wie lange du sie aufbewahrst.",
        "body": """
<p>Die kurze Antwort: Eine <strong>Kundenakte für Personal Trainer</strong> kommt mit sieben Bereichen aus: Kontakt, Organisation, Ziel, Trainingshistorie, Gesundheit, Messwerte und Verlauf. Sobald darin eine Verletzung, eine Vorerkrankung oder die Antworten auf einen Fragebogen stehen, enthält sie Gesundheitsdaten, und die stehen nach Art. 9 DSGVO unter besonderem Schutz. Erfasse nur, was du brauchst, hol die Einwilligung deines Kunden ein und führe den Gesundheitsteil getrennt.</p>

<h2>Was gehört in eine Kundenakte?</h2>
<p>Hier ein möglicher Aufbau. Die letzte Spalte zeigt, wie du jeden Bereich behandelst, denn ob etwas zu den Gesundheitsdaten zählt, entscheidet sich im Einzelfall.</p>
<div class="tablewrap"><table>
<caption>Beispielhafte Bereiche, mit einer vorsichtigen Lesart der DSGVO.</caption>
<thead><tr><th>Bereich</th><th>Was du erfasst</th><th>Art der Daten</th></tr></thead>
<tbody>
<tr><td>Kontakt</td><td>Name, E-Mail, Telefon, Notfallkontakt</td><td>Allgemeine personenbezogene Daten</td></tr>
<tr><td>Organisation</td><td>Zeiten, Ort, Ausstattung, Paket, Startdatum</td><td>Allgemeine personenbezogene Daten</td></tr>
<tr><td>Ziel</td><td>Die eigenen Worte des Kunden, Frist, Motivation</td><td>Allgemein, außer es verrät einen Gesundheitszustand</td></tr>
<tr><td>Trainingshistorie</td><td>Aktuelle Aktivität, sportliche Vorgeschichte, Vorlieben, angestrebte Intensität</td><td>Allgemein, im Einzelfall prüfen</td></tr>
<tr><td>Gesundheit</td><td>Antworten im Fragebogen, berichtete Beschwerden, empfohlene ärztliche Abklärung</td><td>Gesundheitsdaten</td></tr>
<tr><td>Messwerte</td><td>Gewicht, Taillenumfang, Herzfrequenz, Schlaf</td><td>Wie Gesundheitsdaten behandeln</td></tr>
<tr><td>Verlauf</td><td>Tests, Einheiten, Lasten, Befinden, getroffene Entscheidungen</td><td>Sensibel, sobald mit Messwerten kombiniert</td></tr>
</tbody>
</table></div>
<p>Halte beim Ziel die genauen Worte deines Kunden fest. „Die Treppe zu meiner Wohnung schaffen, ohne im zweiten Stock stehen zu bleiben“ hilft dir mehr als „Ausdauer“, wenn du einen Test auswählst oder Fortschritte misst.</p>

<h2>Was zählt in der Kundenakte als Gesundheitsdaten?</h2>
<p>In der EU sind Gesundheitsdaten personenbezogene Daten über die körperliche oder geistige Gesundheit einer Person, aus denen Informationen über ihren Gesundheitszustand hervorgehen (Art. 4 Nr. 15 DSGVO). Gemeint ist der vergangene, gegenwärtige oder künftige Zustand, egal woher die Information stammt. Vorerkrankungen, Krankheiten, Behandlungen und Behinderungen gehören von Natur aus dazu. Auch eine Verletzung, von der dir ein Kunde erzählt, sagt etwas über seine körperliche Gesundheit aus: Sie kommt in denselben Bereich. Die Antworten auf einen <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">Gesundheitsfragebogen</a> behandelst du genauso.</p>
<p>Beim Gewicht kommt es auf den Zusammenhang an. Ein hohes Gewicht kann auf Adipositas hindeuten, und zusammen mit Schrittzahl oder Kalorienaufnahme kann auch das Gewicht zu den Gesundheitsdaten zählen. Herzfrequenz, Gewicht und Körpergröße können ebenfalls sensibel sein, vor allem wenn sie von einem vernetzten Gerät stammen. Eine schriftliche Einordnung von Schlafdaten habe ich nicht gefunden: Behandle sie sicherheitshalber wie Gesundheitsdaten. Deine Kundenakte bündelt all diese Messwerte an einem Ort, also legst du für das Ganze den strengsten Maßstab an.</p>
<p>Um diese Daten aufzubewahren, holst du die ausdrückliche Einwilligung deines Kunden ein, getrennt von deinen AGB, nachdem du ihm erklärt hast, was du erfasst und warum. Der Hintergrund: In der EU ist die Verarbeitung von Gesundheitsdaten grundsätzlich untersagt, außer in bestimmten Ausnahmefällen, und der erste davon ist eine ausdrückliche Einwilligung für einen oder mehrere festgelegte Zwecke. Dein Kunde kann sie jederzeit widerrufen, genauso einfach, wie er sie erteilt hat.</p>
<p>In Deutschland ergänzt das Bundesdatenschutzgesetz (BDSG) die DSGVO; zuständig für dich ist nicht der Bundesdatenschutzbeauftragte, sondern die Datenschutzaufsichtsbehörde deines Bundeslandes, in Bayern das Bayerische Landesamt für Datenschutzaufsicht.</p>

<h2>Was solltest du nicht in die Kundenakte schreiben?</h2>
<ul>
<li><strong>Eine Diagnose.</strong> Schreib zum Beispiel: „Rechtes Knie schmerzt auf der Treppe, gemeldet am 12. Januar, an Arzt verwiesen.“ Füge keinen eigenen Krankheitsnamen hinzu. Du deutest die Gesundheitsdaten deines Kunden nicht: Sobald ein Anzeichen Fragen aufwirft, verweist du ihn an einen Arzt. Krankheiten feststellen, heilen oder lindern darfst du als Nicht-Arzt in Deutschland ohnehin nur mit einer Erlaubnis nach dem Heilpraktikergesetz.</li>
<li><strong>Medizinische Details, die du nicht brauchst.</strong> Du musst wissen, dass ein ärztlicher Rat vorliegt und welche Grenzen er setzt. Die Kopie eines Rezepts oder eines Arztbriefs hat in deiner Akte nichts zu suchen.</li>
<li><strong>Ein Urteil über die Person.</strong> Dein Kunde kann Auskunft über seine Daten verlangen. In der EU musst du dann unverzüglich antworten, spätestens innerhalb eines Monats nach Eingang des Antrags; bei komplexen oder zahlreichen Anträgen kannst du die Frist um zwei weitere Monate verlängern, musst ihn aber innerhalb des ersten Monats darüber und über die Gründe informieren. Schreib jede Zeile so, als würde er sie lesen.</li>
<li><strong>Alles, was an deiner Einheit nichts ändert.</strong> Frag dich bei jedem Feld, was du mit dieser Information anders machen würdest. Fällt dir keine Antwort ein, streich das Feld.</li>
</ul>

<h2>Wie lange solltest du Kundendaten aufbewahren, und wo?</h2>
<p>Leg deine eigene Aufbewahrungsfrist fest, teile sie deinem Kunden mit und lösche den Gesundheitsteil, sobald du ihn nicht mehr brauchst, normalerweise am Ende der Zusammenarbeit. Für Rechnungen gelten eigene steuerliche Regeln: In Deutschland bewahrst du Rechnungen und andere Buchungsbelege acht Jahre auf, gerechnet ab Ende des Kalenderjahres. Trenn deshalb die Verwaltungsakte von der Trainingsakte, dann kannst du die eine löschen, ohne die andere anzurühren.</p>
<p>In der EU gilt, auch wenn du allein arbeitest: Die Ausnahme vom Verzeichnis von Verarbeitungstätigkeiten für Unternehmen mit weniger als 250 Beschäftigten greift nicht, wenn du Daten nicht nur gelegentlich verarbeitest oder wenn du Gesundheitsdaten verarbeitest. Dann musst du ein Verzeichnis führen, zumindest für diese Verarbeitungen. Jeder der beiden Fälle genügt: die regelmäßige Betreuung deiner Kunden ebenso wie Gesundheitsdaten.</p>
<p>Für die Speicherung gilt: In der EU musst du die Daten deiner Kunden mit geeigneten technischen und organisatorischen Maßnahmen schützen, die dem Risiko angemessen sind, zum Beispiel mit Verschlüsselung. Gesundheitsdaten sind sensibel, und ein WhatsApp-Verlauf oder eine ungeschützte Datei passt schlecht dazu.</p>

<h2>Wie hältst du eine Kundenakte aktuell?</h2>
<p>Leg sie beim <a href="/coachs/bilan-forme-premier-rendez-vous.html">Eingangscheck</a> an und ergänze nach jeder Einheit drei Dinge: was gemacht wurde, wie es deinem Kunden ging und was du beim nächsten Mal änderst. Halte auch die Ergebnisse der <a href="/coachs/tests-physiques-nouveau-client.html">Fitnesstests</a> fest, zusammen mit den Bedingungen, unter denen sie stattfanden.</p>
<p>Zeig deinem Kunden diese Zahlen. Eine Metaanalyse von 138 Studien mit 19.951 Personen (Harkin, 2016) zeigt, dass das Verfolgen von Fortschritten hilft, Ziele zu erreichen, mit stärkerem Effekt, wenn das Ergebnis schriftlich festgehalten oder öffentlich gemacht wird. Sie betrifft nicht nur Bewegung: Nimm sie als Orientierung.</p>
<p>Lies den Gesundheitsteil jedes Mal neu, wenn sich die Lage ändert. Neue Schmerzen führen dich zur selben Regel zurück: Du notierst sie, du deutest sie nicht, du verweist weiter.</p>
<p>Dieser Leitfaden dient nur der Information und ersetzt keine Beratung durch einen Anwalt oder einen Datenschutzbeauftragten.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Sieben Bereiche reichen, und jedes Feld sollte an deiner Einheit etwas ändern.</li>
<li>Verletzungen, Vorerkrankungen und Antworten im Fragebogen sind Gesundheitsdaten. Gewicht und Schlaf behandelst du sicherheitshalber genauso.</li>
<li>Halte Fakten fest, ohne sie zu deuten, trenne Gesundheit und Abrechnung und leg eine Aufbewahrungsfrist fest.</li>
</ul>
""",
        "faq": [
            {"q": "Wie legst du als Personal Trainer eine Kundenakte an?", "a": "Plane sieben Bereiche: Kontakt, Organisation, Ziel, Trainingshistorie, Gesundheit, Messwerte und Verlauf. Erfasse nur, was du brauchst, und führe den Gesundheitsteil getrennt, denn Gesundheitsdaten stehen nach Art. 9 DSGVO unter besonderem Schutz. Eine geschützte Tabelle oder eine Software eignen sich beide, solange der Zugang sicher ist."},
            {"q": "Enthält eine Kundenakte Gesundheitsdaten?", "a": "Fast immer. Verletzungen, Vorerkrankungen und Antworten im Fragebogen sind Gesundheitsdaten, und Gewicht oder Schlaf können es ebenfalls sein, besonders zusammen mit anderen Messwerten. Behandle sie im Zweifel so und hol eine ausdrückliche Einwilligung ein, getrennt von deinen AGB."},
            {"q": "Wie lange bewahrt ein Personal Trainer Kundendaten auf?", "a": "Leg deine eigene Frist fest, teile sie deinem Kunden mit und lösche den Gesundheitsteil, sobald du ihn nicht mehr brauchst, meist am Ende der Zusammenarbeit. Rechnungen und andere Buchungsbelege bewahrst du in Deutschland acht Jahre auf, gerechnet ab Ende des Kalenderjahres."},
        ],
        "sources": [
            {"t": "Verordnung (EU) 2016/679 des Europäischen Parlaments und des Rates vom 27. April 2016 zum Schutz natürlicher Personen bei der Verarbeitung personenbezogener Daten, zum freien Datenverkehr und zur Aufhebung der Richtlinie 95/46/EG (Datenschutz-Grundverordnung), Art. 4, 9, 12, 30 und 32. EUR-Lex. 2016.", "u": "https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Article 29 Working Party. Position Paper on the derogations from the obligation to maintain records of processing activities pursuant to Article 30(5) GDPR. 2018 (auf Englisch).", "u": "https://ec.europa.eu/newsroom/article29/items/624045"},
            {"t": "Bundesdatenschutzgesetz (BDSG), § 40 Aufsichtsbehörden der Länder.", "u": "https://www.gesetze-im-internet.de/bdsg_2018/__40.html"},
            {"t": "Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI). Seite mit den Anschriften der Datenschutzaufsichtsbehörden der Länder.", "u": "https://www.bfdi.bund.de/DE/Service/Anschriften/Laender/Laender-node.html"},
            {"t": "Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI). Seite mit der Anschrift der Datenschutzaufsicht in Bayern.", "u": "https://www.bfdi.bund.de/SharedDocs/Adressen/DE/LfD/Bayern.html"},
            {"t": "Gesetz über die berufsmäßige Ausübung der Heilkunde ohne Bestallung (Heilpraktikergesetz), § 1.", "u": "https://www.gesetze-im-internet.de/heilprg/__1.html"},
            {"t": "Abgabenordnung (AO), § 147 Ordnungsvorschriften für die Aufbewahrung von Unterlagen.", "u": "https://www.gesetze-im-internet.de/ao_1977/__147.html"},
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
        ],
    },
    {
        "fr": "bilan-forme-premier-rendez-vous",
        "slug": "eingangscheck-erstgespraech-personal-training",
        "title": "Eingangscheck im Personal Training: So läuft das Erstgespräch ab",
        "seo_title": "Eingangscheck: So läuft das Erstgespräch mit Kunden ab",
        "description": "Eingangscheck im Personal Training: wie du das Erstgespräch vorbereitest, welche Fragen du stellst, was bei Warnzeichen gilt und wie du den Termin abschließt.",
        "body": """
<p>Die kurze Antwort: Ein guter <strong>Eingangscheck im Personal Training</strong> folgt vier Schritten: das Ziel anhören, alles erkennen, was eine ärztliche Abklärung braucht, einen einfachen Ausgangswert messen und dann einen klaren Plan vorschlagen. Eine Norm, die Inhalt oder Dauer festlegt, habe ich nicht gefunden. Der Termin hilft dir zu entscheiden, ob ihr starten könnt, mit welcher Intensität und in welche Richtung. Eine Diagnose stellst du dabei nicht.</p>

<h2>Wie bereitest du das Erstgespräch mit einem neuen Kunden vor?</h2>
<p>Schick vorab drei Dinge, dann verlierst du nicht die Hälfte des Termins:</p>
<ul>
<li><strong>Den <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">Gesundheitsfragebogen</a></strong>, vor dem Termin auszufüllen, mit einer Erklärung, was du mit den Daten machst, und der Bitte um Einwilligung.</li>
<li><strong>Die praktischen Angaben:</strong> Ort, Kleidung, Wasser, Dauer.</li>
<li><strong>Die Art des Termins:</strong> Ob er kostenlos oder bezahlt ist, sagst du vorher. Der Leitfaden zum <a href="/coachs/seance-essai-coach-sportif.html">Probetraining</a> behandelt diese Frage.</li>
</ul>
<p>Nenn den Termin Eingangscheck oder Fitness-Check, nie Gesundheitscheck: Dieses Wort weckt eine Erwartung, die du nicht erfüllen kannst.</p>

<h2>Wie läuft ein Eingangscheck in einer Stunde ab?</h2>
<p>Eine Empfehlung zur Dauer habe ich nicht gefunden. Hier ein Beispiel für 60 Minuten, zum Anpassen:</p>
<ol>
<li><strong>5 Minuten, der Rahmen.</strong> Du erklärst, was passiert und was dein Kunde am Ende mitnimmt.</li>
<li><strong>20 Minuten, zuhören.</strong> Ziel, Trainingsgeschichte, Einschränkungen, Vorlieben.</li>
<li><strong>5 Minuten, Sicherheit.</strong> Gemeinsam geht ihr den Fragebogen durch.</li>
<li><strong>20 Minuten, Bewegung.</strong> Zwei oder drei einfache Tests, mit Aufwärmen, wenn das Protokoll es vorsieht.</li>
<li><strong>10 Minuten, die nächsten Schritte.</strong> Du fasst zusammen und machst deinen Vorschlag.</li>
</ol>
<p><a href="/coachs/tests-physiques-nouveau-client.html">Fitnesstests</a> legen einen Ausgangswert fest. Sie warten, wenn der Fragebogen oder das Gespräch eine gesundheitliche Frage aufwirft. Lass beim ersten Termin Spielraum: nichts Maximales mit jemandem, den du gerade kennenlernst, und kein Test, der in ärztliche Hände gehört. Die französische Gesundheitsbehörde HAS weist darauf hin, dass Belastungstests mit Atemgasanalyse (Spiroergometrie) in spezialisierten Einrichtungen stattfinden, mit eigens geschulten Ärzten.</p>

<h2>Welche Fragen stellst du im Erstgespräch?</h2>
<p>Offene Fragen, und ein Kunde, der mehr redet als du:</p>
<ul>
<li><strong>„Was führt dich gerade jetzt zu mir?“</strong> Der Grund für den Zeitpunkt sagt oft mehr als das genannte Ziel.</li>
<li><strong>„Woran wirst du merken, dass es funktioniert hat?“</strong> Du bekommst ein konkretes Kriterium, in seinen Worten.</li>
<li><strong>„Was hast du schon ausprobiert, und warum hast du aufgehört?“</strong> Du erkennst die Hindernisse, bevor sie wiederkommen.</li>
<li><strong>„Wie viele Einheiten passen wirklich in deine Woche?“</strong> Auf dieser Antwort baut der Trainingsplan auf.</li>
<li><strong>„Was machst du gern, und was kommt für dich nicht infrage?“</strong> Dein Kunde behält bei einem Teil der Entscheidungen die Kontrolle.</li>
</ul>
<p>Dieser letzte Punkt ist wichtig. Eine Übersichtsarbeit über 66 Studien (Teixeira, 2012) zeigt einen durchgängigen Zusammenhang zwischen selbstbestimmten Formen der Motivation und Bewegung, und die intrinsische Motivation sagt das langfristige Dranbleiben besser voraus. Die meisten dieser Studien sind beschreibend: Sie belegen einen Zusammenhang, keine Ursache. Der Leitfaden der HAS weist für die motivierende Gesprächsführung in dieselbe Richtung: Hindernisse erkennen und mit der Person realistische Ziele setzen.</p>

<h2>Was tun, wenn ein Kunde gesundheitliche Probleme angibt?</h2>
<p>Seit 2015 stützt sich das Screening des American College of Sports Medicine (ACSM) auf drei Faktoren: die aktuelle Aktivität, Anzeichen oder bekannte Herz-Kreislauf-, Stoffwechsel- oder Nierenerkrankungen und die angestrebte Intensität. Diese Überarbeitung reagierte auf ein Übermaß: zu viele unnötige Verweise an Ärzte, die Menschen davon abhalten können, sich zu bewegen. Auch die WHO hält eine vorherige ärztliche Freigabe ohne Gegenanzeige allgemein für unnötig, wenn die Aktivität leicht bis mittel ist und nicht über zügiges Gehen hinausgeht.</p>
<p>Die HAS beschreibt, wie du bei Zweifeln vorgehst:</p>
<ul>
<li><strong>Eine positive Antwort im Fragebogen:</strong> Vor dem Start wird ein ärztlicher Rat empfohlen.</li>
<li><strong>Anzeichen, die auf eine Erkrankung hindeuten:</strong> Die Person verzichtet auf Aktivität, egal mit welcher Intensität, und geht zu ihrem Arzt.</li>
<li><strong>45 Jahre oder älter, kein regelmäßiges intensives Training und ein Vorhaben nahe der Maximalbelastung:</strong> Ein ärztlicher Rat wird nahegelegt.</li>
</ul>
<p>In allen drei Fällen deutest du nichts. Du gibst wieder, was du gehört hast, erklärst, dass die Entscheidung bei einem Arzt liegt, notierst das Datum und verschiebst den Bewegungsteil. Hat dein Kunde vor deinen Augen Brustschmerzen oder wird er ohnmächtig, wählst du sofort die 112. Für Beschwerden, die nicht lebensbedrohlich sind, ist in Deutschland der ärztliche Bereitschaftsdienst unter 116 117 da. Diagnosen sind Sache des Arztes, und ein Satz wie „Das ist bestimmt dein Blutdruck“ hat im Eingangscheck nichts verloren.</p>

<h2>Wie beendest du einen Eingangscheck?</h2>
<p>Fass in drei Sätzen zusammen, was du verstanden hast, was du gemessen hast und was du vorschlägst. Nenn dann ein Ziel mit Datum, den Rhythmus der Einheiten und den Termin der nächsten Zwischenbilanz. Halte Bedingungen und Preis schriftlich fest, bevor sich dein Kunde verpflichtet.</p>
<p>Versprich kein Ergebnis in Zahlen, denn du kannst es weder garantieren noch beweisen. Sag, was du messen wirst und wann. In Deutschland brauchst du als Personal Trainer keine gesetzlich vorgeschriebene Ausbildung oder Lizenz; Krankheiten feststellen, heilen oder lindern darfst du als Nicht-Arzt aber nur mit einer Erlaubnis nach dem Heilpraktikergesetz. Eine Expertenantwort im Existenzgründungsportal des Bundeswirtschaftsministeriums (Stand: August 2017) rät selbstständigen Fitnesstrainern zu einer Berufshaftpflicht. Übertrag noch am selben Abend das Wichtigste in die <a href="/coachs/fiche-client-coach-sportif.html">Kundenakte</a>, solange die genauen Worte deines Kunden frisch sind.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Schick den Fragebogen vor dem Termin und mach das Zuhören zum längsten Teil.</li>
<li>Beim kleinsten gesundheitlichen Warnzeichen verschiebst du die Bewegung und verweist an einen Arzt, ohne zu deuten.</li>
<li>Schließ mit einem Ziel mit Datum und schriftlichen Bedingungen ab, ohne ein Ergebnis zu versprechen.</li>
</ul>
""",
        "faq": [
            {"q": "Was passiert beim Eingangscheck mit einem Personal Trainer?", "a": "Der Personal Trainer hört sich Ziel und Trainingsgeschichte an, geht den Gesundheitsfragebogen durch, macht zwei oder drei einfache Tests, wenn nichts dagegen spricht, und schlägt dann einen Plan vor. Dieser Termin bewertet die Fitness. Einen Arztbesuch ersetzt er nicht."},
            {"q": "Wie lange dauert ein Eingangscheck?", "a": "Eine Empfehlung zur Dauer habe ich nicht gefunden. Eine Stunde ist ein praktisches Format: ein Drittel zum Zuhören, ein Drittel für Bewegung, der Rest für Rahmen, Sicherheit und nächste Schritte. Pass es an deinen Kunden und die geplanten Tests an."},
            {"q": "Was fragt man einen neuen Kunden im Erstgespräch?", "a": "Was ihn gerade jetzt herführt, woran er merken wird, dass es funktioniert hat, was er schon ausprobiert hat, wie viel Zeit er wirklich hat, was er gern macht und was für ihn nicht infrage kommt. Dazu kommt der Gesundheitsfragebogen, und sobald eine Antwort es verlangt, verweist du an einen Arzt."},
        ],
        "sources": [
            {"t": "HAS, französische Gesundheitsbehörde. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022 (auf Französisch).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Teixeira PJ, Carraça EV, Markland D, et al. Exercise, physical activity, and self-determination theory: a systematic review. <em>Int J Behav Nutr Phys Act</em>. 2012.", "u": "https://doi.org/10.1186/1479-5868-9-78"},
            {"t": "gesund.bund.de, Bundesministerium für Gesundheit. Ärztlicher Bereitschaftsdienst. Stand: 23.04.2026.", "u": "https://gesund.bund.de/wege-im-gesundheitswesen/erwachsenenleben/notfaelle/aerztlicher-bereitschaftsdienst"},
            {"t": "Bundesagentur für Arbeit. BERUFENET: Fitnesstrainer/in, Zugang zur Tätigkeit.", "u": "https://web.arbeitsagentur.de/berufenet/beruf/15658"},
            {"t": "Gesetz über die berufsmäßige Ausübung der Heilkunde ohne Bestallung (Heilpraktikergesetz), § 1.", "u": "https://www.gesetze-im-internet.de/heilprg/__1.html"},
            {"t": "Existenzgründungsportal des Bundeswirtschaftsministeriums. Selbständig als Fitnesstrainer: Voraussetzungen? Stand: August 2017.", "u": "https://www.existenzgruendungsportal.de/Redaktion/DE/BMWK-Infopool/Antworten/Gruendungsplanung/Freie-Berufe/unterrichtende-Taetigkeit/Selbstaendig-als-Fitnesstrainer-Voraussetzungen"},
        ],
    },
    {
        "fr": "questionnaire-sante-avant-le-sport-client",
        "slug": "gesundheitsfragebogen-vor-dem-training",
        "title": "Gesundheitsfragebogen vor dem Training: Was fragst du ab?",
        "description": "Gesundheitsfragebogen vor dem Training: was du als Personal Trainer abfragst, was beim PAR-Q+ zu beachten ist und was tun, wenn ein Kunde mit Ja antwortet.",
        "body": """
<p>Die kurze Antwort: Ein <strong>Gesundheitsfragebogen vor dem Training</strong> fragt nach der aktuellen Aktivität, bekannten Erkrankungen, neuen Symptomen und der angestrebten Intensität. Eine deutsche Vorschrift, die ihn verlangt, habe ich nicht gefunden, was nicht beweist, dass es keine gibt. Nützlich ist das Werkzeug in jedem Fall. Die französische Gesundheitsbehörde HAS empfiehlt einen selbst auszufüllenden Fragebogen für alle, die eine Aktivität von mindestens mittlerer Intensität beginnen oder steigern wollen, und hält fest, dass Bewegungsfachleute ihn anbieten können. Antwortet ein Kunde mit Ja, deutest du nichts: Du verweist ihn vor dem Start an einen Arzt.</p>

<h2>Brauchen Personal Trainer einen Gesundheitsfragebogen oder ein Attest?</h2>
<p>Eine Vorschrift, die das für Personal Training in Deutschland verlangt, habe ich nicht gefunden; dass es keine gibt, ist damit aber nicht bewiesen. Fest steht: In Deutschland brauchst du als Personal Trainer keine gesetzlich vorgeschriebene Ausbildung oder Lizenz; Krankheiten feststellen, heilen oder lindern darfst du als Nicht-Arzt aber nur mit einer Erlaubnis nach dem Heilpraktikergesetz. Unabhängig von jeder Pflicht kannst du einen Fragebogen oder ein ärztliches Attest in der Regel in deiner Vereinbarung mit dem Kunden zur Bedingung machen. Und prüf, ob deine Berufshaftpflicht abdeckt, was du anbietest.</p>

<h2>PAR-Q+ oder eigener Fragebogen: Was solltest du nutzen?</h2>
<div class="tablewrap"><table>
<caption>Quelle: HAS 2022 und die Nutzungsbedingungen des PAR-Q+, gelesen am 31. Oktober 2026.</caption>
<thead><tr><th>Option</th><th>Einsatz</th><th>Was du wissen solltest</th></tr></thead>
<tbody>
<tr><td>PAR-Q+</td><td>Screening vor der Aktivität, 15 bis 69 Jahre</td><td>7 Fragen, geschützter Text</td></tr>
<tr><td>Eigener Fragebogen</td><td>Was deine Einheit verändert</td><td>Selbst schreiben, ohne den PAR-Q+ zu kopieren</td></tr>
</tbody>
</table></div>
<p>Beim PAR-Q+ ist Vorsicht geboten. Seine Nutzungsbedingungen verlangen eine vorherige schriftliche Erlaubnis, um ihn zu verändern oder in eine App, eine Website, eine Software oder eine Online-Umfrage einzubauen. Die Quelle zu nennen, gilt nicht als Erlaubnis. Unveränderte offizielle Fassungen sind derzeit für bestimmte individuelle, klinische und Bildungszwecke sowie für nicht kommerzielle Forschung kostenlos. Personal Trainer werden in den Bedingungen nicht ausdrücklich genannt, obwohl die Website Material für Bewegungsfachleute anbietet, und für eine kommerzielle Nutzung können Gebühren anfallen. Schreib im Zweifel an den Rechteinhaber.</p>
<p>Der einfachste Weg: Bitte deinen Kunden, ihn selbst auf der offiziellen Website eparmedx.com auszufüllen. Dass der Text anderswo abgedruckt ist, gibt dir keine Erlaubnis, ihn in deinen Fragebogen zu übernehmen.</p>

<h2>Was sollte ein Gesundheitsfragebogen vor dem Sport abfragen?</h2>
<p>Für deinen eigenen Fragebogen gehst du von der Logik des American College of Sports Medicine (ACSM) aus, die sich auf drei Faktoren stützt, und ergänzt, was deiner Einheit dient:</p>
<ul>
<li><strong>Aktuelle Aktivität.</strong> Wie viele Einheiten pro Woche, wie lange, mit welcher Intensität.</li>
<li><strong>Was bekannt ist.</strong> Eine diagnostizierte Herz-Kreislauf-, Stoffwechsel- oder Nierenerkrankung. Ja oder Nein genügt.</li>
<li><strong>Was neu ist.</strong> Ein ungewohntes Anzeichen, in Ruhe oder bei Belastung.</li>
<li><strong>Angestrebte Intensität.</strong> Was dein Kunde machen will, und auf welchem Niveau.</li>
<li><strong>Was die Bewegung einschränkt.</strong> Beschwerden, eine kürzliche Operation, eine Schwangerschaft: alles, was dich zwingt, eine Übung anzupassen.</li>
</ul>
<p>Prüf jede Frage mit demselben Filter: Was änderst du an deiner Einheit, wenn die Antwort Ja lautet? Ändert sich nichts, streich sie.</p>
<p>Die HAS nennt zwei Altersmarken. Ab 45 Jahren, ohne regelmäßige intensive Aktivität und mit einem Vorhaben nahe der Maximalbelastung, wird ein ärztlicher Rat nahegelegt. Ab 70 Jahren wird er für Aktivität von mindestens hoher Intensität empfohlen.</p>

<h2>Was tun, wenn ein Kunde im Fragebogen mit Ja antwortet?</h2>
<p>Die HAS ist eindeutig. Eine positive Antwort: Vor dem Start wird ein ärztlicher Rat empfohlen. Anzeichen oder Symptome, die auf eine Erkrankung hindeuten: Die Person pausiert und geht zu ihrem Arzt. Alles negativ: Sie kann aktiver werden, mit den üblichen Vorsichtsmaßnahmen.</p>
<p>Deine Rolle endet hier. Du beurteilst nicht, wie ernst es ist, und du beruhigst nicht. Du notierst das Datum, wartest, bis dein Kunde dir den erhaltenen Rat und etwaige Grenzen bestätigt, und passt dann an. Lass den Fragebogen erneut ausfüllen, sobald sich die Lage ändert.</p>

<h2>Gesundheitsfragebogen und Datenschutz: Wie gehst du mit den Antworten um?</h2>
<p>Ein Gesundheitsfragebogen enthält Gesundheitsdaten. In der EU ist ihre Verarbeitung grundsätzlich untersagt, außer in bestimmten Ausnahmefällen; der erste ist die ausdrückliche Einwilligung deines Kunden für einen oder mehrere festgelegte Zwecke, die er jederzeit und genauso einfach widerrufen kann, wie er sie erteilt hat. Hol sie getrennt von deinen AGB ein, nachdem du gesagt hast, was du erfasst und warum. Ein Punkt bleibt offen: Eine Einwilligung zählt nur, wenn die Person wirklich ablehnen kann, und ob du einen Kunden abweisen darfst, der den Fragebogen leer lässt, ist nicht geklärt. In Deutschland ergänzt das Bundesdatenschutzgesetz (BDSG) die DSGVO; zuständig für dich ist nicht der Bundesdatenschutzbeauftragte, sondern die Datenschutzaufsichtsbehörde deines Bundeslandes. Bewahre die Antworten im Gesundheitsteil deiner <a href="/coachs/fiche-client-coach-sportif.html">Kundenakte</a> auf.</p>
<p>Dieser Leitfaden dient nur der Information und ersetzt keine Beratung durch einen Arzt oder einen Anwalt.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Eine deutsche Vorschrift, die einen Fragebogen verlangt, habe ich nicht gefunden; die HAS empfiehlt aber einen vor dem Start.</li>
<li>Den PAR-Q+ darfst du ohne schriftliche Erlaubnis nicht in einen eigenen Fragebogen kopieren.</li>
<li>Antwortet ein Kunde mit Ja, deutest du nichts: Du verweist ihn vor dem Start an einen Arzt.</li>
</ul>
""",
        "faq": [
            {"q": "Ist der PAR-Q+ Pflicht?", "a": "Eine Vorschrift, die ihn in Deutschland verlangt, habe ich nicht gefunden, ihr Fehlen ist damit aber nicht bewiesen. Die französische Gesundheitsbehörde HAS empfiehlt einen solchen selbst auszufüllenden Fragebogen, bevor jemand eine Aktivität von mindestens mittlerer Intensität beginnt oder steigert. Die Nutzungsbedingungen des PAR-Q+ verbieten, ihn ohne schriftliche Erlaubnis zu verändern oder in ein Online-Werkzeug einzubauen."},
            {"q": "Darf ein Personal Trainer ein ärztliches Attest verlangen?", "a": "Ja, in der Regel kannst du es in deiner Vereinbarung mit dem Kunden zur Bedingung machen. Eine deutsche Vorschrift, die es verlangt, habe ich nicht gefunden. Machen die Antworten im Fragebogen einen ärztlichen Rat nötig, wartest du ihn vor dem Start ab."},
            {"q": "Was tun, wenn ein Kunde im Gesundheitsfragebogen mit Ja antwortet?", "a": "Deute die Antwort nicht und beruhige nicht. Vor dem Start wird ein ärztlicher Rat empfohlen, und wer Anzeichen oder Symptome einer Erkrankung hat, pausiert und geht zu seinem Arzt. Notiere das Datum und passe an, sobald dein Kunde dir den Rat und etwaige Grenzen bestätigt."},
        ],
        "sources": [
            {"t": "HAS, französische Gesundheitsbehörde. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022 (auf Französisch).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "PAR-Q+ Collaboration. Terms and Conditions. 2026 (auf Englisch).", "u": "https://eparmedx.com/terms-and-conditions/"},
            {"t": "Verordnung (EU) 2016/679 des Europäischen Parlaments und des Rates vom 27. April 2016 zum Schutz natürlicher Personen bei der Verarbeitung personenbezogener Daten, zum freien Datenverkehr und zur Aufhebung der Richtlinie 95/46/EG (Datenschutz-Grundverordnung), Art. 7 und 9. EUR-Lex. 2016.", "u": "https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Bundesdatenschutzgesetz (BDSG), § 40 Aufsichtsbehörden der Länder.", "u": "https://www.gesetze-im-internet.de/bdsg_2018/__40.html"},
            {"t": "Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI). Seite mit den Anschriften der Datenschutzaufsichtsbehörden der Länder.", "u": "https://www.bfdi.bund.de/DE/Service/Anschriften/Laender/Laender-node.html"},
            {"t": "Bundesagentur für Arbeit. BERUFENET: Fitnesstrainer/in, Zugang zur Tätigkeit.", "u": "https://web.arbeitsagentur.de/berufenet/beruf/15658"},
            {"t": "Gesetz über die berufsmäßige Ausübung der Heilkunde ohne Bestallung (Heilpraktikergesetz), § 1.", "u": "https://www.gesetze-im-internet.de/heilprg/__1.html"},
        ],
    },
    {
        "fr": "tests-physiques-nouveau-client",
        "slug": "fitnesstests-neue-kunden",
        "title": "Fitnesstests für neue Kunden: Welche eignen sich?",
        "description": "Fitnesstests für neue Kunden: welche du je nach Profil wählst, wie du sie zuverlässig durchführst, wie du die Ergebnisse liest und was der Ruffier-Test taugt.",
        "body": """
<p>Die kurze Antwort: Eine offizielle Testbatterie für <strong>Fitnesstests mit neuen Kunden</strong> habe ich nicht gefunden. Wähl drei oder vier Tests passend zum Ziel: einen für die Ausdauer, einen für den Unterkörper, einen für den Oberkörper und einen Gleichgewichtstest, wenn das Profil es verlangt. Sie vergleichen deinen Kunden mit sich selbst. Eine Diagnose stellen sie nicht.</p>

<h2>Welche Fitnesstests passen zu welchem Kunden?</h2>
<p>Die französische Gesundheitsbehörde HAS beschreibt die gängigsten Feldtests und weist darauf hin, dass kein einzelner Test die Kraft oder die Beweglichkeit des ganzen Körpers misst. Die Tabelle verbindet ihre Richtwerte mit einigen Studien.</p>
<div class="tablewrap"><table>
<caption>Quelle: HAS 2022; Holland 2014; Jones 1999; Penry 2011.</caption>
<thead><tr><th>Fähigkeit</th><th>Test</th><th>Profil</th><th>Was du wissen solltest</th></tr></thead>
<tbody>
<tr><td>Ausdauer</td><td>6-Minuten-Gehtest</td><td>Einsteiger, ältere Menschen, Wiedereinstieg</td><td>Klinisch validiert, nicht an Sportlern</td></tr>
<tr><td>Ausdauer</td><td>12-Minuten-Lauf</td><td>Junge, bereits aktive Erwachsene</td><td>Intensive Belastung, die geschätzte VO2max mit Vorsicht nehmen</td></tr>
<tr><td>Beine</td><td>30-Sekunden-Aufstehtest</td><td>Ältere Menschen, Einsteiger</td><td>Stuhl ohne Armlehnen, ohne Hände. Validiert ab 60 Jahren</td></tr>
<tr><td>Oberkörper</td><td>Liegestütze ohne Pause</td><td>Erwachsene ohne Schulterbeschwerden</td><td>Mischt Kraft und Ausdauer</td></tr>
<tr><td>Kraft</td><td>10- bis 15-RM</td><td>Einsteiger, ältere Menschen, Wiedereinstieg</td><td>Gilt nur für die jeweilige Übung</td></tr>
<tr><td>Beweglichkeit</td><td>Sit-and-Reach-Test</td><td>Kunden ohne Rückenschmerzen</td><td>Misst vor allem die hintere Oberschenkelmuskulatur</td></tr>
<tr><td>Gleichgewicht</td><td>Einbeinstand mit geschlossenen Augen</td><td>Ältere Menschen</td><td>Drei Versuche, beste Zeit. Bleib daneben, nahe einer Stütze</td></tr>
</tbody>
</table></div>
<p>Zwei Beispiele für eine Auswahl. Für einen bisher inaktiven 55-Jährigen, der wieder einsteigt: 6-Minuten-Gehtest, Aufstehtest, Einbeinstand. Für eine aktive 30-Jährige mit Kraftziel: 12-Minuten-Lauf, Liegestütze und ein 8RM-Test an zwei Übungen, die sie beherrscht, verteilt auf zwei Termine.</p>
<p>Lies vor jedem Test den <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">Gesundheitsfragebogen</a> noch einmal. Verlangt er einen ärztlichen Rat, wartet der Test.</p>

<h2>Wie führst du Fitnesstests durch, ohne die Ergebnisse zu verfälschen?</h2>
<p>Ein Test ist nur etwas wert, wenn du ihn identisch wiederholen kannst. Der technische Standard der European Respiratory Society und der American Thoracic Society (ERS/ATS; Holland, 2014) hält Gehtests bei chronischen Atemwegserkrankungen für valide, zuverlässig und veränderungssensitiv, betont aber, wie empfindlich sie auf kleine methodische Unterschiede reagieren. Er empfiehlt zwei Durchgänge im 6-Minuten-Gehtest, mit mindestens 30 Minuten Abstand, um einen stabilen Ausgangswert zu erhalten.</p>
<ul>
<li><strong>Gleicher Aufbau.</strong> Gleicher Ort, gleiche Strecke, gleiche Tageszeit, gleiche Schuhe, gleicher Stuhl. Die HAS beschreibt den 6-Minuten-Gehtest um zwei Hütchen im Abstand von 30 m. Der ERS/ATS-Standard verlangt einen ebenen Untergrund und mindestens 30 m: Auf einer kürzeren Strecke kannst du die Normwerte vergessen.</li>
<li><strong>Gleiche Worte.</strong> Schreib deine Anweisungen auf und lies sie vor. Für den Gehtest sieht der Standard jede Minute einen festen Satz vor, und sonst nichts. Bleibt dein Kunde stehen, läuft die Zeit weiter.</li>
<li><strong>Gleiche Vorbereitung.</strong> Für den 6-Minuten-Gehtest kein Aufwärmen und keine intensive Belastung in den 2 Stunden davor, so der Standard. Bei den anderen Tests bleibt das Aufwärmen immer gleich.</li>
<li><strong>Schriftlich festhalten.</strong> Notiere die Bedingungen neben dem Ergebnis, sonst vergleichst du am Ende zwei verschiedene Dinge.</li>
</ul>
<p>Meldet dein Kunde Schmerzen, Schwindel, ungewöhnliche Atemnot oder Krämpfe, oder schwankt er oder wird blass, brichst du den Test ab und verweist ihn an einen Arzt. Bei Brustschmerzen oder einer Ohnmacht lässt du ihn sich setzen oder hinlegen und wählst sofort die 112. Für Beschwerden, die nicht lebensbedrohlich sind, ist in Deutschland rund um die Uhr der ärztliche Bereitschaftsdienst unter 116 117 erreichbar.</p>

<h2>Darf ein neuer Kunde einen Maximaltest machen?</h2>
<p>Nicht beim ersten Termin, außer bei einem trainierten Kunden, der den Test schon kennt. Die HAS beschreibt das 1RM als zuverlässigen Indikator für die Kraft und Tests mit 4RM oder 8RM als zuverlässige Schätzung. Tests mit 10 bis 15 Wiederholungen hält sie für sicherer bei älteren, untrainierten oder chronisch kranken Menschen. Auch bei 4 oder 8 Wiederholungen wartest du, bis die Technik sauber ist. Der 12-Minuten-Lauf verlangt bereits eine anhaltende Anstrengung: Heb ihn dir für Kunden auf, die Intensität gewohnt sind.</p>
<p>Verwechsle diese Tests nicht mit einer ärztlichen Belastungsuntersuchung, die mit EKG- und Blutdrucküberwachung in einem klinischen Rahmen stattfindet.</p>

<h2>Wie zuverlässig ist der Ruffier-Test?</h2>
<p>Er bleibt ein einfacher Anhaltspunkt, der die kardiorespiratorische Fitness nur ungenau schätzt. In einer Studie mit 81 gesunden Erwachsenen (Sartor, 2016) korrelierte der Ruffier-Dickson-Index mit -0,40 mit der gemessenen Fitness und erklärte 15 % der Variabilität. In der Testtabelle der HAS taucht er nicht auf. Besteht dein Kunde darauf, vergleichst du seine Werte untereinander und leitest daraus keine VO2max ab.</p>

<h2>Wie liest du die Ergebnisse, und wann testest du erneut?</h2>
<p>Vergleiche deinen Kunden mit sich selbst: Genau dafür steht eine <a href="/methode/ligne-de-base.html">Baseline</a>. Normwerte beschreiben andere Gruppen. Für den 6-Minuten-Gehtest fand Enright (1998) bei 290 gesunden Erwachsenen zwischen 40 und 80 Jahren einen Median von 576 m bei Männern und 494 m bei Frauen, und die Gleichungen erklären etwa 40 % der Varianz. Für den 12-Minuten-Lauf berichtet Penry (2011) eine gute Zuverlässigkeit bei jungen Erwachsenen, mahnt aber zur Vorsicht, wenn man daraus eine VO2max ableitet.</p>
<p>Eine Abweichung von einer Norm erlaubt dir keinen Schluss auf die Gesundheit deines Kunden. Überrascht dich ein Ergebnis, verweist du ihn an einen Arzt, ohne es zu kommentieren. Der Aufstehtest wiederum wurde an 76 Erwachsenen über 60 validiert (Jones, 1999): Seine Werte lassen sich nicht auf einen 30-jährigen Kunden übertragen.</p>
<p>Eine offizielle Häufigkeit für Wiederholungstests habe ich nicht gefunden. Am logischsten testest du am Ende eines Blocks im <a href="/coachs/creer-programme-personnalise-client.html">Trainingsplan</a> erneut, unter denselben Bedingungen, und zeigst die Entwicklung im <a href="/coachs/bilan-mensuel-client-coaching.html">monatlichen Fortschrittsbericht</a>.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Drei oder vier Tests passend zum Ziel reichen, ausgewählt nach Profil.</li>
<li>Nutze jedes Mal dasselbe Protokoll, notiere die Bedingungen und vergleiche deinen Kunden mit sich selbst.</li>
<li>Ein Test stellt keine Diagnose: Beim kleinsten Warnzeichen brichst du ab und verweist an einen Arzt.</li>
</ul>
""",
        "faq": [
            {"q": "Welcher Fitnesstest eignet sich für Anfänger?", "a": "Der 6-Minuten-Gehtest für die Ausdauer, der 30-Sekunden-Aufstehtest für die Beine und bei Bedarf ein 10- bis 15-RM. Diese Tests lassen sich leicht dosieren. Lies vor dem Start immer den Gesundheitsfragebogen noch einmal."},
            {"q": "Ist der Ruffier-Test zuverlässig?", "a": "Er ist ein einfacher Anhaltspunkt, der die kardiorespiratorische Fitness nur ungenau schätzt. In einer Studie mit 81 gesunden Erwachsenen erklärte er 15 % der Variabilität. In der Testtabelle der französischen Gesundheitsbehörde HAS taucht er nicht auf."},
            {"q": "Wie oft sollte man einen Kunden erneut testen?", "a": "Eine offizielle Häufigkeit habe ich nicht gefunden. Am logischsten testest du am Ende eines Trainingsblocks erneut, unter denselben Bedingungen, um deinen Kunden mit sich selbst zu vergleichen."},
        ],
        "sources": [
            {"t": "HAS, französische Gesundheitsbehörde. Guide des connaissances sur l'activité physique et la sédentarité. 2022 (auf Französisch).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2022-08/guide_connaissance_ap_sedentarite_vf.pdf"},
            {"t": "Holland AE, Spruit MA, Troosters T, et al. An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease. <em>Eur Respir J</em>. 2014.", "u": "https://doi.org/10.1183/09031936.00150314"},
            {"t": "Enright PL, Sherrill DL. Reference equations for the six-minute walk in healthy adults. <em>Am J Respir Crit Care Med</em>. 1998.", "u": "https://doi.org/10.1164/ajrccm.158.5.9710086"},
            {"t": "Jones CJ, Rikli RE, Beam WC. A 30-s chair-stand test as a measure of lower body strength in community-residing older adults. <em>Res Q Exerc Sport</em>. 1999.", "u": "https://doi.org/10.1080/02701367.1999.10608028"},
            {"t": "Penry JT, Wilcox AR, Yun J. Validity and reliability analysis of Cooper's 12-minute run and the multistage shuttle run in healthy adults. <em>J Strength Cond Res</em>. 2011.", "u": "https://doi.org/10.1519/JSC.0b013e3181cc2423"},
            {"t": "Sartor F, Bonato M, Papini G, et al. A 45-Second Self-Test for Cardiorespiratory Fitness: Heart Rate-Based Estimation in Healthy Individuals. <em>PLoS One</em>. 2016.", "u": "https://doi.org/10.1371/journal.pone.0168154"},
            {"t": "Europäische Kommission. 112, the EU's emergency phone number. 2026 (auf Englisch).", "u": "https://digital-strategy.ec.europa.eu/en/policies/112"},
            {"t": "gesund.bund.de, Bundesministerium für Gesundheit. Ärztlicher Bereitschaftsdienst. Stand: 23.04.2026.", "u": "https://gesund.bund.de/wege-im-gesundheitswesen/erwachsenenleben/notfaelle/aerztlicher-bereitschaftsdienst"},
        ],
    },
    {
        "fr": "creer-programme-personnalise-client",
        "slug": "trainingsplan-fuer-kunden-erstellen",
        "title": "Trainingsplan für Kunden erstellen: So gehst du vor",
        "description": "Trainingsplan für Kunden erstellen: vom Eingangscheck bis zur Progression, mit Richtwerten von WHO und ACSM für jedes Ziel und den Grenzen bei der Ernährung.",
        "body": """
<p>Die kurze Antwort: Ein <strong>individueller Trainingsplan für Kunden</strong> beginnt beim Eingangscheck, nie bei einer Vorlage. Geh vom Ziel deines Kunden aus, von seiner tatsächlich verfügbaren Zeit und seinem Niveau. Leg Umfang und Intensität fest, wähl eine Aufteilung, die er durchhält, schreib eine Progressionsregel auf und passe dann nach seinen Rückmeldungen an. Das 2026 veröffentlichte Positionspapier des American College of Sports Medicine (ACSM) zeigt, dass nur wenige Variablen die Ergebnisse wirklich verändern: Konzentrier dich auf diese.</p>

<h2>Was musst du wissen, bevor du einen Trainingsplan schreibst?</h2>
<p>Fünf Informationen entscheiden fast alles. Sie stammen aus dem <a href="/coachs/bilan-forme-premier-rendez-vous.html">Eingangscheck</a> und den <a href="/coachs/tests-physiques-nouveau-client.html">Fitnesstests</a>:</p>
<ul>
<li><strong>Das Ziel</strong>, in den Worten deines Kunden, mit einer Frist.</li>
<li><strong>Die tatsächlich verfügbare Zeit:</strong> die Zahl der Einheiten, die er auch in einer vollen Woche durchhält.</li>
<li><strong>Das Niveau:</strong> was er heute macht und was er früher gemacht hat.</li>
<li><strong>Ort und Ausstattung.</strong></li>
<li><strong>Die Grenzen:</strong> gemeldete Beschwerden, ein ausstehender ärztlicher Rat oder ärztlich gesetzte Einschränkungen.</li>
</ul>
<p>Steht ein ärztlicher Rat noch aus, wartet auch der Trainingsplan. Hat dein Kunde Einschränkungen bekommen, setzt du sie genau so um, ohne sie neu auszulegen.</p>

<h2>Wie legst du Trainingsumfang und Intensität fest?</h2>
<p>Zwei Referenzen genügen für die Richtwerte: die WHO für die Gesundheit und das ACSM für das Krafttraining, gestützt auf 137 systematische Übersichtsarbeiten mit mehr als 30.000 Teilnehmenden, alle gesunde Erwachsene.</p>
<div class="tablewrap"><table>
<caption>Quelle: WHO 2020; ACSM 2026; Schoenfeld 2017. Gesunde Erwachsene.</caption>
<thead><tr><th>Ziel</th><th>Richtwert</th><th>Quelle</th></tr></thead>
<tbody>
<tr><td>Gesundheit, Wiedereinstieg</td><td>150 bis 300 Minuten moderate Aktivität pro Woche oder 75 bis 150 Minuten intensive Aktivität, dazu Krafttraining für alle großen Muskelgruppen an 2 oder mehr Tagen</td><td>WHO</td></tr>
<tr><td>Ältere Menschen</td><td>Innerhalb dieses Umfangs vielseitige Aktivität mit Schwerpunkt auf Gleichgewicht und Kraft, an 3 oder mehr Tagen pro Woche</td><td>WHO</td></tr>
<tr><td>Kraft</td><td>80 % des 1RM oder mehr, 2 bis 3 Sätze, 2 oder mehr Einheiten pro Woche</td><td>ACSM</td></tr>
<tr><td>Muskelaufbau</td><td>10 oder mehr Sätze pro Woche und Muskelgruppe. Mehr Umfang, mehr Zuwachs (15 Studien)</td><td>ACSM, Schoenfeld</td></tr>
<tr><td>Schnellkraft</td><td>30 bis 70 % des 1RM, schnelle konzentrische Phase</td><td>ACSM</td></tr>
</tbody>
</table></div>
<p>Diese Zahlen beschreiben das Ziel, weit über die erste Woche hinaus. Die WHO rät allen, die weit davon entfernt sind, klein anzufangen und dann Häufigkeit, Intensität und Dauer schrittweise zu steigern. Verglichen mit gar keinem Training verbessert Krafttraining schon Kraft, Muskelmasse und Gleichgewicht. Für Einsteiger reicht ein einfacher erster Plan.</p>
<p>Andere Stellschrauben zählen weniger, als viele denken. Laut ACSM haben Training bis zum Muskelversagen oder ein Wechsel der Geräteart die Ergebnisse nicht durchgängig verändert. Ein Kunde ohne Studio kann einem echten Trainingsplan folgen, solange Last oder Wiederholungen steigen können.</p>

<h2>Ganzkörper oder Split: Wie verteilst du die Einheiten auf die Woche?</h2>
<p>Wähle nach dem Kalender deines Kunden. Eine Metaanalyse von 14 Studien mit 392 Personen (Ramos-Campo, 2024) fand bei gleichem Umfang keinen signifikanten Unterschied bei Kraft oder Muskelmasse zwischen Ganzkörper- und Splittraining. Die Autoren folgern, dass die Wahl den Vorlieben folgen kann.</p>
<p>Hier eine Beispiellogik, zum Anpassen:</p>
<ul>
<li><strong>2 Einheiten:</strong> jedes Mal Ganzkörper.</li>
<li><strong>3 Einheiten:</strong> Ganzkörper oder ein Wechsel aus Ober- und Unterkörper.</li>
<li><strong>4 Einheiten oder mehr:</strong> Ein Split wird möglich, wenn dein Kunde sie wirklich durchhält.</li>
</ul>
<p>Denk an die verpasste Woche: Fällt eine Einheit aus, bleibt beim Split eine Muskelgruppe auf der Strecke, beim Ganzkörperplan nicht. Bei einem Kraftziel setzt du die wichtigste Übung früh in die Einheit, wie das ACSM anmerkt.</p>

<h2>Wie gestaltest du die Progression im Trainingsplan?</h2>
<p>Schreib die Regel in den Plan, damit dein Kunde weiß, was den nächsten Schritt auslöst. Beispiel: Sobald jeder Satz 12 saubere Wiederholungen erreicht, steigt die Last, und die Wiederholungen gehen auf 8 zurück.</p>
<p>Du hast mehrere Hebel. Eine Studie mit Trainierten (Plotkin, 2022; 43 Teilnehmende zu Beginn, 38 am Ende) zeigt, dass mehr Wiederholungen oder mehr Last über 8 Wochen vergleichbare Anpassungen bringen, mit einem leichten Vorteil für die Last bei der Maximalkraft. Das hilft zu Hause, wenn die verfügbare Last ausgereizt ist. Die Studie ist kurz und betrifft nur Quadrizeps und Waden.</p>
<p>Ändere jeweils nur eine Variable, damit du weißt, was was bewirkt hat. Periodisierung hat die Ergebnisse laut ACSM nicht durchgängig verändert: Heb komplexe Pläne für fortgeschrittene Kunden auf und lies bei Bedarf <a href="/articles/periodisation-entrainement-bases.html">die Grundlagen der Periodisierung</a> nach.</p>

<h2>Wann passt du einen Trainingsplan an, und wo endet deine Rolle?</h2>
<p>Erfrag nach jeder Einheit die empfundene Anstrengung, etwaige Beschwerden und was ausgelassen wurde. Lässt dein Kunde zweimal hintereinander dieselbe Art von Einheit aus, änderst du den Plan, bevor du über Motivation sprichst.</p>
<p>Drei Grenzen stehen fest:</p>
<ul>
<li><strong>Gesundheit.</strong> Laut WHO sollte, wer beim Steigern der Aktivität neue Symptome bekommt, eine Gesundheitsfachkraft aufsuchen. Du pausierst, verweist weiter und deutest nichts.</li>
<li><strong>Ernährung.</strong> Allgemeine Empfehlungen kannst du geben. Je persönlicher die Beratung, desto höher das Risiko, vor allem bei einer Erkrankung: Krankheiten feststellen, heilen oder lindern darfst du als Nicht-Arzt in Deutschland nur mit einer Erlaubnis nach dem Heilpraktikergesetz. In Österreich dürfen Fitnesstrainer ohne entsprechende Ausbildung keine spezifische Ernährungsberatung geben und keine individuellen Ernährungspläne erstellen, sondern nur allgemeine Tipps geben.</li>
<li><strong>Der rechtliche Rahmen.</strong> In Deutschland brauchst du als Personal Trainer keine gesetzlich vorgeschriebene Ausbildung oder Lizenz. In Österreich meldest du für Trainingskonzepte meist das freie Gewerbe „Erstellung von Trainingskonzepten für gesundheitsbewusste Personen“ an, ohne Befähigungsnachweis. Es deckt allgemein gehaltene Konzepte ab; sportwissenschaftliche Beratung und Ernährungsberatung sind dort reglementierte Gewerbe. Kläre außerdem, ob deine Berufshaftpflicht abdeckt, was du anbietest, im Online-Coaching genauso wie bei Einheiten vor Ort.</li>
</ul>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Der Trainingsplan entsteht aus dem Eingangscheck: Ziel, tatsächliche Zeit, Niveau, Ausstattung, Grenzen.</li>
<li>Leg wenige Variablen fest, mit einer schriftlichen Progressionsregel und einer Aufteilung, die dein Kunde durchhält.</li>
<li>Neue Symptome, Ernährung und die Regeln deines Landes: Diese Grenzen gehen dem Trainingsplan vor.</li>
</ul>
""",
        "faq": [
            {"q": "Wie erstellst du einen individuellen Krafttrainingsplan für Kunden?", "a": "Geh vom Eingangscheck aus: Ziel, tatsächlich verfügbare Zeit, Niveau, Ausstattung und Grenzen. Leg dann Umfang und Intensität passend zum Ziel fest, wähl eine Aufteilung, die dein Kunde durchhält, schreib eine Progressionsregel auf und passe nach seinen Rückmeldungen an."},
            {"q": "Wie viele Trainingseinheiten pro Woche sollte ein Trainingsplan haben?", "a": "Die WHO empfiehlt Krafttraining für alle großen Muskelgruppen an 2 oder mehr Tagen pro Woche, das ACSM für die Kraft 2 oder mehr Einheiten. Für Einsteiger sind zwei Ganzkörpereinheiten ein guter Anfang. Die richtige Zahl ist die, die dein Kunde auch in einer vollen Woche durchhält."},
            {"q": "Darf ein Personal Trainer einen Ernährungsplan erstellen?", "a": "Allgemeine Empfehlungen kannst du geben, ohne dich als Ernährungsfachkraft auszugeben. Die Grenze zur individuellen Beratung ist unscharf: Je persönlicher die Beratung, desto höher das Risiko, vor allem bei einer Erkrankung, und dann verweist du an einen Arzt oder eine qualifizierte Ernährungsfachkraft. In Österreich darfst du ohne entsprechende Ausbildung keine individuellen Ernährungspläne erstellen."},
        ],
        "sources": [
            {"t": "Currier BS, D'Souza AC, Singh MAF, et al. American College of Sports Medicine Position Stand. Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults: An Overview of Reviews. <em>Med Sci Sports Exerc</em>. 2026.", "u": "https://doi.org/10.1249/MSS.0000000000003897"},
            {"t": "Schoenfeld BJ, Ogborn D, Krieger JW. Dose-response relationship between weekly resistance training volume and increases in muscle mass: A systematic review and meta-analysis. <em>J Sports Sci</em>. 2017.", "u": "https://doi.org/10.1080/02640414.2016.1210197"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Ramos-Campo DJ, Benito-Peinado PJ, Andreu-Caravaca L, et al. Efficacy of Split Versus Full-Body Resistance Training on Strength and Muscle Growth: A Systematic Review With Meta-Analysis. <em>J Strength Cond Res</em>. 2024.", "u": "https://doi.org/10.1519/JSC.0000000000004774"},
            {"t": "Plotkin D, Coleman M, Van Every D, et al. Progressive overload without progressing load? The effects of load or repetition progression on muscular adaptations. <em>PeerJ</em>. 2022.", "u": "https://doi.org/10.7717/peerj.14142"},
            {"t": "Bundesagentur für Arbeit. BERUFENET: Fitnesstrainer/in, Zugang zur Tätigkeit.", "u": "https://web.arbeitsagentur.de/berufenet/beruf/15658"},
            {"t": "Gesetz über die berufsmäßige Ausübung der Heilkunde ohne Bestallung (Heilpraktikergesetz), § 1.", "u": "https://www.gesetze-im-internet.de/heilprg/__1.html"},
            {"t": "WKO Oberösterreich. Infoblatt: Erstellung von Trainingskonzepten für gesundheitsbewusste Personen, Fitnesstrainer. 2026.", "u": "https://www.wko.at/ooe/tourismus-freizeitwirtschaft/freizeit-sportbetriebe/fitnesstrainer-erstellung-von-trainingskonzepten-fuer-ges-2.pdf"},
        ],
    },
    {
        "fr": "fideliser-clients-coaching-sportif",
        "slug": "kundenbindung-personal-trainer",
        "title": "Warum Kunden abspringen: Kundenbindung für Personal Trainer",
        "description": "Kundenbindung für Personal Trainer: warum Kunden abspringen, was Studien zu Abbrüchen zeigen und wie du deine Bindungsquote aus eigenen Zahlen berechnest.",
        "body": """
<p>Die kurze Antwort: Gute <strong>Kundenbindung für Personal Trainer</strong> beginnt damit, zu messen, wer geht und warum, denn das nimmt dir keine Statistik ab. Eine Abbruchquote speziell für selbstständige Trainer habe ich nicht gefunden. Die Forschung stützt vor allem drei einfache Hebel: ein schriftliches Ziel, festgehaltene Fortschritte und regelmäßige Rückmeldungen. Der Rest steckt in deiner eigenen Kundenliste.</p>

<h2>Wie viele Kunden hören wirklich auf?</h2>
<p>Die einzige belastbare Zahl, die ich behalten habe, stammt aus einem einzigen Fitnessstudio in Rio de Janeiro. Sperandei und Kollegen begleiteten 5.240 Mitglieder: 63 % hatten vor dem dritten Monat aufgehört, und weniger als 4 % kamen auf zwölf Monate durchgehender Aktivität. Die 2016 veröffentlichte Studie betrifft ein einziges Studio, stützt sich auf dessen Mitgliedsdaten und fand in einem Umfeld ohne Betreuung statt, wie ihr Titel sagt. Sie gilt also weder für alle Studios noch für Kunden, die mit einem Trainer arbeiten. Misstraue Abbruchquoten, die ohne Quelle kursieren.</p>
<p>Deine echte Zahl berechnest du in zehn Minuten. Nimm deine aktiven Kunden zu Beginn eines Quartals und zähl, wie viele am Ende noch da sind, ohne neue hinzuzurechnen. Beispielrechnung: 12 Kunden am 1. Januar, davon 9 am 31. März noch aktiv, also 9 ÷ 12 = 75 % Bindungsquote über drei Monate. Bei so wenigen Kunden zählt ein einziger Abgang mehr als 8 Prozentpunkte. Betrachte diese Quote übers ganze Jahr und schau vor allem auf die Gründe.</p>

<h2>Warum hören Kunden beim Personal Training auf?</h2>
<p>Keine der hier zitierten Studien beantwortet das für Kunden selbstständiger Trainer. Deine beste Quelle bleiben deine ehemaligen Kunden. Dieses Arbeitsraster ohne statistischen Wert hilft dir, jeden Abgang einzuordnen:</p>
<ul>
<li><strong>Geplanter Abschied:</strong> Das Ziel ist erreicht, oder dein Kunde kann jetzt allein trainieren. Das ist ein Erfolg und vielleicht eine künftige Empfehlung.</li>
<li><strong>Erzwungener Abschied:</strong> ein Umzug, das Budget, neue Arbeitszeiten, eine Geburt, die Gesundheit. Manchmal kannst du ein leichteres Format oder Online-Coaching anbieten.</li>
<li><strong>Vermeidbarer Abschied:</strong> unsichtbare Fortschritte, Einheiten, die sich alle gleich anfühlen, ein nie überprüftes Ziel, ein Termin, der nicht mehr passt, eine eingeschlafene Beziehung.</li>
</ul>
<p>Stell jedem Kunden, der geht, drei Fragen: Was hat deine Entscheidung ausgelöst, was hätte dich gehalten, was würdest du jemandem sagen, der überlegt anzufangen? Schreib die Antworten wörtlich auf. „Ich kann es mir nicht mehr leisten“ kann auch heißen: „Ich sehe nicht mehr, was es mir bringt.“ Taucht derselbe Grund mehrmals im Jahr auf, hast du deine oberste Priorität gefunden.</p>

<h2>Was hält Kunden langfristig?</h2>
<p>Die Arbeiten, die ich ausgewählt habe, betreffen kein selbstständiges Einzeltraining, aber sie geben eine Richtung vor.</p>
<ul>
<li><strong>Fortschritte festhalten.</strong> Die Metaanalyse von Harkin und Kollegen (2016, 138 Studien, 19.951 Personen) findet einen mittleren Effekt von 0,40 auf das Erreichen von Zielen, stärker, wenn das Ergebnis festgehalten oder geteilt wird. Sie beschränkt sich nicht auf Bewegung.</li>
<li><strong>Über die Selbstbeobachtung hinausgehen.</strong> In 122 Evaluationen mit 44.747 Personen zeigen Michie und Kollegen (2009), dass Interventionen, die sie mit einer weiteren Technik aus der Kontrolltheorie kombinieren, einen Effekt von 0,42 erreichen, gegenüber 0,26 bei den übrigen.</li>
<li><strong>Den Rahmen richtig setzen.</strong> Die Synthese von 55 Übersichtsarbeiten von Collado-Mateo (2021) nennt unter anderem Betreuung, Feedback, Fortschrittskontrolle, Ziele, soziale Unterstützung und Spaß. Sie betrifft Menschen mit chronischen Erkrankungen und ältere Erwachsene, nicht alle Kunden eines Trainers.</li>
</ul>
<p>In der Praxis: Dein Kunde hält fest, du reagierst, und ihr überprüft das Ziel gemeinsam. Ein <a href="/coachs/bilan-mensuel-client-coaching.html">einseitiger monatlicher Fortschrittsbericht</a> reicht, um diesen Rhythmus zu setzen.</p>

<h2>Wann solltest du eingreifen?</h2>
<p>Warte nicht, bis dein Kunde ankündigt, dass er aufhört. Vier Momente verlangen eine Reaktion:</p>
<ul>
<li><strong>Die ersten Wochen.</strong> Im Studio in Rio kam der Abbruch früh, und <a href="/articles/combien-de-temps-pour-prendre-une-habitude.html">eine Gewohnheit braucht Zeit</a>. Plane um die dritte Woche ein kurzes Gespräch: Was funktioniert, was nicht?</li>
<li><strong>Das Ende eines Pakets.</strong> Sprich zwei oder drei Einheiten vor der letzten über das Danach, mit dem Bericht in der Hand. <a href="/coachs/packs-abonnement-seance-coach-sportif.html">Das Angebot, das du machst</a>, spielt in diesem Moment ebenfalls eine Rolle.</li>
<li><strong>Ziel erreicht.</strong> Leg mit ihm das nächste fest oder bereite einen sauberen Abschluss vor, mit allem, was er braucht, um allein weiterzumachen.</li>
<li><strong>Wiederholtes Fehlen.</strong> Wende deine <a href="/coachs/seance-annulee-regles-coach.html">Absageregeln</a> an und frag dann, was sich in seiner Woche verändert hat.</li>
</ul>
<p>Verlass dich nicht darauf, dass der Vertrag jemanden hält. Per AGB darf ein Abo deine Kunden höchstens zwei Jahre binden; verlängert es sich automatisch, dann nur auf unbestimmte Zeit und mit einer Kündigungsfrist von höchstens einem Monat (§ 309 Nr. 9 BGB). Für Werbe-E-Mails an Privatpersonen brauchst du vorher ihre ausdrückliche Einwilligung. Ehemalige Kunden darfst du ohne Einwilligung nur zu ähnlichen eigenen Leistungen anschreiben, wenn du ihre Adresse beim Verkauf erhalten hast, sie nicht widersprochen haben und du schon bei der Erhebung und in jeder Mail klar darauf hinweist, dass sie jederzeit widersprechen können. Für Werbeanrufe gilt diese Ausnahme nicht.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Keine allgemeine Abbruchquote beschreibt dein Geschäft: Berechne deine Bindungsquote aus deinen eigenen Kunden und notiere jeden Grund für einen Abgang.</li>
<li>Schriftliches Ziel, festgehaltene Fortschritte, regelmäßige Rückmeldung: Diese Hebel sind am besten belegt, auch wenn die Studien keine selbstständigen Trainer betreffen.</li>
<li>Handle vor dem Abgang: in den ersten Wochen, am Ende eines Pakets, beim erreichten Ziel, bei wiederholtem Fehlen.</li>
</ul>
""",
        "faq": [
            {"q": "Wie halten Personal Trainer ihre Kunden langfristig?", "a": "Mit einem schriftlichen Ziel, festgehaltenen Fortschritten, regelmäßigen Zwischenbilanzen und einem Gespräch über das Danach, bevor das Paket endet. Frag außerdem jeden Kunden, der geht, was ihn gehalten hätte: Deine eigenen Abgangsgründe lehren dich mehr als eine allgemeine Statistik."},
            {"q": "Wie hoch ist die Abbruchquote im Fitnessstudio?", "a": "Eine verlässliche Gesamtzahl habe ich nicht gefunden. In einem Studio in Rio de Janeiro, an 5.240 Mitgliedern untersucht, hatten 63 % vor dem dritten Monat aufgehört. Das Ergebnis stammt aus einem einzigen Studio ohne Betreuung und gilt weder für alle Studios noch für Kunden mit Trainer."},
            {"q": "Wie berechnet man die Kundenbindungsquote?", "a": "Nimm deine aktiven Kunden zu Beginn eines Quartals und zähl, wie viele am Ende noch da sind, ohne neue hinzuzurechnen. 12 Kunden am 1. Januar und 9 noch aktive am 31. März ergeben zum Beispiel 9 ÷ 12 = 75 % über drei Monate. Bei wenigen Kunden betrachtest du die Quote übers ganze Jahr."},
        ],
        "sources": [
            {"t": "Sperandei S, Vieira MC, Reis AC. Adherence to physical activity in an unsupervised setting: Explanatory variables for high attrition rates among fitness center members. <em>J Sci Med Sport</em>. 2016.", "u": "https://doi.org/10.1016/j.jsams.2015.12.522"},
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Michie S, Abraham C, Whittington C, McAteer J, Gupta S. Effective techniques in healthy eating and physical activity interventions: a meta-regression. <em>Health Psychol</em>. 2009.", "u": "https://doi.org/10.1037/a0016136"},
            {"t": "Collado-Mateo D, Lavín-Pérez AM, Peñacoba C, et al. Key Factors Associated with Adherence to Physical Exercise in Patients with Chronic Diseases and Older Adults: An Umbrella Review. <em>Int J Environ Res Public Health</em>. 2021.", "u": "https://doi.org/10.3390/ijerph18042023"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 309 Klauselverbote ohne Wertungsmöglichkeit.", "u": "https://www.gesetze-im-internet.de/bgb/__309.html"},
            {"t": "Gesetz gegen den unlauteren Wettbewerb (UWG), § 7 Unzumutbare Belästigungen.", "u": "https://www.gesetze-im-internet.de/uwg_2004/__7.html"},
        ],
    },
    {
        "fr": "bilan-mensuel-client-coaching",
        "slug": "monatlicher-fortschrittsbericht-kunden",
        "title": "Fortschrittsbericht für Kunden: Was zeigst du jeden Monat?",
        "description": "Monatlicher Fortschrittsbericht für Kunden: welche Messwerte du zeigst, wie du sie vergleichst, wie das Gespräch läuft und wie du mit Gesundheitsdaten umgehst.",
        "body": """
<p>Die kurze Antwort: Ein <strong>monatlicher Fortschrittsbericht</strong> passt auf eine Seite und beantwortet vier Fragen: Wo steht das Ziel, was habt ihr gemacht, was hat sich verändert, und was änderst du im nächsten Monat? Zeig drei bis fünf Messwerte, immer im Vergleich mit dem Kunden selbst, und schließ mit einer schriftlichen Entscheidung. Der Monatsrhythmus ist eine praktische Wahl; die hier zitierten Studien geben ihn nicht vor.</p>

<h2>Warum lohnt sich eine monatliche Fortschrittskontrolle?</h2>
<p>Von einer Einheit zur nächsten sieht dein Kunde seine Fortschritte kaum. Der Bericht macht sie sichtbar. Die Metaanalyse von Harkin und Kollegen (2016, 138 Studien, 19.951 Personen) zeigt, dass das Verfolgen von Fortschritten hilft, Ziele zu erreichen, mit stärkerem Effekt, wenn das Ergebnis festgehalten oder geteilt wird. Sie beschränkt sich nicht auf Bewegung, aber ein Bericht erfüllt beide Bedingungen: Er ist schriftlich, und er wird mit dir geteilt.</p>
<p>Er hilft dir außerdem, eine Entscheidung zu treffen, statt denselben Plan einfach weiterlaufen zu lassen, und er gibt dir etwas an die Hand, um <a href="/coachs/fideliser-clients-coaching-sportif.html">Kunden langfristig zu halten</a>. Ein Monat liefert schon Material zu Anwesenheit und Lasten. Ein Feldtest kann zwei oder drei Monate warten.</p>

<h2>Was gehört in einen monatlichen Fortschrittsbericht?</h2>
<p>Wähle nach dem Ziel deines Kunden. Dieses Raster deckt die meisten Fälle ab:</p>
<div class="tablewrap"><table>
<caption>Quelle: Arbeitsraster für diesen Leitfaden, für jeden Kunden anzupassen.</caption>
<thead><tr><th>Messwert</th><th>Was du zeigst</th><th>Vorsicht</th></tr></thead>
<tbody>
<tr><td>Anwesenheit</td><td>Absolvierte von geplanten Einheiten</td><td>Unvermeidbare Ausfälle getrennt zählen</td></tr>
<tr><td>Belastung</td><td>Empfundene Anstrengung mal Dauer, Woche für Woche</td><td>Mit dem Kunden selbst vergleichen, nie mit anderen</td></tr>
<tr><td>Leistung</td><td>Zwei oder drei Referenzübungen: Last, Wiederholungen, Zeit</td><td>Dieselbe Übung und dieselben Anweisungen beibehalten</td></tr>
<tr><td>Feldtest</td><td>Nur ein Test, wenn er dem Ziel dient</td><td>Jedes Mal dieselben Bedingungen</td></tr>
<tr><td>Befinden</td><td>Energie, Schlaf, Spaß, bewertet von 1 bis 5</td><td>Lenkt das Gespräch und diagnostiziert nichts</td></tr>
<tr><td>Gewicht, Umfänge</td><td>Nur wenn es sein Ziel ist und er zustimmt</td><td>Nie der einzige Maßstab für Erfolg</td></tr>
</tbody>
</table></div>
<p>Für die Belastung bleibt die Session-RPE die einfachste Methode: eine Bewertung der Anstrengung mal Dauer. Foster und Kollegen haben sie 2001 mit einer herzfrequenzbasierten Methode verglichen und für unterschiedliche Belastungen als valide befunden. Die Auswahl der Tests behandelt unser Leitfaden zu <a href="/coachs/tests-physiques-nouveau-client.html">Fitnesstests für neue Kunden</a>.</p>

<h2>Wie vergleichst du Ergebnisse richtig?</h2>
<p>Der einzige nützliche Vergleich stellt deinen Kunden sich selbst gegenüber, unter gleichen Bedingungen: dieselbe Übung, dieselben Anweisungen, dieselbe Tageszeit, dasselbe Aufwärmen. Diese Sorgfalt ist wichtig. Für den 6-Minuten-Gehtest hält der europäisch-amerikanische Standard von 2014 fest, dass die Ergebnisse empfindlich auf kleine methodische Unterschiede reagieren, und empfiehlt zwei Durchgänge. Dieser Test wurde bei chronischen Atemwegserkrankungen validiert: Bei einem gesunden Kunden dient er nur dem Vergleich mit sich selbst.</p>
<p>Misstraue auch Tests, die zu viel versprechen. In der Studie von Sartor und Kollegen (2016, 81 gesunde Erwachsene) erklärt der Ruffier-Dickson-Index nur 15 % der Variabilität der kardiorespiratorischen Fitness. Nutze ihn als einfachen Anhaltspunkt und leite daraus keine VO2max ab. Bewerte jede Abweichung über mehrere Monate: Ein einzelner Rückgang kann von einer vollen Woche, einer Reise oder einer Erkältung kommen.</p>

<h2>Wie führst du das Monatsgespräch mit deinem Kunden?</h2>
<p>Fünfzehn bis zwanzig Minuten reichen, während einer Einheit oder per Videocall. Ein möglicher Ablauf:</p>
<ol>
<li>Frag zuerst, wie sich der Monat angefühlt hat, bevor du eine einzige Zahl zeigst.</li>
<li>Zeig, was sich verbessert hat, mit dem Ausgangswert daneben.</li>
<li>Stell, was stagniert hat, als Fakten dar: „6 von 8 Einheiten“, ohne Kommentar zur Willenskraft.</li>
<li>Such mit ihm nach der Ursache: Terminkalender, Schlaf, ein zu ehrgeiziger Plan, ein überholtes Ziel.</li>
<li>Entscheide mit ihm über eine bis drei Änderungen und schreib das Ziel für den nächsten Monat auf.</li>
</ol>
<p>Behandle einen schlechten Monat genauso. Schafft dein Kunde keine drei Einheiten pro Woche, passt du den Plan an seine echte Woche an. Versprich kein Ergebnis für den nächsten Monat. Erwähnt er ein neues Symptom, eine Krankheit oder eine Essstörung, deutest du nichts: Du verweist ihn an einen Arzt oder eine Ernährungsfachkraft.</p>

<h2>Datenschutz: Was machst du mit den Daten aus dem Bericht?</h2>
<p>Ein Bericht enthält oft sensible Daten, und Gesundheitsdaten stehen in der EU unter dem besonderen Schutz von Art. 9 DSGVO. Vorerkrankungen, Krankheiten und Behandlungen sind von Natur aus Gesundheitsdaten, und auch das Gewicht kann dazu zählen, besonders zusammen mit Schrittzahl oder Kalorien. Hol eine ausdrückliche Einwilligung ein, getrennt von deinen AGB, und bewahre diese Unterlagen an einem geschützten Ort auf. In Deutschland ergänzt das Bundesdatenschutzgesetz (BDSG) die DSGVO; zuständig für dich ist nicht der Bundesdatenschutzbeauftragte, sondern die Datenschutzaufsichtsbehörde deines Bundeslandes.</p>
<p>Der Bericht bleibt zwischen dir und deinem Kunden. Gib ihn an einen Arzt, eine Physiotherapeutin, einen anderen Trainer oder einen Angehörigen nur mit seiner Zustimmung weiter. Am einfachsten gibst du ihn deinem Kunden, und er teilt ihn, wenn er will. Fotos, auf denen er erkennbar ist, darfst du nur mit seiner Einwilligung veröffentlichen (§ 22 KUG), und eine bestimmte Form schreibt das Gesetz dafür nicht vor. Hol dir vor einem Vorher-nachher-Foto trotzdem eine schriftliche Erlaubnis, die Medium, Zweck und Dauer nennt. Dass er sich fotografieren lässt, reicht nicht.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Eine Seite, drei bis fünf Messwerte, eine schriftliche Entscheidung: Der Bericht soll im nächsten Monat etwas verändern.</li>
<li>Vergleiche deinen Kunden mit sich selbst, unter gleichen Bedingungen, und bewerte Abweichungen über mehrere Monate.</li>
<li>Die Daten im Bericht gehören deinem Kunden: ausdrückliche Einwilligung, ein geschützter Ort, keine Weitergabe ohne seine Zustimmung.</li>
</ul>
""",
        "faq": [
            {"q": "Was gehört in einen monatlichen Fortschrittsbericht im Personal Training?", "a": "Das Ausgangsziel, die Anwesenheit, zwei oder drei Leistungswerte, das Befinden und die für den nächsten Monat beschlossenen Änderungen. Eine Seite genügt. Vergleiche jede Zahl mit dem Kunden selbst, nie mit einem Durchschnitt oder einem anderen Kunden."},
            {"q": "Sollte man Kunden bei jeder Zwischenbilanz wiegen?", "a": "Nur wenn das Gewicht zu ihrem Ziel passt und sie zustimmen. Diese Zahl sollte nie der einzige Erfolgsmaßstab sein, und sie kann zu den Gesundheitsdaten zählen. Erwähnt ein Kunde eine Essstörung oder eine Krankheit, verweist du ihn an einen Arzt oder eine Ernährungsfachkraft."},
            {"q": "Darf ein Personal Trainer den Bericht eines Kunden an dessen Arzt oder Physiotherapeuten schicken?", "a": "Nur mit der Zustimmung des Kunden. Am einfachsten gibst du ihm den Bericht, damit er ihn selbst weiterreicht. Ohne diese Zustimmung schickst du ihn niemandem, auch keiner Gesundheitsfachkraft."},
        ],
        "sources": [
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Foster C, Florhaug JA, Franklin J, et al. A new approach to monitoring exercise training. <em>J Strength Cond Res</em>. 2001.", "u": "https://pubmed.ncbi.nlm.nih.gov/11708692/"},
            {"t": "Holland AE, Spruit MA, Troosters T, et al. An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease. <em>Eur Respir J</em>. 2014.", "u": "https://doi.org/10.1183/09031936.00150314"},
            {"t": "Sartor F, Bonato M, Papini G, et al. A 45-Second Self-Test for Cardiorespiratory Fitness: Heart Rate-Based Estimation in Healthy Individuals. <em>PLoS One</em>. 2016.", "u": "https://doi.org/10.1371/journal.pone.0168154"},
            {"t": "Verordnung (EU) 2016/679 des Europäischen Parlaments und des Rates vom 27. April 2016 zum Schutz natürlicher Personen bei der Verarbeitung personenbezogener Daten, zum freien Datenverkehr und zur Aufhebung der Richtlinie 95/46/EG (Datenschutz-Grundverordnung), Art. 4 und 9. EUR-Lex. 2016.", "u": "https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Bundesdatenschutzgesetz (BDSG), § 40 Aufsichtsbehörden der Länder.", "u": "https://www.gesetze-im-internet.de/bdsg_2018/__40.html"},
            {"t": "Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI). Seite mit den Anschriften der Datenschutzaufsichtsbehörden der Länder.", "u": "https://www.bfdi.bund.de/DE/Service/Anschriften/Laender/Laender-node.html"},
            {"t": "Gesetz betreffend das Urheberrecht an Werken der bildenden Künste und der Photographie (Kunsturhebergesetz, KUG), § 22.", "u": "https://www.gesetze-im-internet.de/kunsturhg/__22.html"},
        ],
    },
    {
        "fr": "lire-etat-de-forme-client",
        "slug": "tagesform-kunden-einschaetzen",
        "title": "Schlaf, Müdigkeit, Belastung: So schätzt du die Tagesform deiner Kunden ein",
        "seo_title": "Tagesform deiner Kunden einschätzen: So gehst du vor",
        "description": "Tagesform von Kunden einschätzen: was du vor dem Training fragst, was eine kurze Nacht ändert, wie du die Belastung misst und was Smartwatch und HRV zeigen.",
        "body": """
<p>Die kurze Antwort: Um die <strong>Tagesform deiner Kunden</strong> einzuschätzen, stellst du vor dem Aufwärmen drei Fragen, vergleichst die Antworten mit dem, was für diesen Kunden normal ist, und passt die Einheit an, wenn mehrere Signale in dieselbe Richtung zeigen. Kein einzelner Marker reicht: weder der Schlaf noch die Herzfrequenzvariabilität noch der Score einer Smartwatch. Diese Messwerte helfen dir, eine Belastung zu dosieren. Eine Diagnose stellen sie nicht.</p>

<h2>Was solltest du Kunden vor dem Training fragen?</h2>
<p>Zwei Minuten reichen. Bleib bei denselben Fragen und derselben Skala von 1 bis 5:</p>
<ul>
<li>Wie hast du im Vergleich zu sonst geschlafen?</li>
<li>Wie viel Energie hast du heute, Stress eingeschlossen?</li>
<li>Hast du neue Schmerzen oder Beschwerden?</li>
</ul>
<p>Die Übersichtsarbeit von Saw und Kollegen (2016, 56 Studien) zeigt, dass subjektive und objektive Messwerte schlecht übereinstimmen und dass die subjektiven die Trainingsbelastung besser abbilden. Sie betrifft Sportler, also wende sie mit Vorsicht an. Notiere jede Antwort, denn nur die Abweichung vom Normalwert deines Kunden sagt etwas aus. Eine 2 von einem Kunden, der immer 4 antwortet, zählt mehr als eine 2 von einem, der oft 2 antwortet.</p>

<h2>Training nach einer schlechten Nacht: Solltest du die Einheit ändern?</h2>
<p>Nicht unbedingt. Die Metaanalyse von Craven und Kollegen (2022, 69 Veröffentlichungen, 959 Teilnehmende, davon 89 % Männer) findet nach 6 Stunden Schlaf oder weniger eine im Schnitt um 7,56 % geringere Leistung, bei sehr hoher Heterogenität zwischen den Studien. Zwei Nuancen helfen in der Praxis:</p>
<ul>
<li><strong>Die Art der Nacht.</strong> Die Effekte waren nur nach einer durchwachten Nacht oder frühem Aufstehen konsistent, nicht nach spätem Zubettgehen. Der Rückgang erreichte dann etwa 0,4 % pro Stunde Wachsein vor der Belastung.</li>
<li><strong>Die Uhrzeit der Einheit.</strong> Belastungen am Nachmittag und Abend waren betroffen, morgendliche kaum.</li>
</ul>
<p>Ein Kunde, der um 5 Uhr aufgestanden ist und um 19 Uhr kommt, ist in einer anderen Lage als einer, der spät ins Bett ging und um 8 Uhr kommt. Seine Einheit sagen diese Durchschnittswerte trotzdem nicht voraus: Schau, wie er auf das Aufwärmen reagiert, bevor du etwas änderst.</p>

<h2>Wie misst du die Trainingsbelastung ohne Geräte?</h2>
<p>Lass deinen Kunden seine Anstrengung nach der Einheit von 0 bis 10 bewerten und multipliziere diese Zahl mit der Dauer: Das ist die Session-RPE. Beispielrechnung: 60 Minuten, bewertet mit 7, ergeben einen Wert von 420. Foster und Kollegen haben sie 2001 mit einer herzfrequenzbasierten Methode verglichen und für unterschiedliche Belastungen als valide befunden. Zähl die Einheiten zusammen, auch das Training ohne dich, und vergleiche dann die Wochen miteinander.</p>
<p>Dieser Wert beschreibt, was dein Kunde empfunden hat. Deine Lasten, Sätze und Strecken beschreiben, was er gemacht hat. Steigt bei gleicher Arbeit die empfundene Anstrengung über mehrere Einheiten, verdient das eine Nachfrage. Das Verhältnis von akuter zu chronischer Belastung (ACWR) lässt du für die Verletzungsvorbeugung dagegen beiseite: Impellizzeri und Kollegen kamen 2020 zu dem Schluss, dass keine Evidenz diese Anwendung stützt.</p>

<h2>Wie zuverlässig sind Smartwatches und HRV?</h2>
<p>Lies sie als Trends, mit bekannten Grenzen.</p>
<ul>
<li><strong>Schlaf.</strong> Bei Chinoy und Kollegen (2021) erkannten sieben damalige Verbrauchergeräte, getragen oder neben dem Bett platziert und bei 34 gesunden jungen Erwachsenen mit der Polysomnografie verglichen, den Schlaf gut (Sensitivität von mindestens 0,93) und das Wachsein schlechter (Spezifität von 0,18 bis 0,54). Die Schlafphasen waren uneinheitlich, und gestörte Nächte wurden schlechter erfasst. Ignoriere die „Tiefschlaf“-Zahl einer einzelnen Nacht.</li>
<li><strong>Herzfrequenzvariabilität.</strong> Laut der Metaanalyse von Bellenger und Kollegen (2016, 27 Studien) steigt sie in Ruhe bei positiver Anpassung und verändert sich bei Overreaching kaum. Ein niedriger Wert beweist kein Übertraining, und ein normaler Wert schließt es nicht aus. Diese Studien betreffen Ausdauersportler, weit weg vom durchschnittlichen Kunden.</li>
<li><strong>Messung.</strong> Die <a href="/methode/variabilite-cardiaque.html">Herzfrequenzvariabilität</a> hängt vom Sensor ab, davon, wie die Uhr sitzt, von Herzrhythmusstörungen oder einem Medikament, das den Herzschlag verlangsamt. Von einem Gerät zum anderen kannst du sie nicht vergleichen.</li>
<li><strong>Bezugspunkt.</strong> Aussagekraft hat nur die eigene <a href="/methode/ligne-de-base.html">Baseline</a> deines Kunden, über mehrere Wochen aufgebaut. Sie zeigt, ob er von seinen Gewohnheiten abweicht, ohne zu sagen, ob diese Gewohnheiten gut sind, und eine langsame Drift kann ihr entgehen.</li>
<li><strong>Erholungsscores.</strong> Sie fassen diese Signale zusammen, mitsamt ihren Grenzen. Ein niedriger Score verbietet nichts, und ein hoher Score erlaubt nichts.</li>
</ul>
<p>Diese Daten gehören deinem Kunden. Er zeigt sie dir, wenn er will, mit seiner ausdrücklichen Einwilligung, und du gibst sie ohne ihn an niemanden weiter. Mach die Einheit nie davon abhängig, dass er sie teilt. Gesundheitsdaten stehen in der EU unter dem besonderen Schutz von Art. 9 DSGVO. In Deutschland ergänzt das Bundesdatenschutzgesetz (BDSG) die DSGVO; zuständig für dich ist nicht der Bundesdatenschutzbeauftragte, sondern die Datenschutzaufsichtsbehörde deines Bundeslandes.</p>

<h2>Wann passt du die Einheit an, und wann verweist du an einen Arzt?</h2>
<p>Achte auf Übereinstimmung: Du beobachtest ein einzelnes Signal und handelst erst bei mehreren.</p>
<div class="tablewrap"><table>
<caption>Quelle: vorsichtige Richtwerte aus diesem Leitfaden, ohne diagnostischen Wert.</caption>
<thead><tr><th>Was du beobachtest</th><th>Mögliche Entscheidung</th></tr></thead>
<tbody>
<tr><td>Kurze Nacht, ordentliche Energie, gutes Aufwärmen</td><td>Einheit wie geplant</td></tr>
<tr><td>Kurze Nacht und wenig Energie, Einheit am Nachmittag oder Abend</td><td>Weniger Umfang, keine Maximallast</td></tr>
<tr><td>Empfundene Anstrengung steigt über mehrere Einheiten</td><td>Leichtere Woche, mit dem Kunden nach der Ursache suchen</td></tr>
<tr><td>Schmerz, der die Bewegung verändert</td><td>Übung streichen, ärztlicher Rat, wenn er anhält</td></tr>
<tr><td>Ungewöhnliche Müdigkeit, die trotz geringerer Belastung anhält</td><td>An einen Arzt verweisen</td></tr>
<tr><td>Schwindel, Brustschmerz, ungewöhnliche Atemnot, Herzstolpern oder Herzrasen</td><td>Sofort abbrechen, ärztlich abklären lassen und im Notfall die 112 wählen</td></tr>
</tbody>
</table></div>
<p>Du musst nicht benennen, was los ist. „Übertraining“ und „Mangel“ sind medizinische Schlussfolgerungen. Beschreib, was du beobachtest, schlag einen Arztbesuch vor und übertrag die Trends in deinen <a href="/coachs/bilan-mensuel-client-coaching.html">monatlichen Fortschrittsbericht</a>.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Drei bewertete Fragen pro Einheit liefern dir schon das Wesentliche: die Abweichung vom Normalwert deines Kunden.</li>
<li>Schlaf, Belastung, Smartwatch und Herzfrequenzvariabilität liest du zusammen und als Trends. Keiner dieser Werte reicht allein.</li>
<li>Du passt die Einheit an und stellst keine Diagnose: Ein neues Symptom oder anhaltende Müdigkeit gehören zum Arzt.</li>
</ul>
""",
        "faq": [
            {"q": "Woran erkennst du, ob ein Kunde zu müde zum Trainieren ist?", "a": "Frag, wie er geschlafen hat, wie viel Energie er hat und ob er neue Schmerzen hat, und schau, wie er auf das Aufwärmen reagiert. Sinken mehrere Signale, machst du die Einheit leichter. Hält die Müdigkeit an oder kommen Symptome dazu, verweist du ihn an einen Arzt."},
            {"q": "Sollte man nach einer schlechten Nacht das Training absagen?", "a": "Nicht unbedingt. Eine kurze Nacht senkt die Leistung im Schnitt, vor allem nachmittags oder abends und nach frühem Aufstehen, aber die Reaktion ist von Mensch zu Mensch verschieden. Behalte die Einheit bei, wenn dein Kunde gut auf das Aufwärmen reagiert, und reduziere sonst Umfang oder Intensität."},
            {"q": "Bedeutet eine niedrige HRV Übertraining?", "a": "Nein. Die Ergebnisse sind widersprüchlich, und laut einer Metaanalyse von 2016 an Ausdauersportlern verändert sich die Ruhe-HRV bei Overreaching kaum. Ein einzelner Rückgang kann von einer schlechten Nacht oder einer weniger sauberen Messung kommen: Lies den Trend, zusammen mit dem Befinden deines Kunden."},
        ],
        "sources": [
            {"t": "Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures: a systematic review. <em>Br J Sports Med</em>. 2016.", "u": "https://doi.org/10.1136/bjsports-2015-094758"},
            {"t": "Craven J, McCartney D, Desbrow B, et al. Effects of Acute Sleep Loss on Physical Performance: A Systematic and Meta-Analytical Review. <em>Sports Med</em>. 2022.", "u": "https://doi.org/10.1007/s40279-022-01706-y"},
            {"t": "Foster C, Florhaug JA, Franklin J, et al. A new approach to monitoring exercise training. <em>J Strength Cond Res</em>. 2001.", "u": "https://pubmed.ncbi.nlm.nih.gov/11708692/"},
            {"t": "Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:Chronic Workload Ratio: Conceptual Issues and Fundamental Pitfalls. <em>Int J Sports Physiol Perform</em>. 2020.", "u": "https://doi.org/10.1123/ijspp.2019-0864"},
            {"t": "Chinoy ED, Cuellar JA, Huwa KE, et al. Performance of seven consumer sleep-tracking devices compared with polysomnography. <em>Sleep</em>. 2021.", "u": "https://doi.org/10.1093/sleep/zsaa291"},
            {"t": "Bellenger CR, Fuller JT, Thomson RL, et al. Monitoring Athletic Training Status Through Autonomic Heart Rate Regulation: A Systematic Review and Meta-Analysis. <em>Sports Med</em>. 2016.", "u": "https://doi.org/10.1007/s40279-016-0484-2"},
            {"t": "Verordnung (EU) 2016/679 des Europäischen Parlaments und des Rates vom 27. April 2016 zum Schutz natürlicher Personen bei der Verarbeitung personenbezogener Daten, zum freien Datenverkehr und zur Aufhebung der Richtlinie 95/46/EG (Datenschutz-Grundverordnung), Art. 9. EUR-Lex. 2016.", "u": "https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Bundesdatenschutzgesetz (BDSG), § 40 Aufsichtsbehörden der Länder.", "u": "https://www.gesetze-im-internet.de/bdsg_2018/__40.html"},
        ],
    },
]
