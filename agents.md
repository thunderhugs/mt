# Agents Documentation

## Project Overview

This project is for a **Website** that publicizes a **Cattery business**. 

Presently, the page is intended just to be a **holding page** for the Website, prior to the launch of the business.

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

## Maintenance Instructions

**IMPORTANT**: Whenever new information that is critical to the maintenance of this project is discovered or created, it **MUST** be documented in this `agents.md` file. This ensures that AI agents and future maintainers have a single source of truth for all critical project information.

