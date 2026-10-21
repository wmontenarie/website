# Bouwt de vier themapagina's (werkdruk.html, burn-out-en-verzuim.html, vitaliteitsbeleid.html, cultuurverandering.html)
# uit themas.py. De kaarten van de artikelen komen uit artikelen.html, dus draai dit opnieuw na een nieuw artikel.
import re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from themas import THEMAS
from pagina_basis import maak_pagina, W

lijst = open(W + 'artikelen.html', encoding='utf-8').read()
KAARTEN = {}
for li in re.findall(r' *<li class="kaart[^"]*">\s*<a href="artikelen/[a-z0-9-]+">.*?</li>\n', lijst, re.S):
    slug = re.search(r'href="artikelen/([a-z0-9-]+)"', li).group(1)
    KAARTEN.setdefault(slug, li.replace(' uitgelicht', ''))

def kaarten(slugs):
    ontbreekt = [s for s in slugs if s not in KAARTEN]
    assert not ontbreekt, 'geen kaart in artikelen.html voor: %s' % ontbreekt
    return '      <ul class="kaarten">\n' + ''.join(KAARTEN[s] for s in slugs) + '      </ul>\n'

def ico(pad): return '<span class="ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg></span>' % pad
I_BOEK = ico('<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5V21h16"/>')
I_GROEP = ico('<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.2c2.8.3 5 2.6 5 5.8"/>')
I_TOOL = ico('<path d="M4 20V10M10 20V4M16 20v-7M21 20H3"/>')

for t in THEMAS:
    wp, tr, tool = t['whitepaper'], t['training'], t['tool']
    andere = ' '.join('<a href="%s">%s</a>' % (a['slug'], a['naam']) for a in THEMAS if a is not t)
    ook = ''
    if t['ook']:
        ook = '      <h2 class="ruim">Ook interessant</h2>\n' + kaarten(t['ook'])
    MAIN = f'''<main>
  <section class="artikelen-kop">
    <div class="wrap">
      <p class="kruimel"><a href="artikelen">Artikelen</a> <span aria-hidden="true">›</span> {t['naam']}</p>
      <h1>{t['h1']}</h1>
      <p class="intro">{t['intro']}</p>
    </div>
  </section>
  <section class="sectie artikelen-lijst">
    <div class="wrap">
      <div class="thema-wat">
        <h2>{t['wat'][0]}</h2>
        <p>{t['wat'][1]}</p>
      </div>
      <div class="thema-hulp">
        <a class="thema-blok wp" href="{wp[0]}"><img src="{wp[3]}" width="560" height="793" alt="Omslag van de whitepaper {wp[1]}" loading="lazy"><span><span class="podcast-label">Gratis whitepaper</span><strong>{wp[1]}</strong><span>{wp[2]}</span><span class="lees">Download de whitepaper</span></span></a>
        <a class="thema-blok" href="{tr[0]}">{I_GROEP}<span><span class="podcast-label">Training</span><strong>{tr[1]}</strong><span>{tr[2]}</span><span class="lees">Bekijk de training</span></span></a>
        <a class="thema-blok" href="{tool[0]}">{I_TOOL}<span><span class="podcast-label">Gratis tool</span><strong>{tool[1]}</strong><span>{tool[2]}</span><span class="lees">Naar de tool</span></span></a>
      </div>
      <h2 class="ruim">Artikelen over {t['naam'].lower()}</h2>
{kaarten(t['artikelen'])}{ook}      <div class="artikel-cta">
        <h2>Hier samen mee aan de slag?</h2>
        <p>Vertel me wat er speelt. In een gratis gesprek van 30 minuten kijken we wat zinvol is voor jouw organisatie.</p>
        <div class="hero-knoppen">
          <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
          <a class="knop omlijnd" href="contact">Neem contact op</a>
        </div>
      </div>
      <p class="thema-andere"><strong>Andere thema's:</strong> {andere}</p>
    </div>
  </section>
</main>
'''
    url = 'https://waltermontenarie.com/' + t['slug']
    LD = [
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": t['wat'][0], "acceptedAnswer": {"@type": "Answer", "text": t['wat'][1]}}]},
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": t['h1'], "description": t['beschr'], "url": url, "inLanguage": "nl",
         "hasPart": [{"@type": "Article", "url": "https://waltermontenarie.com/artikelen/" + s} for s in t['artikelen'] + t['ook']]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Artikelen", "item": "https://waltermontenarie.com/artikelen"},
            {"@type": "ListItem", "position": 2, "name": t['naam'], "item": url}]},
    ]
    maak_pagina(t['slug'], t['titel'], t['beschr'], t['titel'], MAIN, LD=LD, MENU='artikelen')
