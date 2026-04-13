# Agents Documentation

## Project Overview

This project is the **full website** for **Meowtown Cattery** — a premium cat boarding and cat hotel in Cambridge, Cambridgeshire. The site includes: Home, About, Facilities, Pricing, Booking, Find Us, FAQ, Contact, Terms and Privacy pages. Built with plain HTML, CSS and JavaScript (no framework, no build step). A backup of the original holding page is preserved on the `holding-page` branch.

### Local development

To preview the site locally before pushing to GitHub, run a static server from the repository root:

- **Python**: `python -m http.server 8000` then open http://localhost:8000
- **Node**: `npx serve` or `npx live-server`

You can also open `index.html` (and other pages) directly in a browser via file://.

## Project Details

- **Domain**: meowtowncattery.com (owned by project owner, registered via Porkbun)
- **GitHub Repository**: https://github.com/thunderhugs/mt
- **Hosting**: GitHub Pages
- **Custom Domain**: www.meowtowncattery.com (configured via CNAME file)
- **GitHub Pages URL**: https://thunderhugs.github.io/mt (fallback before custom domain is active)

## Hosting Configuration

### GitHub Pages Setup

- **CNAME File**: The repository contains a `CNAME` file with `www.meowtowncattery.com` to configure the custom domain
- **Branch**: GitHub Pages is configured to deploy from the main branch (verify in repository settings)
- **SSL**: GitHub Pages automatically provisions SSL certificates for custom domains (HTTPS enabled)
- **DNS**: Configured via Porkbun (see DNS_SETUP.md for detailed instructions)

### Deployment Process

1. Make changes to website files (index.html, styles.css, etc.)
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```
3. GitHub Pages automatically rebuilds and deploys within 1-5 minutes
4. Changes are live at www.meowtowncattery.com

### DNS Configuration

- **DNS Provider**: Porkbun
- **A Records**: Configured for apex domain (meowtowncattery.com) pointing to GitHub Pages IPs
- **CNAME Record**: Configured for www subdomain pointing to thunderhugs.github.io
- See DNS_SETUP.md for complete DNS configuration instructions

## Reference Folder

The `reference/` folder at the repo root exists for **reference-only** material (e.g. design mocks, copy drafts, external docs, screenshots). It is **gitignored**; nothing inside it is committed or deployed.

**Core files** are any files that are part of the live site or repo integrity, including: all `*.html`, `styles.css`, `main.js`, everything under `files/`, `CNAME`, `sitemap.xml`, `robots.txt`, `favicon.ico`, and any script or config that affects the site or deployment.

**Rule**: Never write, move, or copy core files into `reference/`. Only reference material (drafts, mocks, external docs, assets not used in the site) may be placed there.

## Business operation (from booking/consent form)

Core details for copy, terms, FAQ and future iterations. Authoritative form: `reference/booking-and-consent-form.md`.

- **Trading name / branding:** Meowtown Cattery (form uses "Meow Town Cattery" — confirm preferred spelling with owner if needed).
- **Address:** 7 Mill Road, Lode, Cambridgeshire, CB25 9EN. Licence: 25/04678/ANIMAL.
- **Contact:** Phone 07462 290560. Email meowtowncattery@gmail.com. We try to respond to WhatsApp as well.
- **Opening hours:** Flexible (home-based; effectively always open). Drop-off & collection by arrangement. *Note: The printed booking form's fixed hours are inaccurate; do not use them on the website or in future copy.*
- **Booking & payment:** By appointment only. Full payment at point of booking.
- **Cancellation:** 14 days' notice to amend/cancel; after that no refund.
- **Stay rules:** Minimum 3 days (2 nights). Part days = full days; arrival and departure days each count as full days. £10/day surcharge for Christmas Day, Boxing Day, New Year's Day.
- **Vaccination:** Feline Enteritis and Feline Flu (influenza). Proof mandatory before boarding or at booking in.
- **Neutering:** All male cats over 6 months must be neutered.
- **Food:** Food is **included** (e.g. Felix, Whiskas, Purina, Sheba, GoCat). Owners provide food **only if** their cat has **special dietary requirements**. Also included: treats, bedding, litter, toys, daily grooming, daily play.
- **Vet/medication:** Permission to give medication/parasite treatment as needed or as advised by vet; try owner's vet first, may use cattery's; infectious isolation at Lida vets, charged to owner.
- **Liability:** Not responsible for illness, disease, death, loss in care or during transport, or property damage/loss; cats at owner's risk.
- **Sharing:** Only cats from same household; owner consents to separation if required.
- **Rehoming:** If no contact 14 days after collection date, rehome after all efforts to make contact.
- **Medical history:** Owner must inform at booking and/or on day of arrival.

## Maintenance Instructions

**IMPORTANT**: Whenever new information that is critical to the maintenance of this project is discovered or created, it **MUST** be documented in this `agents.md` file. This ensures that AI agents and future maintainers have a single source of truth for all critical project information.

