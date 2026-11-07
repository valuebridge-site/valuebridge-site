"""Full product pages (G5 draft) for the Compliance Register Suite: 5 registers and 2 suites, v1.0.0.
Copy follows the master wording rules (Legal Review section 3). Pending legal (G6) until signed in QA-02."""

CRS_VERSION = "1.0.0"

SHOT = {
    "dashboard": ("Dashboard of KPI cards calculated from the registers for a fictional group with five sites",
                  "Dashboard: the figures calculate from the registers"),
    "dashboard-chart": ("Status table by site next to a bar chart of statuses on the dashboard", "Status by site, with a chart"),
    "permits": ("Permits register with expiry dates, days to expiry, renewal stage and colour-coded status, priority and alert columns",
                "Permits: status, priority and alert calculate from the expiry date and renewal stage"),
    "starter-list": ("Starter List set to a site in Jamaica in the food and beverage industry, listing obligations and permits to check",
                     "Starter List: pick a site to see starter pointers for its country and industry"),
    "share-view": ("Share View listing permits for sharing, without owners or internal notes",
                   "Share View: a clean permit list for auditors, lenders or head office"),
    "legal-register": ("Legal register rows with the requirement, how it is met, evaluation dates, result and evaluation status",
                       "Legal Register: what each law asks, how you meet it, and when you last evaluated it"),
    "monitoring": ("Monitoring results against limits, with exceedance and near-limit flags",
                   "Monitoring: results checked against Max, Min or Range limits"),
    "waste": ("Waste register with tonnes, route, diversion, carrier licence check and manifest status",
              "Waste: tonnes, diversion and the carrier's licence on the collection date"),
    "incidents": ("Incident register with event type, potential severity, investigation level and due date, notification and status",
                  "Incidents: potential severity sets the investigation level; late notifications are flagged"),
    "ncrs": ("Nonconformance register with repeat flag, severity, disposition, target close date and status",
             "NCRs: repeats on the same product within 12 months are flagged"),
    "risks": ("Risks and opportunities scored by likelihood and consequence, rated High, Medium or Low, with review status",
              "Risks & Opps: scored, rated and reviewed separately"),
    "objectives": ("Quality objectives with target, latest result and status", "Quality Objectives: target, latest result and status"),
    "changes": ("Changes register with approver, implement-by date, change status and calculated status",
                "Changes: planned changes from approval to a review of results"),
    "actions": ("Action register with source, type, priority, owner, current due date, effectiveness check and status",
                "Actions: one list for all registers; corrective actions close after an effectiveness check"),
}

SHOTS = {
    "permits-licences-register": ["dashboard", "permits", "starter-list", "share-view", "dashboard-chart", "actions"],
    "legal-requirements-register": ["legal-register", "dashboard", "starter-list", "dashboard-chart", "actions"],
    "environmental-register": ["dashboard", "monitoring", "waste", "dashboard-chart", "changes", "actions"],
    "incident-capa-register": ["incidents", "dashboard", "dashboard-chart", "changes", "actions"],
    "quality-register": ["dashboard", "ncrs", "risks", "objectives", "changes", "actions"],
    "ehs-registers-suite": ["dashboard", "permits", "starter-list", "monitoring", "incidents", "dashboard-chart", "actions"],
    "integrated-compliance-suite": ["dashboard", "permits", "starter-list", "legal-register", "monitoring", "incidents", "ncrs",
                                    "risks", "dashboard-chart", "actions"],
}

F = {
    "setup": ("Setup and sites", "Organisation, report date (live, or frozen for month-end) and thresholds. Up to 20 sites, each with its own country and industry."),
    "dash": ("Dashboard and trend", "KPI cards, status by site, charts, critical items and the most overdue actions. A monthly trend log with a chart."),
    "actions": ("One action list", "Correction, corrective, preventive and improvement actions with the source ID, owner, revised due dates and effectiveness checks (ISO cl. 10.2 topics)."),
    "checks": ("Data checks and rules", "A data check column on each register names what is missing or inconsistent. The Reference sheet explains the rules the formulas follow."),
    "permits": ("Permits and licences", "Lifecycle (renewable, one-time, to obtain, superseded) kept apart from applicability (confirmed, to verify). Lead time from the row, the regulator or criticality. Status, P1–P4 priority, renewal stage and an alert built from the status."),
    "obligations": ("Obligations and calendar", "Permit conditions and recurring duties (reports, fees, tests) with rolling due dates, and a 12-month renewal calendar."),
    "share": ("Share View", "A clean permit list for one site or all sites, without owners, priorities or internal notes, ready to print or save as PDF."),
    "library": ("Starter List and Library", "170 starter pointers to check (81 permits, 42 legal duties, 47 recurring obligations) for Jamaica, Trinidad and Tobago, Barbados, The Bahamas, Cayman Islands, the United States (federal) and England, plus international good practice, across 12 industries. Each row shows the date it was checked. 64 regulators listed. Add your own rows and countries."),
    "legal": ("Legal register", "What each requirement asks of you and how you meet it, by site or for all sites. Evaluation frequency, last evaluated and by whom, Met / Partly met / Not met, next evaluation and priority (ISO 14001 and 45001 cl. 6.1.3 and 9.1.2 topics)."),
    "cil": ("Change in Law", "Log new or amended laws and guidance with the effective date, the sites affected and the legal register line it changes."),
    "aspects": ("Aspects and impacts", "Severity x probability scoring with significance rules: an aspect linked to a legal requirement or a stakeholder concern counts as significant whatever its score."),
    "monitoring": ("Monitoring", "Results against Max, Min or Range limits with Exceedance and Near limit flags, and a reminder to link an action to each exceedance."),
    "waste": ("Waste and duty of care", "Tonnes from kg, t, L or m3; diversion rate; the carrier's licence checked against the collection date; hazardous waste manifests tracked."),
    "ghg": ("Utilities and emissions estimates", "Electricity, fuels and water by site and month, with Scope 1 and location-based Scope 2 estimates from factors you set."),
    "envevents": ("Environmental events", "Spills, releases, exceedances and complaints with notification tracking. In the suites these go in the Incidents register."),
    "incidents": ("Incidents and near misses", "Actual and potential severity; the investigation level and due date follow from the potential. Root cause category and method, open actions and status."),
    "notify": ("Notification tracking", "Reportable Yes / No / To check with a deadline in days. 'NOT NOTIFIED' and 'Notified late' flags, and starter notification pointers by country to check."),
    "rates": ("Rates", "TRIR (OSHA-style rate) and LTIFR (ILO-style rate) from hours worked by site and month. 'Possible recordable' is a screen, not a recording decision."),
    "changes": ("Changes", "Planned changes to processes, equipment, materials, people or suppliers, from approval to implementation and a review of results (ISO 9001 cl. 6.3 and ISO 45001 cl. 8.1.3 topics)."),
    "ncrs": ("NCRs", "Containment, disposition with concession approver, cost of poor quality, target close by severity, and a repeat flag for the same product within 12 months."),
    "complaints": ("Complaints", "Acknowledge-by and resolve-by targets, justified or not, escalation, and the date the outcome was told to the customer (ISO 10002 topics)."),
    "audits": ("Audits and findings", "Audit programme with method (on site, remote or hybrid) and auditor independence; findings graded with actions and verification (ISO 19011 topics)."),
    "docs": ("Documents and records", "Revision, owner, approver, review cycle, retention period and disposal date."),
    "calibration": ("Calibration", "Intervals, next due, 'Overdue – do not use', accredited provider, and an impact check after a failed calibration."),
    "risks": ("Risks and opportunities", "Scored and rated separately, with planned actions and review dates. References ISO 9001:2026 topics, including separate treatment of risks and opportunities."),
    "objectives": ("Quality objectives", "Target, direction, latest result, due date and status: On target, Off target or Missed."),
    "qpolicy": ("Quality Policy template", "A one-page Word template with guidance, to adapt, sign and review."),
}

FEATURES = {
    "permits-licences-register": ["permits", "obligations", "share", "library", "setup", "dash", "actions", "checks"],
    "legal-requirements-register": ["legal", "cil", "library", "setup", "dash", "actions", "checks"],
    "environmental-register": ["aspects", "monitoring", "waste", "ghg", "envevents", "changes", "setup", "dash", "actions", "checks"],
    "incident-capa-register": ["incidents", "notify", "rates", "changes", "setup", "dash", "actions", "checks"],
    "quality-register": ["ncrs", "complaints", "audits", "docs", "calibration", "risks", "objectives", "changes", "qpolicy", "dash", "actions", "checks"],
    "ehs-registers-suite": ["permits", "obligations", "library", "legal", "aspects", "monitoring", "waste", "ghg", "incidents", "rates", "changes", "dash", "actions", "checks"],
    "integrated-compliance-suite": ["permits", "obligations", "library", "legal", "aspects", "monitoring", "waste", "ghg", "incidents", "rates",
                                    "ncrs", "audits", "risks", "objectives", "changes", "qpolicy", "dash", "actions"],
}

META = {
    "permits-licences-register": dict(
        stem="Permits_Licences_Register",
        title="Permits & Licences Register (Excel) | ValueBridge",
        description="Excel permit and licence register for up to 20 sites: expiry and renewal status that calculates, permit conditions, a renewal calendar and starter pointers by country.",
        lead="Stop typing 'Active' next to a licence that expired last month. This Excel register works out each permit's status, priority and renewal window from its expiry date and your lead times, tracks the conditions attached to it, and shows all your sites on one dashboard. Pick a country and industry to start from a list of permits to check.",
        who=["Operations, EHS and compliance managers who hold permits, licences or certificates that expire",
             "Multi-site businesses in the Caribbean, the US or the UK that need one view of renewals",
             "Anyone preparing for a lender, insurer, head-office or regulator review of permits"],
        steps=[("Look at the Example", "Open the Example workbook: a fictional five-site group with permits in each status."),
               ("Set up your sites", "Type your organisation, sites, countries and industries, and check the renewal lead times."),
               ("Start from the Starter List", "Pick a site to see starter permits and duties for its country and industry. Check each one, then copy the ones that apply."),
               ("Keep dates current", "Update renewal stages and dates. Each month, set the report date and print the Dashboard or Share View.")],
        faq=[("Does it know when my permits expire?", "It calculates from the dates you type. Status, days to expiry, renewal start and priority update against the report date, so they don't go stale."),
             ("Which countries does the Starter List cover?", "Jamaica, Trinidad and Tobago, Barbados, The Bahamas, Cayman Islands, the United States (federal) and England, plus international good practice. Rows are starter pointers to check with the authority, not legal advice. You can add your own countries and rows.")]),
    "legal-requirements-register": dict(
        stem="Legal_Statutory_Register",
        title="Legal & Statutory Requirements Register (Excel) | ValueBridge",
        description="Excel legal register: what each law requires of you, how you meet it, evaluation dates and results, a change-in-law log and starter pointers for 7 countries.",
        lead="A legal register an auditor can test: each line says what the law asks of you, how you meet it and when you last evaluated it, with the next evaluation date, result and priority calculated. Start from starter pointers for your country and industry, and log changes in law as you hear of them.",
        who=["Organisations working to ISO 14001, ISO 45001 or ISO 37301 topics that must show how they identify and evaluate compliance obligations",
             "EHS and compliance managers who inherited a list of laws with no evaluation trail",
             "Consultancies' in-house teams: one licence covers your own organisation"],
        steps=[("Look at the Example", "See a filled legal register with evaluations, results and actions."),
               ("Pick your starter rows", "On Starter List choose a site, then check and copy the rows that apply."),
               ("Write each line plainly", "What it requires of us, how we meet it, the site and who evaluates it."),
               ("Evaluate on a cycle", "Record the date, result and evidence. Partly met or Not met lines link to an action.")],
        faq=[("Is the Library a full legal register for my country?", "No. It is a set of starter pointers, checked as at the date shown on each row. Laws, thresholds and agency names change, so confirm each item with the authority or a qualified adviser."),
             ("Does it update when the law changes?", "No. There is no automatic legal-update service. Use the Change in Law sheet to record changes you learn about, and the 'Change check' column to see lines nobody has checked recently.")]),
    "environmental-register": dict(
        stem="Environmental_Register",
        title="Environmental Register: Aspects, Monitoring & Waste (Excel) | ValueBridge",
        description="Excel environmental register: aspects and impacts, monitoring against permit limits, waste and duty of care, energy and Scope 1 and 2 estimates, events and changes.",
        lead="Aspects, monitoring results, waste collections, energy use and environmental events in one linked Excel workbook. It flags exceedances and near-limit results, checks that the waste carrier's licence was valid on the collection date, and estimates Scope 1 and 2 emissions from factors you set.",
        who=["Environmental and EHS coordinators at sites with discharges, emissions, waste or energy reporting",
             "Organisations working to ISO 14001 topics that need aspects, monitoring and evaluation in one place",
             "Businesses that report waste diversion or a simple Scope 1 and 2 estimate to customers or lenders"],
        steps=[("Look at the Example", "See exceedances, a lapsed carrier licence and emissions estimates working."),
               ("Set up sites and factors", "Add sites, check thresholds and replace the illustrative emission factors with your own."),
               ("Record as you go", "Monitoring results with their limits, each waste collection, monthly utilities and any events."),
               ("Act on the flags", "Link an action to each exceedance and clear the data checks each month.")],
        faq=[("Are the emission factors accurate for my country?", "They are illustrative defaults. Replace them with the factors you report against. Scope 1 and 2 figures are self-prepared estimates, not a verified or assured inventory."),
             ("Does it include my permit limits?", "No. The Example uses illustrative limits. Type the limits from your own permit for each monitoring point.")]),
    "incident-capa-register": dict(
        stem="Incident_CAPA_Register",
        title="Incident, Near Miss & Corrective Action Register (Excel) | ValueBridge",
        description="Excel incident and near-miss register: potential-severity investigation levels, notification tracking, TRIR and LTIFR, changes and corrective actions with effectiveness checks.",
        lead="Log incidents and near misses, let potential severity set the investigation level and deadline, and track whether the authority was notified on time. Corrective actions live in one list and close only after an effectiveness check. Rates calculate from the hours you enter.",
        who=["Safety officers and EHS managers who investigate events and report rates to management",
             "Contractors and multi-site businesses that need investigation and notification deadlines in one place",
             "Teams that want near misses to count, not just injuries"],
        steps=[("Look at the Example", "See near misses with full investigations, a late notification and a reopened action."),
               ("Set thresholds", "Investigation deadlines, whether contractors count in rates, and notification windows."),
               ("Log each event", "Actual and potential severity, outcome, root cause and method."),
               ("Close the loop", "Record actions with the incident ID and confirm they worked before they close.")],
        faq=[("Does it decide what is recordable or reportable?", "No. 'Possible recordable? (screen)' is a simplified screen. Your jurisdiction's rules decide what is recordable and reportable, and notification pointers are starting points to check."),
             ("How is this different from the Safety Statistics Monitor?", "This register is about investigation, notification and corrective action, with simple TRIR and LTIFR. The Safety Statistics Monitor is the deeper statistics tool.")]),
    "quality-register": dict(
        stem="Quality_Register",
        title="Quality Register: NCRs, Complaints, Audits, Risks (Excel) | ValueBridge",
        description="Excel quality register: NCRs with repeat flags, complaints, audits and findings, documents and records, calibration, risks and opportunities, objectives, changes and actions.",
        lead="The day-to-day records of a quality system in one Excel workbook: nonconformities, complaints, audits, documents, calibration, risks and opportunities, objectives and changes, all feeding one action list and one dashboard. It references ISO 9001:2026 topics, including planning of changes and separate treatment of risks and opportunities.",
        who=["Quality managers in small and mid-sized businesses working to ISO 9001 topics",
             "Organisations moving from ISO 9001:2015 to the 2026 edition that want to organise their evidence (2015 certificates are expected to move by September 2029)",
             "Teams tracking complaints and nonconformities in scattered spreadsheets"],
        steps=[("Look at the Example", "See a repeat NCR, a concession, an overdue calibration and a high-rated risk."),
               ("Set your targets", "Close-out targets by severity, complaint response times and review cycles."),
               ("Record as you go", "Raise NCRs and complaints, plan audits, keep documents and instruments current."),
               ("Review monthly", "Check objectives off target, overdue items and actions awaiting an effectiveness check.")],
        faq=[("Does using it lead to certification?", "No product can promise that. The register organises your records and evidence; certification depends on your system and an accredited certification body's audit."),
             ("Is it written for ISO 9001:2026?", "It references ISO 9001:2026 topics, including planning of changes and separate risks and opportunities, and keeps the 2015 clause numbers most readers still use. It does not reproduce the standard.")]),
    "ehs-registers-suite": dict(
        stem="EHS_Registers_Suite",
        title="EHS Registers Suite: Permits, Legal, Environment, Incidents | ValueBridge",
        description="Four linked Excel registers in one workbook: permits and licences, legal requirements, environmental and incidents, with one action list and one dashboard for up to 20 sites.",
        lead="Permits, legal requirements, environmental records and incidents in one linked Excel workbook, with one Setup, one action list and one dashboard across up to 20 sites. Start from starter pointers for your country and industry, and let the registers work out what is expired, overdue, exceeded or still open.",
        who=["EHS managers responsible for permits, legal compliance, environment and safety across several sites",
             "Organisations working to ISO 14001 and ISO 45001 topics that want one register system",
             "Businesses reporting EHS performance to a board, lender or head office"],
        steps=[("Look at the Example", "A fictional five-site group with each register filled in."),
               ("Set up once", "Sites, countries, industries and thresholds feed all four registers."),
               ("Start from the Starter List", "Check and copy the permits, duties and obligations that apply."),
               ("Run the monthly routine", "Update, clear the data checks, freeze the report date and print the Dashboard.")],
        faq=[("Can I buy the registers separately?", "Yes. The Permits & Licences, Legal & Statutory, Environmental and Incident registers are also sold on their own. The suite puts them in one workbook with one dashboard and one action list."),
             ("Where do environmental events go?", "In the suite, spills, releases and exceedances go in the Incidents register with the event type 'Environmental', so there is one investigation process.")]),
    "integrated-compliance-suite": dict(
        stem="Integrated_Compliance_Register_Suite",
        title="Integrated Compliance Register Suite (Excel) | ValueBridge",
        description="All five ValueBridge registers in one Excel workbook: permits, legal, environmental, incidents and quality, plus changes, risks and objectives, one action list and dashboard.",
        lead="Permits, legal requirements, environmental records, incidents and quality in one linked Excel workbook, plus changes, risks and opportunities and quality objectives. One Setup for up to 20 sites, one corrective action list with effectiveness checks, and one dashboard for the whole system.",
        who=["Organisations running an integrated management system across ISO 9001, 14001 and 45001 topics",
             "Compliance, quality and EHS leads who report one set of figures to management",
             "Multi-site businesses that want one register system instead of a folder of separate trackers"],
        steps=[("Look at the Example", "A fictional five-site group with each register and the dashboard filled in."),
               ("Set up once", "Sites, countries, industries and thresholds feed all the registers."),
               ("Start where it matters", "Permits that expire first, then obligations and the legal register; incidents and quality records can start today."),
               ("Run the monthly routine", "Update, clear the data checks, freeze the report date, print the Dashboard and log the trend.")],
        faq=[("Can I buy the registers separately?", "Yes. All five registers are also sold on their own, and the EHS Registers Suite combines the four EHS registers. This suite adds quality and puts everything in one workbook."),
             ("Is it written for ISO 9001:2026?", "It references ISO 9001:2026 topics, including planning of changes and separate risks and opportunities, and keeps the 2015 clause numbers most readers still use. It does not reproduce any standard.")]),
}

COMMON_FAQ = [
    ("Which version of Excel do I need?", "Microsoft Excel 2010 or newer on Windows or Mac. There are no macros. The files open in Google Sheets and LibreOffice, where some drop-downs, colours and charts may look different."),
    ("Does it make us compliant?", "No. It organises your compliance information and applies the rules and thresholds you set. Statuses and flags are a screening aid, not a legal determination or an audit opinion."),
    ("Can a consultant use it with clients?", "Not with this licence: it covers one organisation's own use. A Consultant licence is not offered yet."),
    ("Is it a subscription?", "No. One-time licence, with minor updates within version 1 included."),
]

COMMON_LIMITS = [
    "Excel only: no mobile app, photo capture, e-signatures or email reminders.",
    "Up to 20 sites, with pre-built rows per register (for example 300 permits, 400 legal requirements, 400 incidents, 500 actions). Start Here explains how to extend them.",
    "Starter pointers cover seven countries plus international good practice. They are not a full or up-to-date legal register, and there is no automatic legal-update service.",
    "Statuses, scores and flags apply the rules and thresholds you set. They are a screen, not a legal determination, certification or audit opinion.",
    "Clause pointers use the 2015 / 2018 numbering. The files reference standards only as topics and do not reproduce standard text.",
]
EXTRA_LIMITS = {
    "IN": "The possible-recordable flag and investigation levels are simplified screens; your jurisdiction's rules decide what is recordable and reportable.",
    "EN": "Emission factors are illustrative defaults: replace them. Scope 1 and 2 figures are self-prepared estimates, not a verified or assured inventory.",
}
MODS = {"permits-licences-register": "PL", "legal-requirements-register": "LR", "environmental-register": "EN",
        "incident-capa-register": "IN", "quality-register": "QM", "ehs-registers-suite": "PL LR EN IN",
        "integrated-compliance-suite": "PL LR EN IN QM"}


def details():
    out = {}
    for slug, m in META.items():
        mods = MODS[slug].split()
        stem = m["stem"]
        files = [(f"ValueBridge_{stem}_Blank_v{CRS_VERSION}.xlsx", "your workbook"),
                 (f"ValueBridge_{stem}_Example_v{CRS_VERSION}.xlsx", "the same workbook filled with a fictional organisation"),
                 ("Playbook (Word and PDF, 21 pages)", "set-up, the monthly routine, the rules the formulas follow, standards mapping and limits")]
        if "QM" in mods:
            files.append(("Quality Policy template (Word and PDF)", "a one-page policy to adapt and sign"))
        files.append(("README, LICENCE, CHANGELOG and SHA256SUMS", "plain-text files"))
        limits = COMMON_LIMITS + [EXTRA_LIMITS[k] for k in ("IN", "EN") if k in mods]
        out[slug] = {
            "title": m["title"], "description": m["description"], "lead": m["lead"],
            "gallery": [(f"{slug}-{n}.webp", SHOT[n][0], SHOT[n][1]) for n in SHOTS[slug]],
            "gallery_note": "Example workbook shown, rendered in LibreOffice; colours may differ slightly in Excel. Coralstone Group and all names, sites, permit numbers and figures are fictional.",
            "social_image": f"{slug}-social.jpg",
            "who": m["who"], "steps": m["steps"],
            "features": [F[k] for k in FEATURES[slug]],
            "files": files,
            "requirements": "Microsoft Excel 2010 or newer, desktop, on Windows or Mac. No macros. Opens in Google Sheets and LibreOffice, where some drop-downs, colours and charts may differ. A Word-compatible app or PDF reader for the Playbook. Before release we open the files in desktop Excel and will list the Excel versions used here.",
            "limits": limits,
            "faq": m["faq"] + COMMON_FAQ,
            "licence": "Licensed to one organisation for its own internal use at any number of its sites (an individual buyer: one person). You may share completed registers and reports about your own organisation with auditors, regulators, insurers, lenders, clients and head office. No resale, no sharing of blank templates and no AI training. Minor updates within version 1 included. The full Master Licence, terms of sale and refund policy will be on our Store policies page before release.",
            "licence_label": "One organisation, any number of its sites",
            "privacy": "Your data stays in your file; ValueBridge does not receive it. Registers can hold personal and injury details: you are responsible for storing them securely, limiting access and handling them lawfully, including under Jamaica's Data Protection Act, 2020 or the law that applies to you.",
            "affiliation": "ValueBridge is independent and not affiliated with, endorsed by or sponsored by Microsoft, ISO, OSHA, HSE, US EPA, the Environment Agency, NEPA, EMA, DEPP, Global ACI or any government agency, regulator, accreditation or certification body. Names are used only to describe compatibility or topics. All trademarks belong to their owners.",
            "schema": "Product",
            "trial_live": False,
        }
    return out


CRS_DETAILS = details()
