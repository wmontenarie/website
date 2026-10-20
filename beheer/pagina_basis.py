# Gedeelde bouwfunctie voor gewone pagina's in de hoofdmap (themapagina's, trainingspagina, voorbeeld nieuwsbrief).
# De kop met het menu en de voet komen uit whitepapers.html.
import re, json, os
W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')

def maak_pagina(SLUG, TITEL, BESCHR, OG_TITEL, MAIN, LD=(), ROBOTS=None, MENU=None):
    assert len(TITEL) <= 60 and len(BESCHR) <= 155, (len(TITEL), len(BESCHR))
    basis = open(W + 'whitepapers.html', encoding='utf-8').read()
    kop = basis[:basis.index('<main>')]
    voet = basis[basis.index('</main>') + len('</main>\n'):]
    URL = 'https://waltermontenarie.com/' + SLUG
    kop = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITEL, kop)
    kop = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % BESCHR, kop)
    kop = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % OG_TITEL, kop)
    kop = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % BESCHR, kop)
    kop = kop.replace('https://waltermontenarie.com/whitepapers"', URL + '"')
    kop = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', kop, flags=re.S)
    extra = ''.join('<script type="application/ld+json">%s</script>\n' % json.dumps(d, ensure_ascii=False) for d in LD)
    if ROBOTS:
        extra += '<meta name="robots" content="%s">\n' % ROBOTS
    kop = kop.replace('<link rel="icon"', extra + '<link rel="icon"', 1)
    kop = kop.replace(' aria-current="page"', '')
    if MENU:
        kop = kop.replace('<a href="%s">' % MENU, '<a href="%s" aria-current="page">' % MENU, 1)
    assert 'whitepapers"' not in kop.split('</head>')[0].replace('href="whitepapers"', ''), 'oud adres in kop'
    for teken in ('—', '–'):
        assert teken not in MAIN, 'streepje in tekst'
    open(W + SLUG + '.html', 'w', encoding='utf-8').write(kop + MAIN + voet)
    print('geschreven', SLUG + '.html')
