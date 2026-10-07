# Gedeelde bouwfunctie voor nieuwe artikelen, met een bestaand artikel als sjabloon.
import re, json, html, sys, urllib.parse
import os
W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')
def ico_svg(pad): return '<span class="ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg></span>' % pad
def maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-07', uit=None):
    URL = 'https://waltermontenarie.com/artikelen/' + SLUG
    assert len(TITEL) <= 60 and len(BESCHR) <= 155 and len(H1) <= 70, (len(TITEL), len(BESCHR), len(H1))
    basis = open(W + 'artikelen/vitaliteitsbeleid-opzetten-stappenplan.html', encoding='utf-8').read()
    OUD_SLUG = 'vitaliteitsbeleid-opzetten-stappenplan'
    kop = basis[:basis.index('<main>')]
    voet = basis[basis.index('</main>') + len('</main>\n'):]
    # deelknoppen en nieuwsbriefblok overnemen
    deel = re.search(r'      <aside class="deel".*?</aside>\n', basis, re.S).group(0)
    nb = re.search(r'      <aside class="nb-blok".*?</aside>\n', basis, re.S).group(0)
    oud_titel = 'Vitaliteitsbeleid opzetten: een stappenplan'
    q = lambda s: urllib.parse.quote(s, safe='')
    deel = deel.replace(q(oud_titel), q(H1)).replace(OUD_SLUG, SLUG)
    assert q(oud_titel) not in deel and OUD_SLUG not in deel and deel.count(SLUG) == 6, deel.count(SLUG)

    art = {"@context": "https://schema.org", "@type": "Article", "headline": H1, "description": BESCHR, "inLanguage": "nl", "datePublished": DATUM, "dateModified": DATUM,
           "author": {"@type": "Person", "name": "Walter Montenarie", "jobTitle": "Adviseur duurzame inzetbaarheid", "sameAs": ["https://www.linkedin.com/in/montenarie/"]},
           "publisher": {"@type": "Organization", "name": "Walter Montenarie"}, "mainEntityOfPage": URL, "image": "https://waltermontenarie.com/img/deelafbeelding-2.jpg"}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": v, "acceptedAnswer": {"@type": "Answer", "text": a}} for v, a in VRAGEN]}
    kop = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITEL, kop)
    kop = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % BESCHR, kop)
    kop = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % H1, kop)
    kop = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % BESCHR, kop)
    kop = kop.replace(OUD_SLUG, SLUG)
    ld = re.findall(r'<script type="application/ld\+json">.*?</script>\n', kop, re.S)
    assert len(ld) == 2
    kop = kop.replace(ld[0], '<script type="application/ld+json">%s</script>\n' % json.dumps(art, ensure_ascii=False))
    kop = kop.replace(ld[1], '<script type="application/ld+json">%s</script>\n' % json.dumps(faq, ensure_ascii=False))
    assert OUD_SLUG not in kop and 'Vitaliteitsbeleid opzetten' not in kop

    vragen = '\n'.join('        <h3>%s</h3>\n        <p>%s</p>' % (v, a) for v, a in VRAGEN)
    main = MAIN % dict(h1=H1, vragen=vragen, deel=deel, nb=nb, **{'i_' + k: ico_svg(v) for k, v in ICO.items()})
    uit = uit or W + 'artikelen/' + SLUG + '.html'
    open(uit, 'w', encoding='utf-8').write(kop + main + voet)
    tekst = re.sub(r'<[^>]+>', ' ', re.sub(r'<(aside|section class="bronnen")[\s\S]*?</(aside|section)>', '', main))
    print('geschreven', uit, '| woorden', len(tekst.split()))
    for teken in ('—', '–'):
        assert teken not in main, 'streepje in tekst'
