# -*- coding: utf-8 -*-
# Adaptation allemande du lot 3 des guides coachs (Allemagne ; Autriche et Suisse seulement là
# où la fiche donne une différence vérifiée). Base : tools/en/coachs/batch_3.py.
# Faits : tools/intl/_faits-ue.md et tools/intl/_faits-de.md. La Commission française des clauses
# abusives et le Code de la consommation sont remplacés par le BGB (§§ 307, 309, 312k, 355 à 357a)
# et la directive 93/13/CEE. Les montants d'exemple restent ceux de l'anglais (25,8 % = taux inventé).

ENTRIES = [
    {
        "fr": "coaching-sportif-en-ligne-comment-faire",
        "slug": "online-coaching-starten-personal-trainer",
        "title": "Als Personal Trainer mit Online-Coaching starten",
        "description": "Online-Coaching starten: welches Format passt, was du vor dem ersten Kunden regelst (Widerruf, Kündigungsbutton, Gesundheitsdaten) und wie du Kunden findest.",
        "body": """
<p>Die kurze Antwort: Wenn du <strong>Online-Coaching starten</strong> willst, brauchst du dieselben Grundlagen wie im Studio: eine Ausbildung, die zu deinem Angebot passt, auch wenn das Gesetz in Deutschland keine vorschreibt, und eine Versicherung, die abdeckt, was du anbietest. Dann wählst du ein Format und bereitest vor dem ersten Kunden deine AGB, den Ablauf bei Widerruf und Kündigung und deine Tools vor.</p>

<h2>Brauchst du für Online-Coaching eine Qualifikation?</h2>
<p>Online zu arbeiten stellt dich nicht außerhalb der Regeln. In Deutschland brauchst du als Personal Trainer keine gesetzlich vorgeschriebene Ausbildung oder Lizenz, online wie vor Ort. Ob du ein Gewerbe anmeldest oder als Freiberufler mit unterrichtender Tätigkeit giltst, hängt davon ab, was du konkret anbietest. Geh nie davon aus, dass eine Pflicht, die du im Studio hättest, im Videocall verschwindet.</p>
<p>Ein Programm, das du ohne Betreuung verkaufst, ist die Grauzone. Die Regeln sagen nicht immer, wo in diesem Fall das Coaching beginnt. Sicherheitshalber gehen wir von dieser Grundlage aus: Je individueller deine Betreuung, desto mehr gleicht sie einem Training unter Anleitung, und desto eher dürften die Regeln für das Coaching gelten.</p>

<h2>Welches Format passt zu deinem Online-Coaching?</h2>
<p>Vier Formate gibt es nebeneinander, und sie verlangen dir unterschiedlich viel Zeit und Organisation ab.</p>
<div class="tablewrap"><table>
<caption>Quelle: Einteilung für diesen Leitfaden, ohne rechtlichen Wert.</caption>
<thead><tr><th>Format</th><th>Was dein Kunde bekommt</th><th>Was es dich kostet</th></tr></thead>
<tbody>
<tr><td>Live-Einheit</td><td>Eine Einheit per Video, in Echtzeit korrigiert</td><td>Einen festen Termin und einen guten Bildausschnitt</td></tr>
<tr><td>Online-Betreuung</td><td>Einen angepassten Trainingsplan und regelmäßige Rückmeldungen</td><td>Jede Woche Zeit, die du begrenzen musst</td></tr>
<tr><td>Hybrid</td><td>Online-Betreuung plus einige Einheiten vor Ort</td><td>Kunden, die in deiner Nähe wohnen</td></tr>
<tr><td>Programm ohne Betreuung</td><td>Denselben Plan für alle, als Datei oder in einer App</td><td>Ein Publikum, dem du verkaufst, und eigene Verkaufsregeln</td></tr>
</tbody>
</table></div>
<p>Mit wenigen Kunden startest du am besten mit einem Format, in dem du mit ihnen sprichst, etwa einer <a href="/coachs/coaching-en-visio.html">Live-Einheit per Videocall</a> oder der Online-Betreuung. Leg vom ersten Tag an eine Höchstzahl an Kunden und eine Antwortzeit fest. Für den Preis habe ich keine offizielle Tabelle gefunden; unser Leitfaden zu den <a href="/coachs/tarif-coaching-en-ligne.html">Preisen für Online-Coaching</a> zeigt eine Rechenmethode.</p>

<h2>Was musst du vor dem ersten Online-Kunden regeln?</h2>
<ol>
<li><strong>Deine Absicherung.</strong> Prüf, ob deine Ausbildung abdeckt, was du anbietest. Frag deine Versicherung, ob deine Berufshaftpflicht auch die Arbeit aus der Ferne einschließt. Verkaufst du ein Programm an mehrere Kunden, frag deinen Steuerberater oder dein Finanzamt, wie diese Einnahmen behandelt werden.</li>
<li><strong>Deine AGB.</strong> Gib sie deinem Kunden, bevor er unterschreibt, und veröffentliche sie auf deiner Website.</li>
<li><strong>Widerruf und Kündigung.</strong> Schreib auf, wie dein Kunde widerruft oder kündigt, wie du erstattest und was er für bereits Geleistetes zahlt. Schließt du online mit Privatkunden einen Vertrag, können sie ihn 14 Tage lang widerrufen. Startest du auf ihren ausdrücklichen Wunsch früher, schulden sie bei einem Widerruf Wertersatz für das bereits Geleistete: Halte diesen Wunsch schriftlich fest, zusammen mit der Bestätigung, dass dein Kunde sein Widerrufsrecht verliert, sobald du die Leistung vollständig erbracht hast. Seit dem 19. Juni 2026 brauchst du bei online geschlossenen Verträgen zusätzlich eine gut sichtbare Widerrufsfunktion „Vertrag widerrufen“, die während der ganzen Widerrufsfrist erreichbar ist (§ 356a BGB). Sie dient dem Widerruf und ist kein Kündigungsbutton: Verkaufst du Abos über deine Website, brauchst du außerdem einen Button „Verträge hier kündigen“ (§ 312k BGB), und auf der Bestätigungsseite dürfen laut BGH keine weiteren Angebote stehen, auch keine kostenlose Pause.</li>
<li><strong>Gesundheitsdaten.</strong> Verletzungen, Vorerkrankungen und Gesundheitsfragebögen sind Gesundheitsdaten, und in der EU ist ihre Verarbeitung grundsätzlich untersagt, außer in bestimmten Ausnahmefällen (Art. 9 DSGVO). Der erste ist die ausdrückliche Einwilligung deines Kunden für festgelegte Zwecke: Hol sie getrennt von deinen AGB ein und bewahre diese Daten in einem sicheren Tool auf. Ein WhatsApp-Verlauf oder eine ungeschützte Datei passt schlecht dazu.</li>
<li><strong>Deine Tools.</strong> Du brauchst einen Ort für die Trainingspläne, einen Kanal für Nachrichten und eine Zahlungsmöglichkeit. Wähl, was zu den Punkten oben passt, ohne unnötig viele Abos abzuschließen.</li>
</ol>

<h2>Wie findest du die ersten Kunden fürs Online-Coaching?</h2>
<p>Eine verlässliche Zahl dazu, was am besten funktioniert, habe ich nicht, und misstraue jedem, der dir eine verspricht. Ein paar Grundsätze gelten trotzdem.</p>
<ul>
<li><strong>Fang bei Menschen an, die dich kennen.</strong> Ehemaligen Kunden, deren Adresse du beim Verkauf erhalten hast, darfst du per E-Mail zu ähnlichen eigenen Leistungen schreiben, wenn sie nicht widersprochen haben und du sie schon bei der Erhebung und in jeder Mail darauf hinweist, dass sie jederzeit widersprechen können. Wer noch nie mit dir gearbeitet hat, muss vorher ausdrücklich einwilligen, bevor du ihm Werbung per E-Mail schickst oder ihn anrufst. Für Werbeanrufe gilt die Ausnahme für Bestandskunden nicht.</li>
<li><strong>Prüf, ob du ein Google-Profil haben darfst.</strong> Nach den Google-Richtlinien hat ein Unternehmen, das nur online arbeitet, keinen Anspruch auf ein Unternehmensprofil. Triffst du Kunden auch vor Ort, kommst du vielleicht infrage.</li>
<li><strong>Zeig, wie du anleitest.</strong> Erklär eine Bewegung, korrigier einen typischen Fehler, beschreib deine Betreuung. Ein Online-Kunde will wissen, wie du ihn führst, ohne neben ihm zu stehen.</li>
<li><strong>Schaff Vertrauen, ohne etwas zu versprechen.</strong> Zeig, was sich prüfen lässt, etwa deine Ausbildung. Ein Ergebnis anzukündigen, das du weder liefern noch belegen kannst, kann als irreführende Geschäftspraxis gelten.</li>
</ul>
<p>Dieser Leitfaden dient nur der Information und ersetzt keine Beratung durch einen Anwalt oder einen Steuerberater.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Online zu arbeiten stellt dich nicht außerhalb der Regeln: In Deutschland ist keine Ausbildung vorgeschrieben, aber ob du gewerblich oder freiberuflich tätig bist, hängt von deinem Angebot ab.</li>
<li>Ein Programm ohne Betreuung ist eine Grauzone: Je individueller du arbeitest, desto mehr gleicht es einem Training unter Anleitung.</li>
<li>Bereite vor dem ersten Kunden deine AGB, Widerruf und Kündigung (Widerrufsfunktion, Kündigungsbutton) und die Einwilligung für Gesundheitsdaten vor.</li>
</ul>
""",
        "faq": [
            {"q": "Wie wird man Online-Fitnesscoach?", "a": "In Deutschland schreibt das Gesetz keine Ausbildung vor, eine fundierte Qualifikation bleibt trotzdem deine Grundlage. Prüf, ob deine Versicherung die Arbeit aus der Ferne abdeckt, und kläre, ob du gewerblich oder freiberuflich tätig bist. Wähl dann ein Format und bereite AGB, Widerruf, Kündigung und die Einwilligung für Gesundheitsdaten vor."},
            {"q": "Mit welchem Online-Coaching-Format sollte man anfangen?", "a": "Mit wenigen Kunden wählst du ein Format, in dem du mit ihnen sprichst, etwa Live-Einheiten per Videocall oder Online-Betreuung. Leg von Anfang an eine Höchstzahl an Kunden und eine Antwortzeit fest. Ein Programm ohne Betreuung braucht ein Publikum, dem du es verkaufen kannst."},
            {"q": "Kann ein reiner Online-Coach ein Google-Unternehmensprofil haben?", "a": "Nein, nicht nach den Google-Richtlinien: Ein Unternehmen, das nur online arbeitet, hat keinen Anspruch darauf. Triffst du Kunden auch vor Ort, kommst du vielleicht infrage."},
        ],
        "sources": [
            {"t": "Google. Hilfeseite zum Unternehmensprofil über die Berechtigung von Unternehmen und ihre Inhaberschaft. 2026.", "u": "https://support.google.com/business/answer/13763036?hl=de"},
            {"t": "Bundesagentur für Arbeit. BERUFENET: Fitnesstrainer/in, Zugang zur Tätigkeit.", "u": "https://web.arbeitsagentur.de/berufenet/beruf/15658"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 357a (Wertersatz nach Widerruf von Fernabsatzverträgen und Verträgen außerhalb von Geschäftsräumen).", "u": "https://www.gesetze-im-internet.de/bgb/__357a.html"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 356a (Widerrufsfunktion bei online geschlossenen Verträgen, seit 19. Juni 2026).", "u": "https://www.gesetze-im-internet.de/bgb/__356a.html"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 312k: Kündigung von Verbraucherverträgen im elektronischen Geschäftsverkehr.", "u": "https://www.gesetze-im-internet.de/bgb/__312k.html"},
            {"t": "Bundesgerichtshof, Urteil vom 16. Juli 2026, I ZR 200/25 (Kündigungsbutton eines Fitnessstudios).", "u": "https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/I_ZS/2025/I_ZR_200-25.pdf?__blob=publicationFile"},
            {"t": "Verordnung (EU) 2016/679 des Europäischen Parlaments und des Rates vom 27. April 2016 zum Schutz natürlicher Personen bei der Verarbeitung personenbezogener Daten, zum freien Datenverkehr und zur Aufhebung der Richtlinie 95/46/EG (Datenschutz-Grundverordnung), Art. 7 und 9. EUR-Lex. 2016.", "u": "https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Gesetz gegen den unlauteren Wettbewerb (UWG), § 7 Unzumutbare Belästigungen.", "u": "https://www.gesetze-im-internet.de/uwg_2004/__7.html"},
        ],
    },
    {
        "fr": "coaching-en-visio",
        "slug": "personal-training-per-videocall",
        "title": "Personal Training per Videocall: Ausstattung und Ablauf",
        "description": "Personal Training per Videocall: welche Ausstattung du brauchst, wie du deinen Kunden ins Bild setzt, ein Ablauf für 45 Minuten, Sicherheit und klare Regeln.",
        "body": """
<p>Die kurze Antwort: Für <strong>Personal Training per Videocall</strong> brauchst du wenig Ausstattung: ein stabiles Gerät, klaren Ton, Licht von vorn und eine getestete Verbindung. Die Qualität der Einheit hängt am Bildausschnitt, an deiner Stimme und an einem Notfallplan, den du vorher vorbereitest.</p>

<h2>Welche Ausstattung brauchst du für Training per Video?</h2>
<ul>
<li><strong>Eine stabile Halterung.</strong> Stell Handy oder Laptop so weit weg, dass dein Kunde dich von Kopf bis Fuß sieht, wenn du eine Bewegung vormachst.</li>
<li><strong>Klarer Ton.</strong> Du bewegst dich und entfernst dich vom Gerät: Kabellose Kopfhörer oder ein Ansteckmikrofon sind besser als das eingebaute Mikrofon.</li>
<li><strong>Licht von vorn.</strong> Ein Fenster im Rücken macht dich zur Silhouette. Bitte deinen Kunden um dasselbe, sonst siehst du seine Gelenke nicht.</li>
<li><strong>Eine getestete Verbindung.</strong> Probier deinen Aufbau vor der Einheit aus und halte den Hotspot deines Handys als Reserve bereit.</li>
</ul>
<p>Auf der Seite deines Kunden reichen ein Gerät, das auf dem Boden oder einem Stuhl steht, eine Matte und genug Platz, um sich hinzulegen und die Arme auszustrecken. Mach in der ersten Einheit einen Bildtest. Für eine Kniebeuge bittest du um eine Ansicht von vorn, um die Knie zu sehen, dann um eine Ansicht von der Seite für Rücken und Tiefe.</p>
<p>Bei der Software liest du die Nutzungsbedingungen, prüfst, ob die Anrufe verschlüsselt sind, und meidest Apps, die deine Daten weiterverwenden. Das zählt umso mehr, weil Kunden in diesen Calls manchmal über ihre Gesundheit sprechen.</p>

<h2>Wie läuft eine Trainingseinheit per Videocall ab?</h2>
<div class="tablewrap"><table>
<caption>Quelle: Beispielablauf für diesen Leitfaden, an deinen Kunden anzupassen.</caption>
<thead><tr><th>Zeit</th><th>Phase</th><th>Was du tust</th></tr></thead>
<tbody>
<tr><td>0 bis 5 Min.</td><td>Begrüßung</td><td>Du prüfst Ton, Bildausschnitt und Platz. Du fragst nach Schlaf, Müdigkeit und Schmerzen am heutigen Tag.</td></tr>
<tr><td>5 bis 12 Min.</td><td>Aufwärmen</td><td>Du beobachtest die Beweglichkeit und passt deine Ansagen an.</td></tr>
<tr><td>12 bis 35 Min.</td><td>Hauptteil</td><td>Zwei oder drei Übungen, mit jeweils einer Korrektur.</td></tr>
<tr><td>35 bis 42 Min.</td><td>Cool-down</td><td>Du fährst die Belastung herunter und fragst, wie es sich angefühlt hat.</td></tr>
<tr><td>42 bis 45 Min.</td><td>Abschluss</td><td>Du legst den nächsten Termin fest und notierst, was sich verändert hat.</td></tr>
</tbody>
</table></div>
<p>Aus der Ferne ersetzt deine Stimme deine Hände. Drei Gewohnheiten helfen.</p>
<ul>
<li><strong>Mehr reden.</strong> Dein Kunde schaut auf seine Matte, nicht auf deinen Bildschirm. Kündige jeden Wechsel laut an und zähl die Wiederholungen mit.</li>
<li><strong>Einen Punkt korrigieren.</strong> Gib einen einzigen Hinweis und lass dann eine Wiederholung machen, um ihn zu prüfen.</li>
<li><strong>Bei sicheren Übungen bleiben.</strong> Du kannst weder sichern noch helfen, also bleib bei Übungen, die dein Kunde allein sicher ausführen kann.</li>
</ul>
<p>Steuere die Intensität nach Gefühl. Lass dir bei jedem Block die empfundene Anstrengung nennen, mit einer <a href="/articles/rpe-echelle-effort-percu.html">RPE-Skala</a>, und pass den nächsten Block an.</p>

<h2>Wie sorgst du im Videocall für die Sicherheit deines Kunden?</h2>
<p>Die verfügbaren Daten beruhigen, mit Einschränkungen. Eine Metaanalyse von 2025 (22 Studien, 2.082 Teilnehmende) fand keinen klaren Unterschied bei unerwünschten Ereignissen zwischen Training per Video und vor Ort, bei niedriger Vertrauenswürdigkeit der Evidenz. Eine weitere, ebenfalls von 2025 (28 Studien, 2.086 Personen über 65), kam zu dem Schluss, dass Training per Video sicher erscheint und wirksamer ist als keine Intervention. Diese Studien betreffen vor allem Rehabilitation oder ältere Erwachsene, unter Forschungsbedingungen. Für deine Einheit garantieren sie nichts. Bereite deinen Plan also vor dem Start vor:</p>
<ul>
<li><strong>Die Adresse.</strong> Notiere die genaue Adresse, an der die Einheit stattfindet, und lass sie bestätigen, wenn dein Kunde unterwegs ist. Den Notruf wählst du von deinem Telefon aus: Jede Standortangabe, die dort ankommt, ist deine, nicht die deines Kunden.</li>
<li><strong>Ein Kontakt.</strong> Lass dir mit seinem Einverständnis die Nummer einer nahestehenden Person geben und frag, ob dein Kunde allein ist.</li>
<li><strong>Verbindungsabbrüche.</strong> Leg die Regel vorher fest: Friert das Bild ein, unterbricht dein Kunde die Übung, und du rufst ihn per Telefon an.</li>
<li><strong>Gesundheit.</strong> Biete vor dem Start einen <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">Gesundheitsfragebogen</a> an. Beantwortet dein Kunde eine Frage mit Ja, deutest du das nicht: Du verweist ihn an einen Arzt.</li>
<li><strong>Notfall.</strong> Fühlt sich dein Kunde einer Ohnmacht nahe oder bricht er zusammen, wählst du sofort die 112, sagst, dass die Person an einer anderen Adresse ist, nennst sie und bleibst in der Leitung. Für Beschwerden, die nicht lebensbedrohlich sind, ist in Deutschland der ärztliche Bereitschaftsdienst unter 116 117 da. Arbeitest du von Österreich oder der Schweiz aus, erreichst du den Rettungsdienst dort auch unter 144. Jedes neue Symptom während der Belastung beendet die Einheit und schickt deinen Kunden zu einer Gesundheitsfachkraft.</li>
</ul>

<h2>Welche Regeln gelten für eine Einheit per Videocall?</h2>
<p>Behandle sie wie eine Einheit vor Ort. In Deutschland brauchst du als Personal Trainer keine gesetzlich vorgeschriebene Ausbildung oder Lizenz; Krankheiten feststellen, heilen oder lindern darfst du als Nicht-Arzt aber nur mit einer Erlaubnis nach dem Heilpraktikergesetz, im Videocall genauso wie im Studio. Unser Leitfaden zum <a href="/coachs/coaching-sportif-en-ligne-comment-faire.html">Online-Coaching</a> behandelt den gesamten Rahmen. Video bringt zwei eigene Punkte mit.</p>
<ul>
<li><strong>Aufnahmen.</strong> Dein Kunde ist zu Hause: Nimm nichts ohne sein Einverständnis auf. Fotos oder Videos, auf denen er erkennbar ist, darfst du nur mit seiner Einwilligung veröffentlichen (§ 22 KUG). Eine bestimmte Form schreibt das KUG nicht vor; eine schriftliche Einwilligung, die Medium, Zweck und Dauer nennt, ist trotzdem dein bester Beleg.</li>
<li><strong>Gruppen.</strong> In einer Gruppeneinheit sehen die Teilnehmenden in die Wohnungen der anderen. Weise sie darauf hin und biete einen unscharfen Hintergrund an, wenn dein Tool das erlaubt.</li>
</ul>
<p>Dieser Leitfaden dient nur der Information und ersetzt keine Beratung durch einen Anwalt oder einen Arzt.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Ein stabiles Gerät, klarer Ton, Licht von vorn und eine getestete Verbindung reichen.</li>
<li>Prüf Bildausschnitt und Tagesform deines Kunden, korrigier jeweils einen Punkt und steuere die Intensität nach Gefühl.</li>
<li>Notiere die Adresse, leg die Regel für Verbindungsabbrüche fest und wähl die 112, wenn dein Kunde einer Ohnmacht nahe ist oder zusammenbricht.</li>
</ul>
""",
        "faq": [
            {"q": "Was braucht man für ein Fitnesstraining per Videocall?", "a": "Du brauchst ein Handy oder einen Laptop auf einer stabilen Halterung, klaren Ton, Licht von vorn und eine vorher getestete Verbindung. Dein Kunde braucht ein Gerät, das auf dem Boden oder einem Stuhl steht, eine Matte und genug Platz, um sich hinzulegen und die Arme auszustrecken."},
            {"q": "Wie gibt man eine Trainingseinheit per Videocall?", "a": "Prüf zuerst Ton, Bildausschnitt, Platz und die Tagesform deines Kunden. Dann folgen Aufwärmen, zwei oder drei beherrschte Übungen, ein Cool-down und ein Abschluss. Sprich mehr als im Studio, korrigier jeweils einen Punkt und lass dir bei jedem Block die empfundene Anstrengung nennen."},
            {"q": "Was tun, wenn ein Kunde im Videocall einen Notfall hat?", "a": "Wähl die 112, sag, dass die Person an einer anderen Adresse ist, nenn sie und bleib in der Leitung. Deshalb notierst du vor der Einheit die genaue Adresse und lässt dir die Nummer einer nahestehenden Person geben. Für Beschwerden, die nicht lebensbedrohlich sind, ist in Deutschland der ärztliche Bereitschaftsdienst unter 116 117 erreichbar."},
        ],
        "sources": [
            {"t": "Brown RCC, Simmich J, Cuthbert R, et al. Safety of videoconferencing for physical rehabilitation and exercise: A systematic review and meta-analysis. <em>Clin Rehabil</em>. 2025.", "u": "https://doi.org/10.1177/02692155251361916"},
            {"t": "Toledano-Shubi A, Shapira AL, Fuchsman R, et al. Feasibility and effectiveness of physical exercise for older adults delivered remotely via videoconferencing: systematic review and meta-analysis. <em>Age Ageing</em>. 2025.", "u": "https://doi.org/10.1093/ageing/afaf171"},
            {"t": "gesund.bund.de, Bundesministerium für Gesundheit. Ärztlicher Bereitschaftsdienst. Stand: 23.04.2026.", "u": "https://gesund.bund.de/wege-im-gesundheitswesen/erwachsenenleben/notfaelle/aerztlicher-bereitschaftsdienst"},
            {"t": "Gesetz betreffend das Urheberrecht an Werken der bildenden Künste und der Photographie (Kunsturhebergesetz, KUG), § 22.", "u": "https://www.gesetze-im-internet.de/kunsturhg/__22.html"},
            {"t": "Bundesagentur für Arbeit. BERUFENET: Fitnesstrainer/in, Zugang zur Tätigkeit.", "u": "https://web.arbeitsagentur.de/berufenet/beruf/15658"},
            {"t": "Gesetz über die berufsmäßige Ausübung der Heilkunde ohne Bestallung (Heilpraktikergesetz), § 1.", "u": "https://www.gesetze-im-internet.de/heilprg/__1.html"},
            {"t": "Bundesministerium für Inneres (Österreich). Notrufnummern.", "u": "https://www.bmi.gv.at/notrufnummern/start.html"},
            {"t": "Bundesamt für Kommunikation (BAKOM, Schweiz). Weitere Nummern: kostenpflichtig oder gratis? 2024.", "u": "https://www.bakom.admin.ch/de/weitere-nummern-kostenpflichtig-oder-gratis"},
        ],
    },
    {
        "fr": "suivre-client-a-distance",
        "slug": "kunden-aus-der-ferne-betreuen",
        "title": "Kunden aus der Ferne betreuen, ohne deine Abende zu opfern",
        "description": "Kunden aus der Ferne betreuen: welcher Rhythmus für Rückmeldungen passt, was du jede Woche fragst, wie viel Zeit es wirklich kostet und wo die Daten hingehören.",
        "body": """
<p>Die kurze Antwort: Willst du <strong>Kunden aus der Ferne betreuen</strong>, ohne deine Abende zu opfern, ersetzt du verstreute Nachrichten durch einen schriftlichen Wochen-Check-in: ein kurzes Formular von deinem Kunden, eine gebündelte Antwort von dir in einem festen Zeitfenster. Miss die Zeit, die das kostet, bevor du deinen Preis festlegst. Und denk daran: Die Pflichten, die du vor Ort gegenüber einem Kunden hast, verschwinden aus der Ferne nicht.</p>

<h2>Wie viel Zeit kostet ein Online-Kunde?</h2>
<p>Einen Richtwert habe ich nicht gefunden, also erfasse vier Wochen lang selbst deine Zeit. Zähl alles, vom Lesen des Check-ins über Antworten, Nachrichten und Videos bis zur Anpassung des Plans. Beispielrechnung für 12 Kunden: 15 Minuten pro Kunde und Woche ergeben 3 Stunden, also rund 13 Stunden im Monat. Dazu kommen 30 Minuten pro Kunde und Monat, um den Trainingsplan anzupassen, also 6 Stunden. Summe: rund 19 Stunden im Monat.</p>
<p>Teile dann, was das Angebot einbringt, durch diese tatsächliche Zeit. So erhältst du deinen Stundensatz, den du mit deinen Einheiten vor Ort vergleichst. Geht die Rechnung nicht auf, überarbeite den Inhalt des Angebots, die Zahl der Kunden oder deine <a href="/coachs/tarif-coaching-en-ligne.html">Preise für Online-Coaching</a>. Ein Einsteiger oder ein verletzter Kunde kann mehr Zeit kosten als diese Zahl.</p>

<h2>Wie oft solltest du dich bei Online-Kunden melden?</h2>
<p>Die hier zitierten Studien legen keine ideale Häufigkeit fest. Eine einfache Grundlage hat drei Stufen:</p>
<ul>
<li><strong>Jede Woche:</strong> ein Formular, das an einem festen Tag ausgefüllt wird, und deine schriftliche Antwort innerhalb einer angekündigten Frist.</li>
<li><strong>Alle vier Wochen:</strong> eine Zwischenbilanz und ein angepasster Trainingsplan.</li>
<li><strong>Je nach Angebot:</strong> ein kurzer Videocall statt eines endlosen Chatverlaufs.</li>
</ul>
<p>Schreib diesen Rahmen in dein Angebot: Antworttage, Antwortzeit, Kanal. Ein Kunde, der weiß, wann die Antwort kommt, hakt seltener nach. Sag auch, was dein Coaching nicht abdeckt. Bei Ohnmacht, starken Schmerzen oder einem neuen Symptom wendet sich dein Kunde an einen Arzt, ohne auf deine Nachricht zu warten: bei Beschwerden, die nicht lebensbedrohlich sind, an den ärztlichen Bereitschaftsdienst unter 116 117, im Notfall an die 112.</p>

<h2>Was fragst du Online-Kunden jede Woche?</h2>
<p>Fünf Fragen, nicht mehr. Dein Kunde sollte sie in drei Minuten am Handy beantworten können:</p>
<ol>
<li>Wie viele Einheiten hast du gemacht, von wie vielen geplanten?</li>
<li>Wie anstrengend war die härteste Einheit, von 0 bis 10?</li>
<li>Wie waren Schlaf und Energie, von 1 bis 5?</li>
<li>Gab es Schmerzen oder Beschwerden: wo, und seit wann?</li>
<li>Welche Frage möchtest du mir stellen?</li>
</ol>
<p>Diese Routine stützt sich auf allgemeine Befunde: Keine dieser Studien untersucht Online-Coaching. In 122 Evaluationen mit 44.747 Personen fanden Michie und Kollegen (2009), dass die Selbstbeobachtung die Technik war, die Unterschiede in der Wirksamkeit von Interventionen für Bewegung und gesunde Ernährung am besten erklärte. Die Übersichtsarbeit von Saw und Kollegen (2016), an Sportlern durchgeführt, zeigt, dass subjektive Messgrößen die Trainingsbelastung besser abbilden als objektive. Wie du die Antworten auswertest, zeigt der Leitfaden dazu, wie du <a href="/coachs/lire-etat-de-forme-client.html">die Tagesform deiner Kunden einschätzt</a>. Lass dir ein Video einer Schlüsselübung schicken, wenn die Technik es verlangt.</p>

<h2>Wie antwortest du schnell, ohne unpersönlich zu wirken?</h2>
<ul>
<li><strong>Feste Zeitfenster.</strong> Zwei Blöcke pro Woche, zum Beispiel dienstags und donnerstags vormittags. Außerhalb davon: Benachrichtigungen aus.</li>
<li><strong>Sortieren in drei Stufen.</strong> Kunde macht Fortschritte: zwei Zeilen. Kunde steckt fest: eine Anpassung. Kunde entgleitet dir oder meldet Schmerzen: eine lange Antwort oder ein Anruf.</li>
<li><strong>Eine Bibliothek.</strong> Film deine Demonstrationen einmal und halte Antwortvorlagen für die Hinweise bereit, die immer wiederkommen.</li>
<li><strong>Ein persönlicher Satz.</strong> Jede Antwort greift ein Detail deines Kunden auf: seine Einheit, seine Zahl, seine Frage. Dein Kunde merkt sofort, ob du gelesen hast.</li>
<li><strong>Ein Kanal.</strong> Ein Verlauf pro Kunde, am selben Ort.</li>
</ul>

<h2>Welche Regeln gelten weiter, wenn du Kunden aus der Ferne betreust?</h2>
<p>Die Entfernung nimmt dir keine Pflichten ab. In Deutschland brauchst du als Personal Trainer keine gesetzlich vorgeschriebene Ausbildung oder Lizenz; Krankheiten feststellen, heilen oder lindern darfst du als Nicht-Arzt aber nur mit einer Erlaubnis nach dem Heilpraktikergesetz, online wie vor Ort. Sicherheitshalber gilt: Je individueller dein Coaching, desto mehr gleicht es einem Training unter Anleitung. Die Grundlagen stehen in unserem Leitfaden zum <a href="/coachs/coaching-sportif-en-ligne-comment-faire.html">Online-Coaching</a>.</p>
<p>Dann sind da die Daten. Schlaf, Schmerzen, Gewicht, Herzfrequenz: Diese Antworten können Gesundheitsdaten sein, und in der EU ist deren Verarbeitung grundsätzlich untersagt, außer in bestimmten Ausnahmefällen (Art. 9 DSGVO). Der erste ist die ausdrückliche Einwilligung deines Kunden für festgelegte Zwecke, die er jederzeit und genauso einfach widerrufen kann, wie er sie erteilt hat: Hol sie getrennt von deinen AGB ein. In Deutschland ergänzt das Bundesdatenschutzgesetz (BDSG) die DSGVO; zuständig für dich ist nicht der Bundesdatenschutzbeauftragte, sondern die Datenschutzaufsichtsbehörde deines Bundeslandes.</p>
<p>Ein WhatsApp-Verlauf oder eine ungeschützte Datei passt schlecht zu diesen Daten. Bewahre sie in einem geschützten Bereich auf, erfasse nur das Nötige, lösche sie am Ende des Coachings und gib nichts ohne die Zustimmung deines Kunden an Dritte weiter.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Ein wöchentliches Formular und eine gebündelte Antwort in einem festen Zeitfenster ersetzen verstreute Nachrichten.</li>
<li>Miss deine Zeit, bevor du Preis und Kundenzahl festlegst.</li>
<li>Aus der Ferne bleiben deine Pflichten bestehen: Beachte die Grenze des Heilpraktikergesetzes und schütze die Gesundheitsdaten deiner Kunden nach der DSGVO.</li>
</ul>
""",
        "faq": [
            {"q": "Wie funktioniert Online-Coaching mit einem Personal Trainer?", "a": "Der Trainer erstellt den Trainingsplan, der Kunde trainiert allein und füllt jede Woche ein kurzes Formular aus. Der Trainer antwortet zu festen Zeiten, passt den Plan etwa alle vier Wochen an und kann einen Videocall anbieten. Rahmen, Antwortzeit und Kanal werden von Anfang an angekündigt."},
            {"q": "Wie viel Zeit kostet ein Online-Coaching-Kunde?", "a": "Einen Richtwert habe ich nicht gefunden, also erfasse vier Wochen lang selbst deine Zeit. Als Beispielrechnung ergeben 15 Minuten pro Kunde und Woche plus 30 Minuten pro Kunde und Monat für den Trainingsplan bei 12 Kunden rund 19 Stunden im Monat."},
            {"q": "Kann man Kunden über WhatsApp coachen?", "a": "Ein WhatsApp-Verlauf passt schlecht zu Gesundheitsdaten. Nutze ihn für praktische Nachrichten und bewahre Schmerzen, Gewicht oder Fragebögen in einem geschützten Bereich auf, mit der ausdrücklichen Einwilligung deines Kunden."},
        ],
        "sources": [
            {"t": "Michie S, Abraham C, Whittington C, McAteer J, Gupta S. Effective techniques in healthy eating and physical activity interventions: a meta-regression. <em>Health Psychol</em>. 2009.", "u": "https://doi.org/10.1037/a0016136"},
            {"t": "Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures: a systematic review. <em>Br J Sports Med</em>. 2016.", "u": "https://doi.org/10.1136/bjsports-2015-094758"},
            {"t": "Bundesagentur für Arbeit. BERUFENET: Fitnesstrainer/in, Zugang zur Tätigkeit.", "u": "https://web.arbeitsagentur.de/berufenet/beruf/15658"},
            {"t": "Gesetz über die berufsmäßige Ausübung der Heilkunde ohne Bestallung (Heilpraktikergesetz), § 1.", "u": "https://www.gesetze-im-internet.de/heilprg/__1.html"},
            {"t": "Verordnung (EU) 2016/679 des Europäischen Parlaments und des Rates vom 27. April 2016 zum Schutz natürlicher Personen bei der Verarbeitung personenbezogener Daten, zum freien Datenverkehr und zur Aufhebung der Richtlinie 95/46/EG (Datenschutz-Grundverordnung), Art. 7 und 9. EUR-Lex. 2016.", "u": "https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Bundesdatenschutzgesetz (BDSG), § 40 Aufsichtsbehörden der Länder.", "u": "https://www.gesetze-im-internet.de/bdsg_2018/__40.html"},
            {"t": "Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI). Seite mit den Anschriften der Datenschutzaufsichtsbehörden der Länder.", "u": "https://www.bfdi.bund.de/DE/Service/Anschriften/Laender/Laender-node.html"},
            {"t": "gesund.bund.de, Bundesministerium für Gesundheit. Ärztlicher Bereitschaftsdienst. Stand: 23.04.2026.", "u": "https://gesund.bund.de/wege-im-gesundheitswesen/erwachsenenleben/notfaelle/aerztlicher-bereitschaftsdienst"},
        ],
    },
    {
        "fr": "tarif-coaching-en-ligne",
        "slug": "online-coaching-preise",
        "title": "Preise für Online-Coaching: Wie viel solltest du verlangen?",
        "description": "Preise für Online-Coaching: Einen offiziellen Durchschnitt gibt es nicht. Berechne deinen Monatspreis aus Zeit pro Kunde, Kosten, Steuern und Beiträgen.",
        "body": """
<p>Die kurze Antwort: Für deine <strong>Preise für Online-Coaching</strong> gibt es weder eine offizielle Tabelle noch einen veröffentlichten Durchschnitt. Berechne einen Monatspreis aus drei Zahlen: der Zeit, die ein Kunde kostet, der Zahl zahlender Kunden, die du betreuen kannst, und dem Umsatz, den du brauchst, um Einkommen, Kosten, Steuern und Beiträge zu decken. Im Beispiel dieses Leitfadens liegt die Untergrenze bei 207 € im Monat mit 15 Kunden, ohne Umsatzsteuer. Dieser Betrag gilt nur für seine Annahmen: Ersetze sie durch deine.</p>

<h2>Was kostet ein Online-Coach im Durchschnitt?</h2>
<p>Das weiß niemand. Eine offizielle Quelle für diesen Preis habe ich nicht gefunden. Preise auf Instagram oder auf den Websites von Coaches sind Angebotspreise: Sie sagen weder, wie viele Kunden sie zahlen, noch, wie lange diese Kunden bleiben. Außerdem vergleichen sie unterschiedliche Produkte.</p>
<ul>
<li><strong>Ein einmal verkauftes Programm:</strong> eine Datei oder ein Zugang, ohne Betreuung. Du verkaufst Zeit, die du schon investiert hast.</li>
<li><strong>Monatliche Online-Betreuung:</strong> ein angepasster Trainingsplan, schriftliches Feedback, Nachrichten, eine Zwischenbilanz. Du verkaufst Zeit, die jeden Monat wiederkommt.</li>
<li><strong>Coaching mit Videocalls:</strong> dasselbe, plus reservierte Termine. Diese Termine bepreist du wie <a href="/coachs/tarif-coach-sportif-independant.html">eine Einheit vor Ort</a>.</li>
</ul>

<h2>Wie berechnest du den Preis für monatliches Online-Coaching?</h2>
<ol>
<li><strong>Miss deine Zeit pro Kunde.</strong> Erfasse einen ganzen Monat lang die Zeit für Planung, das Lesen von Rückmeldungen, Nachrichten und die Zwischenbilanz. Das Beispiel rechnet mit 3 Stunden.</li>
<li><strong>Leg eine realistische Kundenzahl fest.</strong> Manche Kunden gehen, andere kommen, und ein freier Platz bringt nichts ein. Das Beispiel rechnet mit durchschnittlich 15 zahlenden Kunden über das Jahr.</li>
<li><strong>Berechne den nötigen Umsatz:</strong> (Zieleinkommen + Kosten) ÷ (1 − Anteil des Umsatzes, der an Steuern und Beiträge geht). Das Beispiel nimmt dafür einen erfundenen Anteil von 25,8 % an. In Deutschland sind Steuern und Beiträge selten ein fester Anteil des Umsatzes: Lass dir den Betrag dann von deinem Steuerberater geben und addiere ihn zu den beiden anderen.</li>
</ol>
<div class="tablewrap"><table>
<caption>Quelle: Beispielrechnung. Alle Beträge, auch die in der Umsatzzeile enthaltenen Steuern und Beiträge (erfundener Anteil von 25,8 %), sind Annahmen in Euro, keine Marktpreise oder Steuersätze.</caption>
<thead><tr><th>Schritt</th><th class="n">Beispiel</th></tr></thead>
<tbody>
<tr><td>Zieleinkommen vor Einkommensteuer (1.800 € × 12)</td><td class="n">21.600 €</td></tr>
<tr><td>Jährliche Kosten</td><td class="n">6.000 €</td></tr>
<tr><td>Nötiger Jahresumsatz, einschließlich Steuern und Beiträgen</td><td class="n">37.197 €</td></tr>
<tr><td>Monatsumsatz</td><td class="n">3.100 €</td></tr>
<tr><td>Zahlende Kunden im Durchschnitt</td><td class="n">15</td></tr>
<tr><td>Untergrenze pro Kunde und Monat</td><td class="n">207 €</td></tr>
</tbody>
</table></div>
<p>Prüf dann deinen Stundensatz: 207 € für 3 Stunden sind 69 € pro Stunde. Kostet dich ein Kunde 5 Stunden, fällt dieser Satz auf 41 €. Variiere auch die Kundenzahl: Mit 10 Kunden steigt die Untergrenze auf 310 €. Mit 20 sinkt sie auf 155 €, für 60 Stunden Coaching im Monat. Schreib deshalb in dein Angebot, was enthalten ist: Zahl der Check-ins, Antwortzeit, Zwischenbilanzen. Ohne diesen Rahmen steigt deine Zeit pro Kunde, und dein tatsächlicher Preis sinkt.</p>

<h2>Welche Kosten rechnest du beim Online-Coaching ein?</h2>
<p>Zu deinen üblichen Kosten kommen Coaching-Software, Videotool, Website, Zahlungsgebühren und Erstattungen. Einkommensteuer zahlst du in Deutschland auf deinen Gewinn, also auf Einnahmen minus Ausgaben; welche Kosten genau abziehbar sind, klärst du mit deinem Steuerberater. Bist du Kleinunternehmer, ziehst du keine Vorsteuer ab: Die Umsatzsteuer auf deinen Software-Abos bleibt dann an dir hängen. Plane außerdem Versicherungen und Buchhaltung ein, wie bei der Arbeit vor Ort.</p>
<p>Zwei Beiträge folgen eigenen Regeln. Eine Krankenversicherung ist in Deutschland Pflicht; freiwillig gesetzlich versichert zahlst du 2026 mindestens 222,80 € (ohne Krankengeld) bzw. 230,71 € (mit Krankengeld) im Monat, bei einem Zusatzbeitrag von 2,9 % und ohne Pflegeversicherung. Und als selbstständiger Trainer kannst du als „Lehrer“ rentenversicherungspflichtig sein, wenn du mehr als 603 € im Monat verdienst und keinen versicherungspflichtigen Mitarbeiter beschäftigst; melden musst du dich innerhalb von drei Monaten bei der Deutschen Rentenversicherung.</p>

<h2>Welche Regeln betreffen dein Angebot?</h2>
<p><strong>Dein Status.</strong> Online zu verkaufen stellt dich nicht außerhalb der Regeln. Ob du ein Gewerbe anmeldest oder als Freiberufler mit unterrichtender Tätigkeit giltst, hängt davon ab, was du konkret anbietest. Sicherheitshalber gilt: Je individueller dein Coaching, desto mehr gleicht es einem Training unter Anleitung. <a href="/coachs/coaching-sportif-en-ligne-comment-faire.html">Dieser Leitfaden zum Online-Coaching</a> behandelt den Rahmen.</p>
<p><strong>Umsatzsteuer.</strong> Personal Training unterliegt in Deutschland grundsätzlich 19 % Umsatzsteuer. Als Kleinunternehmer bist du befreit, wenn dein Umsatz im Vorjahr höchstens 25.000 € betrug und im laufenden Jahr 100.000 € nicht übersteigt; im Gründungsjahr gilt eine Grenze von 25.000 €. Mit 37.197 € liegt das Beispiel darüber, also kommt spätestens im Folgejahr die Umsatzsteuer auf die 207 €. Gibst du sie weiter, zahlt dein Kunde 246,33 €. Prüf deshalb vor jeder Preiserhöhung, ob sie dich über die Kleinunternehmergrenze bringt.</p>
<p><strong>Widerruf.</strong> Schließt du online mit Privatkunden einen Vertrag, können sie ihn 14 Tage lang widerrufen. Rechne Erstattungen also in deine Zahlen ein und halte deinen Ablauf schriftlich fest. Will dein Kunde sofort starten, halte diesen ausdrücklichen Wunsch schriftlich fest und sag, was er für bereits Geleistetes zahlt: Widerruft er danach, schuldet er dafür Wertersatz.</p>
<p><strong>Abos.</strong> Verkaufst du Abos über deine Website, brauchst du einen Kündigungsbutton „Verträge hier kündigen“, der direkt zu einer Bestätigungsseite mit dem Button „jetzt kündigen“ führt (§ 312k BGB). Verlängerungen behandelt <a href="/coachs/packs-abonnement-seance-coach-sportif.html">der Leitfaden zu Paketen und Monatsabos</a>.</p>
<p><strong>Was unsicher bleibt.</strong> Ein Programm, das du vielen Kunden gleich verkaufst, wird steuerlich vielleicht nicht wie individuelles Coaching behandelt. Laut einer Expertenantwort im Existenzgründungsportal des Bundeswirtschaftsministeriums (Stand 2019, nicht mehr aktualisiert) sieht das Finanzamt eine virtuelle Leistungserbringung häufig als Indiz für eine gewerbliche Tätigkeit. Dann fällt Gewerbesteuer an, aber erst oberhalb eines Freibetrags von 24.500 € Gewerbeertrag. Frag deinen Steuerberater oder dein Finanzamt, bevor du es <a href="/coachs/vendre-programme-sportif-en-ligne.html">online verkaufst</a>.</p>
<p>Dieser Leitfaden dient nur der Information und ersetzt keine Beratung durch einen Steuerberater oder einen Anwalt.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Es gibt weder eine offizielle Tabelle noch einen veröffentlichten Durchschnitt: Preise im Netz beweisen nicht, was Kunden zahlen.</li>
<li>Bau einen Monatspreis aus deiner Zeit pro Kunde, deinen zahlenden Kunden, deinen Kosten, Steuern und Beiträgen, und prüf, ob 19 % Umsatzsteuer hinzukommen.</li>
<li>Variiere Zeit pro Kunde und Kundenzahl, bevor du dich auf einen Preis festlegst, und schreib auf, was das Angebot enthält.</li>
</ul>
""",
        "faq": [
            {"q": "Was kostet ein Online-Coach im Durchschnitt?", "a": "Eine offizielle Quelle, die einen Durchschnittspreis veröffentlicht, habe ich nicht gefunden. Die Preise im Netz sind Angebotspreise, für sehr unterschiedliche Angebote, vom einzelnen Programm bis zum Coaching mit Videocalls. Berechne deine eigene Untergrenze aus deiner Zeit pro Kunde, deinen Kosten, Steuern und Beiträgen."},
            {"q": "Wie viel kann man für Online-Coaching pro Monat verlangen?", "a": "Addiere dein Zieleinkommen, deine jährlichen Kosten, Steuern und Beiträge und teile dann durch 12 und durch deine durchschnittliche Zahl zahlender Kunden. Im Beispiel dieses Leitfadens ergibt das 207 € im Monat mit 15 Kunden, ein Ergebnis, das nur für seine Annahmen gilt. Bist du kein Kleinunternehmer, kommen 19 % Umsatzsteuer hinzu."},
            {"q": "Sollte Online-Coaching weniger kosten als Training vor Ort?", "a": "Keine Regel sagt das. Vergleiche die Zeit, die du deinem Kunden tatsächlich gibst: Ein Coaching, das dich 3 Stunden im Monat kostet, ist mindestens 3 Stunden deiner Stundenuntergrenze wert. Vor Ort kosten dich die Wege, online die Tools und die Lesezeit."},
        ],
        "sources": [
            {"t": "Umsatzsteuergesetz (UStG), § 12 Steuersätze.", "u": "https://www.gesetze-im-internet.de/ustg_1980/__12.html"},
            {"t": "Umsatzsteuergesetz (UStG), § 19 (Kleinunternehmerregelung).", "u": "https://www.gesetze-im-internet.de/ustg_1980/__19.html"},
            {"t": "Gewerbesteuergesetz (GewStG), § 11 (Freibetrag von 24.500 Euro für natürliche Personen).", "u": "https://www.gesetze-im-internet.de/gewstg/__11.html"},
            {"t": "Existenzgründungsportal des Bundeswirtschaftsministeriums. Online-Coaching und Ernährungsberatung: freiberufliche oder gewerbliche Tätigkeiten? Stand: August 2019.", "u": "https://www.existenzgruendungsportal.de/Redaktion/DE/BMWK-Infopool/Antworten/Gruendungsplanung/Freie-Berufe/unterrichtende-Taetigkeit/Online-Coaching-und-Ernaehrungsberatung-freiberufliche-oder-gewerbliche-Taetigkeiten.html"},
            {"t": "Bundesministerium für Gesundheit. Beiträge der gesetzlichen Krankenversicherung. 2026.", "u": "https://www.bundesgesundheitsministerium.de/beitraege"},
            {"t": "Deutsche Rentenversicherung. Selbstständige.", "u": "https://www.deutsche-rentenversicherung.de/DRV/DE/Rente/Arbeitnehmer-und-Selbststaendige/03_Selbststaendige/selbststaendige_node.html"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 355 Widerrufsrecht bei Verbraucherverträgen.", "u": "https://www.gesetze-im-internet.de/bgb/__355.html"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 312k: Kündigung von Verbraucherverträgen im elektronischen Geschäftsverkehr.", "u": "https://www.gesetze-im-internet.de/bgb/__312k.html"},
        ],
    },
    {
        "fr": "packs-abonnement-seance-coach-sportif",
        "slug": "paket-oder-monatsabo-personal-training",
        "title": "10er-Karte, Monatsabo oder Einzeleinheit: Was bietest du an?",
        "description": "10er-Karte, Monatsabo oder Einzeleinheit? Berechne den Monatspreis fürs Personal Training und regle Verlängerung, Kündigung und nicht genutzte Einheiten klar.",
        "body": """
<p>Die kurze Antwort: Beim <strong>Monatspreis fürs Personal Training</strong> gewinnt kein Format immer. Einzeleinheiten sind einfach, aber unregelmäßig. Ein Paket wie die 10er-Karte bringt dir Geld im Voraus und verpflichtet dich zu Einheiten, die du noch geben musst. Ein Monatsabo glättet dein Einkommen und braucht die sorgfältigsten Bedingungen. Berechne deinen Monatspreis aus den Wochen, die du tatsächlich arbeitest, und schreib in den Vertrag, was mit nicht genutzten Einheiten passiert.</p>

<h2>Welches Format passt zu welchem Kunden?</h2>
<div class="tablewrap"><table>
<caption>Quelle: Vergleich für diesen Leitfaden.</caption>
<thead><tr><th>Format</th><th>Für dich</th><th>Was du schriftlich festhältst</th></tr></thead>
<tbody>
<tr><td>Einzeleinheit</td><td>Keine Vorauszahlung zu verwalten, unregelmäßiges Einkommen</td><td>Preis, Dauer, Absage</td></tr>
<tr><td>Paket (10er-Karte)</td><td>Geld im Voraus, Einheiten, die du bis zum Ende schuldest</td><td>Zahl der Einheiten, Gültigkeit, Verschiebungen, Erstattungen</td></tr>
<tr><td>Abo mit fester Laufzeit</td><td>Planbares Einkommen, Preis für die Laufzeit fest</td><td>Laufzeit, enthaltene Einheiten, Verlängerung</td></tr>
<tr><td>Unbefristetes Abo</td><td>Stetiges Einkommen, dein Kunde kann mit Frist gehen</td><td>Gleiche Frist für beide Seiten, Preisanpassung</td></tr>
</tbody>
</table></div>
<p>Daten, die diese Formate unter Trainern vergleichen, habe ich nicht gefunden: Das ist eine geschäftliche Entscheidung. Einzeleinheiten passen zu einem Probetraining oder einem unregelmäßigen Kunden, ein Paket zu einem kurzfristigen Ziel und ein Abo zu dem Kunden, der jede Woche wiederkommt.</p>

<h2>Wie berechnest du den Monatspreis fürs Personal Training?</h2>
<p>Monatspreis = Preis pro Einheit × Einheiten pro Woche × gearbeitete Wochen pro Jahr ÷ 12. Beispielrechnung: 50 € pro Einheit, 2 Einheiten pro Woche, 44 gearbeitete Wochen. Das ergibt 88 Einheiten und 4.400 € im Jahr, also 366,67 € im Monat.</p>
<p>Vermeide die Abkürzung „2 Einheiten × 4 Wochen“: Sie ergibt 400 € im Monat, also 54,55 € pro Einheit über diese 88 Einheiten. Schreib stattdessen die Zahl der Einheiten pro Jahr und deine Schließwochen auf.</p>
<p>Prüf jeden Paketrabatt an deiner <a href="/coachs/tarif-coach-sportif-independant.html">Preisuntergrenze</a>. Mit einer Untergrenze von 45 € lässt dir eine 10er-Karte zu 45 € pro Einheit keinen Spielraum. Frag außerdem deinen Steuerberater, für welches Jahr ein Paket zählt. Ermittelst du deinen Gewinn mit der Einnahmenüberschussrechnung (EÜR), also als Überschuss der Einnahmen über die Ausgaben, kann ein im Dezember bezahltes Paket ins laufende Jahr fallen, auch wenn die Einheiten erst im März stattfinden.</p>

<h2>Was passiert mit nicht genutzten Einheiten?</h2>
<p>Geh nicht davon aus, dass ein Paket eine gesetzlich festgelegte Gültigkeitsdauer hat. Du kannst ihm ein Ablaufdatum geben, vor dem Kauf schriftlich festgelegt und realistisch für deinen Kunden. Das Risiko liegt in der Klausel „Keine Einheit wird erstattet, aus keinem Grund“: Sie kann unwirksam sein, vor allem wenn du derjenige bist, der absagt, oder bei höherer Gewalt.</p>
<p>In Deutschland werden AGB nach den §§ 305 bis 310 BGB kontrolliert: Klauseln, die deine Kunden unangemessen benachteiligen oder unklar formuliert sind, sind unwirksam (§ 307 BGB), und die §§ 308 und 309 zählen verbotene Klauseln auf. Eine offizielle Empfehlung speziell für Coaching-Verträge habe ich nicht gefunden. Das EU-Recht setzt denselben Maßstab: Eine nicht ausgehandelte Klausel ist missbräuchlich, wenn sie entgegen dem Gebot von Treu und Glauben zum Nachteil deines Kunden ein erhebliches Missverhältnis der Rechte und Pflichten verursacht, und dann ist sie für ihn unverbindlich (Richtlinie 93/13/EWG). Plane jeden Fall ein:</p>
<ul>
<li><strong>Du hörst auf:</strong> Erstatte die Einheiten, die du nicht gegeben hast. Dieses Geld zu behalten, wenn du den Vertrag beendest, ist schwer zu verteidigen.</li>
<li><strong>Dein Kunde kann nicht mehr kommen:</strong> Sieh eine Verschiebung oder eine Erstattung vor, mit schriftlichen Kriterien, und mach dich nicht zum alleinigen Richter. Klare Kriterien ersparen euch Streit, denn nicht jeder Grund berechtigt zur Kündigung: Der BGH hat 2016 entschieden, dass ein berufsbedingter Umzug grundsätzlich nicht zur vorzeitigen Kündigung eines langfristigen Fitnessstudiovertrags berechtigt. Der Vertrag stammte von 2010, also von vor der Reform des § 309 Nr. 9 BGB im Jahr 2022.</li>
<li><strong>Dein Kunde springt ohne Grund ab:</strong> Behalte höchstens eine angemessene Pauschale, und sieh dasselbe vor, wenn du derjenige bist, der abspringt.</li>
<li><strong>Kurzfristige Absage:</strong> Stell eine Frist von 24 oder 48 Stunden nicht als gesetzliche Regel dar. <a href="/coachs/seance-annulee-regles-coach.html">Leg deine eigene Regel</a> schriftlich fest.</li>
</ul>
<p>Halte außerdem schriftlich fest, was eine Vorauszahlung ist und was mit ihr passiert, wenn einer von euch abspringt. Ein Grund mehr, Pakete kurz zu halten.</p>

<h2>Was gehört in einen Vertrag für ein Monatsabo?</h2>
<p><strong>Laufzeit und automatische Verlängerung.</strong> Per AGB darf ein Abo deine Kunden höchstens zwei Jahre binden; verlängert es sich automatisch, dann nur auf unbestimmte Zeit und mit einer Kündigungsfrist von höchstens einem Monat (§ 309 Nr. 9 BGB). Auch die Kündigungsfrist zum Ende der ersten Laufzeit darf höchstens einen Monat betragen. Eine Erinnerung vor diesem Stichtag ist trotzdem ein fairer Service: Schreib das Datum gut sichtbar in den Vertrag.</p>
<p><strong>Monat für Monat.</strong> Ein Vertrag über einen Monat, der sich von selbst um je einen weiteren Monat verlängert, passt schlecht zu dieser Regel, denn per AGB ist eine stillschweigende Verlängerung nur auf unbestimmte Zeit zulässig. Vermeide diese Konstruktion. Wähl eine feste Laufzeit, die nur durch eine neue Vereinbarung verlängert wird, oder einen unbefristeten Vertrag, der auch so heißt.</p>
<p><strong>Unbefristete Abos.</strong> Verlang von deinem Kunden keine längere Kündigungsfrist als die, die du dir selbst gibst, und berechne keine Kündigungsgebühr. Schreib nicht „ohne Vertragsbindung“, wenn es eine Mindestlaufzeit gibt.</p>
<p><strong>Online.</strong> Verkaufst du Abos über deine Website, brauchst du einen Kündigungsbutton „Verträge hier kündigen“, der direkt zu einer Bestätigungsseite mit dem Button „jetzt kündigen“ führt (§ 312k BGB). Laut BGH (Urteil vom 16. Juli 2026, zu einem Fitnessstudio) dürfen auf dieser Bestätigungsseite keine weiteren Angaben oder Angebote stehen, auch keine kostenlose Pause statt der Kündigung. Fehlt der Button, kann dein Kunde jederzeit ohne Frist kündigen. Schließt du den Vertrag online oder außerhalb deiner Geschäftsräume mit einem Privatkunden, kann er ihn außerdem 14 Tage lang widerrufen.</p>
<p>Dieser Leitfaden dient nur der Information und ersetzt keine Beratung durch einen Anwalt.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Berechne deinen Monatspreis aus den Wochen, die du tatsächlich arbeitest, und schreib die Zahl der Einheiten pro Jahr in den Vertrag.</li>
<li>Regle Ablaufdatum, Verschiebungen und Erstattungen eines Pakets: „Keine Erstattung, aus keinem Grund“ ist eine riskante Klausel.</li>
<li>Vermeide die Verlängerung von Monat zu Monat: Wähl eine feste Laufzeit, die per neuer Vereinbarung verlängert wird, oder einen unbefristeten Vertrag mit gleicher Frist für beide Seiten.</li>
</ul>
""",
        "faq": [
            {"q": "Was kostet ein Personal Trainer im Monat?", "a": "Eine offizielle Tabelle legt das nicht fest. Der Monatspreis hängt vom Preis pro Einheit, von der Zahl der Einheiten pro Woche und von den gearbeiteten Wochen im Jahr ab. Beispielrechnung: 50 € pro Einheit, eine Einheit pro Woche über 44 Wochen, also 183,33 € im Monat."},
            {"q": "Darf ein Personal Trainer die Erstattung einer 10er-Karte verweigern?", "a": "Das hängt vom Grund und vom Vertrag ab. Eine Klausel, die jede Erstattung aus jedem Grund ausschließt, kann nach § 307 BGB unwirksam sein, vor allem wenn der Trainer absagt oder bei höherer Gewalt. Ein Trainer, der den Vertrag nach Belieben beendet, sollte den Preis nicht gegebener Einheiten nicht behalten."},
            {"q": "Kann ein Personal Trainer ein Abo ohne Mindestlaufzeit anbieten?", "a": "Ja, solange der Vertrag klar sagt, wie lange er läuft. Ein unbefristeter Vertrag, den beide Seiten mit derselben Frist und ohne Kündigungsgebühr beenden können, passt zu dieser Idee. Schreib nicht „ohne Vertragsbindung“, wenn es eine Mindestlaufzeit gibt, und vermeide die automatische Verlängerung von Monat zu Monat."},
        ],
        "sources": [
            {"t": "Bürgerliches Gesetzbuch (BGB), § 307 Inhaltskontrolle.", "u": "https://www.gesetze-im-internet.de/bgb/__307.html"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 309 Klauselverbote ohne Wertungsmöglichkeit.", "u": "https://www.gesetze-im-internet.de/bgb/__309.html"},
            {"t": "Richtlinie 93/13/EWG des Rates vom 5. April 1993 über mißbräuchliche Klauseln in Verbraucherverträgen, konsolidierte Fassung. EUR-Lex.", "u": "https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:01993L0013-20220528"},
            {"t": "Bundesgerichtshof, Urteil vom 4. Mai 2016, XII ZR 62/15 (Pressemitteilung Nr. 79/2016).", "u": "https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2016/2016079.html"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 312k: Kündigung von Verbraucherverträgen im elektronischen Geschäftsverkehr.", "u": "https://www.gesetze-im-internet.de/bgb/__312k.html"},
            {"t": "Bundesgerichtshof, Urteil vom 16. Juli 2026, I ZR 200/25 (Kündigungsbutton eines Fitnessstudios).", "u": "https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/I_ZS/2025/I_ZR_200-25.pdf?__blob=publicationFile"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 355 Widerrufsrecht bei Verbraucherverträgen.", "u": "https://www.gesetze-im-internet.de/bgb/__355.html"},
            {"t": "Einkommensteuergesetz (EStG), § 4 (Abs. 3: Einnahmenüberschussrechnung).", "u": "https://www.gesetze-im-internet.de/estg/__4.html"},
        ],
    },
    {
        "fr": "augmenter-ses-tarifs-coach",
        "slug": "preise-erhoehen-personal-trainer",
        "title": "Preise erhöhen als Personal Trainer, ohne Kunden zu verlieren",
        "seo_title": "Personal Trainer: Preise erhöhen, ohne Kunden zu verlieren",
        "description": "Preise erhöhen als Personal Trainer: was jeder Vertrag erlaubt, wie viele Einheiten du verlieren kannst, ohne weniger zu verdienen, und wie du es ankündigst.",
        "body": """
<p>Die kurze Antwort: Willst du deine <strong>Preise als Personal Trainer erhöhen</strong>, fängst du bei neuen Kunden an, informierst die anderen vor dem Stichtag schriftlich und hältst laufende Verträge ein. Niemand kann dir null Abgänge versprechen, und öffentliche Daten zu diesem Risiko unter Trainern habe ich nicht gefunden. Du kannst aber berechnen, wie viele Einheiten du verlieren kannst, ohne weniger zu verdienen. Und prüf vor der Entscheidung die Kleinunternehmergrenze: Sie kann deine Erhöhung auffressen.</p>

<h2>Wie viele Einheiten kannst du verlieren, ohne weniger zu verdienen?</h2>
<p>Dreh die Frage um. Für denselben Umsatz gilt: nötige Einheiten = aktuelle Einheiten × alter Preis ÷ neuer Preis. Hier die Rechnung für 16 Einheiten pro Woche zu 50 €.</p>
<div class="tablewrap"><table>
<caption>Quelle: Beispielrechnung, ohne Marktdaten.</caption>
<thead><tr><th>Neuer Preis</th><th class="n">Erhöhung</th><th class="n">Einheiten für denselben Umsatz</th><th class="n">Spielraum pro Woche</th></tr></thead>
<tbody>
<tr><td>52,50 €</td><td class="n">5 %</td><td class="n">15,2</td><td class="n">0,8 Einheiten</td></tr>
<tr><td>55 €</td><td class="n">10 %</td><td class="n">14,5</td><td class="n">1,5 Einheiten</td></tr>
<tr><td>57,50 €</td><td class="n">15 %</td><td class="n">13,9</td><td class="n">2,1 Einheiten</td></tr>
<tr><td>60 €</td><td class="n">20 %</td><td class="n">13,3</td><td class="n">2,7 Einheiten</td></tr>
</tbody>
</table></div>
<p>Hängen deine Steuern und Beiträge an Umsatz und Gewinn und bleiben deine Fixkosten gleich, bleibt dir beim selben Umsatz derselbe Betrag, für weniger Stunden. Geht dagegen niemand, bringen dir 5 € mehr keine 5 €. Bist du umsatzsteuerpflichtig und sind deine Preise Bruttopreise, stecken darin 19 % Umsatzsteuer: Von 5 € bleiben dir 4,20 € netto, und davon gehen noch Einkommensteuer und Beiträge ab.</p>
<p>Geh von deiner <a href="/coachs/tarif-coach-sportif-independant.html">Preisuntergrenze</a> aus: Sie sagt dir, ob du eine Erhöhung brauchst und wie viel.</p>

<h2>Darfst du die Preise für bestehende Kunden erhöhen?</h2>
<p>Das hängt davon ab, was dein Kunde vereinbart hat.</p>
<ul>
<li><strong>Einzeleinheit:</strong> Es läuft nichts. Der neue Preis gilt für Einheiten, die nach deiner Ankündigung gebucht werden, und dein Kunde muss ihn vor der Buchung kennen.</li>
<li><strong>Bezahltes Paket:</strong> Der Preis steht für alle verbleibenden Einheiten fest. Die Erhöhung gilt erst ab dem nächsten Paket.</li>
<li><strong>Vertrag mit fester Laufzeit:</strong> Behalte dir nicht vor, den Preis allein zu ändern. Die Erhöhung gilt erst nach dem Ende der Laufzeit. Verlängert sich der Vertrag automatisch (per AGB ist das nur auf unbestimmte Zeit zulässig), kündige den neuen Preis sicherheitshalber so früh an, dass dein Kunde noch zum Ende der ersten Laufzeit kündigen kann.</li>
<li><strong>Unbefristeter Vertrag:</strong> Erhöhe den Preis nur, wenn der Vertrag es erlaubt und dein Kunde eine angemessene Frist bekommt, um zu kündigen.</li>
</ul>
<p>Wie viel ist angemessen? Sicherheitshalber mindestens deine Kündigungsfrist plus ein paar Tage zum Überlegen. Die rechtliche Grundlage in Deutschland: Das Verbot von Preiserhöhungen für Leistungen in den ersten vier Monaten nach Vertragsschluss (§ 309 Nr. 1 BGB) gilt ausdrücklich nicht für Dauerschuldverhältnisse wie ein Abo. Eine Preisanpassungsklausel misst sich dort an § 307 BGB, muss also klar und fair sein. Eine Preiserhöhung im laufenden Abo braucht damit eine wirksame Grundlage: eine solche Klausel in deinen AGB oder die Zustimmung deines Kunden.</p>
<p>Das EU-Recht nennt in seiner Beispielliste möglicherweise missbräuchlicher Klauseln solche, mit denen du den Preis erhöhen kannst, ohne dass dein Kunde vom Vertrag zurücktreten darf. Bei einem unbefristeten Vertrag bleibt eine Änderung möglich, wenn du rechtzeitig informierst und dein Kunde frei kündigen kann (Richtlinie 93/13/EWG). Werte Schweigen sicherheitshalber nicht als Zustimmung: Der BGH hat 2021 Bankklauseln für unwirksam erklärt, nach denen das Schweigen des Kunden als Zustimmung galt, auch für Änderungen der Hauptleistung. Das Urteil betrifft nur Banken; ob es sich auf Coaching übertragen lässt, ist offen. Fehlt in deinem Vertrag eine Klausel zur Preisanpassung, bitte deinen Kunden um seine schriftliche Zustimmung. Für die Zukunft <a href="/coachs/packs-abonnement-seance-coach-sportif.html">wählst du ein Format</a>, das die nächste Erhöhung vorbereitet.</p>

<h2>Wie kündigst du deinen Kunden eine Preiserhöhung an?</h2>
<ol>
<li><strong>Fang bei neuen Kunden an.</strong> Du siehst, ob dein Preis hält, ohne die Kunden anzutasten, die schon deine Rechnungen zahlen.</li>
<li><strong>Schreib jedem Kunden.</strong> Stichtag, alter und neuer Preis, was enthalten bleibt, wie man aufhört. Die schriftliche Nachricht ist dein Beleg.</li>
<li><strong>Nenn den echten Grund.</strong> Steigende Kosten, ein voller Kalender, ein überarbeitetes Angebot. Keine falsche Dringlichkeit und keine versprochenen Ergebnisse.</li>
<li><strong>Sprich mit deinen langjährigen Kunden persönlich.</strong> Bestätige es danach schriftlich.</li>
<li><strong>Notiere jeden Abgang und seinen Grund.</strong> So weißt du, ob der Preis das Problem ist oder ob <a href="/coachs/fideliser-clients-coaching-sportif.html">es woanders liegt</a>.</li>
</ol>
<p>Eine Vorlage zum Anpassen, mit den Daten und Beträgen deines Kunden: <em>„Hallo [Vorname], ab dem 1. März kostet eine Einheit 55 € statt 50 €. Einheiten, die du schon bezahlt hast, bleiben beim aktuellen Preis. Wenn du lieber aufhören oder darüber sprechen möchtest, antworte mir bis zum 1. Februar.“</em></p>

<h2>Welche Grenze kann deine Erhöhung auffressen?</h2>
<p>Bevor du den Betrag festlegst, prüf, ob dich der höhere Umsatz über die Kleinunternehmergrenze bringt. Personal Training unterliegt in Deutschland grundsätzlich 19 % Umsatzsteuer; als Kleinunternehmer bist du befreit, wenn dein Umsatz im Vorjahr höchstens 25.000 € betrug und im laufenden Jahr 100.000 € nicht übersteigt (im Gründungsjahr gilt eine Grenze von 25.000 €). Im Beispiel über 44 Wochen bringen 704 Einheiten zu 50 € schon 35.200 €, zu 55 € dann 38.720 €: Beide liegen über 25.000 €, an deinem Status ändert die Erhöhung nichts mehr. Knapp wird es bei kleineren Umsätzen. Mit 11 Einheiten pro Woche, also 484 im Jahr, kommst du zu 50 € auf 24.200 € und zu 55 € auf 26.620 €. Damit bist du im Folgejahr kein Kleinunternehmer mehr, im Gründungsjahr schon ab dem Umsatz, mit dem du die Grenze überschreitest. Dann zahlen deine Kunden entweder 19 % mehr als angekündigt, oder du zahlst die Steuer aus deiner Erhöhung: Von 55 € brutto bleiben dir 46,22 € netto, weniger als die 50 € vorher. Schau dir also deinen Jahresumsatz an, bevor du den Betrag festlegst, und frag deinen Steuerberater.</p>
<p>In Österreich bist du als Kleinunternehmer seit 2025 befreit, solange dein Umsatz 55.000 € brutto im Jahr nicht übersteigt, und eine Überschreitung um bis zu 10 % ist im selben Jahr unschädlich. In der Schweiz wirst du erst ab 100 000 Franken Jahresumsatz mehrwertsteuerpflichtig; der Normalsatz beträgt 8,1 %.</p>
<p>Dieser Leitfaden dient nur der Information und ersetzt keine Beratung durch einen Steuerberater oder einen Anwalt.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Daten dazu, wie viele Kunden nach einer Preiserhöhung gehen, habe ich nicht gefunden: Berechne, wie viele Einheiten du verlieren kannst, ohne weniger zu verdienen.</li>
<li>Ein bezahltes Paket und ein Vertrag mit fester Laufzeit behalten ihren Preis. Ein unbefristeter Vertrag braucht eine klare, faire Klausel oder die Zustimmung deines Kunden, dazu eine angemessene Frist.</li>
<li>Prüf vor jeder Ankündigung deinen Jahresumsatz gegen die Kleinunternehmergrenze von 25.000 €.</li>
</ul>
""",
        "faq": [
            {"q": "Wie kündigt man Kunden eine Preiserhöhung an?", "a": "Schriftlich, an jeden Kunden, vor dem Stichtag. Nenn den alten Preis, den neuen Preis, das Datum, was enthalten bleibt und wie man aufhört. Bereits bezahlte Einheiten bleiben beim vereinbarten Preis."},
            {"q": "Wie lange vorher muss man eine Preiserhöhung ankündigen?", "a": "Eine feste gesetzliche Frist habe ich nicht gefunden. Bei einem unbefristeten Vertrag gibst du deinem Kunden eine angemessene Frist, damit er kündigen kann: mindestens deine Kündigungsfrist plus ein paar Tage. Bei einem Vertrag mit fester Laufzeit gilt der Preis bis zum Ende der Laufzeit."},
            {"q": "Um wie viel sollte ein Personal Trainer seine Preise erhöhen?", "a": "Eine Norm oder offizielle Daten zur Höhe habe ich nicht gefunden. Geh von deiner Preisuntergrenze aus, berechne, wie viele Einheiten du für denselben Umsatz verlieren kannst, und prüf dann, ob dich die Erhöhung über die Kleinunternehmergrenze von 25.000 € bringt."},
        ],
        "sources": [
            {"t": "Bürgerliches Gesetzbuch (BGB), § 309 Klauselverbote ohne Wertungsmöglichkeit.", "u": "https://www.gesetze-im-internet.de/bgb/__309.html"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 307 Inhaltskontrolle.", "u": "https://www.gesetze-im-internet.de/bgb/__307.html"},
            {"t": "Richtlinie 93/13/EWG des Rates vom 5. April 1993 über mißbräuchliche Klauseln in Verbraucherverträgen, konsolidierte Fassung, Anhang Nr. 1 Buchst. l und Nr. 2 Buchst. b. EUR-Lex.", "u": "https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:01993L0013-20220528"},
            {"t": "Bundesgerichtshof, Urteil vom 27. April 2021, XI ZR 26/20 (Pressemitteilung Nr. 88/2021).", "u": "https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2021/2021088.html"},
            {"t": "Umsatzsteuergesetz (UStG), § 12 Steuersätze.", "u": "https://www.gesetze-im-internet.de/ustg_1980/__12.html"},
            {"t": "Umsatzsteuergesetz (UStG), § 19 (Kleinunternehmerregelung).", "u": "https://www.gesetze-im-internet.de/ustg_1980/__19.html"},
            {"t": "Unternehmensserviceportal (Österreich). Kleinunternehmen (Regelung seit 1. Jänner 2025).", "u": "https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html"},
            {"t": "Bundesgesetz über die Mehrwertsteuer (Mehrwertsteuergesetz, MWSTG, Schweiz), Art. 10 und 25. Fedlex.", "u": "https://www.fedlex.admin.ch/eli/cc/2009/615/de"},
        ],
    },
    {
        "fr": "seance-annulee-regles-coach",
        "slug": "absageregeln-personal-training",
        "title": "Absageregeln im Personal Training: Verspätung, No-Show und Fristen",
        "seo_title": "Absageregeln im Personal Training: Ausfallgebühr und Fristen",
        "description": "Absageregeln im Personal Training: welche Regeln du für kurzfristige Absagen, Nichterscheinen, Verspätung und Pakete festlegst und welche Klauseln du meidest.",
        "body": """
<p>Die kurze Antwort: Für deine <strong>Absageregeln im Personal Training</strong> gehst du nicht davon aus, dass eine gesetzliche Frist gilt, weder 24 noch 48 Stunden. Die Regel legst du selbst fest, schriftlich, vor der ersten Einheit: Absagefrist, Verspätung, Nichterscheinen und was passiert, wenn du absagst. Sie hält am ehesten, wenn dein Kunde sie vor Vertragsschluss kannte, wenn sie in beide Richtungen gilt und wenn das, was du behältst, angemessen bleibt.</p>

<h2>Gibt es eine gesetzliche Frist, um eine Einheit abzusagen?</h2>
<p>Eine allgemeingültige habe ich nicht gefunden. Schreib also nie „gesetzliche Absagefrist“ in deine Unterlagen, solange ein Anwalt das nicht bestätigt hat. Die richtige Frist hängt von deinem Geschäft ab: Wie lange brauchst du, um den Termin neu zu vergeben? Ein Trainer, der Hausbesuche im Voraus plant, hat andere Bedürfnisse als ein Trainer im Studio, bei dem Kunden auf einen Termin warten.</p>
<p>Vor allem muss dein Kunde die Regel kennen, bevor er sich bindet. Schreib sie in deine AGB oder deinen Vertrag, lass sie schriftlich akzeptieren und bewahre diesen Nachweis auf. Kommt es zum Streit, willst du ihn vorzeigen können.</p>

<h2>Welche Regeln gehören in deine Absageregeln?</h2>
<p>Hier eine Arbeitsgrundlage, die du an dein Angebot anpasst:</p>
<div class="tablewrap"><table>
<caption>Quelle: Beispiele aus diesem Leitfaden, keine Musterklauseln.</caption>
<thead><tr><th>Situation</th><th>Beispielregel</th><th>Worauf du achtest</th></tr></thead>
<tbody>
<tr><td>Kunde sagt rechtzeitig ab</td><td>Einheit wird kostenlos verschoben</td><td>Welcher Kanal und welcher Zeitstempel zählen</td></tr>
<tr><td>Kunde sagt kurzfristig ab</td><td>Einheit wird berechnet, oder eine begrenzte Zahl an Verschiebungen pro Zeitraum</td><td>Gleiche Regel für alle</td></tr>
<tr><td>Kunde erscheint nicht</td><td>Einheit wird nach einer festgelegten Wartezeit berechnet</td><td>Wartezeit schriftlich festhalten</td></tr>
<tr><td>Kunde kommt zu spät</td><td>Einheit endet pünktlich, Preis unverändert</td><td>Aufwärmen behalten, Umfang kürzen</td></tr>
<tr><td>Du sagst kurzfristig ab</td><td>Verschiebung oder Erstattung nach Wahl des Kunden, mit gleichwertigem Ausgleich</td><td>Dieselbe Verpflichtung eingehen, die du von ihm verlangst</td></tr>
<tr><td>Du kommst zu spät</td><td>Zeit wird nachgeholt oder vom Preis abgezogen</td><td>Dein Kunde entscheidet</td></tr>
<tr><td>Ernster Notfall</td><td>Kostenlose Verschiebung oder Erstattung</td><td>Objektive Kriterien vorher festlegen</td></tr>
</tbody>
</table></div>

<h2>Welche Absageklauseln machen Probleme?</h2>
<p>Gegenüber Verbrauchern kann eine Klausel unwirksam sein, und deine Regel fällt mit ihr. In Deutschland sind Klauseln in deinen AGB, die deine Kunden unangemessen benachteiligen oder unklar formuliert sind, unwirksam (§ 307 BGB). Vier Formulierungen meidest du:</p>
<ul>
<li><strong>„Keine Einheit wird erstattet, aus keinem Grund.“</strong> Sie macht dich angreifbar, vor allem wenn du derjenige bist, der absagt, oder bei höherer Gewalt. Das Geld zu behalten, wenn dein Kunde abspringt, ohne ihm umgekehrt ein gleichwertiges Recht zu geben, ist ebenfalls schwer zu verteidigen.</li>
<li><strong>„Ob ein Grund gilt, entscheidet allein der Trainer.“</strong> Einer Seite die alleinige Macht zu geben, den Vertrag auszulegen, ist eine schwache Grundlage.</li>
<li><strong>Die hohe Strafe.</strong> Eine deutlich unverhältnismäßige Gebühr kann unwirksam sein. Verlang nicht mehr als den Preis der Einheit.</li>
<li><strong>Die Generalklausel zur höheren Gewalt.</strong> Pack nicht jedes Ereignis, das du nicht beeinflussen kannst, unter höhere Gewalt.</li>
</ul>
<p>Eine offizielle deutsche Empfehlung speziell für Coaching-Verträge habe ich nicht gefunden. Den Maßstab setzen die §§ 305 bis 310 BGB: § 307 verlangt klare und ausgewogene Klauseln, und die §§ 308 und 309 zählen Klauseln auf, die verboten sind. Das EU-Recht geht in dieselbe Richtung: Eine nicht ausgehandelte Klausel ist missbräuchlich, wenn sie entgegen dem Gebot von Treu und Glauben zum Nachteil deines Kunden ein erhebliches Missverhältnis der Rechte und Pflichten verursacht. Sie ist dann für ihn unverbindlich, und der übrige Vertrag bleibt bestehen, wenn er ohne sie bestehen kann (Richtlinie 93/13/EWG). Als Beispiel nennt die Richtlinie unter anderem Klauseln, mit denen du nach Belieben kündigen kannst, wenn dein Kunde es nicht kann. Ob eine Klausel hält, entscheidet am Ende ein Gericht im Einzelfall. Prüf deine eigenen Unterlagen an diesem Maßstab.</p>

<h2>Was gilt für Pakete, Anzahlungen und Widerruf?</h2>
<ul>
<li><strong>Pakete.</strong> Halte das Ablaufdatum fest, die Zahl der Verschiebungen und was mit den restlichen Einheiten passiert, wenn du aufhörst zu arbeiten. Den Preis nicht gegebener Einheiten zu behalten, wenn du den Vertrag selbst beendest, ist schwer zu verteidigen. Die Wahl des Formats behandelt unser Leitfaden zu <a href="/coachs/packs-abonnement-seance-coach-sportif.html">Paketen und Monatsabos</a>.</li>
<li><strong>Anzahlungen.</strong> Sag, was die Zahlung ist und was mit ihr passiert, wenn einer von euch abspringt.</li>
<li><strong>Widerruf des Vertrags.</strong> Schließt du online oder außerhalb deiner Geschäftsräume einen Vertrag mit Privatkunden, können sie ihn 14 Tage lang ab Vertragsschluss widerrufen, ohne Gründe zu nennen. Außerhalb deiner Geschäftsräume heißt nach den Leitlinien der EU-Kommission auch: bei deinem Kunden zu Hause, selbst wenn er den Besuch gewünscht hat. Deine Absageregel ersetzt dieses Recht nicht. Will dein Kunde früher starten, muss er das ausdrücklich verlangen: Halte das schriftlich fest, bei einem Vertrag außerhalb deiner Geschäftsräume auf einem dauerhaften Datenträger. Widerruft er danach, schuldet er Wertersatz für das bereits Geleistete, wenn du ihn korrekt über sein Widerrufsrecht informiert hast. In der Schweiz gibt es für online abgeschlossene Verträge kein allgemeines Widerrufsrecht.</li>
</ul>

<h2>Wie setzt du Absageregeln durch, ohne die Beziehung zu belasten?</h2>
<p>Ein paar Gewohnheiten helfen, damit deine Regel greift:</p>
<ul>
<li>Wiederhole sie in der ersten Einheit mündlich, in einem Satz.</li>
<li>Schick am Vortag eine Erinnerung.</li>
<li>Halte einen einzigen Kanal für Absagen bereit, mit Zeitstempel.</li>
<li>Begrenze Ausnahmen, zum Beispiel auf eine außerordentliche Verschiebung pro Quartal.</li>
<li>Zieh die Einheit sofort ab, mit einer neutralen Nachricht.</li>
</ul>
<p>Wiederholte Absagen können auch etwas anderes bedeuten: ein Termin, der nicht mehr passt, ein Plan, der nicht mehr motiviert. Frag, was sich verändert hat. Manchmal ist es das erste Zeichen für einen <a href="/coachs/fideliser-clients-coaching-sportif.html">Kunden, der dir entgleitet</a>.</p>
<p>Dieser Leitfaden dient nur der Information und ersetzt keine Beratung durch einen Anwalt.</p>

<h2>Das Wichtigste in Kürze</h2>
<ul>
<li>Behandle keine Absagefrist als gesetzliche Regel: Deine eigene Regel, schriftlich und vor der ersten Einheit akzeptiert, ist die Grundlage, und ein Gericht kann sie trotzdem prüfen.</li>
<li>Lass deine Regeln in beide Richtungen gleich gelten, auch wenn du absagst, und halte jede Gebühr angemessen.</li>
<li>Eine Einheit absagen und einen Vertrag widerrufen sind zwei verschiedene Themen: Das Widerrufsrecht von 14 Tagen bleibt bestehen.</li>
</ul>
""",
        "faq": [
            {"q": "Darf ein Personal Trainer eine abgesagte Einheit berechnen?", "a": "Wahrscheinlich ja, wenn die Regel vor Vertragsschluss mitgeteilt und akzeptiert wurde, angemessen bleibt und in beide Richtungen gilt. Ein Gericht würde jeden Fall einzeln prüfen. Eine Klausel, die jede Erstattung aus jedem Grund verweigert, kann nach § 307 BGB unwirksam sein, vor allem wenn der Trainer selbst absagt oder bei höherer Gewalt."},
            {"q": "Welche Absagefrist sollte ein Personal Trainer festlegen?", "a": "Eine gesetzlich festgelegte Frist habe ich nicht gefunden. Wähl eine Frist danach, wie lange du brauchst, um den Termin neu zu vergeben, schreib sie in deine AGB oder deinen Vertrag und wende sie bei allen Kunden an. Stell sie nie als gesetzliche Frist dar."},
            {"q": "Was tun, wenn der Trainer selbst eine Einheit absagt?", "a": "Biete Verschiebung oder Erstattung nach Wahl des Kunden an und halte das vorher schriftlich fest. Berechnen deine Bedingungen eine kurzfristige Absage des Kunden, sieh einen gleichwertigen Ausgleich vor, wenn du kurzfristig absagst. Gleiche Regeln in beide Richtungen senken das Risiko einer unwirksamen Klausel."},
        ],
        "sources": [
            {"t": "Bürgerliches Gesetzbuch (BGB), § 307 Inhaltskontrolle.", "u": "https://www.gesetze-im-internet.de/bgb/__307.html"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 309 Klauselverbote ohne Wertungsmöglichkeit.", "u": "https://www.gesetze-im-internet.de/bgb/__309.html"},
            {"t": "Richtlinie 93/13/EWG des Rates vom 5. April 1993 über mißbräuchliche Klauseln in Verbraucherverträgen, konsolidierte Fassung, Art. 3 und 6 und Anhang. EUR-Lex.", "u": "https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:01993L0013-20220528"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 355 Widerrufsrecht bei Verbraucherverträgen.", "u": "https://www.gesetze-im-internet.de/bgb/__355.html"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 356 (Widerrufsrecht bei Fernabsatzverträgen und Verträgen außerhalb von Geschäftsräumen).", "u": "https://www.gesetze-im-internet.de/bgb/__356.html"},
            {"t": "Bürgerliches Gesetzbuch (BGB), § 357a (Wertersatz nach Widerruf von Fernabsatzverträgen und Verträgen außerhalb von Geschäftsräumen).", "u": "https://www.gesetze-im-internet.de/bgb/__357a.html"},
            {"t": "Bekanntmachung der Kommission: Leitlinien zur Auslegung und Anwendung der Richtlinie 2011/83/EU des Europäischen Parlaments und des Rates über die Rechte der Verbraucher (2021/C 525/01). EUR-Lex.", "u": "https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:52021XC1229(04)"},
            {"t": "KMU-Portal des Bundes (Schweiz). What is a cancellation right? (auf Englisch).", "u": "https://www.kmu.admin.ch/en/what-is-a-cancellation-right"},
        ],
    },
]
