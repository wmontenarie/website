# Voegt aan elk artikel toe: kruimelpad (Artikelen > thema), leestijd en een blok over de auteur.
# Veilig om vaker te draaien: eerdere toevoegingen worden eerst weggehaald.
# Draai na elk nieuw of gewijzigd artikel: python3 beheer/artikel_extra.py
# De bouwscripts van artikelen (artikel_basis.py) roepen dit zelf aan.
import re, os, sys, glob, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from themas import thema_van
W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')

AUTEUR = '''      <aside class="auteur" aria-label="Over de auteur">
        <img src="../img/walter-montenarie-auteur.webp" width="96" height="96" alt="Walter Montenarie" loading="lazy">
        <div>
          <p class="auteur-naam">Walter Montenarie</p>
          <p>Ik ben adviseur duurzame inzetbaarheid, coach en trainer. Na mijn burn-out in 2010 help ik organisaties om gezonder en met meer plezier te werken. Ik heb ruim 30 jaar ervaring in gezondheidscoaching, management en strategie.</p>
          <div class="auteur-links">
            <a href="../over-mij">Meer over mij</a>
            <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
          </div>
        </div>
      </aside>
'''

def kaarten_bijwerken(tijden):
    # zet dezelfde leestijd op de kaarten van de overzichtspagina
    pad = W + 'artikelen.html'
    s = open(pad, encoding='utf-8').read()
    def zet(m):
        slug = m.group(1)
        return m.group(0) if slug not in tijden else re.sub(r'\d+ min lezen', '%d min lezen' % tijden[slug], m.group(0))
    s = re.sub(r'<a href="artikelen/([a-z0-9-]+)">.*?</a>', zet, s, flags=re.S)
    open(pad, 'w', encoding='utf-8').write(s)

def ontdoe(s):
    s = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "BreadcrumbList".*?</script>\n', '', s)
    s = re.sub(r' *<p class="kruimel">.*?</p>\n(?= *<p class="artikel-meta">)', '', s)
    s = re.sub(r' \| <span class="leestijd">\d+ min lezen</span>', '', s)
    s = re.sub(r' *<aside class="auteur".*?</aside>\n', '', s, flags=re.S)
    return s

def verrijk(pad):
    slug = os.path.basename(pad)[:-5]
    s = ontdoe(open(pad, encoding='utf-8').read())
    t = thema_van(slug)
    assert t, 'artikel %s hoort bij geen thema: zet het in beheer/themas.py' % slug
    h1 = re.search(r'<h1>(.*?)</h1>', s).group(1)
    # leestijd: alle tekst van het artikel tot de deelknoppen, 220 woorden per minuut
    main = s[s.index('<main>'):s.index('<aside class="deel"')]
    woorden = len(re.sub(r'<[^>]+>', ' ', main).split())
    minuten = max(1, math.ceil(woorden / 220))
    s, n = re.subn(r'(<p class="artikel-meta">[^<]*)</p>', r'\1 | <span class="leestijd">%d min lezen</span></p>' % minuten, s, count=1)
    assert n == 1
    kruimel = '<p class="kruimel"><a href="../artikelen">Artikelen</a> <span aria-hidden="true">›</span> <a href="../%s">%s</a></p>' % (t['slug'], t['naam'])
    s, n = re.subn(r'( *)(<p class="artikel-meta">)', lambda m: m.group(1) + kruimel + '\n' + m.group(1) + m.group(2), s, count=1)
    assert n == 1
    assert s.count('<aside class="deel"') == 1
    s = s.replace('      <aside class="deel"', AUTEUR + '      <aside class="deel"', 1)
    import html as H
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Artikelen", "item": "https://waltermontenarie.com/artikelen"},
        {"@type": "ListItem", "position": 2, "name": t['naam'], "item": "https://waltermontenarie.com/" + t['slug']},
        {"@type": "ListItem", "position": 3, "name": H.unescape(h1), "item": "https://waltermontenarie.com/artikelen/" + slug}]}
    s = s.replace('<link rel="icon"', '<script type="application/ld+json">%s</script>\n<link rel="icon"' % json.dumps(ld, ensure_ascii=False), 1)
    open(pad, 'w', encoding='utf-8').write(s)
    kaarten_bijwerken({slug: minuten})
    return minuten

if __name__ == '__main__':
    tijden = {}
    for pad in sorted(glob.glob(W + 'artikelen/*.html')):
        tijden[os.path.basename(pad)[:-5]] = verrijk(pad)
        print(tijden[os.path.basename(pad)[:-5]], 'min', os.path.basename(pad))
    kaarten_bijwerken(tijden)
