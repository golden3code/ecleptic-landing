# Guides pour coachs en espagnol, allemand, italien, néerlandais et portugais : consigne des rédacteurs

Le site ecleptic.health publie 28 guides pour coachs sportifs indépendants en anglais
(`tools/en/coachs/batch_1.py` à `batch_4.py`), adaptés des guides français. Tu écris la version
d'un lot dans une langue. Ce n'est pas une traduction : c'est le guide qu'un auteur du pays aurait
écrit pour un coach de son pays, avec les mêmes méthodes, les mêmes études et les mêmes
chiffres, et le droit du pays à la place des phrases générales de l'anglais. Le but : qu'un coach
qui tape sa question sur Google dans sa langue tombe sur ce guide et le trouve juste.

## 1. Le lecteur
| Langue | Lecteur | Registre | Pays dont on donne les règles |
|---|---|---|---|
| es | entrenador personal autónomo en Espagne | « tú », jamais « usted » ni « vosotros » ; espagnol d'Espagne (móvil, ordenador) | Espagne (communautés autonomes) |
| de | selbstständiger Personal Trainer | « du », minuscule (du, dein, dir) | Allemagne ; Autriche et Suisse seulement là où la fiche donne une différence importante |
| it | personal trainer indipendente | « tu » | Italie |
| nl | zelfstandig personal trainer (zzp'er) | « je / jij », jamais « u » | Pays-Bas ; Belgique seulement là où la fiche donne une différence importante |
| pt | personal trainer autônomo | portugais du BRÉSIL, « você » ; jamais « tu, teu, tua, contigo » | Brésil ET Portugal (le texte est lu dans les deux) |

## 2. Ce que tu gardes de l'anglais
- La structure : mêmes h2 (reformulés en vraies requêtes de la langue), mêmes listes, mêmes
  tableaux (même balisage `<div class="tablewrap"><table><caption>…`, même nombre de lignes,
  légende traduite), même ordre.
- Les méthodes, protocoles, études, chiffres d'études, exemples de calcul. Recalcule chaque
  chiffre dérivé si tu changes une donnée d'exemple (voir § 5).
- Les règles de Google et de Meta (elles valent partout).
- Les liens internes : EXACTEMENT ceux de l'anglais, avec leurs chemins français
  (`/coachs/<slug-fr>.html`, `/articles/…`, `/methode/…`). Le générateur les réécrit vers la
  langue, ou les retire en gardant le texte si la page n'existe pas dans la langue. N'en ajoute
  aucun, aucun lien externe dans le corps.
- Les garde-fous de santé (orienter vers un médecin, ne pas interpréter, arrêter la séance).
- La phrase de prudence finale (« This guide is general information… »), traduite.
- En cas de doute sur le sens, lis le guide français d'origine (`tools/coachs/batch_*.py`,
  même slug que la clé `fr`).

## 3. Ce que tu adaptes au pays (le cœur du travail)
Les fiches de faits vérifiés sont la SEULE source de droit, de taux, de seuils et
d'organismes : `tools/intl/_faits-ue.md` (droit de l'UE, 5 langues) et `tools/intl/_faits-<langue>.md`.
Chaque fait a une « Phrase prête » : reprends-la ou adapte-la sans changer son sens.
- « Check the rules where you work: qualification, insurance and consumer law vary by country » :
  remplace-la par ce qui est vrai dans le pays pour CE guide (qualification pour un guide sur la
  première séance, droit de la consommation pour un guide sur les packs, etc.), en une ou deux
  phrases tirées des fiches. Une fois par guide, comme l'anglais. Si la fiche n'a rien de vérifié
  sur ce point, garde une phrase générale vraie, sans inventer.
- « If you work in the EU or the UK, health data is specially protected » : la version du pays
  (RGPD art. 9 et autorité nationale ; au Brésil, LGPD et ANPD).
- Numéros d'urgence : 112 dans l'UE ; en portugais, SAMU 192 au Brésil et 112 au Portugal.
  Jamais 911, 999, 988 ni Samaritans.
- Références françaises de l'anglais (Commission française des clauses abusives, « French
  consumer rules », CNIL) : remplace-les par la règle de l'UE ou du pays tirée des fiches. Une
  règle française n'est jamais présentée comme applicable au lecteur.
- Taxes : « sales tax », « VAT », « tax threshold », « tax office » deviennent les noms du pays
  (IVA, Umsatzsteuer et Kleinunternehmerregelung, IVA et regime forfettario, btw et KOR, ISS et
  IVA…), avec les seuils des fiches s'ils sont vérifiés.
- Qualification : « a recognized certification » devient le vocabulaire du pays (titre exigé par
  région en Espagne, inscription au CREF au Brésil, etc.), selon les fiches.
- Interdit : toute loi, tout taux, seuil, organisme, montant ou chiffre qui n'est ni dans
  l'anglais ni dans une fiche. Un fait marqué « NON VÉRIFIÉ » ne s'écrit pas. Un fait qui varie
  (région, statut) se dit comme tel.
- Chaque fait de fiche que tu utilises ajoute sa source officielle à `sources` (même URL que dans
  la fiche, titre dans la langue du document).

### Faits à regarder en premier, guide par guide
Codes des fiches : F = fiche du pays (BR-F, PT-F, AT-F, CH-F, BE-F selon la langue), U = fiche UE.
| Clé `fr` | Faits |
|---|---|
| fiche-client-coach-sportif | F3, U1, U2, U3 (au Brésil BR-F4), U6, F1 |
| bilan-forme-premier-rendez-vous | F15, F1, F2 |
| questionnaire-sante-avant-le-sport-client | F18, F3, U2, F1, F2 |
| tests-physiques-nouveau-client | F15 |
| creer-programme-personnalise-client | F1 (en allemand : AT-F1, ce qu'un entraîneur sans diplôme ne peut pas faire), F2 |
| fideliser-clients-coaching-sportif | F8, F10, U12 |
| bilan-mensuel-client-coaching | F3 |
| lire-etat-de-forme-client | F3 |
| trouver-des-clients-coach-sportif | F1 (au Brésil, numéro CREF sur les annonces), F10, U12 |
| coach-sportif-google-fiche-etablissement | F11, U11 |
| instagram-coach-sportif | F3, F12, F11 |
| seance-essai-coach-sportif | F2, F3, U2, F6, U8 |
| avis-recommandations-coach-sportif | F11, U11, F12 |
| coaching-sportif-en-entreprise | F14, F17, F1 |
| tarif-coach-sportif-independant | F13, F14, U14 |
| coaching-sportif-en-ligne-comment-faire | F1, F2, F6, U8, U9, F3, U2, F10, U12 |
| coaching-en-visio | F15, F12, F1 |
| suivre-client-a-distance | F1, F3 |
| tarif-coaching-en-ligne | F13, F14 |
| packs-abonnement-seance-coach-sportif | F7, U10, F8, F6, F14 |
| augmenter-ses-tarifs-coach | F9, U10, F13, U14 |
| seance-annulee-regles-coach | F7, U10, F6, U8 |
| logiciel-coach-sportif-comment-choisir | U4, U5, F3, F13 |
| application-coach-sportif-gratuite-ou-payante | U5, F3 |
| excel-whatsapp-logiciel-coaching | F3, U7, F16 |
| application-suivi-client-coach | F3 |
| changer-logiciel-coaching | U5, F16 |
| verifier-logiciel-coaching-avant-de-choisir | U5, F3 |

## 4. Quand ne pas écrire un guide
Si, une fois adapté, un guide n'apporte presque rien au lecteur de la langue, ne l'écris pas et
dis-le dans ton rapport. C'est un bon résultat. Ne raccourcis pas un guide pour gagner du temps.

## 5. Chiffres et monnaie
- Décimales et milliers : 1,6 ; 1.863 (es, de, it, nl, pt). Pourcentages : « 25,8 % » en es et
  de, « 25,8% » en it, nl et pt.
- Monnaie : es « 60 € », de « 60 € », it « 60 € », nl « € 60 ». Les montants d'exemple de
  l'anglais (déjà en euros, présentés comme inventés) restent tels quels en es, de, it et nl.
- pt : les exemples passent en reais (« R$ 120 »), avec des montants plausibles au Brésil, et TOUS
  les chiffres qui en découlent sont recalculés exactement (vérifie chaque division). Dis qu'ils
  sont inventés, comme l'anglais. Le taux d'exemple de cotisations reste un exemple.
- Le « taux d'exemple de 25,8 % » des guides de tarifs reste un exemple inventé ; ajoute, si la
  fiche le permet, une phrase sur la façon dont le pays calcule vraiment (forfait mensuel, impôt
  sur le bénéfice…).

## 6. Structures fixes
| | es | de | it | nl | pt |
|---|---|---|---|---|---|
| Début du corps | `<p>La respuesta corta: …` | `<p>Die kurze Antwort: …` | `<p>La risposta breve: …` | `<p>Het korte antwoord: …` | `<p>A resposta curta: …` |
| Section finale (h2, 3 puces) | Puntos clave | Das Wichtigste in Kürze | In sintesi | In het kort | Em resumo |

- Titre (h1) : vraie requête de la langue ; garde la forme « Préfixe: suite » quand l'anglais l'a
  (elle déclenche l'animation du titre). Plus de 60 caractères : ajoute `seo_title` (60 au plus).
- Description : 140 à 160 caractères, avec la requête principale.
- FAQ : 3 questions = vraies requêtes de la langue, réponses autonomes de 2 ou 3 phrases.
- Le mot entre `<strong>` de la première phrase est la requête principale.

## 7. Glossaire (même mot dans tous les lots d'une langue)
- es : entrenador personal ; cliente ; sesión ; plan de entrenamiento ; ficha de cliente ;
  cuestionario de salud ; valoración inicial ; bono de sesiones ; cuota mensual ; sesión de
  prueba ; reseñas ; recomendaciones ; seguro de responsabilidad civil ; autónomo ; IVA ; RGPD ;
  datos de salud ; entrenamiento online ; videollamada ; software para entrenadores ; app.
- de : Personal Trainer ; Kunde, Kundin, Kunden ; Einheit, Trainingseinheit ; Trainingsplan ;
  Kundenakte ; Gesundheitsfragebogen ; Eingangscheck ; 10er-Karte, Paket ; Monatsabo ;
  Probetraining ; Bewertungen ; Empfehlungen ; Berufshaftpflicht ; Selbstständige ;
  Umsatzsteuer ; DSGVO ; Gesundheitsdaten ; Online-Coaching ; Videocall ; Coaching-Software ; App.
- it : personal trainer ; cliente ; seduta, allenamento ; scheda di allenamento ; scheda cliente ;
  questionario sulla salute, anamnesi ; valutazione iniziale ; pacchetto di sedute ; abbonamento
  mensile ; lezione di prova ; recensioni ; passaparola ; assicurazione di responsabilità civile ;
  partita IVA ; GDPR ; dati sulla salute ; coaching online ; videochiamata ; software per personal
  trainer ; app.
- nl : personal trainer ; klant ; sessie, training ; trainingsschema ; klantdossier ;
  gezondheidsvragenlijst ; intake ; strippenkaart, pakket ; maandabonnement ; proeftraining ;
  reviews ; aanbevelingen ; beroepsaansprakelijkheidsverzekering ; zzp'er ; btw ; AVG ;
  gezondheidsgegevens ; online coaching ; videogesprek ; coachingsoftware ; app.
- pt : personal trainer ; aluno (cliente pour le commercial et le contrat) ; treino, aula ;
  planilha de treino ; ficha do aluno ; anamnese, questionário de saúde ; avaliação física ; pacote
  de aulas ; plano mensal, mensalidade ; aula experimental ; avaliações ; indicações ; seguro de
  responsabilidade civil ; autônomo ; LGPD (Brésil), RGPD (Portugal) ; dados de saúde ;
  consultoria online (le mot brésilien du coaching à distance) ; videochamada ; academia ;
  celular ; tela ; app (masculin) ; software para personal.

## 8. Style
Phrases courtes, voix du fondateur, sans prétendre être coach. Jamais le mot « Ecleptic » dans le
corps, le titre ou la description. Pas de tiret cadratin. Pas de formule « ce n'est pas X, c'est
Y », pas de phrase creuse, pas d'anecdote ni de témoignage inventé. Écriture neutre quand c'est
facile (« quien entrena », « wer trainiert »), sans alourdir.

## 9. Format du fichier
```python
# -*- coding: utf-8 -*-
ENTRIES = [
    {
        "fr": "tests-physiques-nouveau-client",      # clé de l'anglais, inchangée
        "slug": "tests-fisicos-cliente-nuevo",        # ASCII minuscule, tirets, 3 à 7 mots-clés de la langue
        "title": "…",
        "seo_title": "…",                            # seulement si le titre dépasse 60 caractères
        "description": "…",                          # 140 à 160 caractères
        "body": """…""",
        "faq": [{"q": "…", "a": "…"}, {"q": "…", "a": "…"}, {"q": "…", "a": "…"}],
        "sources": [{"t": "…", "u": "https://…"}, …], # au moins 2 : celles de l'anglais qui restent + celles des fiches utilisées
    },
]
```
Écris le fichier avec l'outil Write (pas de heredoc shell) : guillemets typographiques de la
langue dans le texte (« » en es, it et pt ; „ “ en de ; ‘ ’ ou " " en nl), jamais de `"""` dans
un corps.

## 10. Contrôle jusqu'à zéro problème
```bash
cd /Users/augustephilypriou/Desktop/Auros/landing-guides-intl
python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" tools/<langue>/coachs/batch_<n>.py
python3 tools/check_intl.py tools/<langue>/coachs/batch_<n>.py
```
Les « ⚠ » ne bloquent pas : relis chacun et corrige ce qui doit l'être (la France citée comme
règle, un vouvoiement…).

## 11. Ton périmètre
Tu crées UNIQUEMENT `tools/<langue>/coachs/batch_<n>.py`. Pas de build, pas de git, aucun autre
fichier modifié. Fichiers de travail éventuels dans le scratchpad.

## 12. Rapport (10 lignes au plus)
Guides écrits avec leur slug ; guides non écrits et pourquoi ; par guide, l'adaptation au pays en
quelques mots ; doutes ; sortie du contrôle.
