# DNS Configuration Instructions for Porkbun

This guide will walk you through configuring DNS records in Porkbun to point your domain (meowtowncattery.com) to GitHub Pages.

## Overview

To use a custom domain with GitHub Pages, you need to configure:
- **A Records** for the apex domain (meowtowncattery.com) - points directly to GitHub Pages IP addresses
- **CNAME Record** for the www subdomain (www.meowtowncattery.com) - points to your GitHub Pages URL

## Step-by-Step Instructions

### Step 1: Log into Porkbun

1. Go to https://porkbun.com
2. Click "Login" in the top right corner
3. Enter your credentials and sign in

### Step 2: Access DNS Management

1. Once logged in, you'll see your dashboard with a list of domains
2. Find and click on **meowtowncattery.com** in your domain list
3. Click on the **"DNS"** tab or **"DNS Records"** option
4. You should now see the DNS management interface

### Step 3: Configure A Records (for apex domain)

These records allow `meowtowncattery.com` (without www) to work with GitHub Pages.

1. In the DNS records section, look for existing A records for the apex domain (records with name `@` or blank)
2. You'll need to add **4 A records** with the following values:

   **Record 1:**
   - **Type**: A
   - **Name**: `@` (or leave blank if Porkbun uses `@` for apex domain)
   - **Value/Answer**: `185.199.108.153`
   - **TTL**: 600 (or use default if available)

   **Record 2:**
   - **Type**: A
   - **Name**: `@` (or leave blank)
   - **Value/Answer**: `185.199.109.153`
   - **TTL**: 600

   **Record 3:**
   - **Type**: A
   - **Name**: `@` (or leave blank)
   - **Value/Answer**: `185.199.110.153`
   - **TTL**: 600

   **Record 4:**
   - **Type**: A
   - **Name**: `@` (or leave blank)
   - **Value/Answer**: `185.199.111.153`
   - **TTL**: 600

3. Click **"Add"** or **"Save"** after adding each record
4. If there are existing A records for the apex domain that conflict, you may need to delete or modify them first

**Note**: Some DNS interfaces use `@` to represent the apex domain, while others use a blank field. Porkbun typically uses `@` for the root domain.

### Step 4: Configure CNAME Record (for www subdomain)

This record allows `www.meowtowncattery.com` to work with GitHub Pages.

1. In the DNS records section, look for an existing CNAME record for `www`
2. Add or modify a CNAME record with:
   - **Type**: CNAME
   - **Name**: `www`
   - **Value/Answer**: `thunderhugs.github.io`
   - **TTL**: 600 (or use default)

3. Click **"Add"** or **"Save"**

**Important**: The CNAME value must match your GitHub username/organization followed by `.github.io`. In this case: `thunderhugs.github.io`

### Step 5: Verify DNS Records

After adding all records, your DNS configuration should look like this:

```
Type    Name    Value/Answer              TTL
A       @       185.199.108.153           600
A       @       185.199.109.153           600
A       @       185.199.110.153           600
A       @       185.199.111.153           600
CNAME   www     thunderhugs.github.io     600
```

### Step 6: Wait for DNS Propagation

DNS changes can take anywhere from a few minutes to 48 hours to propagate globally, though most changes are visible within 5-60 minutes.

**To check if DNS has propagated:**

1. **Using Command Line (Windows PowerShell)**:
   ```powershell
   nslookup meowtowncattery.com
   nslookup www.meowtowncattery.com
   ```

2. **Using Online Tools**:
   - https://www.whatsmydns.net/ - Check DNS propagation globally
   - https://dnschecker.org/ - Verify DNS records worldwide

3. **Check A Records**:
   - The apex domain should resolve to one of the GitHub Pages IP addresses (185.199.108.153, 185.199.109.153, 185.199.110.153, or 185.199.111.153)

4. **Check CNAME Record**:
   - `www.meowtowncattery.com` should resolve to `thunderhugs.github.io`

### Step 7: Enable GitHub Pages Custom Domain

1. Go to your GitHub repository: https://github.com/thunderhugs/mt
2. Navigate to **Settings** → **Pages**
3. Under **Custom domain**, you should see `www.meowtowncattery.com` (this is automatically detected from the CNAME file)
4. If not automatically detected, enter `www.meowtowncattery.com` in the custom domain field
5. Check the box **"Enforce HTTPS"** (this will be available after DNS is configured and GitHub provisions the SSL certificate)
6. Click **Save**

### Step 8: Verify SSL Certificate

GitHub Pages automatically provisions SSL certificates for custom domains, but this can take a few minutes to several hours after DNS is configured.

1. Wait 10-30 minutes after DNS propagation
2. Visit https://www.meowtowncattery.com
3. Check that the site loads with HTTPS (you should see a padlock icon in your browser)
4. If HTTPS isn't working yet, wait a bit longer and check again

### Step 9: Test Both Domain Variants

After everything is configured, test both:
- https://meowtowncattery.com (apex domain)
- https://www.meowtowncattery.com (www subdomain)

Both should load your website. GitHub Pages will automatically redirect one to the other based on your CNAME configuration.

## Troubleshooting

### DNS Not Propagating

- **Wait longer**: DNS changes can take up to 48 hours, though usually much faster
- **Clear DNS cache**: On Windows, run `ipconfig /flushdns` in PowerShell as Administrator
- **Check for typos**: Verify all IP addresses and the CNAME value are correct
- **Check TTL**: Lower TTL values (300-600 seconds) help with faster updates

### HTTPS Not Working

- **Wait for SSL provisioning**: GitHub needs time to provision the certificate (usually 10-60 minutes after DNS is configured)
- **Verify DNS is correct**: SSL won't work if DNS isn't properly configured
- **Check GitHub Pages settings**: Ensure the custom domain is set in repository settings
- **Clear browser cache**: Sometimes browsers cache old SSL states

### Site Not Loading

- **Verify GitHub Pages is enabled**: Check repository Settings → Pages
- **Check branch**: Ensure the correct branch (main/master) is selected as the source
- **Verify CNAME file**: The CNAME file should contain `www.meowtowncattery.com`
- **Check repository visibility**: If the repository is private, you need GitHub Pro/Team/Enterprise for custom domains

### Both www and non-www Not Working

- **A Records**: Verify all 4 A records are added correctly
- **CNAME Record**: Verify the www CNAME points to `thunderhugs.github.io`
- **DNS Propagation**: Use dnschecker.org to verify records are propagated globally

## Additional Notes

### Porkbun-Specific Tips

- Porkbun's interface may vary slightly, but the DNS management should be accessible from the domain management page
- If you can't find the DNS section, look for "DNS Records", "DNS Management", or "DNS Settings"
- Porkbun typically uses `@` to represent the apex domain in DNS records
- Some Porkbun interfaces may show TTL in seconds, others in minutes - 600 seconds = 10 minutes

### GitHub Pages Limitations

- Custom domains work with public repositories on free GitHub accounts
- Private repositories require GitHub Pro, Team, or Enterprise for custom domains
- GitHub Pages sites are served over HTTPS by default once SSL is provisioned
- The CNAME file in your repository root is required for custom domain configuration

### Maintenance

- DNS records typically don't need to be changed unless you switch hosting providers
- GitHub Pages IP addresses are stable but can change - check GitHub's documentation if issues arise
- The CNAME record value (`thunderhugs.github.io`) should match your GitHub username/organization

## Verification Checklist

After completing the setup, verify:

- [ ] All 4 A records are added for the apex domain
- [ ] CNAME record is added for www subdomain
- [ ] DNS has propagated (check with dnschecker.org)
- [ ] GitHub Pages is enabled in repository settings
- [ ] Custom domain is configured in GitHub Pages settings
- [ ] HTTPS is working (padlock icon in browser)
- [ ] Site loads at https://www.meowtowncattery.com
- [ ] Site loads at https://meowtowncattery.com (or redirects to www)

## Support Resources

- **Porkbun Support**: https://porkbun.com/support
- **GitHub Pages Documentation**: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site
- **DNS Propagation Checker**: https://www.whatsmydns.net/
- **GitHub Pages Status**: https://www.githubstatus.com/

---

**Last Updated**: 2024-12-19
**Repository**: https://github.com/thunderhugs/mt
**Domain**: meowtowncattery.com

