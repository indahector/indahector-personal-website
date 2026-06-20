# -*- coding: utf-8 -*-
"""Generate the bilingual (EN/ES) static site with a language toggle."""
import os

# ---------------------------------------------------------------------------
# Set to True to publish the Spanish version and show the EN / ES toggle.
# Set to False to hide it (English-only): no toggle, and the es/ pages are
# not generated. All Spanish content is preserved in this file either way,
# so flipping this back to True and re-running fully restores the ES site.
# ---------------------------------------------------------------------------
SHOW_ES = False

BASE = "https://hectorindadiaz.com/"
ICONS = {
"mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
"github":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.58 2 12.25c0 4.53 2.87 8.37 6.84 9.73.5.1.68-.22.68-.49 0-.24-.01-.88-.01-1.73-2.78.62-3.37-1.37-3.37-1.37-.46-1.18-1.11-1.5-1.11-1.5-.91-.64.07-.62.07-.62 1 .07 1.53 1.06 1.53 1.06.89 1.57 2.34 1.12 2.91.86.09-.66.35-1.12.63-1.38-2.22-.26-4.56-1.14-4.56-5.07 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.71 0 0 .84-.28 2.75 1.05a9.3 9.3 0 0 1 5 0c1.91-1.33 2.75-1.05 2.75-1.05.55 1.41.2 2.45.1 2.71.64.72 1.03 1.63 1.03 2.75 0 3.94-2.34 4.81-4.57 5.06.36.32.68.94.68 1.9 0 1.37-.01 2.48-.01 2.82 0 .27.18.6.69.49A10.02 10.02 0 0 0 22 12.25C22 6.58 17.52 2 12 2Z"/></svg>',
"scholar":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3 1 9l11 6 9-4.91V17h2V9L12 3Z"/><path d="M5 13.18v3.32L12 20l7-3.5v-3.32L12 17l-7-3.82Z" opacity=".55"/></svg>',
"linkedin":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9h4v12H3V9Zm6 0h3.8v1.64h.05c.53-.95 1.83-1.95 3.76-1.95 4.02 0 4.76 2.5 4.76 5.76V21h-4v-5.3c0-1.27-.02-2.9-1.77-2.9-1.77 0-2.04 1.38-2.04 2.8V21H9V9Z"/></svg>',
}
def iconrow(extra_class=""):
    a=lambda h,k,lbl:f'<a href="{h}" {"target=_blank rel=noopener" if not h.startswith("mailto") else ""} aria-label="{lbl}" title="{lbl}">{ICONS[k]}</a>'
    return (f'<div class="iconrow{extra_class}">'
            + a("mailto:indahector@gmail.com","mail","Email")
            + a("https://github.com/indahector","github","GitHub")
            + a("https://scholar.google.com/citations?user=MBdNFm0AAAAJ","scholar","Google Scholar")
            + a("https://www.linkedin.com/in/indahector","linkedin","LinkedIn")
            + '</div>')

NAV = {
 "en":[("index.html","Home"),("work.html","Work"),("publications.html","Publications"),("writing.html","Science communication")],
 "es":[("index.html","Inicio"),("work.html","Proyectos"),("publications.html","Publicaciones"),("writing.html","Divulgación")],
}
SKIP={"en":"Skip to content","es":"Saltar al contenido"}

def nav(lang, active, counterpart):
    lis="\n".join(
        f'      <li><a href="{href}"{" class=\"active\"" if href==active else ""}>{label}</a></li>'
        for href,label in NAV[lang])
    if lang=="en":
        toggle=f'<span class="cur">EN</span><span class="sep">/</span><a href="{counterpart}">ES</a>'
    else:
        toggle=f'<a href="{counterpart}">EN</a><span class="sep">/</span><span class="cur">ES</span>'
    lang_div = f'\n      <div class="lang" aria-label="Language">{toggle}</div>' if SHOW_ES else ''
    return f'''<header class="nav">
  <div class="nav-in">
    <a class="brand" href="index.html">Héctor A. Inda Díaz<span class="dot">.</span></a>
    <div class="nav-right">
      <nav><ul class="nav-links" id="navlinks">
{lis}
      </ul></nav>{lang_div}
      <button class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="navlinks"><span></span></button>
    </div>
  </div>
</header>'''

def head(lang, pre, title, desc, en_url, es_url):
    alts = (f'\n<link rel="alternate" hreflang="en" href="{en_url}">'
            f'\n<link rel="alternate" hreflang="es" href="{es_url}">') if SHOW_ES else ''
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{pre}assets/favicon.png">{alts}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,380;9..144,460;9..144,560&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;450;500;600&display=swap" rel="stylesheet">
<script>document.documentElement.classList.add('js');</script>
<link rel="stylesheet" href="{pre}styles.css">
</head>
<body>'''

def footer(lang, pre):
    return f'''<footer class="foot">
  <div class="wrap foot-in">
    <span>© <span data-year>2026</span> Héctor A. Inda Díaz</span>
    <span class="mono">Sacramento · Davis, CA</span>
  </div>
</footer>
<script src="{pre}script.js"></script>
</body>
</html>'''

def render(lang, filename, title, desc, main_html, active, counterpart, en_url, es_url):
    pre = "../" if lang=="es" else ""
    html = "\n".join([
        head(lang,pre,title,desc,en_url,es_url),
        f'<a class="skip" href="#main">{SKIP[lang]}</a>\n',
        nav(lang,active,counterpart),
        '\n<main id="main">',
        main_html,
        '</main>\n',
        footer(lang,pre),
    ])
    outdir = "es" if lang=="es" else "."
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir,filename),"w",encoding="utf-8") as f:
        f.write(html)

U=lambda p: BASE+p          # en url
ES=lambda p: BASE+"es/"+p   # es url

# =========================================================================
# HOME
# =========================================================================
def home_main(lang):
    if lang=="en":
        return f'''  <section class="hero">
    <svg class="hero-contours js-contours" data-stroke="#17605c" data-opacity="0.15" data-lines="15" aria-hidden="true"></svg>
    <div class="wrap hero-in">
      <div class="hero-copy">
        <span class="eyebrow">Atmospheric &amp; Geospatial Data Scientist</span>
        <h1>Héctor A. Inda Díaz</h1>
        <p class="lead">I turn large-scale weather and climate data into models and tools that people — utilities, agencies, and fellow scientists — can act on.</p>
        <div class="hero-meta">
          <span>BS Physics</span><span>MS Physical Oceanography</span><span>PhD Atmospheric Science</span><span>Atmospheric Scientist at Eagle Rock Analytics</span>
        </div>
        <div class="actions">
          # <a class="btn btn-primary" href="assets/Resume_IndaDiaz.pdf" target="_blank" rel="noopener">Résumé (PDF)</a>
          <a class="btn btn-primary" href="assets/0.pdf" target="_blank" rel="noopener">Résumé (PDF)</a>
          <a class="btn btn-ghost" href="work.html">See my work</a>
        </div>
        {iconrow()}
      </div>
      <div class="portrait">
        <div class="portrait-frame">
          <img src="assets/hector.jpg" alt="Héctor A. Inda Díaz at his workstation with atmospheric data on screen" width="720" height="900">
          <span class="tag">Climate &amp; weather modeling</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="about">
    <div class="wrap">
      <div class="sec-head reveal"><span class="idx">01</span><h2>About</h2></div>
      <div class="two-up">
        <div class="reveal">
          <p class="lead" style="max-width:46ch;color:#2b333a">I'm an atmospheric scientist at <a href="https://www.eaglerockanalytics.com/" target="_blank" rel="noopener" style="color:var(--current);text-decoration:none;border-bottom:1px solid var(--mist)">Eagle Rock Analytics</a>, building cloud-based climate and weather data platforms for California's energy and government agencies.</p>
          <p style="color:var(--slate);margin-top:6px">My background spans atmospheric science and physical oceanography, and I work across the whole pipeline — numerical modeling, big-data analysis, QA/QC, and turning results into tools that non-scientists can actually use.</p>
          <p style="color:var(--slate)">I'm especially drawn to extreme and compound events — atmospheric rivers, the North American Monsoon, extreme precipitation, heat waves, and wildfire-weather — and to the supercomputing and open-source software that make studying them at scale possible.</p>
        </div>
        <div class="reveal">
          <div class="focus-list" style="grid-template-columns:1fr">
            <div><div class="k">Currently</div><div class="v">Atmospheric scientist at Eagle Rock Analytics — climate &amp; weather data platforms</div></div>
            <div><div class="k">Methods</div><div class="v">Numerical modeling · machine learning · large-scale geospatial pipelines · rigorous QA/QC</div></div>
            <div><div class="k">Domains</div><div class="v">Energy · government · climate adaptation · multi-hazard risk</div></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="work">
    <div class="wrap">
      <div class="sec-head reveal"><span class="idx">02</span><h2>Selected work</h2></div>
      <div class="grid cols-3">
        <a class="card reveal" href="work.html#cal-adapt" style="text-decoration:none">
          <span class="eyebrow">Platform</span><h3>Cal-Adapt &amp; Analytics Engine</h3>
          <p>California's cloud climate-data platform — downscaled CMIP6 projections and open-source tools used by utilities, regulators, and the public.</p></a>
        <a class="card reveal" href="work.html#hist-obs" style="text-decoration:none">
          <span class="eyebrow">Data platform</span><h3>Historical Observations Platform</h3>
          <p>~15,900 weather stations from 27 networks across the Western U.S., with custom QA/QC for energy-relevant extremes.</p></a>
        <a class="card reveal" href="work.html#nyserda" style="text-decoration:none">
          <span class="eyebrow">Toolkit</span><h3>NY Storm &amp; Compound Events</h3>
          <p>A Python toolkit that turns decades of messy NCEI storm records into compound-hazard analysis and stakeholder-ready summaries.</p></a>
      </div>
      <p style="margin-top:26px" class="reveal"><a href="work.html" style="color:var(--current);text-decoration:none;font-weight:500">View all work →</a></p>
    </div>
  </section>

  <section class="section">
    <div class="wrap two-up">
      <div class="reveal">
        <div class="sec-head"><span class="idx">03</span><h2>Interests</h2></div>
        <div class="tags">
          <span class="tag">Atmospheric Science</span><span class="tag">Physical Oceanography</span><span class="tag">Climate</span>
          <span class="tag">Atmospheric Rivers</span><span class="tag">Extreme &amp; Compound Events</span><span class="tag">Numerical Modeling</span>
          <span class="tag">Supercomputing</span><span class="tag">Open Science</span><span class="tag">Geospatial Data</span>
        </div>
        <p style="color:var(--slate-soft);font-size:.9rem;margin-top:22px" class="mono">Away from the screen: volleyball · snowboarding · specialty coffee</p>
      </div>
      <div class="reveal">
        <div class="sec-head"><span class="idx">04</span><h2>Education</h2></div>
        <div class="deflist">
          <div class="edu-item"><div><div class="deg">Ph.D., Atmospheric Science</div><div class="org">University of California, Davis</div></div><div class="yr">2021</div></div>
          <div class="edu-item"><div><div class="deg">M.S., Physical Oceanography</div><div class="org">CICESE, Ensenada, Mexico</div></div><div class="yr">2015</div></div>
          <div class="edu-item"><div><div class="deg">B.Sc., Physics</div><div class="org">Universidad Nacional Autónoma de México</div></div><div class="yr">2012</div></div>
          <div class="edu-item"><div><div class="deg">Data Science Certification</div><div class="org">The Data Incubator — Fellowship</div></div><div class="yr">2023</div></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="other-projects">
    <div class="wrap">
      <div class="sec-head reveal"><span class="idx">05</span><h2>Other projects</h2></div>
      <div class="card reveal" style="max-width:none">
        <span class="eyebrow">Family business · Specialty coffee</span>
        <h3>Origen Tequepexpan Café</h3>
        <p style="margin-bottom:0">My family's specialty-coffee project. We grow, process, and roast our own micro-lots from <em>Finca Origen</em> in Tequepexpan, Nayarit — the village where our coffee tradition began — and serve them at our coffee bar in Tepic. I'm a co-founder and coffee producer; my brother Emilio leads roasting and cupping. Natural, honey, and experimental fermentations, with shipping across Mexico.</p>
        <div class="linklist">
          <a href="https://elcafedemitierra.com/origen-tequepexpan-cafe-el-rostro-del-sabor-nayarita.html" target="_blank" rel="noopener">Featured story ↗</a>
          <a href="https://www.instagram.com/origentequepexpancafe/" target="_blank" rel="noopener">Instagram ↗</a>
          <a href="https://www.facebook.com/OrigenTequepexpanCafe/" target="_blank" rel="noopener">Facebook ↗</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="other-interests">
    <div class="wrap">
      <div class="sec-head reveal"><span class="idx">06</span><h2>Other interests</h2></div>
      <div class="two-up">
        <div class="reveal">
          <p class="lead" style="max-width:42ch;color:#2b333a">Amateur barista.</p>
          <p style="color:var(--slate)">Coffee is where the science and the family farm meet a craft. I spend a fair amount of time on espresso, pour-overs, and latte art — chasing the same thing I chase at work: a small, controlled experiment with a delicious result.</p>
          <div class="linklist">
            <a href="https://www.instagram.com/stories/highlights/18035989631492737/?hl=en" target="_blank" rel="noopener">Latte art ↗</a>
            <a href="https://www.instagram.com/stories/highlights/17891385401490586/?hl=en" target="_blank" rel="noopener">Brewing ↗</a>
            <a href="https://www.instagram.com/p/CiVLR_qO-QA/?hl=en" target="_blank" rel="noopener">A favorite pour ↗</a>
            <a href="https://www.facebook.com/photo.php?fbid=667133621339994&set=pb.100063566950868.-2207520000&type=3" target="_blank" rel="noopener">On Facebook ↗</a>
          </div>
        </div>
        <div class="reveal">
          <div class="focus-list" style="grid-template-columns:1fr">
            <div><div class="k">Also</div><div class="v">Volleyball · snowboarding</div></div>
            <div><div class="k">Always</div><div class="v">Specialty coffee — from cherry to cup</div></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section contact">
    <svg class="hero-contours js-contours" data-stroke="#7fd0c9" data-opacity="0.10" data-lines="13" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2">
      <span class="eyebrow">Get in touch</span>
      <h2 style="margin:.5rem 0 1.4rem;max-width:18ch">Open to roles in climate, weather, and geospatial data science.</h2>
      <a class="maillink" href="mailto:indahector@gmail.com">indahector@gmail.com</a>
      {iconrow(" ")}
    </div>
  </section>'''
    else:
        return f'''  <section class="hero">
    <svg class="hero-contours js-contours" data-stroke="#17605c" data-opacity="0.15" data-lines="15" aria-hidden="true"></svg>
    <div class="wrap hero-in">
      <div class="hero-copy">
        <span class="eyebrow">Científico de Datos Atmosféricos y Geoespaciales</span>
        <h1>Héctor A. Inda Díaz</h1>
        <p class="lead">Convierto grandes volúmenes de datos de clima y tiempo en modelos y herramientas con los que la gente —empresas de energía, gobiernos y colegas científicos— puede tomar decisiones.</p>
        <div class="hero-meta">
          <span>Lic. Física</span><span>M.C. Oceanografía Física</span><span>Dr. Ciencias de la Atmósfera</span><span>Científico atmosférico en Eagle Rock Analytics</span>
        </div>
        <div class="actions">
          # <a class="btn btn-primary" href="../assets/Resume_IndaDiaz.pdf" target="_blank" rel="noopener">CV (PDF)</a>
          <a class="btn btn-primary" href="../assets/0.pdf" target="_blank" rel="noopener">CV (PDF)</a>
          <a class="btn btn-ghost" href="work.html">Ver proyectos</a>
        </div>
        {iconrow()}
      </div>
      <div class="portrait">
        <div class="portrait-frame">
          <img src="../assets/hector.jpg" alt="Héctor A. Inda Díaz en su escritorio con datos atmosféricos en pantalla" width="720" height="900">
          <span class="tag">Modelación de clima y tiempo</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="about">
    <div class="wrap">
      <div class="sec-head reveal"><span class="idx">01</span><h2>Acerca de mí</h2></div>
      <div class="two-up">
        <div class="reveal">
          <p class="lead" style="max-width:48ch;color:#2b333a">Soy científico atmosférico en <a href="https://www.eaglerockanalytics.com/" target="_blank" rel="noopener" style="color:var(--current);text-decoration:none;border-bottom:1px solid var(--mist)">Eagle Rock Analytics</a>, donde construyo plataformas de datos de clima y tiempo en la nube para agencias de energía y de gobierno de California.</p>
          <p style="color:var(--slate);margin-top:6px">Mi formación abarca ciencias de la atmósfera y oceanografía física, y trabajo en todo el flujo: modelación numérica, análisis de grandes datos, control de calidad (QA/QC), y convertir resultados en herramientas que personas no científicas puedan realmente usar.</p>
          <p style="color:var(--slate)">Me interesan en especial los eventos extremos y compuestos —ríos atmosféricos, el Monzón de Norteamérica, precipitación extrema, olas de calor y la relación entre clima e incendios— y el supercómputo y el software libre que hacen posible estudiarlos a gran escala.</p>
        </div>
        <div class="reveal">
          <div class="focus-list" style="grid-template-columns:1fr">
            <div><div class="k">Actualmente</div><div class="v">Científico atmosférico en Eagle Rock Analytics — plataformas de datos de clima y tiempo</div></div>
            <div><div class="k">Métodos</div><div class="v">Modelación numérica · aprendizaje automático · flujos geoespaciales a gran escala · QA/QC riguroso</div></div>
            <div><div class="k">Dominios</div><div class="v">Energía · gobierno · adaptación climática · riesgo multiamenaza</div></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="work">
    <div class="wrap">
      <div class="sec-head reveal"><span class="idx">02</span><h2>Proyectos destacados</h2></div>
      <div class="grid cols-3">
        <a class="card reveal" href="work.html#cal-adapt" style="text-decoration:none">
          <span class="eyebrow">Plataforma</span><h3>Cal-Adapt &amp; Analytics Engine</h3>
          <p>La plataforma de datos climáticos en la nube de California — proyecciones CMIP6 reescaladas y herramientas de código abierto usadas por empresas, reguladores y el público.</p></a>
        <a class="card reveal" href="work.html#hist-obs" style="text-decoration:none">
          <span class="eyebrow">Plataforma de datos</span><h3>Plataforma de Observaciones Históricas</h3>
          <p>~15,900 estaciones meteorológicas de 27 redes en el oeste de EE. UU., con QA/QC a la medida para extremos relevantes a la energía.</p></a>
        <a class="card reveal" href="work.html#nyserda" style="text-decoration:none">
          <span class="eyebrow">Herramienta</span><h3>Tormentas y Eventos Compuestos (NY)</h3>
          <p>Una librería en Python que convierte décadas de registros desordenados de tormentas (NCEI) en análisis de amenazas compuestas y resúmenes listos para tomadores de decisiones.</p></a>
      </div>
      <p style="margin-top:26px" class="reveal"><a href="work.html" style="color:var(--current);text-decoration:none;font-weight:500">Ver todos los proyectos →</a></p>
    </div>
  </section>

  <section class="section">
    <div class="wrap two-up">
      <div class="reveal">
        <div class="sec-head"><span class="idx">03</span><h2>Intereses</h2></div>
        <div class="tags">
          <span class="tag">Ciencias de la Atmósfera</span><span class="tag">Oceanografía Física</span><span class="tag">Clima</span>
          <span class="tag">Ríos Atmosféricos</span><span class="tag">Eventos Extremos y Compuestos</span><span class="tag">Modelación Numérica</span>
          <span class="tag">Supercómputo</span><span class="tag">Ciencia Abierta</span><span class="tag">Datos Geoespaciales</span>
        </div>
        <p style="color:var(--slate-soft);font-size:.9rem;margin-top:22px" class="mono">Fuera de la pantalla: voleibol · snowboard · café de especialidad</p>
      </div>
      <div class="reveal">
        <div class="sec-head"><span class="idx">04</span><h2>Formación</h2></div>
        <div class="deflist">
          <div class="edu-item"><div><div class="deg">Doctorado en Ciencias de la Atmósfera</div><div class="org">Universidad de California, Davis</div></div><div class="yr">2021</div></div>
          <div class="edu-item"><div><div class="deg">Maestría en Oceanografía Física</div><div class="org">CICESE, Ensenada, México</div></div><div class="yr">2015</div></div>
          <div class="edu-item"><div><div class="deg">Licenciatura en Física</div><div class="org">Universidad Nacional Autónoma de México</div></div><div class="yr">2012</div></div>
          <div class="edu-item"><div><div class="deg">Certificación en Ciencia de Datos</div><div class="org">The Data Incubator — Fellowship</div></div><div class="yr">2023</div></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="other-projects">
    <div class="wrap">
      <div class="sec-head reveal"><span class="idx">05</span><h2>Otros proyectos</h2></div>
      <div class="card reveal" style="max-width:none">
        <span class="eyebrow">Empresa familiar · Café de especialidad</span>
        <h3>Origen Tequepexpan Café</h3>
        <p style="margin-bottom:0">El proyecto de café de especialidad de mi familia. Cultivamos, procesamos y tostamos nuestros propios microlotes de <em>Finca Origen</em>, en Tequepexpan, Nayarit —el pueblo donde nació nuestra tradición cafetera— y los servimos en nuestra barra en Tepic. Soy cofundador y productor de café; mi hermano Emilio dirige el tueste y la catación. Procesos naturales, honey y fermentaciones experimentales, con envíos a toda la república.</p>
        <div class="linklist">
          <a href="https://elcafedemitierra.com/origen-tequepexpan-cafe-el-rostro-del-sabor-nayarita.html" target="_blank" rel="noopener">Reportaje ↗</a>
          <a href="https://www.instagram.com/origentequepexpancafe/" target="_blank" rel="noopener">Instagram ↗</a>
          <a href="https://www.facebook.com/OrigenTequepexpanCafe/" target="_blank" rel="noopener">Facebook ↗</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="other-interests">
    <div class="wrap">
      <div class="sec-head reveal"><span class="idx">06</span><h2>Otros intereses</h2></div>
      <div class="two-up">
        <div class="reveal">
          <p class="lead" style="max-width:42ch;color:#2b333a">Barista aficionado.</p>
          <p style="color:var(--slate)">El café es donde la ciencia y la finca familiar se encuentran con un oficio. Dedico buen tiempo al espresso, los métodos de filtrado y el arte latte — buscando lo mismo que en el trabajo: un experimento pequeño, controlado y con un resultado delicioso.</p>
          <div class="linklist">
            <a href="https://www.instagram.com/stories/highlights/18035989631492737/?hl=en" target="_blank" rel="noopener">Arte latte ↗</a>
            <a href="https://www.instagram.com/stories/highlights/17891385401490586/?hl=en" target="_blank" rel="noopener">Preparación ↗</a>
            <a href="https://www.instagram.com/p/CiVLR_qO-QA/?hl=en" target="_blank" rel="noopener">Una taza favorita ↗</a>
            <a href="https://www.facebook.com/photo.php?fbid=667133621339994&set=pb.100063566950868.-2207520000&type=3" target="_blank" rel="noopener">En Facebook ↗</a>
          </div>
        </div>
        <div class="reveal">
          <div class="focus-list" style="grid-template-columns:1fr">
            <div><div class="k">También</div><div class="v">Voleibol · snowboard</div></div>
            <div><div class="k">Siempre</div><div class="v">Café de especialidad — del fruto a la taza</div></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section contact">
    <svg class="hero-contours js-contours" data-stroke="#7fd0c9" data-opacity="0.10" data-lines="13" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2">
      <span class="eyebrow">Contacto</span>
      <h2 style="margin:.5rem 0 1.4rem;max-width:20ch">Abierto a oportunidades en ciencia de datos de clima, tiempo y datos geoespaciales.</h2>
      <a class="maillink" href="mailto:indahector@gmail.com">indahector@gmail.com</a>
      {iconrow(" ")}
    </div>
  </section>'''

# =========================================================================
# WORK
# =========================================================================
def work_entry(role, org, yr, h3, body, chips, links=""):
    chips_html="".join(f'<span class="chip">{c}</span>' for c in chips)
    links_html=f'<div class="links">{links}</div>' if links else ""
    anchor=h3[1]
    return f'''      <article class="work-entry reveal" id="{anchor}">
        <div class="meta"><div class="role">{role}</div><div class="org">{org}</div><div class="yr">{yr}</div></div>
        <div class="body"><h3>{h3[0]}</h3><p>{body}</p><div class="chips">{chips_html}</div>{links_html}</div>
      </article>'''

WORK = {
 "en":{
   "eyebrow":"Work","title":"Selected projects",
   "lead":"Most of this work shares a pattern: take large, messy environmental data and turn it into something validated, reproducible, and usable by the people who make decisions with it.",
   "entries":[
     ("Platform","Eagle Rock Analytics","2023 — present",("Cal-Adapt &amp; the Analytics Engine","cal-adapt"),
      "Co-develop California's cloud-based climate-data platform, delivering downscaled CMIP6 projections and analytical tools to energy utilities, regulators, and the public. I build the open-source Python packages and Jupyter notebooks that guide users through geospatial climate analysis — work that underpins California's Fifth Climate Change Assessment.",
      ["Python","xarray","CMIP6","AWS","Jupyter","open source"],'<a href="https://cal-adapt.org/" target="_blank" rel="noopener">cal-adapt.org ↗</a>'),
     ("Data platform","Eagle Rock Analytics","2023 — present",("Historical Observations Data Platform","hist-obs"),
      "An open-source platform synthesizing ~15,900 surface weather stations from 27 networks across the Western U.S. (1980–2022). I helped design custom QA/QC protocols that reliably flag energy-relevant extremes — Santa Ana winds, heat, precipitation, solar radiation — so the dataset is both defensible and ready for downscaling work.",
      ["Python","QA/QC","NetCDF","pandas","cloud storage"],'<a href="https://github.com/Eagle-Rock-Analytics/historical-obs-platform" target="_blank" rel="noopener">GitHub ↗</a>'),
     ("Toolkit","Eagle Rock Analytics","2024 — present",("New York Storm &amp; Compound-Event Toolkit","nyserda"),
      "A Python toolkit and notebook suite that ingests decades of NOAA / NCEI Storm Events records and detects compound hazards — co-occurring and back-to-back events — at the county level. The hard parts were the data and the definitions: schema drift across years, county-vs-NWS-zone geography, reporting bias over time, and making \"compound event\" an explicit, configurable definition. It runs operationally, refreshing classifications and stakeholder-ready HTML summaries as new data is published.",
      ["Python","GeoPandas","Matplotlib","Bokeh","pipelines"],'<a href="https://github.com/Eagle-Rock-Analytics/nyserda" target="_blank" rel="noopener">GitHub ↗</a>'),
     ("Climate × energy","Eagle Rock Analytics","2023 — present",("Renewable Generation Under a Changing Climate","renewables"),
      "High-resolution hourly profiles of solar-PV and wind generation potential through end-of-century for the California Energy Commission's SB100 supply analysis. The focus is on extreme low-generation events — solar and wind \"droughts,\" and their co-occurrence (<em>Dunkelflaute</em>) — that stress a zero-carbon grid.",
      ["Python","xarray","time-series","reV","AWS"]),
     ("Wildfire × weather","Eagle Rock Analytics","2022 — present",("Pyregence — Wildfire &amp; Climate","pyregence"),
      "Built a station-siting optimization algorithm and characterized the regional weather patterns that drive fire events, as part of California's Pyregence consortium. A good example of systems thinking — connecting upstream fire-weather conditions to downstream hydrologic and grid impacts.",
      ["Python","optimization","geospatial","pattern recognition"],'<a href="https://pyregence.org/" target="_blank" rel="noopener">pyregence.org ↗</a>'),
     ("Forecast tooling","Eagle Rock Analytics","2024 — present",("Weather-Pattern Recognition for Santa Clara Watersheds","santa-clara"),
      "A precipitation \"forecast handbook\" for the Santa Clara Valley Water District, using pattern recognition to link large-scale weather patterns to rainfall and runoff — so the district can act on a storm's forecast rather than react to its impacts.",
      ["Python","downscaled models","hydrology","clustering"]),
     ("Vulnerability assessment","Eagle Rock Analytics × AECOM","2024 — present",("SMUD Climate Vulnerability Assessment","smud"),
      "Climate projections for the Sacramento Municipal Utility District (1.5M+ customers), translating temperature, precipitation, wildfire, wind, and hydropower signals into infrastructure and operations guidance — framed for planning and executive audiences.",
      ["Python","CMIP6","risk translation","stakeholder reports"]),
     ("Postdoc · modeling","Lawrence Berkeley National Lab","2022 — 2023",("Regionally-Refined E3SM &amp; the 1997 California Flood","rrm-e3sm"),
      "Ported and ran the Regionally Refined E3SM model on the BigRed200 supercomputer, generating 200+ TB of historical and future output. I designed a 14 km regionally-refined grid and engineered Dask + SLURM pipelines across ~3,840 cores — cutting analysis of 200+ TB from months to about a week — and contributed to recreating California's 1997 New Year's flood in a regionally refined Earth system model.",
      ["E3SM","Dask","SLURM / HPC","Fortran","CUDA","xarray"],'<a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023MS003793" target="_blank" rel="noopener">JAMES paper ↗</a>'),
   ],
   "cta_q":"Want the full record?",
  #  "cta":'<a class="btn btn-primary" href="assets/Resume_IndaDiaz.pdf" target="_blank" rel="noopener">Résumé (PDF)</a><a class="btn btn-ghost" href="assets/CV_IndaDiaz.pdf" target="_blank" rel="noopener">Academic CV (PDF)</a><a class="btn btn-ghost" href="publications.html">Publications</a>',
   "cta":'<a class="btn btn-primary" href="assets/0.pdf" target="_blank" rel="noopener">Résumé (PDF)</a><a class="btn btn-ghost" href="assets/1.pdf" target="_blank" rel="noopener">Academic CV (PDF)</a><a class="btn btn-ghost" href="publications.html">Publications</a>',
 },
 "es":{
   "eyebrow":"Proyectos","title":"Proyectos destacados",
   "lead":"La mayoría de estos proyectos comparten un patrón: tomar datos ambientales grandes y desordenados y convertirlos en algo validado, reproducible y útil para quienes toman decisiones con ellos.",
   "entries":[
     ("Plataforma","Eagle Rock Analytics","2023 — actualidad",("Cal-Adapt &amp; el Analytics Engine","cal-adapt"),
      "Co-desarrollo la plataforma de datos climáticos en la nube de California, que entrega proyecciones CMIP6 reescaladas y herramientas analíticas a empresas de energía, reguladores y el público. Construyo los paquetes de Python de código abierto y los notebooks de Jupyter que guían a los usuarios por el análisis geoespacial del clima — un trabajo que sustenta la Quinta Evaluación del Cambio Climático de California.",
      ["Python","xarray","CMIP6","AWS","Jupyter","código abierto"],'<a href="https://cal-adapt.org/" target="_blank" rel="noopener">cal-adapt.org ↗</a>'),
     ("Plataforma de datos","Eagle Rock Analytics","2023 — actualidad",("Plataforma de Observaciones Históricas","hist-obs"),
      "Una plataforma de código abierto que integra ~15,900 estaciones meteorológicas de superficie de 27 redes en el oeste de EE. UU. (1980–2022). Ayudé a diseñar protocolos de QA/QC a la medida que detectan de forma confiable extremos relevantes para la energía —vientos de Santa Ana, calor, precipitación, radiación solar— para que el conjunto de datos sea defendible y esté listo para el reescalado.",
      ["Python","QA/QC","NetCDF","pandas","almacenamiento en la nube"],'<a href="https://github.com/Eagle-Rock-Analytics/historical-obs-platform" target="_blank" rel="noopener">GitHub ↗</a>'),
     ("Herramienta","Eagle Rock Analytics","2024 — actualidad",("Tormentas y Eventos Compuestos (Nueva York)","nyserda"),
      "Una librería en Python y un conjunto de notebooks que ingiere décadas de registros de tormentas de NOAA / NCEI y detecta amenazas compuestas —eventos simultáneos y consecutivos— a nivel de condado. Lo difícil fueron los datos y las definiciones: cambios de formato entre años, geografía de condado vs. zona del NWS, sesgo de reporte en el tiempo, y hacer de \"evento compuesto\" una definición explícita y configurable. Corre de forma operativa, actualizando clasificaciones y resúmenes en HTML listos para tomadores de decisiones conforme se publican datos nuevos.",
      ["Python","GeoPandas","Matplotlib","Bokeh","pipelines"],'<a href="https://github.com/Eagle-Rock-Analytics/nyserda" target="_blank" rel="noopener">GitHub ↗</a>'),
     ("Clima × energía","Eagle Rock Analytics","2023 — actualidad",("Generación Renovable ante un Clima Cambiante","renewables"),
      "Perfiles horarios de alta resolución del potencial de generación solar fotovoltaica y eólica hasta fin de siglo, para el análisis de suministro SB100 de la Comisión de Energía de California. El foco está en eventos de generación extremadamente baja —\"sequías\" solares y eólicas y su coincidencia (<em>Dunkelflaute</em>)— que tensionan una red cero-carbono.",
      ["Python","xarray","series de tiempo","reV","AWS"]),
     ("Incendios × tiempo","Eagle Rock Analytics","2022 — actualidad",("Pyregence — Incendios y Clima","pyregence"),
      "Construí un algoritmo de optimización para ubicar estaciones y caractericé los patrones de tiempo regionales que impulsan los incendios, como parte del consorcio Pyregence de California. Un buen ejemplo de pensamiento sistémico — conectar las condiciones de tiempo-incendio aguas arriba con sus impactos hidrológicos y a la red aguas abajo.",
      ["Python","optimización","geoespacial","reconocimiento de patrones"],'<a href="https://pyregence.org/" target="_blank" rel="noopener">pyregence.org ↗</a>'),
     ("Pronóstico","Eagle Rock Analytics","2024 — actualidad",("Reconocimiento de Patrones de Tiempo para las Cuencas de Santa Clara","santa-clara"),
      "Un \"manual de pronóstico\" de precipitación para el Santa Clara Valley Water District, que usa reconocimiento de patrones para ligar patrones de tiempo a gran escala con la lluvia y el escurrimiento — de modo que el distrito pueda actuar con el pronóstico de una tormenta en lugar de reaccionar a sus impactos.",
      ["Python","modelos reescalados","hidrología","clustering"]),
     ("Evaluación de vulnerabilidad","Eagle Rock Analytics × AECOM","2024 — actualidad",("Evaluación de Vulnerabilidad Climática de SMUD","smud"),
      "Proyecciones climáticas para el Sacramento Municipal Utility District (más de 1.5M de clientes), traduciendo señales de temperatura, precipitación, incendios, viento e hidroelectricidad en orientación de infraestructura y operación — formulada para audiencias de planeación y dirección.",
      ["Python","CMIP6","traducción de riesgo","reportes para tomadores de decisiones"]),
     ("Postdoctorado · modelación","Lawrence Berkeley National Lab","2022 — 2023",("E3SM de Refinamiento Regional y la Inundación de California de 1997","rrm-e3sm"),
      "Porté y corrí el modelo E3SM de refinamiento regional en la supercomputadora BigRed200, generando más de 200 TB de salida histórica y futura. Diseñé una malla refinada a 14 km y construí flujos con Dask + SLURM en ~3,840 núcleos —reduciendo el análisis de 200+ TB de meses a cerca de una semana— y contribuí a recrear la inundación de Año Nuevo de 1997 de California en un modelo del sistema terrestre de refinamiento regional.",
      ["E3SM","Dask","SLURM / HPC","Fortran","CUDA","xarray"],'<a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023MS003793" target="_blank" rel="noopener">Artículo JAMES ↗</a>'),
   ],
   "cta_q":"¿Quieres el historial completo?",
   #"cta":'<a class="btn btn-primary" href="../assets/Resume_IndaDiaz.pdf" target="_blank" rel="noopener">CV (PDF)</a><a class="btn btn-ghost" href="../assets/CV_IndaDiaz.pdf" target="_blank" rel="noopener">CV académico (PDF)</a><a class="btn btn-ghost" href="publications.html">Publicaciones</a>',
   "cta":'<a class="btn btn-primary" href="../assets/0.pdf" target="_blank" rel="noopener">CV (PDF)</a><a class="btn btn-ghost" href="../assets/1.pdf" target="_blank" rel="noopener">CV académico (PDF)</a><a class="btn btn-ghost" href="publications.html">Publicaciones</a>',
 },
}
def work_main(lang):
    d=WORK[lang]
    entries="\n\n".join(work_entry(*e) for e in d["entries"])
    return f'''  <section class="hero" style="border-bottom:1px solid var(--mist)">
    <svg class="hero-contours js-contours" data-stroke="#17605c" data-opacity="0.13" data-lines="14" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2;padding-block:clamp(48px,8vw,84px)">
      <span class="eyebrow">{d['eyebrow']}</span>
      <h1 style="margin:.5rem 0 1rem;font-size:clamp(2.2rem,5vw,3.4rem)">{d['title']}</h1>
      <p class="lead" style="max-width:54ch">{d['lead']}</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
{entries}
    </div>
  </section>

  <section class="section" style="text-align:center">
    <div class="wrap">
      <p class="lead reveal" style="max-width:38ch;margin-inline:auto">{d['cta_q']}</p>
      <div class="actions reveal" style="justify-content:center;margin-top:18px">{d['cta']}</div>
    </div>
  </section>'''

# =========================================================================
# PUBLICATIONS
# =========================================================================
def pub(yr, title, authors, venue, links=""):
    links_html=f'<div class="links">{links}</div>' if links else ""
    return f'''      <div class="pub reveal">
        <div class="yr">{yr}</div>
        <div><div class="ttl">{title}</div><div class="authors">{authors}</div><div class="venue">{venue}</div>{links_html}</div>
      </div>'''

ME='<span class="me">Inda-Díaz, H.A.</span>'
ARTICLES=[
 ("2023","Recreating the California New Year's flood event of 1997 in a regionally refined Earth system model",
  f"Rhoades, A.M., Zarzycki, C.M., {ME}, Ombadi, M., Pasquier, U., Srivastava, A., Hatchett, B.J., et al.",
  "Journal of Advances in Modeling Earth Systems, 15(10)",'<a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023MS003793" target="_blank" rel="noopener">DOI: 10.1029/2023MS003793</a>'),
 ("2023","Relationship between atmospheric rivers and the dry-season extreme precipitation in central-western Mexico",
  f"{ME} &amp; O'Brien, T.A.","Journal of Geophysical Research: Atmospheres",
  '<a href="https://essopenarchive.org/users/560530/articles/623615-relationship-between-atmospheric-rivers-and-the-dry-season-extreme-precipitation-in-central-western-mexico" target="_blank" rel="noopener">{READ} ↗</a>'),
 ("2022","Increases in future AR count and size: overview of the ARTMIP Tier 2 CMIP5/6 experiment",
  f"O'Brien, T.A., Wehner, M.F., Payne, A.E., Shields, C.A., Rutz, J.J., Leung, L.-R., Ralph, F.M., {ME}, et al.",
  "Journal of Geophysical Research: Atmospheres, 127(6)",'<a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021JD036013" target="_blank" rel="noopener">DOI: 10.1029/2021JD036013</a>'),
 ("2021","Constraining and characterizing the size of atmospheric rivers: a perspective independent from the detection algorithm",
  f"{ME}, O'Brien, T.A., Zhou, Y. &amp; Collins, W.D.","Journal of Geophysical Research: Atmospheres, 126(16)",
  '<a href="https://doi.org/10.1029/2020JD033746" target="_blank" rel="noopener">DOI: 10.1029/2020JD033746</a>'),
 ("2020","Detection of atmospheric rivers with inline uncertainty quantification: TECA-BARD v1.0.1",
  f"O'Brien, T.A., Risser, M.D., Loring, B., Elbashandy, A.A., Krishnan, H., Johnson, J., Patricola, C.M., {ME}, et al.",
  "Geoscientific Model Development, 13(12)",'<a href="https://doi.org/10.5194/gmd-13-6131-2020" target="_blank" rel="noopener">DOI: 10.5194/gmd-13-6131-2020</a>'),
 ("2020","Detection uncertainty matters for understanding atmospheric rivers",
  f"O'Brien, T.A., Payne, A.E., Shields, C.A., Rutz, J., Brands, S., Castellano, C., {ME}, et al.",
  "Bulletin of the American Meteorological Society, 101(6)",""),
]
TALKS=[
 ("2024","Addressing an energy-sector need for a comprehensive, quality-controlled historical weather data platform in Western North America",
  f"Ford, V.L., Di Cecco, G., Doherty, O., Buddhavarapu, S., McClenny, E., <span class=\"me\">Inda-Díaz, H.</span>, et al.","American Meteorological Society Annual Meeting"),
 ("2023","Storyline-based investigations of compound extreme events with a regionally refined Earth system model: the 1997 California New Year's flood",
  f"Rhoades, A., Zarzycki, C.M., {ME}, Ombadi, M., et al.","AGU Fall Meeting"),
 ("2022","Change in size of atmospheric rivers under future climate scenarios: a perspective independent of the detection algorithm",
  f"{ME}, Zhou, Y., O'Brien, T.A. &amp; Collins, W.D.","International Atmospheric River Conference"),
 ("2022","Using long-term composites and objective tracking to assess the spatiotemporal characteristics, variability, and future changes in atmospheric rivers",
  f"{ME}","{THESIS} — University of California, Davis"),
 ("2021","Anthropogenic and meteorological contributions to the 2021 Pacific Northwest heatwave",
  f"Bercos-Hickey, E., O'Brien, T., Wehner, M., Swenson, L.M., Patricola, C., {ME}, et al.","AGU Fall Meeting"),
]
PUBS={
 "en":{"eyebrow":"Publications","title":"Publications &amp; talks",
   "lead":"Peer-reviewed work on atmospheric rivers, extreme and compound events, and regionally refined Earth system modeling.",
  #  "btns":'<a class="btn btn-primary" href="https://scholar.google.com/citations?user=MBdNFm0AAAAJ" target="_blank" rel="noopener">Full list on Google Scholar ↗</a><a class="btn btn-ghost" href="assets/CV_IndaDiaz.pdf" target="_blank" rel="noopener">Academic CV (PDF)</a>',
   "btns":'<a class="btn btn-primary" href="https://scholar.google.com/citations?user=MBdNFm0AAAAJ" target="_blank" rel="noopener">Full list on Google Scholar ↗</a><a class="btn btn-ghost" href="assets/1.pdf" target="_blank" rel="noopener">Academic CV (PDF)</a>',
   "h_articles":"Peer-reviewed articles","h_talks":"Selected talks &amp; theses","read":"Read preprint","thesis":"Ph.D. dissertation"},
 "es":{"eyebrow":"Publicaciones","title":"Publicaciones y ponencias",
   "lead":"Trabajo revisado por pares sobre ríos atmosféricos, eventos extremos y compuestos, y modelación del sistema terrestre con refinamiento regional.",
  #  "btns":'<a class="btn btn-primary" href="https://scholar.google.com/citations?user=MBdNFm0AAAAJ" target="_blank" rel="noopener">Lista completa en Google Scholar ↗</a><a class="btn btn-ghost" href="../assets/CV_IndaDiaz.pdf" target="_blank" rel="noopener">CV académico (PDF)</a>',
   "btns":'<a class="btn btn-primary" href="https://scholar.google.com/citations?user=MBdNFm0AAAAJ" target="_blank" rel="noopener">Lista completa en Google Scholar ↗</a><a class="btn btn-ghost" href="../assets/1.pdf" target="_blank" rel="noopener">CV académico (PDF)</a>',
   "h_articles":"Artículos revisados por pares","h_talks":"Ponencias y tesis seleccionadas","read":"Leer preprint","thesis":"Tesis doctoral"},
}
def pubs_main(lang):
    d=PUBS[lang]
    arts="\n".join(pub(y,t,a,v,lk.replace("{READ}",d["read"])) for (y,t,a,v,lk) in ARTICLES)
    tks="\n".join(pub(y,t,a,v.replace("{THESIS}",d["thesis"])) for (y,t,a,v) in TALKS)
    pre="../" if lang=="es" else ""
    return f'''  <section class="hero" style="border-bottom:1px solid var(--mist)">
    <svg class="hero-contours js-contours" data-stroke="#17605c" data-opacity="0.13" data-lines="14" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2;padding-block:clamp(48px,8vw,84px)">
      <span class="eyebrow">{d['eyebrow']}</span>
      <h1 style="margin:.5rem 0 1rem;font-size:clamp(2.2rem,5vw,3.4rem)">{d['title']}</h1>
      <p class="lead" style="max-width:52ch">{d['lead']}</p>
      <div class="actions" style="margin-top:22px">{d['btns']}</div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal"><span class="idx">01</span><h2>{d['h_articles']}</h2></div>
{arts}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal"><span class="idx">02</span><h2>{d['h_talks']}</h2></div>
{tks}
    </div>
  </section>'''

# =========================================================================
# SCIENCE COMMUNICATION (writing.html)
# =========================================================================
def scicomm_main(lang):
    pre="../" if lang=="es" else ""
    ar_href="rios-atmosfericos.html" if lang=="es" else "atmospheric-rivers.html"
    if lang=="en":
        return f'''  <section class="hero" style="border-bottom:1px solid var(--mist)">
    <svg class="hero-contours js-contours" data-stroke="#17605c" data-opacity="0.13" data-lines="14" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2;padding-block:clamp(48px,8vw,84px)">
      <span class="eyebrow">Science communication</span>
      <h1 style="margin:.5rem 0 1rem;font-size:clamp(2.2rem,5vw,3.4rem)">Notes &amp; explainers</h1>
      <p class="lead" style="max-width:54ch">Short pieces that try to make weather and climate science legible — the way I'd explain a result to a planner, a coffee grower, or a curious friend, not another specialist.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="grid cols-2">
        <a class="note-card reveal" href="{ar_href}">
          <div class="k"><span>Explainer · Atmospheric rivers</span><span>→</span></div>
          <h3>What is an atmospheric river?</h3>
          <p>The "rivers in the sky" that deliver much of the West Coast's water — and its floods. What they are, why they matter, and how a warming climate is changing them. <strong>Read on this site →</strong></p>
        </a>
        <a class="note-card reveal" href="https://elcafedemitierra.com/rios-atmosfericos-cabanuelas-o-perjuicios-a-la-cosecha-de-cafe.html" target="_blank" rel="noopener">
          <div class="k"><span>Published · El Café de Mi Tierra (ES)</span><span>↗</span></div>
          <h3>Atmospheric rivers and the coffee harvest</h3>
          <p>My Spanish-language feature for a coffee magazine: how winter atmospheric rivers — folk-predicted by the <em>cabañuelas</em> — damage Mexico's Pacific coffee harvest, and what producers can do about it.</p>
        </a>
        <a class="note-card reveal" href="https://github.com/Eagle-Rock-Analytics/nyserda" target="_blank" rel="noopener">
          <div class="k"><span>Explainer · Compound hazards</span><span>↗</span></div>
          <h3>When hazards stack: compound &amp; cascading events</h3>
          <p>A heatwave during a drought, or back-to-back storms, can be far worse than either alone. What "compound event" means, and how I detect them in decades of messy records.</p>
        </a>
        <a class="note-card reveal" href="https://cal-adapt.org/" target="_blank" rel="noopener">
          <div class="k"><span>Practice · Data for decisions</span><span>↗</span></div>
          <h3>Making climate data usable for non-scientists</h3>
          <p>A model output is not a decision. How Cal-Adapt turns downscaled projections into tools a utility planner or regulator can actually pick up and use.</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section contact">
    <svg class="hero-contours js-contours" data-stroke="#7fd0c9" data-opacity="0.10" data-lines="13" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2">
      <span class="eyebrow">Let's talk</span>
      <h2 style="margin:.5rem 0 1.4rem;max-width:20ch">Have a science-communication project, or want to collaborate?</h2>
      <a class="maillink" href="mailto:indahector@gmail.com">indahector@gmail.com</a>
    </div>
  </section>'''
    else:
        return f'''  <section class="hero" style="border-bottom:1px solid var(--mist)">
    <svg class="hero-contours js-contours" data-stroke="#17605c" data-opacity="0.13" data-lines="14" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2;padding-block:clamp(48px,8vw,84px)">
      <span class="eyebrow">Divulgación</span>
      <h1 style="margin:.5rem 0 1rem;font-size:clamp(2.2rem,5vw,3.4rem)">Notas y explicaciones</h1>
      <p class="lead" style="max-width:56ch">Textos breves que buscan hacer legible la ciencia del clima y el tiempo — como se lo explicaría a un planificador, a un caficultor o a un amigo curioso, no a otro especialista.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="grid cols-2">
        <a class="note-card reveal" href="{ar_href}">
          <div class="k"><span>Explicación · Ríos atmosféricos</span><span>→</span></div>
          <h3>¿Qué es un río atmosférico?</h3>
          <p>Los "ríos en el cielo" que traen buena parte del agua de la costa oeste — y también sus inundaciones. Qué son, por qué importan y cómo los está cambiando el calentamiento global. <strong>Leer en este sitio →</strong></p>
        </a>
        <a class="note-card reveal" href="https://elcafedemitierra.com/rios-atmosfericos-cabanuelas-o-perjuicios-a-la-cosecha-de-cafe.html" target="_blank" rel="noopener">
          <div class="k"><span>Publicado · El Café de Mi Tierra</span><span>↗</span></div>
          <h3>Ríos atmosféricos y la cosecha de café</h3>
          <p>Mi artículo para una revista de café: cómo los ríos atmosféricos de invierno —que las <em>cabañuelas</em> intentan predecir— dañan la cosecha de café de la vertiente del Pacífico mexicano, y qué pueden hacer los productores.</p>
        </a>
        <a class="note-card reveal" href="https://github.com/Eagle-Rock-Analytics/nyserda" target="_blank" rel="noopener">
          <div class="k"><span>Explicación · Amenazas compuestas</span><span>↗</span></div>
          <h3>Cuando las amenazas se apilan: eventos compuestos y en cascada</h3>
          <p>Una ola de calor durante una sequía, o tormentas consecutivas, pueden ser mucho peores que cada una por separado. Qué significa "evento compuesto" y cómo los detecto en décadas de registros desordenados.</p>
        </a>
        <a class="note-card reveal" href="https://cal-adapt.org/" target="_blank" rel="noopener">
          <div class="k"><span>Práctica · Datos para decidir</span><span>↗</span></div>
          <h3>Hacer útiles los datos climáticos para no científicos</h3>
          <p>La salida de un modelo no es una decisión. Cómo Cal-Adapt convierte proyecciones reescaladas en herramientas que un planificador o un regulador realmente pueden usar.</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section contact">
    <svg class="hero-contours js-contours" data-stroke="#7fd0c9" data-opacity="0.10" data-lines="13" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2">
      <span class="eyebrow">Hablemos</span>
      <h2 style="margin:.5rem 0 1.4rem;max-width:22ch">¿Tienes un proyecto de divulgación o quieres colaborar?</h2>
      <a class="maillink" href="mailto:indahector@gmail.com">indahector@gmail.com</a>
    </div>
  </section>'''

# =========================================================================
# ARTICLE: What is an atmospheric river?
# =========================================================================
def article_main(lang):
    if lang=="en":
        back="writing.html"
        return f'''  <section class="hero article" style="border-bottom:1px solid var(--mist)">
    <svg class="hero-contours js-contours" data-stroke="#17605c" data-opacity="0.13" data-lines="14" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2;padding-block:clamp(44px,7vw,76px)">
      <span class="eyebrow">Explainer · Atmospheric rivers</span>
      <h1 style="margin:.5rem 0 .6rem;font-size:clamp(2.1rem,4.6vw,3.2rem)">What is an atmospheric river?</h1>
      <div class="article-meta"><span>Héctor A. Inda Díaz</span><span>~7 min read</span><span><a href="{back}" style="color:var(--current);text-decoration:none">← Science communication</a></span></div>
    </div>
  </section>

  <section class="section article">
    <div class="wrap prose">
      <p class="lead" style="font-size:1.2rem;color:#2b333a">Have you ever heard older relatives predict the whole year's weather from the first days of January? In Mexico that tradition is called the <em>cabañuelas</em>. It has no scientific basis — but the winter rains it tries to read are very real, and one of their biggest drivers has a name: the atmospheric river.</p>

      <h2>Rivers in the sky</h2>
      <p>Atmospheric rivers — sometimes called "flying rivers" or "rivers of vapor" — are long, narrow corridors in the atmosphere that carry enormous amounts of water as vapor over long distances. A single one is typically narrow (300–800 km wide) but very long (1,500–3,000 km), stretching from the tropics and subtropics toward colder regions, and it usually lasts one to three days.</p>

      <div class="keyfacts">
        <div><div class="n">300–800 km</div><div class="l">typical width</div></div>
        <div><div class="n">1,500–3,000 km</div><div class="l">typical length</div></div>
        <div><div class="n">1–3 days</div><div class="l">typical duration</div></div>
      </div>

      <h2>How they turn into rain</h2>
      <p>As long as that vapor stays aloft, nothing dramatic happens. But when an atmospheric river runs into a cold air mass moving down from the north, or a mountain range that forces it to rise, the vapor cools, condenses, and falls — as rain or snow. Depending on the conditions and how long it lingers, the result can be intense, "atypical" precipitation that reshapes local weather, alters the water supply, and can do real damage on the ground.</p>

      <h2>Why they matter</h2>
      <p>Atmospheric rivers are a major part of the planet's water cycle. On the U.S. West Coast they deliver much of the year's water — and many of its worst floods. They redistribute where and how much it rains, which makes them central both to water security and to flood risk. That dual role is exactly why they're a major subject of study in atmospheric science: the better we understand them, the better we can anticipate and prepare for their impacts.</p>

      <h2>A warming climate is changing them</h2>
      <p>Global warming changes the timing and intensity of many weather phenomena, and atmospheric rivers are no exception. Studies project that their frequency may rise by roughly 30%, and that the amount of vapor they transport may increase by up to about 37%, with rivers that are, on average, longer and wider. More water, arriving more often, makes the activities that depend on stable weather — agriculture especially — more vulnerable.</p>

      <h2>The view from a coffee farm</h2>
      <p>That last point isn't abstract for me. My family grows coffee in Nayarit, on Mexico's Pacific slope, and the coffee harvest runs from roughly November to March — right through the season when these winter rivers arrive. In February 2024, a single atmospheric river dropped about 60 mm of rain in two days across the Pacific coffee states — Nayarit, Jalisco, Colima, and Guerrero. In Nayarit it knocked roughly half the harvest to the ground, and about a quarter of the cherries split and dried on the branch. Excess moisture rots fruit, splits cherries, saturates soils, and stalls the sun-drying that natural and honey-processed coffees depend on.</p>
      <p>I wrote about that event, and what growers can do to soften the next one, in a Spanish-language feature for a coffee magazine.</p>
      <blockquote>Global climate change, deforestation, and soil degradation may make atmospheric rivers more frequent and intense — while also lowering the resilience of coffee agro-ecosystems to their effects.</blockquote>
      <p><a href="https://elcafedemitierra.com/rios-atmosfericos-cabanuelas-o-perjuicios-a-la-cosecha-de-cafe.html" target="_blank" rel="noopener">Read the full piece in El Café de Mi Tierra ↗</a></p>

      <h2>How we study them</h2>
      <p>Part of my research is about a deceptively hard question: how big <em>is</em> an atmospheric river? The answer depends on how you choose to detect it, so I've worked on ways to measure their size and intensity that don't depend on any single detection algorithm — and on quantifying the uncertainty that comes with the choice. Getting that right is what lets us say something defensible about how they'll change.</p>
      <p><a href="https://doi.org/10.1029/2020JD033746" target="_blank" rel="noopener">See the research paper ↗</a> · <a href="{back}">More notes &amp; explainers</a></p>
    </div>
  </section>'''
    else:
        back="writing.html"
        return f'''  <section class="hero article" style="border-bottom:1px solid var(--mist)">
    <svg class="hero-contours js-contours" data-stroke="#17605c" data-opacity="0.13" data-lines="14" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2;padding-block:clamp(44px,7vw,76px)">
      <span class="eyebrow">Explicación · Ríos atmosféricos</span>
      <h1 style="margin:.5rem 0 .6rem;font-size:clamp(2.1rem,4.6vw,3.2rem)">¿Qué es un río atmosférico?</h1>
      <div class="article-meta"><span>Héctor A. Inda Díaz</span><span>~7 min de lectura</span><span><a href="{back}" style="color:var(--current);text-decoration:none">← Divulgación</a></span></div>
    </div>
  </section>

  <section class="section article">
    <div class="wrap prose">
      <p class="lead" style="font-size:1.2rem;color:#2b333a">¿Alguna vez escuchaste a los mayores predecir el clima de todo el año a partir de los primeros días de enero? En México esa tradición se llama las <em>cabañuelas</em>. No tiene base científica — pero las lluvias de invierno que intenta leer son muy reales, y uno de sus principales causantes tiene nombre: el río atmosférico.</p>

      <h2>Ríos en el cielo</h2>
      <p>Los ríos atmosféricos —también llamados "ríos voladores" o "ríos de vapor"— son corredores largos y estrechos en la atmósfera que transportan enormes cantidades de agua en forma de vapor a grandes distancias. Suelen ser estrechos (300–800 km de ancho) pero muy largos (1,500–3,000 km), extendiéndose desde regiones tropicales y subtropicales hacia zonas más frías, y duran aproximadamente de uno a tres días.</p>

      <div class="keyfacts">
        <div><div class="n">300–800 km</div><div class="l">ancho típico</div></div>
        <div><div class="n">1,500–3,000 km</div><div class="l">longitud típica</div></div>
        <div><div class="n">1–3 días</div><div class="l">duración típica</div></div>
      </div>

      <h2>Cómo se convierten en lluvia</h2>
      <p>Mientras ese vapor permanece en las alturas, no ocurre nada dramático. Pero cuando un río atmosférico se encuentra con una masa de aire frío que baja desde el norte, o con una cordillera que lo obliga a elevarse, el vapor se enfría, se condensa y cae — como lluvia o nieve. Según las condiciones y cuánto se prolongue, el resultado puede ser una precipitación intensa y "atípica" que altera el clima local, modifica el suministro de agua y puede causar daños reales en el terreno.</p>

      <h2>Por qué importan</h2>
      <p>Los ríos atmosféricos son una pieza central del ciclo del agua del planeta. En la costa oeste de Estados Unidos aportan buena parte del agua del año — y muchas de sus peores inundaciones. Redistribuyen dónde y cuánto llueve, lo que los vuelve clave tanto para la seguridad hídrica como para el riesgo de inundación. Ese doble papel es justo lo que los hace un gran objeto de estudio en las ciencias atmosféricas: entenderlos mejor nos permite anticipar y prevenir sus impactos.</p>

      <h2>El calentamiento global los está cambiando</h2>
      <p>El calentamiento global modifica la periodicidad e intensidad de muchos fenómenos, y los ríos atmosféricos no son la excepción. Se proyecta que su frecuencia aumente alrededor de 30%, y que el vapor que transportan se incremente hasta cerca de 37%, con ríos en promedio más largos y anchos. Más agua, llegando con más frecuencia, vuelve más vulnerables a las actividades que dependen de un clima estable — la agricultura en especial.</p>

      <h2>La vista desde una finca de café</h2>
      <p>Ese último punto no es abstracto para mí. Mi familia cultiva café en Nayarit, en la vertiente del Pacífico mexicano, y la cosecha va de noviembre a marzo — justo en la temporada en que llegan estos ríos de invierno. En febrero de 2024, un solo río atmosférico dejó cerca de 60 mm de lluvia en dos días sobre los estados cafetaleros del Pacífico —Nayarit, Jalisco, Colima y Guerrero—. En Nayarit tiró al menos la mitad de la cosecha, y alrededor de una cuarta parte de los frutos se reventaron y secaron en la rama. El exceso de humedad pudre el fruto, lo revienta, satura el suelo y frena el secado al sol del que dependen los cafés de proceso natural y honey.</p>
      <p>Escribí sobre ese evento, y sobre lo que los productores pueden hacer para suavizar el siguiente, en un artículo para una revista de café.</p>
      <blockquote>El cambio climático global, la deforestación y la degradación de los suelos pueden aumentar la frecuencia e intensidad de los ríos atmosféricos — y a la vez reducir la resiliencia de los agroecosistemas de cafetales ante sus efectos.</blockquote>
      <p><a href="https://elcafedemitierra.com/rios-atmosfericos-cabanuelas-o-perjuicios-a-la-cosecha-de-cafe.html" target="_blank" rel="noopener">Leer el artículo completo en El Café de Mi Tierra ↗</a></p>

      <h2>Cómo los estudiamos</h2>
      <p>Parte de mi investigación gira en torno a una pregunta engañosamente difícil: ¿qué tan grande <em>es</em> un río atmosférico? La respuesta depende de cómo decidas detectarlo, así que he trabajado en formas de medir su tamaño e intensidad que no dependan de un único algoritmo de detección — y en cuantificar la incertidumbre que conlleva esa elección. Hacerlo bien es lo que nos permite decir algo defendible sobre cómo van a cambiar.</p>
      <p><a href="https://doi.org/10.1029/2020JD033746" target="_blank" rel="noopener">Ver el artículo científico ↗</a> · <a href="{back}">Más notas y explicaciones</a></p>
    </div>
  </section>'''

# =========================================================================
# 404
# =========================================================================
def notfound_main(lang):
    if lang=="en":
        return '''  <section class="hero" style="border-bottom:none">
    <svg class="hero-contours js-contours" data-stroke="#17605c" data-opacity="0.14" data-lines="15" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2;padding-block:clamp(80px,16vw,160px);text-align:center">
      <span class="eyebrow">Error 404</span>
      <h1 style="margin:.6rem 0 1rem;font-size:clamp(3rem,9vw,6rem)">Off the map</h1>
      <p class="lead" style="max-width:40ch;margin-inline:auto">This page drifted out of the domain. Let's get you back to solid ground.</p>
      <div class="actions" style="justify-content:center;margin-top:26px">
        <a class="btn btn-primary" href="index.html">Back to home</a>
        <a class="btn btn-ghost" href="work.html">See the work</a>
      </div>
    </div>
  </section>'''
    else:
        return '''  <section class="hero" style="border-bottom:none">
    <svg class="hero-contours js-contours" data-stroke="#17605c" data-opacity="0.14" data-lines="15" aria-hidden="true"></svg>
    <div class="wrap" style="position:relative;z-index:2;padding-block:clamp(80px,16vw,160px);text-align:center">
      <span class="eyebrow">Error 404</span>
      <h1 style="margin:.6rem 0 1rem;font-size:clamp(3rem,9vw,6rem)">Fuera del mapa</h1>
      <p class="lead" style="max-width:40ch;margin-inline:auto">Esta página se salió del dominio. Volvamos a tierra firme.</p>
      <div class="actions" style="justify-content:center;margin-top:26px">
        <a class="btn btn-primary" href="index.html">Volver al inicio</a>
        <a class="btn btn-ghost" href="work.html">Ver proyectos</a>
      </div>
    </div>
  </section>'''

# =========================================================================
# BUILD ALL
# =========================================================================
PAGES=[
 # (filename, en_title, en_desc, es_title, es_desc, main_fn, active)
 ("index.html",
  "Héctor A. Inda Díaz — Atmospheric &amp; Geospatial Data Scientist",
  "Héctor A. Inda Díaz is an atmospheric and geospatial data scientist building climate and weather data platforms, numerical models, and decision tools.",
  "Héctor A. Inda Díaz — Científico de Datos Atmosféricos y Geoespaciales",
  "Héctor A. Inda Díaz es científico de datos atmosféricos y geoespaciales: plataformas de datos de clima y tiempo, modelación numérica y herramientas de decisión.",
  home_main,"index.html"),
 ("work.html",
  "Work — Héctor A. Inda Díaz","Selected projects in climate and weather data platforms, multi-hazard analysis, and numerical modeling.",
  "Proyectos — Héctor A. Inda Díaz","Proyectos en plataformas de datos de clima y tiempo, análisis multiamenaza y modelación numérica.",
  work_main,"work.html"),
 ("publications.html",
  "Publications — Héctor A. Inda Díaz","Peer-reviewed publications and selected talks on atmospheric rivers and Earth system modeling.",
  "Publicaciones — Héctor A. Inda Díaz","Publicaciones revisadas por pares y ponencias sobre ríos atmosféricos y modelación del sistema terrestre.",
  pubs_main,"publications.html"),
 ("writing.html",
  "Science communication — Héctor A. Inda Díaz","Notes and explainers on atmospheric rivers, compound hazards, and making climate data usable.",
  "Divulgación — Héctor A. Inda Díaz","Notas y explicaciones sobre ríos atmosféricos, amenazas compuestas y datos climáticos útiles.",
  scicomm_main,"writing.html"),
 ("404.html",
  "Page not found — Héctor A. Inda Díaz","Page not found.",
  "Página no encontrada — Héctor A. Inda Díaz","Página no encontrada.",
  notfound_main,""),
]

for (fn,ent,edc,est,edsc,mfn,active) in PAGES:
    render("en",fn,ent,edc,mfn("en"),active,"es/"+fn,U(fn),ES(fn))
    if SHOW_ES:
        render("es",fn,est,edsc,mfn("es"),active,"../"+fn,U(fn),ES(fn))

# Article pages (different filenames per language)
render("en","atmospheric-rivers.html",
       "What is an atmospheric river? — Héctor A. Inda Díaz",
       "A plain-language explainer on atmospheric rivers: what they are, why they matter, how climate change is altering them, and what they mean for the coffee harvest.",
       article_main("en"),"writing.html","es/rios-atmosfericos.html",
       U("atmospheric-rivers.html"),ES("rios-atmosfericos.html"))
if SHOW_ES:
    render("es","rios-atmosfericos.html",
           "¿Qué es un río atmosférico? — Héctor A. Inda Díaz",
           "Una explicación accesible sobre los ríos atmosféricos: qué son, por qué importan, cómo los cambia el clima y qué significan para la cosecha de café.",
           article_main("es"),"writing.html","../atmospheric-rivers.html",
           U("atmospheric-rivers.html"),ES("rios-atmosfericos.html"))

print("Built pages:")
for f in sorted(os.listdir(".")):
    if f.endswith(".html"): print("  ", f)
if SHOW_ES and os.path.isdir("es"):
    print("  es/:")
    for f in sorted(os.listdir("es")):
        if f.endswith(".html"): print("    ", f)
else:
    print("  (Spanish version hidden — SHOW_ES = False)")
