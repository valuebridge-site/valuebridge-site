#!/usr/bin/env python3
"""Build the ValueBridge static site from data/catalog.py into site/.
Run:  python3 tools/build.py
Every product, department, collection and bundle page is generated from the catalogue,
so the website always matches the product tracker. Edit data/catalog.py, then rebuild.
"""
import html
import os
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "data"))
import catalog as C  # noqa: E402

OUT = os.path.join(ROOT, "site")
DOMAIN = "https://valuebridgeja.com"
E = html.escape
BY_SLUG = {p["slug"]: p for p in C.P}
DEPT = {a: (b, c) for a, b, c in C.DEPARTMENTS}
COLL = {a: (b, c) for a, b, c in C.COLLECTIONS}
PAGES = []  # for sitemap

ICONS = {  # simple line icons (inline SVG paths)
    "templates": '<path d="M6 3h9l5 5v13H6z"/><path d="M14 3v6h6"/><path d="M9 13h8M9 17h6"/>',
    "business-tools": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "productivity": '<circle cx="12" cy="12" r="8"/><path d="M12 7v5l3 2"/>',
    "design-assets": '<circle cx="12" cy="12" r="9"/><circle cx="8.5" cy="10" r="1.2"/><circle cx="12" cy="7.5" r="1.2"/><circle cx="15.5" cy="10" r="1.2"/><path d="M12 21c-1.5 0-2-1.5-1-2.5s0-2.5-1.5-2.5"/>',
    "learning-development": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>',
    "lifestyle": '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>',
}


def rel(depth):
    return "../" * depth


def price_text(p):
    pr = p["price"]
    live = p["web"] == "released"
    if pr == "0":
        return "Free" if live else "Planned price: Free"
    if pr == "TBA":
        return "Price to be announced"
    return f"US${pr}" if live else f"Planned price: US${pr}"


LEMON_JS = '<script src="https://app.lemonsqueezy.com/js/lemon.js" defer></script>'


def buy_button(url, label="Buy now"):
    """Lemon Squeezy overlay checkout: the button opens checkout in a window over the page.
    lemon.js is loaded only on pages that have a button, so every other page stays script-free.
    ?embed=1 keeps the overlay; without JavaScript the link still opens the hosted checkout page."""
    sep = "&" if "?" in url else "?"
    return f'<a class="btn lemonsqueezy-button" href="{E(url)}{sep}embed=1&media=0&logo=0">{E(label)}</a>'


def any_released():
    return any(p["web"] == "released" for p in C.P)


def badge(p):
    label, stage = C.WEB_STATUS[p["web"]]
    return f'<span class="badge{" live" if p["web"]=="released" else ""}">{E(label)}</span><span class="stage">{E(stage)}</span>'


def card(p, d):
    label, stage = C.WEB_STATUS[p["web"]]
    return f"""<a class="card" href="{rel(d)}products/{p['slug']}.html">
  <span class="badge{' live' if p['web']=='released' else ''}">{E(label)}</span>
  <h3>{E(p['name'])}</h3>
  <p>{E(p['short'])}</p>
  <div class="meta"><span>{E(p['coll_name'])}</span><span>{E(price_text(p).replace('Planned price: ', '').replace('Price to be announced','Price TBA'))}</span></div>
  <div class="stage-sm">{E(stage)}</div>
</a>"""


def page(path, title, body, desc, d, active="", head="", noindex=False):
    nav = [("index.html", "Home"), ("catalogue.html", "All products"), ("departments/business-tools.html", "Departments"), ("collections/technology.html", "Technology"), ("collections/marketing.html", "Social"),
           ("bundles.html", "Bundles"), ("about.html", "About"), ("contact.html", "Contact")]
    notice = ("Our store is open: products marked Available now can be bought today. Other products are coming soon." if any_released()
              else "Our store is not open yet. Every product is coming soon; the first releases are planned for December 2026.")
    navhtml = "".join(f'<a href="{rel(d)}{h}"{" class=on" if active == n else ""}>{n}</a>' for h, n in nav)
    full = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="icon" href="{rel(d)}assets/icon.png">
<link rel="stylesheet" href="{rel(d)}assets/site.css">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
{'<meta name="robots" content="noindex,nofollow">' if noindex else ''}{head}
</head>
<body>
<div class="notice">{notice}</div>
<header class="top"><div class="wrap">
  <a class="logo" href="{rel(d)}index.html"><img src="{rel(d)}assets/logo.png" alt="ValueBridge" width="154" height="39"></a>
  <input type="checkbox" id="m" class="mtoggle"><label for="m" class="mbtn" aria-label="Menu">Menu</label>
  <nav>{navhtml}</nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap fgrid">
  <div><img src="{rel(d)}assets/logo.png" alt="ValueBridge" width="140" height="36"><p>Digital solutions tailored to you.</p><p>Jamaica · <a href="mailto:hello@valuebridgeja.com">hello@valuebridgeja.com</a></p></div>
  <div><h4>Shop</h4><a href="{rel(d)}catalogue.html">All products</a><a href="{rel(d)}bundles.html">Bundles</a><a href="{rel(d)}quote.html">Tailored setup</a></div>
  <div><h4>Departments</h4>{''.join(f'<a href="{rel(d)}departments/{a}.html">{E(b)}</a>' for a, b, _ in C.DEPARTMENTS)}</div>
  <div><h4>Help</h4><a href="{rel(d)}how-downloads-work.html">How downloads work</a><a href="{rel(d)}faq.html">FAQ</a><a href="{rel(d)}contact.html">Contact</a><a href="{rel(d)}privacy.html">Privacy notice</a><a href="{rel(d)}policies.html">Store policies</a></div>
</div>
<div class="wrap legal"><p>Product names of other companies are trademarks of their owners. ValueBridge is independent and not affiliated with or endorsed by any software maker, standards body, regulator or agency named on this site. Templates and tools support your own work; they are not legal, tax, financial, safety or engineering advice.</p>
<p>© {date.today().year} ValueBridge. Catalogue as at {C.AS_AT}.</p></div></footer>
</body></html>
"""
    fp = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(full)
    if not noindex:
        PAGES.append(path)


def rich_product(p, D, cta, bund, related, note=""):
    """Full product page for products with a DETAILS entry in the catalogue (G5 content)."""
    import json
    slug = p["slug"]
    A = f"../assets/products/{slug}/"
    live = p["web"] == "released"
    trial_on = D.get("trial_live") and os.path.exists(os.path.join(ROOT, "staging", "try", slug, "index.html"))
    v = D.get("video")
    video = ""
    if v:
        lng = v.get("long")
        video = f"""<figure class="pvideo"><video controls preload="none" playsinline poster="{A}{v['poster']}" width="1920" height="1080">
<source src="{A}{v['file']}" type="video/mp4"><track kind="captions" src="{A}{v['captions']}" srclang="en" label="English" default></video>
<figcaption>{E(v['title'])}{f' · <a href="{A}{lng["file"]}">{E(lng["label"])}</a>' if lng else ''}</figcaption>
<details class="transcript"><summary>Read the video transcript</summary><p>{E(v['transcript'])}</p></details></figure>"""
    gallery = '<div class="gallery">' + "".join(
        f'<figure><a href="{A}{f}"><img src="{A}{f}" alt="{E(alt)}" width="1440" height="900" loading="lazy" decoding="async"></a><figcaption>{E(cap)}</figcaption></figure>'
        for f, alt, cap in D.get("gallery", [])) + "</div>"
    who = "".join(f"<li>{E(x)}</li>" for x in D.get("who", []))
    steps = "".join(f"<li><b>{E(a)}</b><span>{E(b)}</span></li>" for a, b in D.get("steps", []))
    feats = "".join(f"<div><h3>{E(a)}</h3><p>{E(b)}</p></div>" for a, b in D.get("features", []))
    files = "".join(f"<li><b>{E(a)}</b>: {E(b)}</li>" for a, b in D.get("files", []))
    limits = "".join(f"<li>{E(x)}</li>" for x in D.get("limits", []))
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in D.get("faq", []))
    trial = ""
    if trial_on and D.get("trial"):
        rows = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in D["trial"]["rows"])
        trial = f"""<h2 id="try">Try it free</h2><p>Open the free trial version in your browser: no signup, sample data included.</p>
<p><a class="btn" href="../try/{slug}/">Open the free trial</a></p>
<div class="tablewrap"><table class="cat cmp"><thead><tr><th></th><th>Free trial</th><th>Full version</th></tr></thead><tbody>{rows}</tbody></table></div>"""
    if trial_on:
        cta = cta + f'<a class="btn ghost" href="../try/{slug}/">Try it free</a>'
    body = f"""<section class="wrap pagehead"><p class="crumb"><a href="../index.html">Home</a> / <a href="../departments/{p['dept']}.html">{E(p['dept_name'])}</a> / <a href="../collections/{p['coll']}.html">{E(p['coll_name'])}</a></p></section>
<section class="wrap product">
<div class="pmain">
  <div class="pbadges">{badge(p)}</div>
  <h1>{E(p['name'])}</h1>
  <p class="lead">{E(D['lead'])}</p>
  <p class="mprice"><b>{E(price_text(p))}</b> · {E(C.WEB_STATUS[p['web']][0])}{' · <a href="#try">Try it free</a>' if trial_on else ''}</p>
  {video}
  <h2>Screenshots</h2><p class="small">{E(D.get("gallery_note", "Example data shown. All people, tasks and dates are fictional."))}</p>{gallery}
  <h2>Who it's for</h2><ul class="ticks">{who}</ul>
  <h2>How it works</h2><ol class="steps">{steps}</ol>
  <h2>{"What's included" if live else "What's planned to be included"}</h2><div class="features">{feats}</div>
  <h3 class="h3s">In the download</h3><ul>{files}</ul>
  <h2>Requirements</h2><p>{E(D['requirements'])}</p>
  <h2>Limits</h2><ul class="limits">{limits}</ul>
  {trial}
  <h2>Questions</h2><div class="faq">{faq}</div>
  <h2>Licence</h2><p>{E(D['licence'])}</p>
  <p class="fine">{E(D['privacy'])}</p>
  <p class="fine">{E(D['affiliation'])}</p>
  {f'<p class="fine">{E(note)}</p>' if note else ''}
</div>
<aside class="pbox">
  <div class="price">{E(price_text(p))}</div>
  {'<p class="small">Prices may change before release.</p>' if not live else ''}
  {cta}
  <dl><dt>Format</dt><dd>{E(p['fmt'])}</dd><dt>Version</dt><dd>{E(p['version'])}</dd><dt>Licence</dt><dd>{E(D.get('licence_label', 'One-time, up to 3 devices'))}</dd><dt>Status</dt><dd>{E(C.WEB_STATUS[p['web']][1])}</dd></dl>
  {bund}
  {'<p class="small"><a href="#' + 'try">Try the free trial</a></p>' if trial_on else ''}
  <p class="small">Questions? <a href="mailto:hello@valuebridgeja.com?subject={E(p['name'])}">hello@valuebridgeja.com</a></p>
</aside>
</section>
{('<section class="wrap"><h2 class="h2s">More in ' + E(p['coll_name']) + '</h2>' + grid(related, 1) + '</section>') if related else ''}"""
    url = f"{DOMAIN}/products/{slug}.html"
    img = f"{DOMAIN}/assets/products/{slug}/{D['social_image']}"
    imgs = [img] + [f"{DOMAIN}/assets/products/{slug}/{f}" for f, _, _ in D.get("gallery", [])[:3]]
    if D.get("schema") == "Product":
        app = {"@type": "Product", "name": p["name"], "description": D["description"], "url": url, "image": imgs,
               "sku": f"{slug}-{p['version']}", "brand": {"@type": "Brand", "name": "ValueBridge"}}
    else:
        app = {"@type": "SoftwareApplication", "name": p["name"], "applicationCategory": "BusinessApplication",
               "operatingSystem": "Web browser", "softwareVersion": p["version"], "description": D["description"], "url": url,
               "image": imgs, "publisher": {"@type": "Organization", "name": "ValueBridge", "url": DOMAIN}}
    if live and p["checkout"]:
        app["offers"] = {"@type": "Offer", "price": p["price"], "priceCurrency": "USD", "availability": "https://schema.org/InStock", "url": url}
    graph = [{"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
        {"@type": "ListItem", "position": 2, "name": p["dept_name"], "item": f"{DOMAIN}/departments/{p['dept']}.html"},
        {"@type": "ListItem", "position": 3, "name": p["coll_name"], "item": f"{DOMAIN}/collections/{p['coll']}.html"},
        {"@type": "ListItem", "position": 4, "name": p["name"], "item": url}]}, app]
    if v:
        graph.append({"@type": "VideoObject", "name": v["title"], "description": D["description"],
                      "thumbnailUrl": f"{DOMAIN}/assets/products/{slug}/{v['poster']}", "uploadDate": v["uploaded"],
                      "duration": v["duration"], "contentUrl": f"{DOMAIN}/assets/products/{slug}/{v['file']}"})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace("</", "<\\/")
    head = (f'\n<link rel="canonical" href="{url}">\n<meta property="og:type" content="product">\n<meta property="og:site_name" content="ValueBridge">\n'
            f'<meta property="og:title" content="{E(p["name"])}">\n<meta property="og:description" content="{E(D["description"])}">\n'
            f'<meta property="og:url" content="{url}">\n<meta property="og:image" content="{img}">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
            f'<meta property="og:image:alt" content="{E(p["name"])}: {E(p["short"])}">\n<meta name="twitter:card" content="summary_large_image">\n'
            f'<script type="application/ld+json">{ld}</script>')
    return body, head, trial_on


def sync_trials():
    """Publish trial builds only for products whose DETAILS entry has trial_live=True; remove the rest."""
    import shutil
    for slug, D in getattr(C, "DETAILS", {}).items():
        src = os.path.join(ROOT, "staging", "try", slug, "index.html")
        dst_dir = os.path.join(OUT, "try", slug)
        if D.get("trial_live") and os.path.exists(src):
            os.makedirs(dst_dir, exist_ok=True)
            shutil.copyfile(src, os.path.join(dst_dir, "index.html"))
        elif os.path.isdir(dst_dir):
            shutil.rmtree(dst_dir)


def grid(products, d):
    return '<div class="grid">' + "".join(card(p, d) for p in products) + "</div>"


def order(ps):
    rank = {"released": -1, "testing": 0, "enquiry": 1, "review": 2, "dev": 3, "review2027": 4, "new": 5}
    return sorted(ps, key=lambda p: (rank[p["web"]], p["name"]))


def build():
    # ---------- home ----------
    d = 0
    depts = "".join(f"""<a class="tile" href="departments/{a}.html"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[a]}</svg>
<h3>{E(b)}</h3><p>{E(c)}</p><span class="count">{(lambda n: f"{n} product" + ("" if n == 1 else "s"))(sum(1 for p in C.P if p['dept']==a))}</span></a>""" for a, b, c in C.DEPARTMENTS)
    colls = "".join(f'<a class="chip" href="collections/{a}.html">{E(b)} <span>{sum(1 for p in C.P if p["coll"]==a or a in p["also"])}</span></a>' for a, b, _ in C.COLLECTIONS)
    first = [p for p in C.P if p["web"] == "testing"]
    body = f"""<section class="hero"><div class="wrap">
<h1>Digital solutions tailored to you.</h1>
<p class="lead">Spreadsheet templates, document kits and software for small businesses, professionals and households, built in Jamaica.</p>
<div class="hero-stats"><div><b>{len(C.P)}</b><span>products in our catalogue</span></div><div><b>{len(C.BUNDLES)}</b><span>bundles</span></div><div><b>Dec 2026</b><span>first releases planned</span></div></div>
<p class="note">Nothing is on sale yet. Each product is released only after it passes our review process: technical tests, user or specialist review, and a legal check of the licence and wording.</p>
<a class="btn" href="catalogue.html">Browse the catalogue</a>
</div></section>
<section class="wrap"><h2>Shop by department</h2><div class="tiles">{depts}</div></section>
<section class="wrap"><h2>Collections</h2><div class="chips">{colls}<a class="chip" href="bundles.html">Bundles <span>{len(C.BUNDLES)}</span></a></div></section>
{('<section class="wrap"><h2>Available now</h2>' + grid(sorted([p for p in C.P if p["web"]=="released"], key=lambda p: p["name"]), d) + '</section>') if any_released() else ''}
<section class="wrap"><h2>{'Coming next' if any_released() else 'First releases'}</h2><p class="sub">These products are in final testing and are planned for December 2026.</p>{grid(sorted(first, key=lambda p: p['name']), d)}</section>
<section class="wrap how"><h2>How our products are released</h2><ol class="steps">
<li><b>Built</b><span>Files and examples created and self-checked.</span></li>
<li><b>Tested</b><span>Opened and used on real computers and phones.</span></li>
<li><b>Reviewed</b><span>Real users, or a qualified specialist for safety, finance, environmental and engineering products.</span></li>
<li><b>Checked</b><span>Licence and product wording reviewed by an attorney.</span></li>
<li><b>Released</b><span>Listed for sale with a download you can test-buy.</span></li></ol></section>"""
    page("index.html", "ValueBridge · Digital solutions tailored to you", body,
         "ValueBridge: spreadsheet templates, document kits and software for small businesses, professionals and households. Coming soon.", d, "Home")

    # ---------- catalogue ----------
    rows = ""
    for p in order(C.P):
        label, stage = C.WEB_STATUS[p["web"]]
        rows += f'<tr data-s="{p["web"]}"><td><a href="products/{p["slug"]}.html">{E(p["name"])}</a></td><td>{E(p["dept_name"])}</td><td>{E(p["coll_name"])}</td><td>{E(price_text(p).replace("Planned price: ", ""))}</td><td>{E(stage)}</td></tr>'
    body = f"""<section class="wrap pagehead"><h1>All products</h1><p class="sub">{len(C.P)} products. All are coming soon; planned prices may change before release.</p>
<div class="filters"><button data-f="all" class="on">All</button>{'<button data-f="released">Available now</button>' if any_released() else ''}<button data-f="testing">Final testing</button><button data-f="review">Specialist review (early 2027)</button><button data-f="review2027">Specialist review (2027)</button><button data-f="dev">In development</button><button data-f="new">Newly built</button></div>
<div class="tablewrap"><table class="cat"><thead><tr><th>Product</th><th>Department</th><th>Collection</th><th>Planned price</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table></div></section>
<script>
document.querySelectorAll('.filters button').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.filters button').forEach(x=>x.classList.remove('on'));b.classList.add('on');
var f=b.dataset.f;document.querySelectorAll('tr[data-s]').forEach(r=>{{r.style.display=(f==='all'||r.dataset.s===f||(f==='review'&&r.dataset.s==='enquiry'))?'':'none'}})}});
</script>"""
    page("catalogue.html", "All products · ValueBridge", body, "The full ValueBridge catalogue with release status.", 0, "All products")

    # ---------- departments ----------
    for a, b, c in C.DEPARTMENTS:
        ps = [p for p in C.P if p["dept"] == a]
        sections = ""
        for ca, cb, _ in C.COLLECTIONS:
            sub = [p for p in ps if p["coll"] == ca]
            if sub:
                sections += f'<h2 class="h2s"><a href="../collections/{ca}.html">{E(cb)}</a></h2>{grid(order(sub), 1)}'
        side = "".join(f'<a href="{x}.html"{" class=on" if x == a else ""}>{E(y)}</a>' for x, y, _ in C.DEPARTMENTS)
        body = f"""<section class="wrap pagehead"><p class="crumb"><a href="../index.html">Home</a> / Departments</p><h1>{E(b)}</h1><p class="sub">{E(c)}</p>
<div class="tabs">{side}</div></section><section class="wrap">{sections or '<p>More products are on the way.</p>'}</section>"""
        page(f"departments/{a}.html", f"{b} · ValueBridge", body, c, 1, "Departments")

    # ---------- collections ----------
    for a, b, c in C.COLLECTIONS:
        ps = order([p for p in C.P if p["coll"] == a or a in p["also"]])
        bl = [x for x in C.BUNDLES if x[4] == a]
        bh = ""
        if bl:
            bh = '<h2 class="h2s">Bundles in this collection</h2><ul class="blist">' + "".join(
                f'<li><a href="../bundles.html#{x[0]}">{E(x[1])}</a> · planned US${x[2]}</li>' for x in bl) + "</ul>"
        body = f"""<section class="wrap pagehead"><p class="crumb"><a href="../index.html">Home</a> / Collections</p><h1>{E(b)}</h1><p class="sub">{E(c)}</p></section>
<section class="wrap">{grid(ps, 1)}{bh}</section>"""
        page(f"collections/{a}.html", f"{b} · ValueBridge", body, c, 1, {"technology": "Technology", "marketing": "Social"}.get(a, ""))

    # ---------- products ----------
    for p in C.P:
        label, stage = C.WEB_STATUS[p["web"]]
        bullets = "".join(f"<li>{E(x)}</li>" for x in p["bullets"])
        inb = [x for x in C.BUNDLES if p["slug"] in x[3]]
        bund = ""
        if inb:
            bund = f"<p><b>{'Also in' if p['web']=='released' else 'Also planned in'}:</b> " + ", ".join(f'<a href="../bundles.html#{x[0]}">{E(x[1])}</a>' for x in inb) + "</p>"
        note = {"A": "", "Service": "",
                "B": "A planning and tracking tool, not accounting, tax, investment or legal advice.",
                "C": "Templates and tools support your own work. They are not legal, safety, environmental or engineering advice; adapt them to your situation and have them checked by a competent person."}[p["tier"]]
        related = [q for q in order(C.P) if q["coll"] == p["coll"] and q["slug"] != p["slug"]][:3]
        if p["tier"] == "Service":
            cta = '<a class="btn" href="../quote.html">About tailored setup</a>'
        elif p["web"] == "released" and p["checkout"]:
            cta = buy_button(p["checkout"]) + '<p class="small">Secure checkout by Lemon Squeezy, our payment partner. Card, PayPal and Apple/Google Pay where available. Prices in US dollars; taxes shown at checkout.</p>'
        elif p["web"] == "released":
            raise SystemExit(f"{p['slug']} is marked released but has no checkout link")
        else:
            cta = '<span class="btn disabled" aria-disabled="true">Coming soon</span>'
        head = LEMON_JS if (p["web"] == "released" and p["checkout"]) else ""
        D = getattr(C, "DETAILS", {}).get(p["slug"])
        if D:
            body, rhead, _ = rich_product(p, D, cta, bund, related, note)
            page(f"products/{p['slug']}.html", D["title"], body, D["description"], 1, head=head + rhead)
            continue
        body = f"""<section class="wrap pagehead"><p class="crumb"><a href="../index.html">Home</a> / <a href="../departments/{p['dept']}.html">{E(p['dept_name'])}</a> / <a href="../collections/{p['coll']}.html">{E(p['coll_name'])}</a></p></section>
<section class="wrap product">
<div class="pmain">
  <div class="pbadges">{badge(p)}</div>
  <h1>{E(p['name'])}</h1>
  <p class="lead">{E(p['short'])}</p>
  <h2>{"What's included" if p["web"]=="released" else "What's planned to be included"}</h2><ul class="ticks">{bullets}</ul>
  {f'<p class="fine">{E(note)}</p>' if note else ''}
</div>
<aside class="pbox">
  <div class="price">{E(price_text(p))}</div>
  {'<p class="small">Prices may change before release.</p>' if p["web"] != "released" else ''}
  {cta}
  <dl><dt>Format</dt><dd>{E(p['fmt'])}</dd><dt>Version</dt><dd>{E(p['version'])}</dd><dt>Status</dt><dd>{E(stage)}</dd></dl>
  {bund}
  <p class="small">Questions? <a href="mailto:hello@valuebridgeja.com?subject={E(p['name'])}">hello@valuebridgeja.com</a></p>
</aside>
</section>
{('<section class="wrap"><h2 class="h2s">More in ' + E(p['coll_name']) + '</h2>' + grid(related, 1) + '</section>') if related else ''}"""
        page(f"products/{p['slug']}.html", f"{p['name']} · ValueBridge", body, p["short"], 1, head=head)

    # ---------- bundles ----------
    items = ""
    for slug, name, price, parts, coll in C.BUNDLES:
        sep = sum(float(BY_SLUG[x]["price"]) for x in parts)
        li = "".join(f'<li><a href="products/{x}.html">{E(BY_SLUG[x]["name"])}</a></li>' for x in parts)
        items += f"""<div class="bundle" id="{slug}"><span class="badge">Coming soon</span><h3>{E(name)}</h3><p class="sub">{E(COLL[coll][0])}</p>
<ul>{li}</ul><div class="price">Planned price: US${price}</div><p class="small">Available once each product in it has been released.</p></div>"""
    body = f"""<section class="wrap pagehead"><h1>Bundles</h1><p class="sub">Related products together for less. A bundle is released only when every product in it has been released.</p></section>
<section class="wrap"><div class="bgrid">{items}</div></section>"""
    page("bundles.html", "Bundles · ValueBridge", body, "ValueBridge product bundles (coming soon).", 0, "Bundles")

    # ---------- info pages ----------
    info = {
        "about.html": ("About ValueBridge", "About", """<p class="lead">ValueBridge makes practical digital tools: spreadsheet templates, document kits and small software apps for small businesses, professionals and households.</p>
<p>We are a Jamaican business. Our products come from hands-on experience in quality, compliance, safety, environmental management and business administration, and they are designed for the way small teams actually work: offline-friendly, buy once where possible, and with worked examples so you can see a tool working before you start.</p>
<h2>How we release products</h2><p>Nothing goes on sale until it has passed our review process. Before release, each product is tested on real computers and phones, then reviewed by real users or, for safety, finance, environmental and engineering products, by a qualified specialist. Licence and product wording are checked by an attorney. That is why every product is marked <b>Coming soon</b> today.</p>
<h2>Departments</h2><p>Templates · Business Tools · Productivity · Design Assets · Learning &amp; Development · Lifestyle Solutions</p>"""),
        "contact.html": ("Contact", "Contact", """<p class="lead">We'd like to hear from you.</p>
<div class="contact"><div><h3>General enquiries</h3><p><a href="mailto:hello@valuebridgeja.com">hello@valuebridgeja.com</a></p></div>
<div><h3>Product support</h3><p><a href="mailto:support@valuebridgeja.com">support@valuebridgeja.com</a></p><p class="small">For help with a product you have bought (once the store opens).</p></div></div>
<p class="small">We aim to reply within 3 working days. Please don't send passwords, payment details or other people's personal information by email.</p>"""),
        "faq.html": ("Frequently asked questions", "", """<h3>Can I buy anything today?</h3><p>Not yet. The store opens when the first products pass our review process. Releases are planned from December 2026.</p>
<h3>Why do products say "Coming soon"?</h3><p>Each product must pass testing, user or specialist review and a legal check before it is sold. The status line on each product shows where it is.</p>
<h3>Will prices change?</h3><p>Prices shown are planned prices and may change before release.</p>
<h3>How will I receive my files?</h3><p>Products are digital downloads delivered by email straight after payment. See <a href="how-downloads-work.html">How downloads work</a>.</p>
<h3>What software do I need?</h3><p>Each product page lists its format, for example an Excel workbook, Word and PDF documents, or a single HTML file that opens in a web browser. Supported versions will be listed on each product page at release, based on our own tests.</p>
<h3>Do you offer setup or custom work?</h3><p>Yes: see <a href="quote.html">Tailored setup</a>.</p>"""),
        "how-downloads-work.html": ("How downloads work", "", """<ol class="numbered"><li>Choose a product and check out. Payment is handled by our payment platform, which acts as the merchant of record.</li>
<li>You receive an email with your download link and receipt straight after payment.</li><li>Download the ZIP file and open the Start Here or README file first.</li>
<li>Keep a copy of your files. Your licence terms are included in the download and on our store policies page.</li>
<li>Problems? Email <a href="mailto:support@valuebridgeja.com">support@valuebridgeja.com</a> with your order number.</li></ol>
<p class="small">The store is not open yet; this page describes how it will work.</p>"""),
        "quote.html": ("Tailored setup", "", """<p class="lead">Prefer us to set things up for you? Our first service is the Business KPI Dashboard Tailored Setup.</p>
<p>We configure the Pro dashboard with your industry, KPIs, targets and revenue lines, load up to 12 months of your past figures and walk you through it. Planned price: US$149.</p>
<p><span class="badge">Coming soon</span> Enquiries open when the store launches. Until then, you can write to <a href="mailto:hello@valuebridgeja.com?subject=Tailored%20setup">hello@valuebridgeja.com</a>; please don't send business figures yet.</p>"""),
        "privacy.html": ("Privacy notice", "", """<p class="lead">This website does not use cookies, analytics, advertising trackers or forms.</p>
<p>Our website is hosted by Cloudflare, which processes technical data such as IP addresses to deliver and protect the site. Fonts are loaded from Google Fonts, which receives your IP address when a page loads.</p>
<p>If you email us, we use your message and email address only to reply to you, and we keep it no longer than we need to.</p>
<p>A full privacy policy will be published before the store opens and before we collect any customer details. Questions: <a href="mailto:hello@valuebridgeja.com">hello@valuebridgeja.com</a>.</p>"""),
        "policies.html": ("Store policies", "", """<p class="lead">Our licence, terms of sale, refund policy and privacy policy are being reviewed by a Jamaican attorney.</p>
<p>They will be published here before the store opens, and linked from every product page and the checkout.</p>"""),
    }
    for path, (t, act, b) in info.items():
        page(path, f"{t} · ValueBridge", f'<section class="wrap pagehead"><h1>{E(t)}</h1></section><section class="wrap prose">{b}</section>', t, 0, act)
    # Private test page for the Lemon Squeezy test-mode product (not linked, not indexed)
    if C.TEST_CHECKOUT_URL:
        tbody = f"""<section class="wrap pagehead"><h1>Checkout test</h1><p class="sub">Internal page. Test mode: use card 4242 4242 4242 4242, any future date, any CVC. No real charge is made.</p>
<p>{buy_button(C.TEST_CHECKOUT_URL, "Open test checkout")}</p>
<ol class="numbered"><li>Click the button. The checkout should open in a window over this page.</li><li>Pay with the test card.</li><li>Check that the receipt email arrives and the download link works.</li><li>Tell Claude the result.</li></ol></section>"""
    else:
        tbody = """<section class="wrap pagehead"><h1>Checkout test</h1><p class="sub">Internal page. No test checkout link has been set yet: add it as TEST_CHECKOUT_URL in data/catalog.py and rebuild.</p></section>"""
    page("test-checkout.html", "Checkout test · ValueBridge", tbody, "Internal", 0, head=LEMON_JS if C.TEST_CHECKOUT_URL else "", noindex=True)
    page("404.html", "Page not found · ValueBridge", '<section class="wrap pagehead"><h1>Page not found</h1><p><a href="/">Go to the home page</a></p></section>', "Not found", 0)
    PAGES.remove("404.html")

    sync_trials()
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for pth in PAGES:
            f.write(f"  <url><loc>{DOMAIN}/{'' if pth == 'index.html' else pth}</loc></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    print(f"Built {len(PAGES)+1} pages into site/")


if __name__ == "__main__":
    build()
