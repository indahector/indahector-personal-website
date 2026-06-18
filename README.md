# hectorindadiaz.com

Personal website for **Héctor Inda Díaz** — atmospheric & geospatial data scientist.

Plain HTML / CSS / JavaScript. No framework, no build step, no dependencies.
Open `index.html` in a browser and it just works.

🌐 **Live:** https://hectorindadiaz.com

---

## Pages

| File | Purpose |
|------|---------|
| `index.html` | Home — about, selected work, interests, education, contact |
| `work.html` | Full project list |
| `publications.html` | Peer-reviewed papers, talks, theses |
| `writing.html` | Notes / science communication |
| `404.html` | Friendly not-found page |

## Supporting files

| File | Purpose |
|------|---------|
| `styles.css` | All styling. Design tokens (colors, fonts) live at the top in `:root` |
| `script.js` | Mobile nav, contour-line signature, scroll reveal |
| `assets/` | Photos, résumé/CV PDFs, favicon |
| `CNAME` | Custom domain for GitHub Pages (`hectorindadiaz.com`) |
| `.nojekyll` | Tells GitHub Pages to serve files as-is (no Jekyll processing) |
| `robots.txt`, `sitemap.xml` | Basic SEO |
| `.github/workflows/deploy.yml` | Optional automated deploy to GitHub Pages |
| `LICENSE` | MIT (see scope note below) |

---

## Preview locally

No tooling required — just open `index.html`. For an exact-as-deployed preview
(so paths and the custom-domain behavior match), run a tiny local server:

```bash
# Python 3
python3 -m http.server 8000
# then visit http://localhost:8000
```

---

## Put it on GitHub

```bash
cd path/to/this/folder
git init
git add .
git commit -m "Initial commit: personal site"
git branch -M main
# create an empty repo on github.com first, then:
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

**Repo naming**
- For a **user site** at `https://<your-username>.github.io`, name the repo
  exactly `<your-username>.github.io`.
- For a **project site** at `https://<your-username>.github.io/<repo-name>`,
  any repo name works.
- With the custom domain (below), the repo name doesn't affect the final URL.

---

## Deploy with GitHub Pages

Pick **one** of these. Option A is simplest.

### Option A — Deploy from a branch (no workflow needed)
1. Push the repo (above).
2. Repo → **Settings → Pages**.
3. **Source:** *Deploy from a branch* → Branch: `main` → Folder: `/ (root)` → **Save**.
4. Wait ~1 minute; your site goes live at the URL shown on that page.

### Option B — GitHub Actions (uses the included workflow)
1. Repo → **Settings → Pages** → **Source:** *GitHub Actions*.
2. Push to `main`. The `.github/workflows/deploy.yml` workflow builds and deploys
   automatically on every push (and can be re-run from the **Actions** tab).

> The included workflow only takes effect when Source is set to *GitHub Actions*.
> If you use Option A, the workflow simply stays dormant.

---

## Custom domain (hectorindadiaz.com)

The `CNAME` file already tells GitHub which domain to use. You also need DNS
records at your domain registrar:

**Apex domain** (`hectorindadiaz.com`) → four `A` records:
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```
(Optionally add the matching `AAAA` records for IPv6.)

**`www` subdomain** → one `CNAME` record pointing to `<your-username>.github.io`.

Then in **Settings → Pages → Custom domain**, enter `hectorindadiaz.com`, save,
and tick **Enforce HTTPS** once the certificate is issued.

> GitHub's Pages IPs are stable but can change — confirm the current values in
> GitHub's official "Managing a custom domain for your GitHub Pages site" docs.

---

## Editing

- **Text & links:** edit the `.html` files directly — it's all plain HTML.
- **Colors & fonts:** change the variables under `:root` in `styles.css`.
  The accent is `--current` (deep teal) — change it once and the whole site follows.
- **Hero photo:** replace `assets/hector.jpg`, or point the hero `<img>` in
  `index.html` at `assets/hector-formal.jpg` (the formal headshot, included).
- **Résumé / CV:** replace the PDFs in `assets/` (keep the filenames, or update
  the links).
- **Add a writing post:** duplicate a `.note-card` block in `writing.html`, or add
  a new HTML page and link it from the nav in each file.
- After editing, remember to update `<lastmod>` dates in `sitemap.xml`.

Fonts (Fraunces, IBM Plex Sans, IBM Plex Mono) load from Google Fonts via CDN.

---

## License

The **site code** (HTML/CSS/JS) is released under the [MIT License](LICENSE).
**Personal content** — the biography, photographs, résumé/CV, and publication
list — is © Héctor Inda Díaz and not covered by the MIT grant.
