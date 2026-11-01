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

A product moves to "released" only after it passes gate G9 of the Product Review & Approval Process (qa/QA-01 in the project). When the first product is released, add a `released` status with a Buy button that links to its checkout.

## Wording rules

All product text follows the master wording rules in the Legal Review:
- No "complete", "every", "never", "zero", "compliant", "certified", "approved", "guaranteed" or verdict words as claims.
- No standards or agencies in product titles.

The site has no forms, cookies or analytics, and must stay that way until the privacy policy and OIC registration are in place.

## Cloudflare Pages settings

Framework preset: **None** · Build command: *(leave blank)* · Build output directory: **site**
