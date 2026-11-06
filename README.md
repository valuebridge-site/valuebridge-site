# valuebridgeja.com

The ValueBridge website: a static site generated from one product catalogue.

## How it fits together

| Folder | What it holds |
|---|---|
| `data/catalog.py` | **Single source of truth** for every product, department, collection, bundle and release status. It mirrors the Product Development Tracker. |
| `tools/build.py` | Builds every page in `site/` from the catalogue. |
| `site/` | The published website, which is what Cloudflare Pages serves. |

## Updating the site

1. Edit `data/catalog.py`. Typical edits are a product's `web` status, `price`, `short` text or `bullets`, or adding a product with `add(...)`.
2. Run `python3 tools/build.py`.
3. Commit and push. Cloudflare Pages republishes within about a minute.

You can ask Claude to do all three steps, for example: "Mark PDF Studio as released and add its checkout link."

## Release status labels (`web` field)

| Key | Shown on the site |
|---|---|
| `testing` | Coming soon · Final testing · planned for December 2026 |
| `review` | Coming soon · Awaiting specialist review · planned for early 2027 |
| `review2027` | Coming soon · Awaiting specialist review · planned for 2027 |
| `dev` | Coming soon · In development |
| `new` | Coming soon · Newly built · awaiting market review and testing |
| `enquiry` | Coming soon · Enquiries open when the store launches |
| `released` | Available now · Instant download after checkout (shows a **Buy now** button) |

## Releasing a product (only after gate G9 is signed in QA-02)

1. In Lemon Squeezy, open the live product and copy its checkout link (`https://valuebridgeja.lemonsqueezy.com/checkout/buy/<uuid>`).
2. In `data/catalog.py`, on that product's `add(...)` line set `web="released"` and `checkout="<that link>"`.
3. Run `python3 tools/build.py` (it refuses to build if a released product has no link), commit and push.

The Buy button uses Lemon Squeezy's overlay checkout (`lemon.js`), loaded only on pages that have a button. Without JavaScript the same link opens the hosted checkout page. The site banner and home page switch to "store open" wording automatically once any product is released.

**Test checkout:** set `TEST_CHECKOUT_URL` in `data/catalog.py` to a test-mode product's link and rebuild; the button appears on `/test-checkout.html`, which is unlisted and marked noindex. Clear it again before go-live.

## Wording rules

All product text follows the master wording rules in the Legal Review:
- No "complete", "every", "never", "zero", "compliant", "certified", "approved", "guaranteed" or verdict words as claims.
- No standards or agencies in product titles.

The site has no forms, cookies or analytics, and must stay that way until the privacy policy and OIC registration are in place.

## Cloudflare Pages settings

Framework preset: **None** · Build command: *(leave blank)* · Build output directory: **site**
