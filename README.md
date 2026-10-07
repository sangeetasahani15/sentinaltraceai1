# SentinelTrace AI – Email Forensic Intelligence

Runs 100% in your browser. No install, no internet, no dependencies.

## Run
- Easiest: double-click `index.html`
- Or: `python start.py` (opens http://127.0.0.1:8000)

## Use
1. Click **Load Demo Threat** (Overview or Email Analyzer), or paste/upload a real `.eml`.
2. Explore Header Forensics, Email Trace, Geolocation, Domain & Threat Intelligence, Relationship Graph.
3. Create a Case, save Evidence (SHA-256 hash) and download a JSON Report.

## Notes
- Scoring is rule-based (SPF/DKIM/DMARC, lookalike domains, Reply-To mismatch, urgency/finance wording, link checks).
- Geolocation uses a small built-in demo table; plug in a GeoIP database for real lookups.
- Overview KPIs and Campaigns are demo data. Emails are never uploaded anywhere.
