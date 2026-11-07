"""ValueBridge master catalogue: single source for tracker v4 and the website.
As at 31 Oct 2026. Gate status follows qa/QA-01 and the QA-02 snapshot.
Gate keys: G0 Market, G1 Build, G2 Tech QA, G3 Expert/users, G4 Fix & RC, G5 Marketing,
G6 Legal, G7 Proof, G8 Release readiness, G9 Publish.
Values: Y passed, P partly, N not done, AI = Claude pre-review only (not a sign-off), - not needed, ? confirm
"""

AS_AT = "31 Oct 2026"

DEPARTMENTS = [
    ("templates", "Templates", "Ready-to-use spreadsheets and document templates for running a business."),
    ("business-tools", "Business Tools", "Registers, audit kits and toolkits for safety, compliance, sustainability and finance."),
    ("productivity", "Productivity", "Software and toolkits that help you plan, focus and get documents done."),
    ("design-assets", "Design Assets", "Branding and social media resources for your projects."),
    ("learning-development", "Learning & Development", "Tools that help you build skills, careers and knowledge."),
    ("lifestyle", "Lifestyle Solutions", "Resources for your home, money and everyday life."),
]

COLLECTIONS = [
    ("business-planning", "Business Planning & Performance", "Plan, measure and report on how your business is doing."),
    ("finance", "Finance & Accounting", "Budgets, cash flow, bookkeeping and personal money tools."),
    ("productivity-ai", "Productivity & AI", "Desktop-style apps and AI workflows for everyday work."),
    ("careers", "Careers", "Resumes, cover letters and job applications."),
    ("marketing", "Social Media & Marketing", "Brand kits, content planners and social media templates."),
    ("safety", "Safety & Health", "Risk assessments, permits, toolbox talks, safety reports and policies."),
    ("quality-compliance", "Quality & Compliance", "Registers for permits, legal requirements, incidents and quality."),
    ("environment", "Environment", "Environmental audits, reports, policies and field forms."),
    ("esg-climate", "ESG & Climate", "ESG audits, sustainability reporting, policies and carbon management."),
    ("energy", "Energy & Renewables", "Audit kits for solar PV plants and wind farms."),
    ("project-management", "Project Management", "Project packs, reporting templates and dashboards."),
    ("security-operations", "Security & Operations", "Security audits, plans and reports, and operations management resources."),
    ("research", "Research & Analysis", "Software for qualitative and statistical research analysis."),
    ("lifestyle-solutions", "Lifestyle Solutions", "Tools for your home, household money and everyday life."),
    ("study-exams", "Study & Exams", "Revision planners, flashcards and practice exams."),
    ("technology", "Technology & Software", "ValueBridge apps that open in your web browser on phone and computer, designed to work offline on your own device."),
]

WEB_STATUS = {
    "testing": ("Coming soon", "Final testing · planned for December 2026"),
    "review": ("Coming soon", "Awaiting specialist review · planned for early 2027"),
    "review2027": ("Coming soon", "Awaiting specialist review · planned for 2027"),
    "dev": ("Coming soon", "In development"),
    "enquiry": ("Coming soon", "Enquiries open when the store launches"),
    "new": ("Coming soon", "Newly built · awaiting market review and testing"),
    "released": ("Available now", "Instant download after checkout"),
}

# Lemon Squeezy checkout.
# To release a product: set web="released" and checkout="https://valuebridgeja.lemonsqueezy.com/checkout/buy/<uuid>"
# on its add(...) line, run tools/build.py, commit and push. Do this only after gate G9 is signed in QA-02.
# TEST_CHECKOUT_URL: a test-mode product's checkout link, shown only on /test-checkout.html (noindex). Leave "" to hide.
STORE_URL = "https://valuebridgeja.lemonsqueezy.com"
TEST_CHECKOUT_URL = ""

# Common gate rows
def g(g0, g1, g2, g3, g5, g6):
    return {"G0": g0, "G1": g1, "G2": g2, "G3": g3, "G4": "N", "G5": g5, "G6": g6,
            "G7": "N", "G8": "N", "G9": "N"}

P = []  # products


def add(**k):
    k.setdefault("other", "")
    k.setdefault("bundles", [])
    k.setdefault("checks", 0)
    k.setdefault("checks_note", "")
    k.setdefault("also", [])
    k.setdefault("checkout", "")
    P.append(k)


# ---------------- Gate A (soft launch target 14 Dec 2026) ----------------
add(slug="pdf-studio", name="ValueBridge PDF Studio", version="1.0", dept="productivity", coll="productivity-ai",
    tier="A", route="Gate A", wave="Launch", price="39", other="Team US$149 · Site US$349", fmt="Software (single HTML file, offline)",
    short="A set of everyday PDF tools in one app that opens in your web browser and is designed to work offline on your own device.",
    bullets=["Merge, split, organise, rotate and extract pages",
             "Convert images, Word, text and CSV files to PDF, and PDF to images or text",
             "Watermarks, page numbers, headers, Bates numbering, signatures and form filling",
             "Password protection, metadata tools, redaction with page flattening (check every output before sharing)",
             "Workflows that chain steps and run them on batches of files"],
    gates=g("Y", "P", "N", "N", "N", "AI"), checks=1, checks_note="6 screenshots done; copy passes except the 'never uploads' claim (QA-27)",
    blockers="Support email in files; browser and device tests; network trace before any privacy claim; lawyer review of the device-count licence; decide trial build for the demo",
    reviewer="User trial (3-5 users)", web="testing", bundles=["productivity-pair"], listing="claude/ValueBridge_PDF_Studio_Listing.md")

add(slug="tempo", name="ValueBridge Tempo", version="1.0", dept="productivity", coll="productivity-ai",
    tier="A", route="Gate A", wave="Launch", price="29", other="Team US$119 · Site US$249", fmt="Software (single HTML file, offline)",
    short="Plan your day, protect your focus: tasks, scheduling, a focus timer, habits and reviews in one app for phone and desktop.",
    bullets=["Today view with a capacity meter, timeline and your three priorities",
             "Tasks with quick add, projects, priorities, checklists and repeats",
             "Week and day scheduler with drag and drop and a 7-day auto-plan",
             "Work/break focus timer, habits, insights, and daily and weekly reviews",
             "Alerts while Tempo is open, or through your calendar app via .ics export"],
    gates=g("Y", "P", "N", "N", "N", "AI"), checks=1, checks_note="Copy passes check 5 after QA fixes",
    blockers="Support email in files and a Help line in Settings; phone and browser tests (alerts, touch drag); screenshots and video; lawyer review of licence",
    reviewer="User trial (3-5 users)", web="testing", bundles=["productivity-pair"], listing="claude/ValueBridge_Tempo_Listing.md")

add(slug="resume-studio", name="ValueBridge Resume Studio", version="2.0", dept="learning-development", coll="careers",
    tier="A", route="Gate A", wave="Launch", price="29", other="Coach US$129 · Campus US$399 (full launch)", fmt="Software (single HTML file, offline)",
    short="Build, score and tailor resumes, write matching cover letters and track your applications in one app on your own device.",
    bullets=["8 templates with live preview and a fit-to-one-page option",
             "Resume Score with about 50 checks and a view of what a generic PDF parser reads",
             "Job match: paste a posting to see missing keywords and gaps",
             "Cover letters, application tracker and interview practice",
             "Scores are guidance only and do not promise interviews or offers"],
    gates=g("?", "P", "N", "N", "N", "AI"), checks=1, checks_note="10 screenshots done",
    blockers="Support email; 3-5 job-seeker trials; title and comparison fixes (QA-09); network trace; lawyer review of Personal tier",
    reviewer="User trial (3-5 job seekers)", web="testing", bundles=[], listing="claude/ValueBridge_Resume_Studio_Listing.md")

add(slug="kpi-dashboard-lite", name="Business KPI Dashboard – Lite", version="1.0", dept="templates", coll="business-planning",
    tier="A", route="Gate A", wave="Launch", price="19", fmt="Excel workbook (Blank + Sample) and quick-start guide",
    short="See your key business numbers in about 15 minutes a month: 10 KPIs with on track, watch and off track status lights.",
    bullets=["10 core KPIs: revenue, margins, profit, customers, churn, acquisition cost, conversion, order value, cash",
             "Status lights against your own targets, a month selector and year-to-date totals",
             "4 trend charts and locked formulas",
             "Sample and blank files plus a quick-start guide"],
    gates=g("?", "P", "N", "N", "N", "N"), checks=0, checks_note="Listing copy not in project docs (I-06)",
    blockers="Recreate listing copy; support email; desktop Excel test; lawyer review",
    reviewer="User trial", web="testing", bundles=[], listing="Not in project (I-06); Sales_and_Listing_Kit.md sent 23 Oct")

add(slug="kpi-dashboard-pro", name="Business KPI Dashboard – Pro", version="1.0", dept="templates", coll="business-planning",
    tier="A", route="Gate A", wave="Launch", price="39", fmt="Excel workbook (Blank + Sample) and quick-start guide",
    short="Everything in Lite, plus written monthly insights, an action plan, cash and break-even measures and a printable monthly report.",
    bullets=["15 KPIs with trend arrows and last-year comparison",
             "Written monthly insights and an action plan with overdue alerts",
             "Cash cover, break-even revenue and debtor days",
             "6 industry presets, 2 custom KPIs and a one-page monthly report"],
    gates=g("?", "P", "N", "N", "N", "N"), checks=0, checks_note="Listing copy not in project docs (I-06)",
    blockers="Recreate listing copy; support email; desktop Excel test; lawyer review",
    reviewer="User trial", web="testing", bundles=["business-starter"], listing="Not in project (I-06)")

add(slug="kpi-dashboard-tailored", name="Business KPI Dashboard – Tailored Setup", version="1.0", dept="business-tools", coll="business-planning",
    tier="Service", route="Service", wave="Launch", price="149", fmt="Service: configured workbook and walkthrough",
    short="We set up the Pro dashboard for your business: your KPIs, your targets and up to 12 months of your past figures.",
    bullets=["Short intake form about your business and targets",
             "Pro dashboard configured with your industry, KPIs and revenue lines",
             "Up to 12 months of history loaded, plus a walkthrough",
             "Sold by quote and invoice, not through the online store"],
    gates={"G0": "-", "G1": "-", "G2": "-", "G3": "-", "G4": "-", "G5": "N", "G6": "N", "G7": "N", "G8": "N", "G9": "N"},
    checks=0, checks_note="Service: website enquiry page only",
    blockers="Enquiry page wording cleared by lawyer; service terms; privacy notice before taking client data",
    reviewer="Lawyer (service terms)", web="enquiry", bundles=[], listing="Not in project")

add(slug="project-dashboard-kit", name="Project Dashboard Kit", version="1.0", dept="templates", coll="project-management",
    tier="A", route="Gate A", wave="Launch", price="29", fmt="Excel workbooks (Blank + Example)",
    short="Track several projects in one workbook: schedule, budget, risks, issues and changes, with a one-page status report.",
    bullets=["Dashboard with KPI cards, charts, milestones and a risk heat map",
             "Tasks with working-day durations, a predecessor, holidays and a Gantt view",
             "Planned and earned value, forecast cost and status lights",
             "Risks, issues, changes, costs and a 12-week resource view"],
    gates=g("Y", "P", "N", "N", "N", "AI"), checks=1, checks_note="Copy passes check 5",
    blockers="Support email; desktop Excel test; real-project test (launch plan section 10); lawyer review",
    reviewer="Real-project test (owner)", web="testing", bundles=["business-starter"], listing="claude/ValueBridge_Project_Dashboard_Listing.md")

add(slug="ai-prompt-workflow-toolkit", name="AI Prompt & Workflow Toolkit", version="1.0", dept="productivity", coll="productivity-ai",
    tier="A", route="Gate A", wave="Launch", price="29", fmt="Excel workbook, playbook (Word + PDF) and CSV",
    short="110 fill-in prompts, 12 workflow chains and a playbook for using the AI tool you already have in everyday business work.",
    bullets=["Prompt library in 11 categories with a prompt finder and builder",
             "12 workflow chains and a tracker for your own time estimates",
             "AI use and risk register and a place to record your own rules",
             "46-page playbook with methods, templates and a 30-day plan"],
    gates=g("Y", "P", "N", "N", "N", "AI"), checks=1, checks_note="Copy passes check 5",
    blockers="Support email; owner runs 5-10 prompts; desktop Excel test; non-affiliation additions; lawyer review",
    reviewer="Owner prompt tests", web="testing", bundles=[], listing="claude/ValueBridge_AI_Toolkit_Listing.md")

# ---------------- Gate B (accountant / safety practitioner) ----------------
add(slug="financial-dashboard-kit", name="Small Business Financial Dashboard Kit", version="1.0", dept="business-tools", coll="finance",
    tier="B", route="Gate B", wave="Launch", price="39", fmt="Excel workbooks (Blank + Example)",
    short="Budget, cash flow, profit and invoices in one workbook: enter your budget once, log payments in one place and the reports update.",
    bullets=["Dashboard, profit and loss and cash flow from one payment log",
             "13-week cash forecast and budget vs actual",
             "Sales tax tracker (records only; it does not file returns)",
             "A planning tool, not accounting or tax advice"],
    gates=g("?", "P", "N", "N", "N", "AI"), checks=1, checks_note="Copy passes check 5",
    blockers="Accountant review (required); support email; desktop Excel test; lawyer review",
    reviewer="R06d Accountant", web="review", bundles=["business-starter"], listing="claude/ValueBridge_Financial_Dashboard_Listing.md")

add(slug="personal-budget-system", name="Personal Budget System", version="1.0", dept="lifestyle", coll="lifestyle-solutions", also=["finance"],
    tier="B", route="Gate B", wave="Launch", price="29", fmt="Excel workbooks (Blank + Example)",
    short="One connected workbook for your money: log a payment once and your budget, accounts, goals and net worth update.",
    bullets=["Budget with a 'left to assign' check and a monthly review",
             "Bills calendar, paycheck planner and subscriptions review",
             "Savings goals, a pardner / susu planner and net worth by month",
             "Debt plan comparisons shown as illustrative estimates from your inputs"],
    gates=g("?", "P", "N", "N", "N", "AI"), checks=1, checks_note="Copy passes check 5",
    blockers="Accountant or adviser read; support email; desktop Excel test; lawyer review",
    reviewer="R06d Accountant", web="review", bundles=[], listing="claude/ValueBridge_Personal_Budget_Listing.md")

add(slug="business-plan-startup-kit", name="Business Plan & Startup Kit", version="1.0", dept="templates", coll="business-planning",
    tier="B", route="Gate B", wave="Launch", price="39", fmt="Excel workbooks, playbook and plan template (Word + PDF)",
    short="Plan a new business and prepare for funding conversations: a linked 36-month forecast, playbook and business plan template.",
    bullets=["21 linked sheets: start-up costs, revenue, costs, funding and a 36-month forecast",
             "Scenarios, pricing, validation log, lean canvas and competitor matrix",
             "68-task launch checklist and a funding readiness score (not lender approval)",
             "20-page playbook and a 14-section business plan template"],
    gates=g("Y", "P", "N", "N", "N", "AI"), checks=1, checks_note="Copy passes check 5",
    blockers="Accountant check of tax and payroll placeholders (required); support email; desktop Excel test; lawyer review",
    reviewer="R06d Accountant", web="review", bundles=[], listing="claude/ValueBridge_Startup_Kit_Listing.md")

SAFETY_BLOCK = "Safety practitioner review; rebuild per Safety Practitioner Review section 2 (NFPA edition, rate labels); support email; desktop tests; lawyer review"
add(slug="risk-assessment-toolkit", name="Risk Assessment Toolkit", version="2.0", dept="business-tools", coll="safety",
    tier="C", route="Gate B", wave="Launch", price="24", other="Consultant US$99 (full launch)", fmt="Excel workbook",
    short="Record hazards, score them on a 5×5 matrix and track controls, with a job safety analysis and worker sign-off.",
    bullets=["Risk register with scoring, residual risk, review dates and overdue actions",
             "Live 5×5 heat map using your own rating bands",
             "Task analysis (JSA), review and sign-off, and worker acknowledgement",
             "Hazard library with typical harms and example controls"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), checks=0, checks_note="Copy needs Works-with fix",
    blockers=SAFETY_BLOCK, reviewer="R06a Safety practitioner", web="review", bundles=["workplace-safety"], listing="claude/ValueBridge_Safety_Listings.md")
add(slug="toolbox-talks-pack", name="Safety Toolbox Talks Pack: 52 Talks", version="2.0", dept="business-tools", coll="safety",
    tier="C", route="Gate B", wave="Launch", price="19", other="Consultant US$79 (full launch)", fmt="Word + PDF",
    short="A year of weekly 10-minute safety talks for supervisors, each with key points, questions and a sign-off sheet.",
    bullets=["52 talks plus a blank template",
             "Why it matters, key points, do's and don'ts and discussion questions",
             "Attendance and sign-off sheet for each talk",
             "Annual planner to schedule and log talks"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), checks=0, blockers=SAFETY_BLOCK, reviewer="R06a Safety practitioner",
    web="review", bundles=["workplace-safety"], listing="claude/ValueBridge_Safety_Listings.md")
add(slug="permit-to-work-bundle", name="Permit-to-Work Templates", version="2.0", dept="business-tools", coll="safety",
    tier="C", route="Gate B", wave="Launch", price="19", other="Consultant US$79 (full launch)", fmt="Word + PDF",
    short="Editable permit templates for higher-risk work, with registers and an audit checklist for running a permit system.",
    bullets=["7 permits: general work, hot work, confined space, work at height, isolation, excavation, lifting",
             "Extension, shift handover and hand-back sections",
             "Permit register, authorised persons register and audit checklist",
             "Covers permit topics found in common frameworks; adapt to your workplace"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), checks=0, blockers=SAFETY_BLOCK, reviewer="R06a Safety practitioner",
    web="review", bundles=["workplace-safety"], listing="claude/ValueBridge_Safety_Listings.md")
add(slug="safety-statistics-monitor", name="Safety Statistics Monitor", version="2.0", dept="business-tools", coll="safety",
    tier="C", route="Gate B", wave="Launch", price="49", other="Consultant US$199 (full launch)", fmt="Excel workbook",
    short="Log each incident once and see safety rates under three common recording approaches, against your targets and last year.",
    bullets=["Incident log with US-style, UK-style and ILO-style rate calculations",
             "Dashboard with headline rates, leading indicators and charts",
             "Separate employee and contractor hours; 5 years of monthly data",
             "Reference table of definitions and rate bases (check current rules)"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), checks=0, blockers=SAFETY_BLOCK, reviewer="R06a Safety practitioner",
    web="review", bundles=["workplace-safety"], listing="claude/ValueBridge_Safety_Listings.md")

# ---------------- Not at soft launch ----------------
add(slug="social-media-branding-kit", name="Social Media & Branding Kit (works with Canva) – Starter", version="1.0", dept="design-assets", coll="marketing",
    tier="A", route="Full launch at earliest", wave="Launch", price="19", fmt="Excel planner, playbook, Canva template links",
    short="Plan your brand and content: a brand setup and content planner with caption and hook banks, plus starter Canva templates.",
    bullets=["Brand setup with an indicative colour-contrast check",
             "90-day content calendar, 60 captions and 40 hooks",
             "Size guide, Caribbean dates and a 30-day launch plan",
             "21-page playbook"],
    gates=g("Y", "N", "N", "N", "N", "AI"), checks=0, checks_note="Legal pre-review: do not sell yet",
    blockers="4 Canva steps (template links, replace stock photo, strip third-party content, written licence confirmation); support email; more templates before raising price",
    reviewer="User trial", web="dev", bundles=[], listing="claude/ValueBridge_Social_Branding_Kit_Listing.md")

# ---------------- Wave 2: review and release ----------------
W2_SAFETY = "Safety practitioner review (W2-1); rebuild from review findings; support email; desktop tests; lawyer review"
add(slug="safety-report-writing-kit", name="Safety Report Writing Kit", version="1.0", dept="business-tools", coll="safety",
    tier="C", route="Wave 2 (W2-1)", wave="Wave 2", price="39", other="Consultant US$149", fmt="Word + PDF guide and templates, Excel tracker",
    short="Write clear incident, inspection, audit and monthly safety reports with templates, a phrase bank and a report tracker.",
    bullets=["25-page writing guide with investigation and finding-statement methods",
             "13 report templates from flash report to board report",
             "Report tracker with due dates, a quality check and monthly rates",
             "Phrase bank of clear alternatives to vague wording"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), blockers=W2_SAFETY, reviewer="R06a Safety practitioner",
    web="review2027", bundles=["safety-documentation"], listing="claude/ValueBridge_Safety_Report_Policy_Kits_Listing.md")
add(slug="safety-policy-kit", name="Safety Policy Kit", version="1.0", dept="business-tools", coll="safety",
    tier="C", route="Wave 2 (W2-1)", wave="Wave 2", price="49", other="Consultant US$199", fmt="Word + PDF manual, Excel register",
    short="A policy statement and 30 topic policies to adapt, plus a register to track review, acknowledgement and gaps.",
    bullets=["How to choose, write, approve and roll out policies",
             "Policy statement plus 30 topic policies, including severe weather",
             "Register with an applicability screen, review status and acknowledgements",
             "The ESG Policy Kit has one general H&S policy; this is the fuller safety set"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), blockers=W2_SAFETY + "; employment-law read of harassment policies", reviewer="R06a Safety practitioner",
    web="review2027", bundles=["safety-documentation"], listing="claude/ValueBridge_Safety_Report_Policy_Kits_Listing.md")
add(slug="traffic-management-plan-kit", name="Traffic Management Plan Kit", version="1.0", dept="business-tools", coll="safety",
    tier="C", route="Wave 2 (W2-1)", wave="Wave 2", price="39", other="Consultant US$149", fmt="Word + PDF template, Excel workbooks",
    short="Plan site traffic and temporary traffic control with a plan template, risk register and planning calculator.",
    bullets=["37-page plan template with 10 appendices",
             "Risk register, hazard library, inspections, deliveries and incidents",
             "Planning calculator for tapers and sign spacing (planning estimate only)",
             "Confirm layouts against your road authority's manual and a competent designer"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), blockers=W2_SAFETY + " (traffic management experience)", reviewer="R06a Safety practitioner (traffic)",
    web="review2027", bundles=[], listing="claude/ValueBridge_TMP_Kit_Listing.md")

CRS_BLOCK = "EHS practitioner review (W2-2); Quality & Compliance review findings; 'starter pointers to verify' wording; support email; desktop tests; lawyer review"
for slug, nm, pr, sh in [
    ("permits-licences-register", "Permits & Licences Register", "39", "Track permits and licences across sites, with expiry and renewal flags and linked actions."),
    ("legal-requirements-register", "Legal & Statutory Requirements Register", "39", "Record the legal requirements that apply to you, with starter pointers to verify and review dates."),
    ("environmental-register", "Environmental Register", "39", "Record environmental aspects, monitoring, waste and emissions estimates for up to 20 sites."),
    ("incident-capa-register", "Incident, Near Miss & Corrective Action Register", "35", "Log incidents and near misses and track corrective actions through to an effectiveness check."),
    ("quality-register", "Quality Register", "39", "Nonconformities, complaints, audits and document control in one register."),
]:
    add(slug=slug, name=nm, version="1.0", dept="business-tools", coll="quality-compliance", tier="C", route="Wave 2 (W2-2)",
        wave="Wave 2", price=pr, fmt="Excel workbooks (Blank + Example), playbook",
        short=sh,
        bullets=["Up to 20 sites, each with country and industry", "Dashboard, trend view and shared action tracker",
                 "Part of the Compliance Register Suite; 18-page playbook included"],
        gates=g("P", "P", "N", "AI", "N", "AI"), blockers=CRS_BLOCK, reviewer="R06c Quality & compliance; EHS practitioner",
        web="review2027", bundles=[], listing="claude/ValueBridge_Compliance_Register_Suite_Listing.md")
add(slug="ehs-registers-suite", name="EHS Registers Suite", version="1.0", dept="business-tools", coll="quality-compliance",
    tier="C", route="Wave 2 (W2-2)", wave="Wave 2", price="99", fmt="Excel workbook (Blank + Example), playbook",
    short="Permits, legal requirements, environmental and incident registers together in one linked workbook.",
    bullets=["Four registers sharing one action tracker and dashboard", "Up to 20 sites", "Starter pointers to verify for several Caribbean countries, the US and the UK"],
    gates=g("P", "P", "N", "AI", "N", "AI"), blockers=CRS_BLOCK + "; rename from 'EHS Compliance Suite'", reviewer="R06c; EHS practitioner",
    web="review2027", bundles=[], listing="claude/ValueBridge_Compliance_Register_Suite_Listing.md")
add(slug="integrated-compliance-suite", name="Integrated Compliance Register Suite", version="1.0", dept="business-tools", coll="quality-compliance",
    tier="C", route="Wave 2 (W2-2)", wave="Wave 2", price="129", fmt="Excel workbook (Blank + Example), playbook",
    short="All five registers (permits, legal, environmental, incidents and quality) in one linked workbook.",
    bullets=["Five registers with a shared action tracker", "Dashboard and trend view across sites", "18-page playbook"],
    gates=g("P", "P", "N", "AI", "N", "AI"), blockers=CRS_BLOCK, reviewer="R06c; EHS practitioner",
    web="review2027", bundles=[], listing="claude/ValueBridge_Compliance_Register_Suite_Listing.md")

ESG_BLOCK = "ESG auditor review (W2-3); framework landscape re-check; verdict labels (QA-26); support email; desktop tests; lawyer review"
add(slug="esg-audit-kit", name="ESG Audit Kit", version="1.0", dept="business-tools", coll="esg-climate",
    tier="C", route="Wave 2 (W2-3)", wave="Wave 2", price="59", other="Consultant US$249", fmt="Excel workbooks, playbook and report template",
    short="Run a scored ESG readiness review: a 148-item checklist, findings tracker, GHG inventory and printable report.",
    bullets=["Checklist in 16 sections with Foundation and Advanced levels",
             "Findings with target dates, KPI register, GHG inventory and targets",
             "Results shown as meeting or not meeting the thresholds you set",
             "A readiness review aid; not assurance"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), blockers=ESG_BLOCK + "; rename from 'ESG Compliance Audit Kit'", reviewer="R06b ESG auditor",
    web="review2027", bundles=["esg-audit", "esg-complete"], listing="claude/ValueBridge_ESG_Audit_Listings.md")
add(slug="esg-audit-resource-pack", name="ESG Audit Resource Pack", version="1.0", dept="business-tools", coll="esg-climate",
    tier="C", route="Wave 2 (W2-3)", wave="Wave 2", price="29", other="Consultant US$119", fmt="Word + PDF forms, Excel logs",
    short="The forms around an ESG audit: requests, materiality, data traces, interviews, claims screening and close-out.",
    bullets=["24 forms from scope letter to close-out", "Audit logs workbook with a dashboard", "Companion to the ESG Audit Kit"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), blockers=ESG_BLOCK + "; labour specialist for worker-interview forms", reviewer="R06b ESG auditor",
    web="review2027", bundles=["esg-audit", "esg-complete"], listing="claude/ValueBridge_ESG_Audit_Listings.md")
add(slug="esg-report-writing-kit", name="ESG Report-Writing Kit", version="1.0", dept="business-tools", coll="esg-climate",
    tier="C", route="Wave 2 (W2-3)", wave="Wave 2", price="49", other="Consultant US$199", fmt="Word + PDF template and guide, Excel workbook",
    short="Build and check your own sustainability report: template, data workbook, claims check and writing guide.",
    bullets=["18-page report template with guidance", "Metrics register, GHG calculator, targets and content index",
             "Claims check that flags wording to review", "16-page writing guide"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), blockers=ESG_BLOCK, reviewer="R06b ESG auditor",
    web="review2027", bundles=["esg-starter", "esg-complete"], listing="claude/ValueBridge_ESG_Report_Policy_Listings.md")
add(slug="esg-policy-kit", name="ESG Policy Kit", version="1.0", dept="business-tools", coll="esg-climate",
    tier="C", route="Wave 2 (W2-3)", wave="Wave 2", price="49", other="Consultant US$199", fmt="Word + PDF policies, Excel register",
    short="17 one-page ESG policy templates and a register to track adoption, acknowledgement and training.",
    bullets=["17 policy templates with local-law pointers to check", "Gap assessment and policy register",
             "Implementation guide; a starting point to review with a qualified adviser"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), blockers=ESG_BLOCK + "; employment/corporate lawyer read of all 17 policies", reviewer="R06b; lawyer",
    web="review2027", bundles=["esg-starter", "esg-complete"], listing="claude/ValueBridge_ESG_Report_Policy_Listings.md")

ENV_BLOCK = "Market gap review first (G0); environmental auditor review (W2-3); guide depth vs price (QA-12); support email; desktop tests; lawyer review"
for slug, nm, pr, cp, sh, bl in [
    ("environmental-audit-kit", "Environmental Management Audit Kit", "59", "249",
     "A scored EMS and compliance audit checklist with findings, permits, monitoring, waste and resources sheets.",
     ["126-item checklist in 16 sections", "Obligations, monitoring, waste and resource sheets", "Printable audit report and playbook"]),
    ("environmental-resource-kit", "Environmental Management Resource Kit", "29", "119",
     "Forms for before, during and after an environmental audit, including permit and data traces and a waste trail.",
     ["25 forms", "Audit logs workbook with dashboard", "Companion to the Audit Kit"]),
    ("environmental-report-writing-kit", "Environmental Report-Writing Kit", "49", "199",
     "Plan, gather the numbers, write and check an environmental performance report that is ready for review.",
     ["15-section report template", "Data workbook with claims check", "Writing guide"]),
    ("environmental-policy-kit", "Environmental Policy Kit", "49", "199",
     "16 one-page environmental policies with a gap assessment and register to track adoption and review.",
     ["16 policy templates", "Gap assessment and policy register", "Implementation guide"]),
]:
    add(slug=slug, name=nm, version="1.0", dept="business-tools", coll="environment", tier="C", route="Wave 2 (W2-3)",
        wave="Wave 2", price=pr, other=f"Consultant US${cp}", fmt="Excel workbooks and Word + PDF documents", short=sh, bullets=bl,
        gates=g("N", "P", "N", "AI", "N", "AI"), blockers=ENV_BLOCK, reviewer="R06b Environmental auditor",
        web="review2027", bundles=[], listing="claude/ValueBridge_Environmental_Listings.md")
for s in ["environmental-audit-kit", "environmental-resource-kit"]:
    next(x for x in P if x["slug"] == s)["bundles"] += ["env-audit", "env-complete"]
for s in ["environmental-report-writing-kit", "environmental-policy-kit"]:
    next(x for x in P if x["slug"] == s)["bundles"] += ["env-starter", "env-complete"]

CARB_BLOCK = "Market gap review first (G0); GHG verifier and carbon market specialist (W2-4); verdict labels; factor sourcing (QA-13); support email; desktop tests; lawyer review"
for slug, nm, pr, cp, sh, bl, bund in [
    ("carbon-footprint-calculator-kit", "Carbon Footprint Calculator Kit", "49", "199",
     "Estimate Scope 1, 2 and 3 emissions from your inputs, track a base year and plan reduction actions.",
     ["Fuels, refrigerants, electricity and Scope 3 screening", "Base year, targets and action cost ranking", "Indicative factor library to verify and replace"],
     ["carbon-starter", "carbon-complete"]),
    ("carbon-credit-tracker", "Carbon Credit Portfolio & Registry Tracker", "49", "199",
     "Know what you bought, what you retired and what you can still claim, and test claims against the rules you set.",
     ["Project screening against your own criteria", "Purchases, retirements and inventory", "Not financial or investment advice"],
     ["carbon-complete"]),
    ("carbon-inventory-review-kit", "Carbon Inventory Review Kit", "59", "249",
     "Check a greenhouse gas inventory before outside verification: checklist, sampling, data traces and findings.",
     ["110-item checklist", "Sampling, data trace and materiality sheets", "Readiness review only; not a verification opinion"],
     ["carbon-complete"]),
    ("carbon-playbook-policy-pack", "Carbon Management Playbook & Policy Pack", "49", "199",
     "A plain-language carbon management playbook with six policy templates, a plan template and a training deck.",
     ["35-page playbook and glossary", "6 policy templates and a management plan template", "18-slide training deck"],
     ["carbon-starter", "carbon-complete"]),
]:
    add(slug=slug, name=nm, version="1.0", dept="business-tools", coll="esg-climate", tier="C", route="Wave 2 (W2-4)",
        wave="Wave 2", price=pr, other=f"Consultant US${cp}", fmt="Excel workbooks and Word + PDF documents", short=sh, bullets=bl,
        gates=g("N", "P", "N", "AI", "N", "AI"), blockers=CARB_BLOCK, reviewer="R06b GHG verifier; carbon market specialist",
        web="review2027", bundles=bund, listing="claude/ValueBridge_Carbon_Management_Listings.md")

ENG_BLOCK = "PV / wind engineer review (W2-5); verdict labels (QA-26); support email; desktop tests; lawyer review"
add(slug="solar-pv-audit-kit", name="Solar PV Plant Audit Kit", version="1.0", dept="business-tools", coll="energy",
    tier="C", route="Wave 2 (W2-5)", wave="Wave 2", price="59", other="Consultant US$249", fmt="Excel workbooks, playbook, report template, field checklist",
    short="A scored audit checklist for utility-scale solar PV plants, with string tests, thermography and performance sheets.",
    bullets=["200 items in 18 sections, including storm readiness and cybersecurity", "String tests, thermography and performance ratio",
             "Results shown against the thresholds you set; printable report"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), blockers=ENG_BLOCK, reviewer="R06e PV engineer",
    web="review2027", bundles=["solar-pv-audit"], listing="claude/ValueBridge_Solar_PV_Audit_Kit_Listing.md")
add(slug="solar-pv-audit-resource-pack", name="Solar PV Plant Audit Resource Pack", version="1.0", dept="business-tools", coll="energy",
    tier="C", route="Wave 2 (W2-5)", wave="Wave 2", price="29", other="Consultant US$119", fmt="Word + PDF forms, Excel logs",
    short="22 forms and audit logs for planning, running and closing out a solar PV plant audit.",
    bullets=["Document requests, audit plan, briefings and interview records", "Pre- and post-storm checklists", "Companion to the Audit Kit"],
    gates=g("P", "P", "N", "AI", "N", "AI"), blockers=ENG_BLOCK, reviewer="R06e PV engineer",
    web="review2027", bundles=["solar-pv-audit"], listing="claude/ValueBridge_Solar_PV_Audit_Resource_Pack_Listing.md")
add(slug="wind-farm-audit-kit", name="Wind Farm Audit Kit", version="1.0", dept="business-tools", coll="energy",
    tier="C", route="Wave 2 (W2-5)", wave="Wave 2", price="59", other="Consultant US$249", fmt="Excel workbooks, playbook, report template, field checklist",
    short="A scored audit checklist for onshore wind farms, with turbine, blade, lightning protection and performance sheets.",
    bullets=["200 items in 18 sections", "Turbine register, blades, LPS tests and bolt checks",
             "Indicative power curve screen (not a power performance test)"],
    gates=g("Y", "P", "N", "AI", "N", "AI"), blockers=ENG_BLOCK, reviewer="R06e Wind turbine engineer",
    web="review2027", bundles=[], listing="claude/ValueBridge_Wind_Farm_Audit_Kit_Listing.md")

BOOKS_BLOCK = "Accountant review (W2-6); one real month run in parallel; buy-once vs subscription pricing (QA-11); subscription terms (Schedule 5); support email; lawyer review"
add(slug="books-free", name="ValueBridge Books – Free", version="1.0", dept="business-tools", coll="finance",
    tier="B", route="Wave 2 (W2-6)", wave="Wave 2", price="0", fmt="Software (browser app)",
    short="Simple accounting for micro businesses and non-profits: sales, stock, bills, expenses, invoices and basic reports.",
    bullets=["Point of sale, stock, bills and expenses", "Up to 25 invoices a month and payroll for 2", "Profit and loss, balance sheet and a deadline calendar"],
    gates=g("?", "P", "N", "N", "N", "AI"), blockers=BOOKS_BLOCK, reviewer="R06d Accountant",
    web="review2027", bundles=[], listing="claude/ValueBridge_Books_notes.md")
add(slug="books-business", name="ValueBridge Books – Business", version="1.0", dept="business-tools", coll="finance",
    tier="B", route="Wave 2 (W2-6)", wave="Wave 2", price="15/month", other="US$150/year; buy-once price under review", fmt="Software (browser app)",
    short="Adds bank import and reconciliation, quotes, statements, journals, cash flow and roles for growing businesses.",
    bullets=["Bank import and reconciliation", "Quotes, statements, ageing and journals", "Up to 5 users"],
    gates=g("?", "P", "N", "N", "N", "AI"), blockers=BOOKS_BLOCK, reviewer="R06d Accountant",
    web="review2027", bundles=[], listing="claude/ValueBridge_Books_notes.md")
add(slug="books-pro", name="ValueBridge Books – Pro", version="1.0", dept="business-tools", coll="finance",
    tier="B", route="Wave 2 (W2-6)", wave="Wave 2", price="39/month", other="US$390/year; buy-once price under review", fmt="Software (browser app)",
    short="Adds multi-currency, projects, fixed assets, approvals, budgets and a 13-week forecast.",
    bullets=["Multi-currency and projects", "Fixed assets, approvals and budget vs actual", "Unlimited users"],
    gates=g("?", "P", "N", "N", "N", "AI"), blockers=BOOKS_BLOCK, reviewer="R06d Accountant",
    web="review2027", bundles=[], listing="claude/ValueBridge_Books_notes.md")


# ---------------- Built 30 Oct 2026, confirmed as ValueBridge products 31 Oct (not yet through G0) ----------------
NEW_BLOCK = "G0 market and overlap review; listing doc; price; support email; tests; reviewer per tier; lawyer review"
for slug, nm, dept, coll, tier, rev, fmt, sh, url in [
    ("security-audit-kit", "Security Audit Kit", "business-tools", "security-operations", "C", "R06f Security practitioner (new role)",
     "Kit (format to confirm)", "A structured kit for planning and recording a security review, with findings and follow-up actions.",
     "https://claude.ai/artifact/JHzrUzeXBZtxcY9zyAjSQk"),
    ("security-plan-template", "Security Plan Development Template", "business-tools", "security-operations", "C", "R06f Security practitioner (new role)",
     "Template (format to confirm)", "A template for developing a written security plan for a site or organisation.",
     "https://claude.ai/artifact/TqNyNsG3auYAZvGM2izafe"),
    ("security-reporting-template", "Security Reporting Template", "business-tools", "security-operations", "C", "R06f Security practitioner (new role)",
     "Template (format to confirm)", "A template for clear, consistent security reports.",
     "https://claude.ai/artifact/9tsDXqhnQ6hjEH5TfwgDLK"),
    ("security-management-resource-kit", "Security Management Resource Kit", "business-tools", "security-operations", "C", "R06f Security practitioner (new role)",
     "Kit (format to confirm)", "Supporting forms and resources for managing security day to day.",
     "https://claude.ai/artifact/Dm6RuYT8nmUxgL4aooqPur"),
    ("operations-management-resource-kit", "Operations Management Resource Kit", "business-tools", "security-operations", "A", "User trial",
     "Kit (format to confirm)", "Practical resources for planning, running and reviewing day-to-day operations.",
     "https://claude.ai/artifact/QukiDsv2qH6zpKN6qUsZQV"),
    ("project-management-pack", "Project Management Pack", "templates", "project-management", "A", "User trial / real-project test",
     "Templates (format to confirm)", "Templates for running a project from start-up to close.",
     "https://claude.ai/artifact/H1nqkdZWDgig7eQxH2qjXU"),
    ("project-reporting-templates", "Project Reporting Templates Suite", "templates", "project-management", "A", "User trial",
     "Templates (format to confirm)", "A set of templates for project status and progress reporting.",
     "https://claude.ai/artifact/To4C6Xmq9PfWgS7QAHDWDp"),
    ("ims-policy-procedure-suite", "Integrated Management System Policy & Procedure Template Suite", "business-tools", "quality-compliance", "C", "R06c Quality & compliance",
     "Templates (format to confirm)", "Policy and procedure templates for an integrated quality, environmental and safety management system.",
     "https://claude.ai/artifact/8khHhC91G7aLB4hFXfUgt5"),
    ("qda-studio", "QDA Studio", "learning-development", "research", "A", "User trial (researchers)",
     "Software (browser app)", "Qualitative data analysis in your browser: import transcripts, code text, build a codebook, run queries and export reports.",
     "https://claude.ai/artifact/E7we8P5Vdr6cVMPWZKPd1y"),
    ("sem-studio", "SEM Studio", "learning-development", "research", "A", "User trial + statistician check of results",
     "Software (browser app)", "Structural equation modelling in your browser for research projects.",
     "https://claude.ai/artifact/Uwv6zXdS27HLnS9L1cs8Xy"),
]:
    add(slug=slug, name=nm, version="1.0", dept=dept, coll=coll, tier=tier, route="To plan at G0", wave="Unassigned (G0)",
        price="TBA", fmt=fmt, short=sh, bullets=["Full details will be published at release"],
        gates=g("N", "P", "N", "N", "N", "N"), checks=0, checks_note="No listing doc yet",
        blockers=NEW_BLOCK, reviewer=rev, web="new", bundles=[], listing="None yet (artifact: " + url + ")")

# ---------------- Lifestyle web-app drafts (status note: working drafts; must move to ValueBridge hosting before sale) ----------------
for slug, nm, sh, url in [
    ("kingston-basket", "Kingston Basket", "A household shopping and grocery planning app.", "https://claude.ai/artifact/UjrmT71PfsTM55urszYaav"),
    ("home-improvement-planner", "Property & Home Improvement Planner", "Plan home improvement projects: scope, budget and progress in one place.", "https://claude.ai/artifact/T9hwvRBTu7zMoVEkxHf6oG"),
    ("room-yard-planner", "Room & Yard Planner", "Sketch and plan room and yard layouts before you buy or build.", "https://claude.ai/artifact/Maxdm5RcphtzKSSK2nryzg"),
]:
    add(slug=slug, name=nm, version="draft", dept="lifestyle", coll="lifestyle-solutions", tier="A", route="To plan at G0",
        wave="Unassigned (G0)", price="TBA", fmt="Software (browser app)", short=sh,
        bullets=["Full details will be published at release"],
        gates=g("N", "N", "N", "N", "N", "N"), checks=0, checks_note="Working draft; no listing doc",
        blockers="G0 market review; finish build and move to ValueBridge hosting; listing doc; price; tests; user trial; lawyer review",
        reviewer="User trial", web="dev", bundles=[], listing="None yet (artifact: " + url + ")")

# ---------------- Social packs (design drafts; placement chosen by the owner 7 Nov 2026) ----------------
for slug, nm, dept, coll, sh, url in [
    ("small-business-social-pack", "Small Business Social Pack", "business-tools", "business-planning",
     "Ready-made social media post designs for small businesses: promotions, announcements, opening hours and customer thank-yous.",
     "https://claude.ai/artifact/1es2NU2wqYCzPdFC3m8ent"),
    ("coaches-creators-social-pack", "Coaches & Creators Social Pack", "design-assets", "marketing",
     "Social media post designs for coaches and content creators: tips, quotes, offers and session announcements.",
     "https://claude.ai/artifact/DZ46rh7U65xSztGGJjkwWx"),
    ("beauty-wellness-social-pack", "Beauty & Wellness Social Pack", "lifestyle", "lifestyle-solutions",
     "Social media post designs for salons, spas, barbers and wellness services: services, price lists, bookings and offers.",
     "https://claude.ai/artifact/QhsUbVXz4JrVZfGz7QHte4"),
    ("real-estate-social-pack", "Real Estate Social Pack", "lifestyle", "lifestyle-solutions",
     "Social media post designs for property listings: new listings, open houses, sold notices and market tips.",
     "https://claude.ai/artifact/EnnyrVwW7JNG1irVP7eKPD"),
]:
    add(slug=slug, name=nm, version="draft", dept=dept, coll=coll, tier="A", route="To plan at G0",
        wave="Unassigned (G0)", price="TBA", fmt="Social media templates (format to confirm: Canva template links or PNG/PDF)",
        short=sh, bullets=["Full details will be published at release"],
        gates=g("N", "P", "N", "N", "N", "N"), checks=0, checks_note="Design draft; no listing doc",
        blockers="G0 market review and price; export as Canva template links or PNG/PDF; remove stock photos and third-party names; Canva licence check; listing doc; lawyer review",
        reviewer="User trial", web="dev", bundles=[], listing="None yet (artifact: " + url + ")")

# ---------------- Software built 3–7 Nov 2026 (listing docs in the project) ----------------
add(slug="dueline", name="ValueBridge Dueline", version="1.0.0", dept="lifestyle", coll="lifestyle-solutions", also=["productivity-ai"],
    tier="A", route="Gate A", wave="Launch", price="19", fmt="Software (single HTML file, offline)",
    short="Renewals, expiry dates, deadlines and birthdays in one private place, in the right order, with the yearly cost worked out.",
    bullets=["Builds your list from your household, vehicles and home; you fill in the dates on one screen",
             "Moves tax deadlines off weekends and public holidays",
             "Warns when a renewal needs another document to be valid first",
             "Logs each renewal and rolls on to the next date",
             "Shows the next 12 months' costs and a monthly amount to put aside",
             "Alerts while Dueline is open, or through your phone's calendar app via .ics export"],
    gates=g("AI", "Y", "AI", "N", "AI", "AI"), checks=1, checks_note="Build checks passed; real-device tests pending",
    blockers="Owner real-device tests (Safari, Firefox, Edge, Android, iPhone, .ics imports); user trial; lawyer review",
    reviewer="User trial (3-5 users)", web="testing", bundles=[], listing="claude/ValueBridge_Dueline_Listing.md")
add(slug="highlighter", name="ValueBridge Highlighter", version="1.0.0", dept="learning-development", coll="study-exams",
    tier="A", route="Gate A", wave="Launch", price="19", fmt="Software (single HTML file, offline)",
    short="Revise in the gaps in your day: flashcards, quizzes, games and timed mock exams, paced to your exam dates.",
    bullets=["Add a subject and its exam date; paste your notes and Highlighter finds flashcards in them",
             "Or prepare a prompt for the AI chat assistant you already use",
             "Quizzes, games and timed mock exams",
             "Study pace planned around your exam dates",
             "Works offline with no account; your data stays on your device"],
    gates=g("AI", "Y", "AI", "N", "AI", "AI"), checks=1, checks_note="Build checks passed; real-device tests pending",
    blockers="Owner real-device tests (Safari, iPhone/iPad, Android, read-aloud voices); user trial with students; lawyer review; name conflict check (G0)",
    reviewer="User trial (students)", web="testing", bundles=[], listing="claude/ValueBridge_Highlighter_Listing.md")
add(slug="keepline", name="ValueBridge Keepline", version="1.0.0", dept="lifestyle", coll="lifestyle-solutions", also=["finance"],
    tier="B", route="Specialist review", wave="Launch", price="24", fmt="Software (single HTML file, offline)",
    short="Your pensions, insurance cover and savings in one private place, tracked against your own targets.",
    bullets=["Log a balance whenever a statement arrives; charts show how each account has moved",
             "Checks whether planned contributions keep pace with your targets",
             "Insurance cover with premiums and renewal dates",
             "One-page summary to take to a licensed adviser",
             "Optional passcode encrypts your figures on your device",
             "A tracking and planning aid, not financial, pension or insurance advice"],
    gates=g("AI", "Y", "AI", "N", "AI", "AI"), checks=1, checks_note="Build checks passed; real-device tests pending",
    blockers="Financial adviser or accountant review (R06d); owner real-device tests; lawyer review",
    reviewer="R06d Finance", web="review", bundles=[], listing="claude/ValueBridge_Keepline_Listing.md")
add(slug="estate-plan-organizer", name="ValueBridge Estate Plan Organizer", version="1.0.0", dept="lifestyle", coll="lifestyle-solutions",
    tier="C", route="Specialist review", wave="Launch", price="24", fmt="Software (single HTML file, offline)",
    short="Everything your executor and family need to know, in one private place, with a letter of instruction ready to hand over.",
    bullets=["What you own and owe, and which assets pass by your will or directly to a joint owner or nominee",
             "Beneficiaries, executor, guardians and where every original document is kept",
             "Your wishes for your funeral, pets and digital accounts",
             "Readiness checklist and a guide of points to check with your attorney",
             "An organizer and planning aid; not a will and not legal advice"],
    gates=g("AI", "Y", "AI", "N", "AI", "AI"), checks=1, checks_note="Build checks passed; real-device tests pending",
    blockers="Wills & estates attorney review (R06g, can combine with G6); owner real-device tests",
    reviewer="R06g Wills & estates attorney", web="review", bundles=[], listing="claude/ValueBridge_Estate_Plan_Organizer_Listing.md")
add(slug="ledgerline-bursar", name="Ledgerline Bursar", version="1.0", dept="business-tools", coll="finance",
    tier="B", route="To plan at G0", wave="Unassigned (G0)", price="79", fmt="Software (single HTML file, offline)",
    short="A finance desk for a school bursary: fees, receipts, payroll, payables, budget, bank and an audit pack in one app.",
    bullets=["Profiles for high school, primary, private/prep and college",
             "Fee payments with numbered receipts, invoices, statements and arrears",
             "Payroll with Jamaican statutory deductions (rates editable; confirm with the authorities)",
             "Supplier invoices, budget tracking, deposit slips and bank reconciliation",
             "Approval roles and an audit trail"],
    gates=g("N", "P", "N", "N", "N", "N"), checks=0, checks_note="Support email placeholder in README and LICENCE",
    blockers="G0 market and overlap review (Books, Virtual Accountant); accountant review of payroll; lawyer review; support email; screenshots",
    reviewer="R06d Accountant", web="new", bundles=[], listing="claude/ValueBridge_Ledgerline_Bursar_Listing.md")
add(slug="virtual-accountant", name="ValueBridge Virtual Accountant", version="1.0", dept="business-tools", coll="finance",
    tier="B", route="To plan at G0", wave="Unassigned (G0)", price="TBA", fmt="Software (browser app)",
    short="Bookkeeping help for small businesses: post entries, reconcile, close the month and read your statements.",
    bullets=["Trial balance, balance sheet and cash flow statements",
             "Month-end close checklist and tax calendar",
             "Planned to be included in Books Pro and sold separately"],
    gates=g("N", "P", "N", "N", "N", "N"), checks=0, checks_note="No listing doc yet (notes only)",
    blockers="G0 market and overlap review against Books and the Financial Dashboard Kit; accountant review; lawyer review",
    reviewer="R06d Accountant", web="new", bundles=[], listing="claude/ValueBridge_Virtual_Accountant_notes.md")

BUNDLES = [
    ("workplace-safety", "Workplace Safety Bundle", "89", ["risk-assessment-toolkit", "toolbox-talks-pack", "permit-to-work-bundle", "safety-statistics-monitor"], "safety"),
    ("productivity-pair", "Productivity Pair", "59", ["pdf-studio", "tempo"], "productivity-ai"),
    ("business-starter", "Business Starter Pack", "79", ["kpi-dashboard-pro", "financial-dashboard-kit", "project-dashboard-kit"], "business-planning"),
    ("safety-documentation", "Safety Documentation Bundle", "75", ["safety-report-writing-kit", "safety-policy-kit"], "safety"),
    ("solar-pv-audit", "Solar PV Audit Bundle", "75", ["solar-pv-audit-kit", "solar-pv-audit-resource-pack"], "energy"),
    ("esg-audit", "ESG Audit Bundle", "75", ["esg-audit-kit", "esg-audit-resource-pack"], "esg-climate"),
    ("esg-starter", "ESG Starter Bundle", "79", ["esg-report-writing-kit", "esg-policy-kit"], "esg-climate"),
    ("esg-complete", "ESG Full Suite", "149", ["esg-audit-kit", "esg-audit-resource-pack", "esg-report-writing-kit", "esg-policy-kit"], "esg-climate"),
    ("env-audit", "Environmental Audit Bundle", "75", ["environmental-audit-kit", "environmental-resource-kit"], "environment"),
    ("env-starter", "Environmental Starter Bundle", "79", ["environmental-report-writing-kit", "environmental-policy-kit"], "environment"),
    ("env-complete", "Environmental Full Suite", "149", ["environmental-audit-kit", "environmental-resource-kit", "environmental-report-writing-kit", "environmental-policy-kit"], "environment"),
    ("carbon-starter", "Carbon Accounting Starter Bundle", "79", ["carbon-footprint-calculator-kit", "carbon-playbook-policy-pack"], "esg-climate"),
    ("productivity-trio", "Productivity Trio", "69", ["pdf-studio", "tempo", "dueline"], "productivity-ai"),
    ("household-admin", "Household Admin Bundle", "39", ["dueline", "personal-budget-system"], "lifestyle-solutions"),
    ("household-money", "Household Money Pair", "45", ["keepline", "personal-budget-system"], "lifestyle-solutions"),
    ("carbon-complete", "Carbon Management Full Suite", "159", ["carbon-footprint-calculator-kit", "carbon-credit-tracker", "carbon-inventory-review-kit", "carbon-playbook-policy-pack"], "esg-climate"),
]
# Tracker-only bundles: contents not in project docs (QA-04) -> not on website
BUNDLES_UNCONFIRMED = [("Finance Toolkit", "69"), ("Operations Bundle", "119"), ("Marketing Starter", "65"), ("Career & Education", "49")]

PIPELINE_NOT_BUILT = [
    ("Wave 2", "Toolbox web apps (4)", "US$7/month from June 2027"),
    ("Wave 2", "Workplace Inspection Checklist Pack", "US$25"),
    ("Wave 2", "KPI workshop", "Service"),
    ("Wave 2", "Custom tools for local businesses", "Service"),
    ("Wave 3", "Pricing Calculator", ""), ("Wave 3", "Invoice Kit (consider dropping: Books overlaps)", ""),
    ("Wave 3", "Document Control Register", ""), ("Wave 3", "Training Matrix", ""), ("Wave 3", "SOP Kit", ""),
    ("Wave 3", "CRM", ""), ("Wave 3", "Inventory (Books overlaps)", ""), ("Wave 3", "Meeting Minutes", ""), ("Wave 3", "Notion OS", ""),
    ("Wave 4", "12 items (names in tracker v3)", ""),
]

UNREGISTERED = []  # all 10 confirmed as ValueBridge products on 31 Oct 2026

SUPERSEDED = [("Inkwell PDF Signer", "PDF Studio"), ("Dayline Planner", "Tempo"), ("CV Kit", "Resume Studio"),
              ("Cash Flow tool", "Financial Dashboard Kit"), ("Debt Calculator", "Personal Budget System"),
              ("Social Media Calendar", "Social Media & Branding Kit"),
              ("Quality, Compliance & EHS Toolkit; Compliance Obligations Register; CAPA Register", "Compliance Register Suite"),
              ("Audit Checklist & Action Tracker", "ESG, Environmental and Carbon audit kits"),
              ("Personal Finance Bundle (US$24)", "Dropped"), ("JSE Portfolio Tracker; Momentum Desk", "Not for sale")]

STAGE_FROM_GATES = "Built (G1 partly) – In QA next"


def stage(p):
    if p["tier"] == "Service":
        return "Approved to build (service) – enquiry page pending"
    if p["gates"]["G1"] == "N":
        return "In development (G1 not passed)"
    return "Built – awaiting G2 Tech QA" if p["gates"]["G0"] in ("Y", "P", "?") else "Built without G0 – market review needed"


for p in P:
    if p["fmt"].startswith("Software") and "technology" not in p["also"] and p["coll"] != "technology":
        p["also"].append("technology")
    p["stage"] = stage(p)
    p["dept_name"] = dict((a, b) for a, b, _ in DEPARTMENTS)[p["dept"]]
    p["coll_name"] = dict((a, b) for a, b, _ in COLLECTIONS)[p["coll"]]
