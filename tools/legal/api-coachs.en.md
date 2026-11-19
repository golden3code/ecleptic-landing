<!-- version-fr: 2026-11-19 -->
<!-- English translation of ~/Desktop/Auros/legal/api-coachs.md. Update it, and the date above, every time the French API documentation changes; tools/build_terms.py refuses to build otherwise. -->
# Coach API: documentation

**Last updated: 19 November 2026**

The Ecleptic API connects your coach space to your other tools: a spreadsheet, your accounting, your gym software, Zapier. It does two things:

- **read** your management data (clients, planned sessions, sales, class bookings) with a key;
- **notify** your tool when something happens (client joined, sale, class booked…) through a webhook: Ecleptic sends a short message to the address you choose.

It is open to every plan, trial included. It is read-only: no key can create, change or delete a client, a session or a sale. **No health data ever leaves through the API or the webhooks**, whatever the settings.

You choose the tools you connect, and you are responsible for them (coach terms of sale, article 9 octies, in French: https://ecleptic.health/cgv-coachs.html). What happens to your clients' data is explained in the privacy policy, section 2.14: https://ecleptic.health/en/privacy.html.

## 1. Keys

- Create a key in the console, **Settings › Connections and API**, at https://coach.ecleptic.health.
- Tick what it can read: clients, planned sessions, sales, bookings. The “Manages its webhooks (Zapier)” box also lets it subscribe an address to your events. Tick as little as possible.
- Validity: 1 year, 90 days or no end date. You can revoke it at any time: it stops working at once.
- Keys start with `ecl_`. A key is shown **only once**, when it is created. Ecleptic only keeps a fingerprint of it: nobody can read it again. If you lose it, revoke it and create another one.
- 5 active keys at most.
- Keep it like a password. It must never live in a web page: a call made from a browser (one that carries an `Origin` header) is refused.

Every call carries the key in the `Authorization` header:

```
GET https://avbmycfngmxhkjesdiyq.supabase.co/functions/v1/coach-api/v1/sales?since=2026-11-01T00:00:00Z
Authorization: Bearer ecl_…
```

## 2. Reading

Base URL: `https://avbmycfngmxhkjesdiyq.supabase.co/functions/v1/coach-api/v1`

| Route | Box to tick | What it returns |
|---|---|---|
| `GET /me` | none | Your name, the key's name, its boxes, its end date, the limits |
| `GET /students` | Clients | One row per client (their latest follow-up), without prospects |
| `GET /sessions` | Planned sessions | Sessions and appointments planned for a client, without your personal slots |
| `GET /sales` | Sales | Payments and refunds |
| `GET /bookings` | Bookings | Places booked in your classes |

### Pages

The four lists take the same parameters:

- `since` and `until`: date bounds, in ISO 8601 (`2026-11-01` or `2026-11-01T08:00:00+01:00`). `since` is included, `until` is not. Always give a time zone (`Z` for UTC).
- `limit`: 1 to 100 rows per page, 50 by default.
- `cursor`: the `next_cursor` value of the previous page, to read the next one (with the same `since` and `until`).

The response is always `{"data": [...], "next_cursor": "…"}`. Rows go from oldest to newest. `next_cursor` is `null` on the last page.

The date used for the bounds and the order: start of the follow-up for `/students`, session time for `/sessions`, payment or refund date for `/sales`, booking date for `/bookings`.

### Fields

A client always appears in the same form: `{"id": "stu_…", "name": "…"}`. `id` is a code specific to your space: it stays the same from one follow-up to the next, is used nowhere else, and is never the client's account identifier. `name` is the username you see in your list; it is `null` for someone who has never been your client.

| Route | Fields |
|---|---|
| `/me` | `coach.name`; `key.name`, `key.scopes`, `key.expires_at` (`null` with no end date); `limits.per_minute` (60), `limits.per_day` (5,000), `limits.page_max` (100) |
| `/students` | `id`, `name`, `status` (`active` or `ended`), `started_at`, `ended_at` |
| `/sessions` | `id`, `kind` (`workout` or `appointment`), `title`, `starts_at`, `minutes` (planned length), `status`, `student` |
| `/sales` | `id`, `type` (`payment` or `refund`), `student`, `package` (name of the offer), `package_kind` (`unit`, `pack`, `subscription` or `class`), `amount_cents`, `currency` (`eur`), `occurred_at`, `invoice_number`, `refunded_cents` (on a payment: total already refunded on the purchase), `livemode` (`false` for a Stripe test payment) |
| `/bookings` | `id`, `class` (`id`, `title`, `starts_at`, `minutes`, `status`: `scheduled` or `cancelled`), `student` (`null` for a participant without an account), `guest` (`true` for a participant without an account), `status` (`pending`, `confirmed` or `cancelled`), `created_at`, `confirmed_at`, `cancelled_at` |

A session's `status` is `planned` or `cancelled`. It is only `done` or `missed` for a client in an active follow-up who gave the “Connected tools” consent in their app (section 5); for everyone else, a session that is not cancelled always reads `planned`.

Amounts are in cents. Dates are in ISO 8601, in UTC. A field with no value is `null`.

## 3. Webhooks

A webhook tells your tool as soon as an event happens, without it having to poll the API.

### Addresses

- Create an address in the console (**Settings › Connections and API › Add an address**), or through the API with a key that “manages its webhooks” (section 4).
- 3 addresses at most, however they were created. `https` only, on port 443, to a public address: no address written as an IP number, no local network. Ecleptic checks it when it is saved and before every delivery.
- You choose which events are sent. You can pause the address, turn it back on, delete it.
- “Send a test” sends a `webhook.test` event (`{"test": true}`), once a minute at most, with no retry if it fails.

### Events

| Event | When | `data` |
|---|---|---|
| `student.joined` | A client starts their follow-up (or a prospect becomes a client) | `student`, `status`, `started_at`, `ended_at` |
| `student.left` | A follow-up ends | `student`, `status`, `started_at`, `ended_at` |
| `sale.paid` | A payment is received | `sale` (the same `id` as in `/sales`), `student`, `package`, `package_kind`, `amount_cents`, `currency`, `occurred_at`, `invoice_number`, `livemode` |
| `sale.refunded` | A refund is made | same fields (`amount_cents`: amount refunded) |
| `class.booked` | A place in a class is confirmed | `booking`, `class` (`id`, `title`, `starts_at`, `minutes`), `student`, `guest`, `status` |
| `form.signed` | A form is signed | `form` (`kind`: `form` or `health`, `title`), `student`, `signed_at` |
| `checkin.submitted` | A recurring check-in is filled in | `student`, `submitted_at` |
| `session.completed` | A planned session is done | `session`, `title`, `starts_at`, `student` |

Events about the client's activity are only sent with their consent (section 5).

### Delivery

Each event is sent as a `POST` with a JSON body:

```
{"id": "evt_…", "type": "sale.paid", "created_at": "2026-11-19T09:12:03.512345+00:00", "data": {…}}
```

Headers: `Content-Type: application/json`, `User-Agent: Ecleptic-Webhooks/1.0`, `Ecleptic-Event-Id` (the event's `id`), `Ecleptic-Event-Type`, `Ecleptic-Signature`.

- Answer with a 2xx code within **10 seconds**. The body of your answer is not read.
- Ecleptic follows **no redirect**: a 3xx answer counts as a failure.
- If a delivery fails, it is tried again after 1 minute, 10 minutes, then 1 hour (4 deliveries in all). The first one leaves within a minute of the event.
- After **20 failures in a row**, the address is turned off. You are told in the console and on your dashboard, and you turn it back on in one click.
- The same event may arrive twice (a lost answer, for example): keep the `Ecleptic-Event-Id` values you have already handled. The order of arrival is not guaranteed: rely on `created_at`.
- A delivery weighs 8 KB at most.

### Signature

Every delivery is signed with the address's secret. The secret starts with `whsec_`. It is shown only once, when the address is created and each time you regenerate it.

```
Ecleptic-Signature: t=1795165923,v1=5f2b…
```

- `t`: the time of sending, in seconds since 1 January 1970 (UTC).
- `v1`: the HMAC-SHA256, in hexadecimal, of the text `t` + `.` + the body received, keyed with the whole secret (`whsec_…` included).

To check a delivery:

1. Read the **raw** body, exactly as received, before any JSON parsing.
2. Compute the HMAC-SHA256 of `t.body` with your secret and compare it with `v1`, in constant time.
3. Refuse the delivery if `t` is more than 5 minutes away from your clock.

Example in Node.js:

```
const crypto = require('crypto');

function signatureOk(header, rawBody, secret) {
  const parts = Object.fromEntries(header.split(',').map((p) => p.trim().split('=')));
  const t = Number(parts.t);
  if (!t || Math.abs(Date.now() / 1000 - t) > 300) return false;
  const expected = crypto.createHmac('sha256', secret).update(t + '.' + rawBody).digest('hex');
  const given = Buffer.from(parts.v1 || '', 'hex');
  return given.length === 32 && crypto.timingSafeEqual(given, Buffer.from(expected, 'hex'));
}
```

## 4. Subscribing an address through the API (Zapier and similar tools)

With a key that “manages its webhooks”, a tool can create and remove its own address:

- `POST /webhooks`, body `{"url": "https://…", "events": ["sale.paid", "student.joined"]}` (1 to 8 events from the list above). Answer `201`: `{"id", "url", "events", "secret"}`. The secret is only returned at that moment.
- `DELETE /webhooks/{id}`: removes an address created by the same key. Answer `200`: `{"deleted": true}`.

An address created this way shows in your console, counts towards the 3, and goes away with the key when you revoke it.

The Ecleptic app for Zapier will be offered by invitation. Until then, any tool that can receive a webhook or call an address with a key can use the API.

## 5. What is only sent with the client's consent

The client gives this consent in their app, in “What my coach sees”, box “Tools connected by” their coach. They can withdraw it whenever they want: deliveries still waiting for them are cancelled. The consent ends with the follow-up. It cannot be given during a trial. Do not ask for it any other way than through the app.

Without this consent, none of this is sent:

- `session.completed` (session done): the title of the session you sent, its date, the client;
- `checkin.submitted` (check-in filled in): the date, the client;
- `form.signed` for a **health questionnaire**: only the kind (`health`) and the date, the client, never the title or the answers;
- in `/sessions`, the `done` or `missed` status.

Even with consent, no figure is sent: no actual duration, effort, load or set.

Without consent, an ordinary signed form is sent (kind `form`, its title, the date, the client), because it is data you manage.

## 6. What never leaves

Through no key, no webhook, no setting:

- weight, measurements, body fat, photos;
- sleep, Readiness, physiological state, heart rate and heart rate variability, watch data;
- actual duration, perceived effort, loads and sets of a session done;
- meals, intake, followed meal plans;
- answers to forms and check-ins, result of the health questionnaire;
- the client's file, notes and tags, messages, voice notes, weekly reports;
- the client's email address, phone number, date of birth, age, sex, account identifier;
- first name and email of a buyer or participant without an account, place and video link of a class, Stripe references, service fees.

The titles you write (sessions, classes, forms) can leave: never write health data in them.

## 7. Limits and errors

- **60 calls per minute and 5,000 per day** (UTC day), per key. Beyond that: a `429` answer with a `Retry-After` header (in seconds).
- Every call is logged for 30 days: the key, the route without its parameters, the answer, the duration, and a fingerprint of the caller's IP address, never the address itself. You see the latest calls in the console.
- Subscription ended (read-only): the API can still be read, webhooks stop, no key or address can be created. Coach space suspended or closed: everything stops.

An error returns `{"error": "…", "message": "…"}`:

| Code | `error` | Meaning |
|---|---|---|
| 400 | `bad_since`, `bad_until`, `bad_limit`, `bad_cursor`, `bad_webhook`, `bad_url`, `bad_events` | Malformed parameter or body |
| 401 | `unauthorized` | Key missing, unknown, revoked or expired, or coach space suspended (always the same answer) |
| 403 | `forbidden`, `browser_not_allowed`, `read_only`, `not_coach` | Box not ticked for this route, call from a browser, subscription ended (to create an address), coach space not active |
| 404 | `not_found` | Unknown route or address |
| 405 | `method_not_allowed` | Method refused (the `Allow` header says which one to use) |
| 409 | `too_many`, `duplicate` | Already 3 addresses, or address already saved |
| 429 | `rate_limited` | Too many calls |
| 503 | `unavailable` | Service unavailable: try again later |

## 8. Team API

A structure (gym, studio) that brings several coaches together in an Ecleptic team can connect its software with a **team key**. This key reads the management data of **all coaches who are members of the team**, the manager included.

- Only the **manager** creates a key, in the console: **Team › API › New key**. Same rules as a coach key: `ecl_…`, shown only once, 1 year, 90 days or no end date, revocable at any time, 5 active keys at most per team.
- Same base URL and routes as a coach's API (`/me`, `/students`, `/sessions`, `/sales`, `/bookings`, `/webhooks`), same pages, same limits (60 calls per minute, 5,000 per day, per key), same errors. Server-to-server calls only.
- Every row also carries `coach`: `{"id": "coa_…", "name": "…"}`, a code specific to the team and the coach's username.
- `student.id` is a code specific to the team: the same whichever coach the client has in the team, and different from the code each coach sees in their own API.
- `GET /me` returns `org.name` (the team's name), `coaches` (codes and usernames of the member coaches), `key` and `limits`.
- `/students` returns one row per follow-up: the latest one of each client with each coach of the team.
- Only **current** members are read: a coach who leaves the team no longer appears.

**No activity data**: a session is only ever `planned` or `cancelled`, never `done` or `missed`. No check-ins, no forms. Nothing listed in section 6 leaves either.

### Team webhooks

- No address is typed in the console: the software subscribes itself through the API (`POST /webhooks`, `DELETE /webhooks/{id}`), with a key that has the “webhooks” box.
- 3 addresses at most per team. Same deliveries, signature, retries and turn-off as for a coach (section 3).
- **5 management events only**:

| Event | When | `data` |
|---|---|---|
| `student.joined` | A client starts a follow-up with a coach of the team (including after a change of coach) | `student`, `coach`, `status`, `started_at`, `ended_at` |
| `student.left` | A follow-up ends | same fields |
| `sale.paid` | A payment is received | `sale`, `student`, `coach`, `package`, `package_kind`, `amount_cents`, `currency`, `occurred_at`, `invoice_number`, `livemode` |
| `sale.refunded` | A refund is made | same fields |
| `class.booked` | A place in a class is confirmed | `booking`, `class` (`id`, `title`, `starts_at`, `minutes`), `student`, `coach`, `guest`, `status` |

`form.signed`, `checkin.submitted` and `session.completed` do not exist for a team.

Manager's subscription ended (read-only): reading still works, nothing is sent. Team closed: everything stops.

A manager who creates a team key gives their software the management data of every coach in the team: they are responsible for it (coach terms of sale, article 3 ter), keep the key like a password and revoke it as soon as it is no longer used.

## 9. Changes

The version is in the URL (`/v1`). Fields, routes or events may be added without a new version: your tool must ignore what it does not know. Before removing or changing a field, a route or an event, Ecleptic tells coaches in the coach space.

Questions: contact@ecleptic.app.
