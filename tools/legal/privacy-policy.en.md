<!-- version-fr: 2026-10-30 -->
<!-- English translation of ~/Desktop/Auros/legal/politique-de-confidentialite.md. Update it, and the date above, every time the French policy changes; tools/build_privacy.py refuses to build otherwise. -->
# Privacy policy — Ecleptic

**Last updated: 30 October 2026**

This policy describes how the **Ecleptic** application (the "Application") processes its users' personal data, in accordance with Regulation (EU) 2016/679 ("GDPR") and the amended French Data Protection Act no. 78-17 of 6 January 1978 ("loi Informatique et Libertés").

## Article 1 — Data controller

- **Data controller**: Auguste Phily-Priou, **sole trader (Entrepreneur individuel, EI)**
- **Address**: 10 Rue du Commerce, 86400 Civray, France
- **SIREN**: registration in progress — it will be added here as soon as it is obtained.
- **Privacy contact**: contact@ecleptic.app
- **Data protection officer (DPO)**: not appointed to date.

## Article 2 — Data collected

### 2.1. Account and identification data

When the account is created and during the welcome questionnaire: email address (or the identifier provided by "Sign in with Apple" / Google, on iPhone as on Android), first name or nickname, date of birth, sex, height, goals and tracking preferences.

### 2.2. ⚕️ Health and wellness data (special category — art. 9 GDPR)

The Application processes data that belongs to the **special categories of data** within the meaning of article 9 GDPR (data concerning health). It is clearly identified and processed with enhanced safeguards:

- physical activity data (workouts, heart rate, estimated VO2 max, energy expenditure);
- sleep data (duration, stages, awakenings, how you felt);
- nutrition data (meals, meal photos, estimated intake, photos of nutrition labels, food entries and corrections — see 2.6);
- body data (weight, measurements, estimated body composition, body scan photos);
- derived indicators (scores, "biological age" estimate, recommendations);
- data imported from the system's health services (Apple Health on iPhone, Health Connect on Android) or from connected devices, with the user's consent (see 2.7);
- on Android, during a workout and at the user's request: heart rate and beat-to-beat intervals read live from a **Bluetooth** heart rate sensor (chest strap, watch in broadcast mode). Bluetooth is only used to connect to the chosen sensor: it is never used to locate the user;
- conversations with Éos, the Application's AI assistant (free-text messages, which may contain health information);
- approximate location (for weather and altitude), precise location during a GPS-tracked workout and, at the end of a session recorded live, the location at that moment to recognise the place of the session (see 2.8), if the user allows it.

### 2.3. Payment data

Subscriptions are purchased in-app through the App Store (iPhone) or Google Play (Android): payment is handled by Apple or by Google, and the publisher **never** receives card details. Through its subscription management provider (RevenueCat), the publisher only receives information about the subscription status (plan purchased, start and expiry dates, renewal status).

### 2.4. Technical and usage data

Technical account identifier, sign-in timestamps and server-side technical logs (security, usage quotas for AI features, errors and processing times). **Usage statistics**: the Application records usage events (screen shown, onboarding step completed, feature used, error encountered), attached to a **random installation identifier**, unrelated to the account, renewed at every sign-out and at least every 13 months. These events **never** contain health data (no weight, heart rate, calories, score, biological age or questionnaire answer) or any text you typed (food search, message to Éos, meal title). They only carry categories (for example "meal logged by photo") and technical information (app and system version — iOS or Android —, platform, device model, language, device region). No IP address is stored. No advertising tool is built in.

### 2.5. Mandatory or optional data

The data needed to create the account and provide the service is marked as mandatory; without it, the service concerned cannot be provided. Other data (in particular most health data) is **optional**: the user chooses which tracking features to turn on.

### 2.6. Contributions to the food database

When a food cannot be found or an entry looks wrong, the user may, if they wish:

- **photograph a product's nutrition label**: the photo is read by an AI model (see article 4), which extracts the values; the user checks and corrects them before saving;
- **create a food entry** from these values (name, brand, barcode, nutritional values, serving);
- **correct** an existing entry or **report an error** (reason and optional note);
- **correct the match** of a food recognised when a meal is analysed.

A created entry stays **private**: it only serves its author. The publisher only reviews it if the user **submits it for review**; the label photo is then kept only for that check. A correction or an entry approved at review is then published in the shared food database **with no link to the account** (no name, nickname or identifier): only the product's nutritional values are published, never the photo. Reports are only used for review and are never published.

These contributions relate to what the user eats: they receive the same treatment as nutrition data (2.2).

### 2.7. Data read from Health Connect (Android) and Apple Health (iPhone) — limited use

**What is read**, only for the types the user allows on the Health Connect (or Apple Health) screen: sleep and its stages; workouts (type, duration, distance, calories); heart rate, resting heart rate, heart rate variability; VO2 max; oxygen saturation; respiratory rate; skin temperature (on Android, the deviation from the baseline); active energy and resting energy; steps and distance; running, cycling or rowing power, cadence and speed; periods. On Android, the Application also asks for access to **history** (without it, Health Connect limits reading to the last 30 days) and **background** reading (nights and vitals updated without opening the Application).

**What is written**: only the period dates entered in the Application, if the user has turned on cycle tracking.

**Limited use.** Data read from Health Connect or Apple Health:

- is used **only** for the features visible in the Application: history of nights and workouts, vitals, Readiness Score, biological age, recovery, calorie targets, cycle tracking, the Lab, Éos (AI assistant) and, if the user turns it on, the Society (2.9), for the sports data they choose to share only;
- is **never sold**, nor transferred to advertising platforms, data brokers or information resellers;
- is **never used for advertising**, personalised or not;
- is never used to assess creditworthiness or for lending, nor with a product or service that may qualify as a medical device, nor in any processing of protected health information within the meaning of the US HIPAA law;
- is only transferred to a third party with the user's **explicit consent**, for security purposes, to comply with the law, or as part of a merger or acquisition the user would be informed of. The technical providers in article 4 process it on the publisher's behalf, with no right to use it for themselves. In particular, when the user requests a report or asks **Éos** (the AI assistant) a question, a summary of their measurements, without name, email or identifier, is sent to the AI providers in article 4 (Google, Anthropic): this is stated on the screen shown before the Health Connect permission;
- is **read by no human**, except with the user's explicit consent (for example to handle a support request they send), for security purposes, to comply with the law, or in aggregated and anonymous form for internal operations.

**Withdrawal.** The user can withdraw the Application's access at any time in Health Connect (or in Apple Health): reading stops immediately. Data already imported stays in their Account until they delete it or delete their Account (article 6); they can also ask for it to be erased through the contact in article 1.

### 2.8. Origin, place and zones of workouts

This information is first of all for the user themselves. It is shown to nobody else as long as they have not turned on the Society (2.9).

- **Origin** of a workout imported from Apple Health or Health Connect: the application that recorded it (for example Strava, Garmin Connect, Nike Run Club), the device (watch or phone) and whether it was entered by hand. This information avoids duplicates and sets a **level of proof** (declared, phone, watch).
- **Place** of the workout (gym, pool, stadium, club…), recognised from the end-of-session location, a check-in or the place's QR code. The location is sent to the server for this search, then it is **not kept**: only the recognised place is.
- **Zones** crossed by an outdoor workout: municipality, district or large public space (for example "Quais de Seine, rive gauche"), with the kilometres and time spent in each. The calculation is done **on the phone**: the GPS track does not leave the device for this calculation.
- **Efforts**: best performances per session (estimated 1RM per exercise, load per machine, best running and swimming times), calculated from workouts.
- **Strava archive**, if the user imports the file they downloaded themselves from Strava: the file is read on the phone. Only workout summaries (sport, date, duration, distance, average and maximum heart rate, calories, elevation) are saved, never tracks, photos, comments or followers. These workouts stay "declared": they do not enter any board.

### 2.9. The Society (social network)

The **Society** is the Application's social space. It is **optional** and **off by default**: nothing is shared with other users until the user has turned it on themselves. Once it is on, each type of data has its own setting (Settings › Social network): "No one", "Partners" or "Everyone", the latter meaning Society members, never the public on the Internet.

- **Profile**: nickname, generated avatar (an initial and a colour), visibility settings, anonymous mode, age group (adult, minor or unknown) calculated from the date of birth, status (Legend, Founder, league division, month of arrival), featured specialities and records, figures for the year and the last 4 weeks.
- **Profile photo** (optional): cropped to a 512-pixel square and compressed on the phone, stored in a private space with no public address. Visible to partners by default.
- **Partners and feed**: partner code and QR code, requests, partnerships, reactions. In the feed and on the profile, a workout shows the sport, the day (without the time), the duration, the distance, the place or zone if places are visible, records and reactions. The "Don't show this session on my public profile" box removes it from the profile and the feed; it still counts in challenges, the league and boards, which only show totals.
- **Challenges**: duels, Expeditions (groups of 3 to 6) and public challenges, including the Défi de l'Optimisateur: participation, progress and result. Joining a public challenge shows the nickname on its board, except in anonymous mode.
- **Place and spot boards**, place by place and on agreement when entering: values, rank and month of each record, never the time, the day or the session. Crowns, Founders, frozen monthly seasons and the hall of fame derive from them. Some boards are split by category (women, men, all), based on the sex entered in the profile.
- **Witnesses**: an adult partner present at the same place can confirm a performance; each then sees the other's request.
- **Proof video** (optional): 15 seconds at most, chosen by the user from their photo library, stored in a private space. Only the author and the place's reviewers see it (Ecleptic team, approved manager, Founders of the place who are still members).
- **Weekly league**, on sign-up and for adults: effort points, visible to the other members of the cohort of 30.
- **City Cup**: monthly ranking of cities and places, in totals only, with no member's name. A member's active days at their places contribute to it.
- **Racket**: declared matches (sport, opponent, score, optional place), confirmed by the opponent within 72 hours, and a calculated Elo rating.
- **Weight class**: the month's class (IPF classes), calculated from the weight on the 1st of the month. Only the class is kept and shared, never the weight, and it is visible to no one by default.
- **Suggestions**: a missing place (name, type, city and location taken on site) or a spot (name, sports, 40-metre corridor around a route shortened by its first and last 500 metres and simplified on the phone). A suggestion stays linked to the account and visible to the team. Once accepted, the place or spot is public, with no link to its author.
- **Gym screen**: on a separate agreement, unticked by default, given place by place and reserved for adults, the nickname and the month's active days may appear on a gym's screen, visible to anyone present, with no photo or time, and never in anonymous mode.
- **Place managers**: management request (account, place, date, decision), verified by the Ecleptic team.
- **"Your year" review**: calculated for the user alone; they choose whether or not to share its card.
- **Society safety**: reports sent, blocked accounts, moderation decisions concerning them and their reasons, and anti-abuse counters (number of actions per day).

**What is never shown to other users**: the GPS track, real-time location, heart rate, exact weight, exact age, sleep, nutrition and body composition data.

**Turning it off.** The user can turn off the Society at any time (Settings › Social network): what they shared immediately stops being visible to other members. Their social data stays in their Account in case they turn the Society back on; they can ask for it to be erased through the contact in article 1, or delete their Account. Leaving a board removes their lines at once, seasons included.

### 2.10. Push notifications

If the user has turned on the Society and allowed notifications on their phone, the Application saves the device's **notification token** (a technical identifier provided by Apple or Google), the platform, the time zone, the language and their notification settings. The server then prepares the notifications that originate with another member (reaction, partnership request, challenge invitation, witness, video to review, match to confirm, crown taken back, place or spot opened): 3 per day at most, delayed between 10 pm and 8 am. They contain the other member's nickname or the place's name and the nature of the event, never a health figure. The token is removed at sign-out and when the user turns off the Society. The "Social network (Society)" switch in Settings › Notifications turns them off at any time.

## Article 3 — Purposes and legal bases

| Purpose | Data concerned | Legal basis (art. 6 GDPR) |
|---|---|---|
| Creating and managing the account, providing the Services | Account data | Performance of the contract (art. 6.1.b) |
| Health/wellness tracking features, personalised calculations and recommendations | Health data (2.2) | **Explicit consent** (art. 6.1.a and **art. 9.2.a**) |
| Label reading, private entries, corrections and reports; publisher review of the contributions the user submits | Contributions (2.6) | **Explicit consent** (art. 6.1.a and **art. 9.2.a**), given by the act of photographing, saving or submitting for review |
| Publication in the shared food database of approved values | A product's nutritional values, with no link to the account | Legitimate interest (6.1.f — reliability of the food database); licence in article 10.5 of the Terms of Use |
| Origin, level of proof, removing duplicate workouts | Origin (2.8) | Performance of the contract (6.1.b); explicit consent to health data already collected (art. 9.2.a) |
| Place and zones of workouts | Place, zones (2.8) | **Explicit consent** (art. 9.2.a), collected with location |
| Efforts, excluding implausible performances from rankings | Efforts (2.8) | Performance of the contract (6.1.b); legitimate interest (6.1.f — fairness of rankings) |
| Sharing in the Society: partners, feed, challenges, boards, league, City Cup, racket | Society data (2.9) | **Explicit consent** (art. 6.1.a and **art. 9.2.a**), given when turning it on, set type of data by type of data and completed by an agreement when entering each board; withdrawable at any time |
| Profile photo, proof video, suggestions of places and spots | Photo, video, location, route (2.9) | Consent (6.1.a), given by the act of sending |
| Gym screen | Nickname, active days of the month | Separate **consent** (6.1.a), place by place, withdrawable at any time |
| Push notifications | Notification token (2.10) | Consent (6.1.a), given through the system permission; withdrawal in Settings › Notifications |
| Society safety: nickname filter, reports, blocks, reasoned decisions | Nickname, reports, decisions (2.9) | Legal obligation (6.1.c — Digital Services Act, DSA, art. 16 and 17); legitimate interest (6.1.f) |
| Subscription management and billing | Account, payment | Performance of the contract (6.1.b) and legal obligation (6.1.c — accounting) |
| Security, fraud prevention, logs | Technical data | Legitimate interest (6.1.f — securing the service) |
| Audience measurement and product improvement | Usage events (2.4), attached to a random installation identifier, with no health data or content | Legitimate interest (6.1.f — knowing which features are used and where people drop off, to improve the Application); objection at any time in Settings › Privacy (article 7) |
| Service communications (transactional emails, alerts) | Email, account | Performance of the contract (6.1.b) |
| Marketing / newsletter | Email | Consent (6.1.a), withdrawable at any time |
| Responding to requests to exercise rights and legal obligations | Depending on the request | Legal obligation (6.1.c) |

### Collecting explicit consent for health data

On first use of the tracking features, the Application collects **explicit, specific and informed consent** (dedicated screen, separate positive action, clear information about the processing). The user can **withdraw their consent at any time** from the Application's Settings (Privacy section), free of charge and without affecting the lawfulness of prior processing; withdrawal stops the processing concerned and, depending on the user's choice, deletes the related data.

## Article 4 — Recipients and processors

The data is accessible to the data controller and, within the limits of their tasks, to the following processors:

| Provider | Role | Location |
|---|---|---|
| Supabase, Inc. | Database hosting, authentication, photo storage, server-side processing | European Union (Ireland) |
| Google LLC (Gemini models) | AI processing: meal analysis, nutrition label reading, Éos (AI assistant) reports and conversations | United States |
| Anthropic, PBC (Claude models) | AI processing: photo analysis (meals, body composition), Éos reports | United States |
| RevenueCat, Inc. | Subscription status management (no card data) | United States |
| Apple Inc. | Distribution of the Application on iPhone, collection of App Store in-app purchases | United States / Ireland |
| Google (Google Play) | Distribution of the Application on Android, collection of in-app purchases (Google Play Billing) | United States / Ireland |
| Google LLC (sign in with Google) | Sign-in with a Google account, at the user's request: receives the sign-in request, never health data | United States |
| Google LLC (Google Maps SDK) | Displaying the Application's maps, on Android and on the iPhone versions that use it: receives the technical information needed to load map tiles (IP address, area displayed), with no account identifier or health data | United States |
| Apple Inc. (Apple Push Notification service) | Delivering push notifications on iPhone: receives the device token and the text of the notification (2.10), with no health data | United States / Ireland |
| Google LLC (Firebase Cloud Messaging) | Delivering push notifications on Android: receives the device token and the text of the notification (2.10), with no health data | United States |
| Open-Meteo | Weather data from an approximate location (no identifier sent) | European Union |
| Google LLC (Google Maps Platform) | Recognising the gym on versions of the Application that do not use Ecleptic's place catalogue yet (2.8): receives an area of about 110 m around the location, without the exact location or any user identifier | United States |
| Functional Software, Inc. (Sentry) | Reporting the Application's errors and crashes (technical data only, never health data) | United States |
| PostHog, Inc. | Aggregated usage statistics, **on a transitional basis**: until it is removed, ten of the usage events (2.4) are also relayed to it — end of onboarding; subscription screen; purchase; opening a notification (its category); reading the Éos report (its origin and age), expanding its details, first question asked to Éos from a report; report frequency chosen; monthly recap viewed or shared. Never health data, nor the content of reports or messages; a separate anonymous identifier, unrelated to the account, reset at sign-out; the objection in article 7 also stops this relay | European Union (EU hosting) |
| Windsor Group AG (Windsor.ai) | Reading, for the publisher's internal dashboard, statistics that are **already aggregated** (daily counts, without any identifier, even anonymous) | Switzerland; hosting in Germany |

Until 27 September 2026, versions of the Application recognised the gym by directly querying OpenStreetMap's public **Overpass** service, which then received the end-of-session location and the device's IP address, without an account identifier; those versions keep doing so until they are updated.

Reference nutritional values come from the ANSES **Ciqual** table (public data source, Etalab licence): no personal data is sent to it. Data sent to AI providers is **minimised**: no name, email or direct identifier is sent to the models.

The nutritional values of a contribution approved at review (2.6) are visible to all users of the Application, with no link to their author's account.

**Other users.** If the user has turned on the Society, other members only see what they have chosen to show them (2.9). A few recipients are specific to certain features: the place's reviewers for a proof video, the witness asked, the opponent in a match, the Ecleptic team for suggestions and moderation. A place's manager receives no workout data about its members: they only know the number of members shown on their gym's screen and see the videos to review for their place. A gym's screen is visible to anyone present.

**Places and zones.** The place catalogue (Overture Maps Foundation) and the zone outlines (IGN) are open data imported into Ecleptic's database: the user's location is never sent to them. Places: © Overture Maps Foundation and its contributors (CDLA Permissive 2.0, Apache 2.0, CC0 licences). Zones: © IGN – ADMIN EXPRESS and BD TOPO (Licence Ouverte 2.0).

Each processor is bound by a contract compliant with article 28 GDPR. The data is **neither sold nor rented** to third parties. It may be disclosed to the authorities where required by law.

## Article 5 — Transfers outside the European Union

Some processors listed in article 4 (Google, Anthropic, RevenueCat, Apple, Sentry) process data in the **United States**, including Apple and Google for delivering push notifications; Supabase, a US company, hosts the Application's data in the European Union (Ireland). Windsor.ai is established in **Switzerland**, a country recognised by the European Commission as providing an adequate level of protection, and only receives counts without identifiers. When data is transferred to a country outside the EU/EEA that does not provide an adequate level of protection, the transfer is governed by appropriate safeguards: an adequacy decision of the European Commission (including, for the United States, the EU–US Data Privacy Framework for certified providers) or the Commission's **standard contractual clauses**, supplemented where necessary by additional measures. The user can obtain a copy of the applicable safeguards through the privacy contact.

## Article 6 — Retention periods

| Category | Active retention | Afterwards |
|---|---|---|
| Account data | Lifetime of the account | Deleted within 30 days of the account being deleted |
| Health / tracking data | Lifetime of the account (or until consent is withdrawn / the user deletes it) | Deleted; backups purged within 30 days |
| Nutrition label photos (2.6) | Kept only if the user submits their entry for review, until the decision (approval or rejection) and **90 days at most** after they are sent | Deleted automatically |
| Label readings by AI (extracted values, attached to an image fingerprint, with no link to the account) | 30 days | Deleted automatically |
| Contributions: entries, corrections, reports (2.6) | Lifetime of the account | Deleted with the account; approved and published values stay in the food database, with no link to the account |
| Workout-by-workout efforts (2.8) | 90 days | Only the month's best per measure and per place is kept, as long as the account exists |
| Social profile, partnerships, reactions, challenges, boards, crowns, seasons, league, racket, weight class, zones and place of workouts (2.8, 2.9) | Lifetime of the account | Deleted with the account |
| Profile photo (2.9) | As long as it is in place. Replaced or removed by the user: erased within 2 days. Removed by moderation: erased after 30 days. Account inactive for 12 months (no sign-in, workout or change to the social profile): erased, the avatar replaces it | Deleted automatically; deleted with the account |
| Proof video (2.9) | 30 days after the decision, or 30 days without a decision | Deleted automatically; the decision stays, without the video |
| Suggestions of places and spots (2.9) | Lifetime of the account | Deleted with the account; an accepted place or spot stays public, with no link to the account |
| Reports sent, blocked accounts, moderation decisions, anti-abuse counters (2.9) | Lifetime of the account | Deleted with the account |
| Notification token (2.10) | Until sign-out, turning off the Society, or its refusal by Apple or Google | Deleted with the account |
| Notification sending queue (2.10) | 14 days; a notification not sent after 3 days expires | Deleted automatically |
| Proofs of consent | Lifetime of the account | Deleted with the account |
| Billing data | 10 years (accounting obligation) | Intermediate archiving with restricted access |
| Technical and security logs | 12 months | Deleted |
| Usage events (2.4) and installation identifier | 13 months | Deleted automatically |
| Aggregated statistics (daily counts, without identifier) | 25 months | Deleted automatically |
| Error and response-time logs | 90 days | Deleted automatically |
| Marketing data | 3 years after the last contact | Deleted |
| Cookies / trackers | See article 9 | — |

## Article 7 — Rights of individuals

In accordance with articles 15 to 22 GDPR and the French Data Protection Act, the user has the following rights:

- **access** to their data and a copy of it;
- **rectification** of inaccurate data;
- **erasure** ("right to be forgotten") in the cases provided for by article 17;
- **restriction** of processing;
- **objection** to processing based on legitimate interest, and objection without reason to marketing;
- **portability** of the data provided, in a structured and commonly used format;
- **withdrawal of consent** at any time, for processing based on it;
- **post-mortem instructions** on what happens to their data after their death (art. 85 of the French Data Protection Act);
- **objection to usage statistics**: an "Anonymous usage statistics" switch in Settings › Privacy immediately stops events from being sent and empties those waiting on the device.

**Data export**: Settings › Export my data provides a file that also includes Society data: social profile, efforts, zones, partnerships, reactions, challenges, boards, crowns, league, seasons, racket, suggestions, proof video requests, management requests, weight class, devices registered for notifications, reports sent, blocks and moderation decisions. The file gives the path of the profile photo; the image file itself, like that of a proof video, is provided on request through the contact in article 1.

**Exercising rights**: by email to the privacy contact in article 1, or directly from the Application's Settings (account deletion and data export are available there). A response is given within one month, extendable by two months for complex requests. Proof of identity may be requested in case of reasonable doubt about the requester's identity.

## Article 8 — Security

The data controller implements appropriate technical and organisational measures (art. 32 GDPR), including: encryption of data in transit (TLS) and at rest at the host, strict access control and authentication, separated environments, logging, minimisation of data sent to providers (including AI providers), regular backups. Data tables are protected by row-level access rules (each user only accesses their own data) and photos are stored in private spaces, partitioned per account. In the Society, any access to another member's data goes through a single server-side check, which applies their visibility settings and blocks; profile photos and proof videos have no public address.

In the event of a data breach likely to result in a risk to people's rights and freedoms, the CNIL will be notified within 72 hours and, in the event of a high risk, the people concerned will be informed (art. 33 and 34 GDPR).

## Article 9 — Cookies and trackers

9.1. The Application uses trackers that are **strictly necessary** for it to work (authentication token, local preferences, security), exempt from consent, and an **audience measurement run by the publisher itself**: a random installation identifier stored on the device, used only to produce anonymous usage statistics, never cross-referenced with the account or other processing, kept for 13 months at most (identifier and events), and which the user can object to at any time in Settings › Privacy. These statistics are only shared with third parties in aggregated form, except for the transitional relay to PostHog described in article 4. This setup aims at the consent exemption provided by the CNIL for audience measurement. No advertising tracker is built in; no cross-app tracking (no App Tracking Transparency on iPhone; on Android, the advertising identifier is neither requested nor read).

9.2. If trackers subject to consent were added (for example a non-exempt audience measurement tool), prior consent would be collected through a dedicated interface offering, at the same level, the possibility to accept, refuse and configure, withdrawable at any time from the Settings, with the choice remaining valid for no more than 13 months.

## Article 10 — Minors

The Application is intended for people aged at least **16** (18 for the body composition scan and the conversation with Éos). In France, the age of digital consent is set at **15** (art. 45 of the French Data Protection Act): below that age, processing based on consent requires the joint consent of the minor and the holder of parental authority. If the data controller learns that an account was created in breach of these conditions, it will delete it along with the related data.

In the Society, a 16- or 17-year-old user **never** appears in a public ranking: they are only visible to their partners, whom they add in person (QR code or link), and so is their photo. The league, public challenges, the gym screen and place management are reserved for adults, and they only play racket with their partners. An unknown date of birth counts as being a minor.

## Article 11 — Complaint to the CNIL

If the user considers that their rights are not respected, they may lodge a complaint with the **Commission Nationale de l'Informatique et des Libertés (CNIL)** — 3 place de Fontenoy, TSA 80715, 75334 Paris Cedex 07 — www.cnil.fr — or with the supervisory authority of their EU member state of residence.

## Article 12 — Updates to this policy

This policy may be updated, in particular when the Services or the regulations change. Any substantial change (new purpose, new recipient, change of legal basis) will be brought to users' attention by an appropriate means (notification in the Application and/or email) before it takes effect and, where the law requires it, will lead to new consent being collected.
