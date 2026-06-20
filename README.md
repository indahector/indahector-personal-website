# hectorindadiaz.com

Personal website for **Héctor Inda Díaz** — atmospheric & geospatial data scientist.

Plain HTML / CSS / JavaScript. No framework, no build step, no dependencies.
Open `index.html` in a browser and it just works.

🌐 **Live:** https://hectorindadiaz.com

---

## Pages

The site is **bilingual**. English lives at the root; Spanish mirrors it under `es/`.
A small **EN / ES toggle** in the top-right of every page links to its counterpart.

| English (root) | Spanish (`es/`) | Purpose |
|------|------|---------|
| `index.html` | `es/index.html` | Home — about, selected work, interests, education, **Other projects**, **Other interests**, contact |
| `work.html` | `es/work.html` | Full project list |
| `publications.html` | `es/publications.html` | Peer-reviewed papers, talks, theses |
| `writing.html` | `es/writing.html` | **Science communication / Divulgación** — notes & explainers |
| `atmospheric-rivers.html` | `es/rios-atmosfericos.html` | Explainer article: *What is an atmospheric river?* |
| `404.html` | `es/404.html` | Friendly not-found page |

> Note: the science-communication page keeps the filename `writing.html` (so existing links/bookmarks still work); only its **label** is "Science communication" / "Divulgación".

## How the pages are generated

All HTML is produced by **`build.py`** — a small Python script that holds the
content for both languages and stamps out every page with an identical
nav / footer / language-toggle. This keeps the two language versions in sync.

```bash
python3 build.py        # regenerates all HTML files
```

### Show / hide the Spanish version

At the top of `build.py` there's a single switch:

```python
SHOW_ES = False   # English only — no EN/ES toggle, no es/ pages
# SHOW_ES = True  # publishes the Spanish mirror + the EN/ES toggle
```

All Spanish content always lives in `build.py`, so hiding it loses nothing.
To bring Spanish back: set `SHOW_ES = True`, run `python3 build.py`, and
uncomment the `es/` block in `sitemap.xml`.

**Two ways to edit:**
- **Content or structure change** → edit `build.py`, then re-run it. This is the
  source of truth and keeps EN/ES consistent.
- **Tiny one-off tweak** → you can edit a generated `.html` file directly. Just
  remember a later `python3 build.py` will overwrite it, so fold lasting changes
  back into `build.py`.

To add a translated page, add its content block (both `en` and `es`) in `build.py`
and a `render(...)` call, then update `sitemap.xml`.

## Supporting files

| File | Purpose |
|------|---------|
| `styles.css` | All styling. Design tokens (colors, fonts) live at the top in `:root` |
| `script.js` | Mobile nav, contour-line signature, scroll reveal |
| `build.py` | Generates all EN/ES pages (see "How the pages are generated") |
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
