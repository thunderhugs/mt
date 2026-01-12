# Meowtown Cattery - Holding Page

A single-page holding website for Meowtown Cattery, a cat boarding and cat hotel facility in Cambridge, Cambridgeshire. Designed to help the domain (meowtowncattery.com) get indexed by search engines and build authority over time.

## Project Overview

This is a modern, SEO-optimized holding page that includes:
- Schema.org structured data (JSON-LD format) with Cambridge location
- Comprehensive SEO meta tags optimized for target keywords
- Social media optimization (Open Graph, Twitter Cards)
- Responsive, mobile-first design
- Color scheme matching the Meowtown Cattery logo

## Target Keywords

The site is optimized to index for:
- **Cattery**
- **Cat Boarding**
- **Cat Hotel**
- **Cambridge**
- **Cambridgeshire**

## Files Structure

```
/
├── index.html          # Main HTML page with semantic markup and Schema.org data
├── styles.css          # CSS with logo-based color scheme
├── logo.jpg            # Meowtown Cattery logo
├── sitemap.xml         # XML sitemap for search engines
├── robots.txt          # Robots file for crawlers
├── CNAME               # Custom domain configuration for GitHub Pages
└── README.md           # This file
```

## Deployment Instructions

### Option 1: Static Hosting (Recommended)

1. **Upload all files** to your web hosting root directory:
   - `index.html`
   - `styles.css`
   - `logo.jpg`
   - `sitemap.xml`
   - `robots.txt`

2. **Ensure the domain** `meowtowncattery.com` points to your hosting

3. **Verify SSL certificate** is active (HTTPS required for best SEO)

4. **Test the site**:
   - Visit `https://meowtowncattery.com`
   - Check mobile responsiveness
   - Validate HTML: https://validator.w3.org/
   - Test Schema.org markup: https://search.google.com/test/rich-results

### Option 2: GitHub Pages (Current Setup)

This site is configured to be hosted on GitHub Pages with a custom domain.

#### Initial Setup (One-time)

1. **Push all files to GitHub repository**:
   ```bash
   git add .
   git commit -m "Initial commit for GitHub Pages"
   git push origin main
   ```
   (Or use `master` if that's your default branch)

2. **Enable GitHub Pages**:
   - Go to repository settings: https://github.com/thunderhugs/mt/settings/pages
   - Under "Source", select your branch (typically `main` or `master`)
   - Click "Save"
   - The `CNAME` file in the repository root automatically configures the custom domain

3. **Configure DNS** (see DNS_SETUP.md for detailed Porkbun instructions):
   - Add A records for apex domain (meowtowncattery.com)
   - Add CNAME record for www subdomain (www.meowtowncattery.com)
   - Wait for DNS propagation (usually 5-60 minutes, can take up to 48 hours)

4. **Verify HTTPS**:
   - GitHub Pages automatically provisions SSL certificates for custom domains
   - This may take a few minutes after DNS is configured
   - Check status in repository Settings → Pages

#### Repository Information

- **Repository**: https://github.com/thunderhugs/mt
- **Custom Domain**: www.meowtowncattery.com (configured via CNAME file)
- **GitHub Pages URL**: https://thunderhugs.github.io/mt (before custom domain is active)

#### Updating the Site

Simply push changes to the repository:
```bash
git add .
git commit -m "Update website content"
git push origin main
```

GitHub Pages will automatically rebuild and deploy within a few minutes.

### Post-Deployment Checklist

- [ ] Verify site loads at `https://meowtowncattery.com`
- [ ] Test on mobile devices
- [ ] Submit sitemap to Google Search Console
- [ ] Submit sitemap to Bing Webmaster Tools
- [ ] Verify Schema.org markup with Google Rich Results Test
- [ ] Test Open Graph tags with Facebook Sharing Debugger
- [ ] Test Twitter Cards with Twitter Card Validator
- [ ] Check robots.txt is accessible at `https://meowtowncattery.com/robots.txt`
- [ ] Verify sitemap is accessible at `https://meowtowncattery.com/sitemap.xml`

## SEO Features

### Technical SEO
- Semantic HTML5 structure
- Proper heading hierarchy (H1, H2)
- Mobile-responsive design
- Fast loading (minimal dependencies)
- Valid HTML markup
- Canonical URL specified

### On-Page SEO
- Optimized title tag with target keywords (Cattery, Cat Boarding, Cat Hotel, Cambridge, Cambridgeshire)
- Compelling meta description incorporating all target keywords naturally
- Proper alt text for images with location keywords
- Clean URL structure
- Location-based content for local SEO

### Structured Data (Schema.org)
- **LocalBusiness** schema - Primary business information with Cambridge, Cambridgeshire location
- **Organization** schema - Brand identity
- **WebSite** schema - Site information
- All in JSON-LD format (Google's recommended format)
- Location data included for local search optimization

### Social Media Optimization
- Open Graph tags for Facebook/LinkedIn
- Twitter Card tags
- Logo image used for social previews

## Color Scheme

The color palette is extracted from the Meowtown Cattery logo:
- **Primary Orange**: `#F7931E` (cat)
- **Primary Blue**: `#2A7FB8` (house and text)
- **Accent Yellow**: `#FEE100` (splatters)
- **Black**: `#000000` (outlines)
- **Background Cream**: `#F8F5ED` (background)

## Maintenance Notes

### Updating Content

When the business launches, update:
1. Contact information in `index.html` (email, phone)
2. Business address in Schema.org LocalBusiness schema
3. Social media links in Organization schema (`sameAs` array)
4. Remove "Coming Soon" messaging
5. Add actual business content and services

### SEO Maintenance

- Update `sitemap.xml` `lastmod` date when content changes
- Monitor Google Search Console for indexing status
- Check for crawl errors regularly
- Update meta descriptions if needed
- Add new pages to sitemap as site expands

### Performance

- Keep images optimized (logo.jpg should be under 200KB)
- Monitor Core Web Vitals in Google Search Console
- Consider adding more pages as business grows

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Accessibility

- Semantic HTML elements
- ARIA labels where appropriate
- Keyboard navigation support
- Focus indicators
- Reduced motion support
- High contrast mode support

## License

Copyright © 2024 Meowtown Cattery. All rights reserved.

