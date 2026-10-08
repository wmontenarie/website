# Bouwt vitaliteitsmeter.html uit inhoud.py, met de kop en voet van tools.html.
import sys, re, json, html, math, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from meter_inhoud import *
W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')
E = html.escape
TITEL = 'Vitaliteitsmeter: gratis vitaliteitsscan voor organisaties'
BESCHR = 'Hoe vitaal is je organisatie? Beantwoord %d stellingen en zie direct je score op zes thema\'s. Gratis vitaliteitsmeter voor directie, HR en leidinggevenden.' % AANTAL
assert len(TITEL) <= 60 and len(BESCHR) <= 155, (len(TITEL), len(BESCHR))

ICO = {
 'inzicht': '<path d="M4 20V10M10 20V4M16 20v-7M21 20H3"/>',
 'werkdruk': '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 2h6"/>',
 'energie': '<path d="M13 2L5 14h6l-1 8 8-12h-6z"/>',
 'leiderschap': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 'beleid': '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h6M9 18h3"/>',
 'gedrag': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
}
def ico(n): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % ICO[n]

def boog(f0, f1, r=80, cx=100, cy=100):
    p = lambda f: (cx + r * math.cos(math.pi * (1 - f)), cy - r * math.sin(math.pi * (1 - f)))
    (x0, y0), (x1, y1) = p(f0), p(f1)
    return 'M%.1f %.1fA%d %d 0 0 1 %.1f %.1f' % (x0, y0, r, r, x1, y1)
def meter(extra=''):
    return ('<svg class="vm-meter"%s viewBox="0 0 200 118" aria-hidden="true" focusable="false">'
            '<path d="%s" stroke="#e8742c"/><path d="%s" stroke="#f0a830"/><path d="%s" stroke="#3aa5b2"/>'
            '<g class="vm-naald"><path d="M100 100L100 34" stroke="#23406e" stroke-width="5" stroke-linecap="round"/></g><circle cx="100" cy="100" r="9" fill="#23406e"/></svg>') % (extra, boog(0, .392), boog(.408, .692), boog(.708, 1))

VRAGEN = [
 ('Is de vitaliteitsmeter gratis?', 'Ja. Invullen en je scores bekijken is gratis. Voor het rapport met eerste stappen per thema vraag ik je naam, organisatie en e-mailadres.'),
 ('Voor wie is de vitaliteitsmeter?', 'Voor directeuren, HR-managers en leidinggevenden. Je beantwoordt de stellingen over je eigen organisatie of afdeling.'),
 ('Is dit een gevalideerd meetinstrument?', 'Nee. De meter is gebaseerd op wetenschappelijke modellen en geeft een indicatie. De grenzen tussen de drie niveaus heb ik zelf gekozen. Er is geen vergelijking met andere organisaties.'),
 ('Wat gebeurt er met mijn antwoorden?', 'Je antwoorden blijven in je browser. Vraag je het rapport aan dan ontvang ik je naam, organisatie, e-mailadres en de scores per thema.'),
 ('Hoe lang duurt het invullen?', 'Ongeveer vijf minuten. Het zijn %d stellingen verdeeld over zes thema\'s.' % AANTAL),
]

nr = 0; themas = ''
for i, t in enumerate(THEMAS):
    st = ''
    for j, s in enumerate(t['stellingen']):
        nr += 1
        # Een vervolgstelling is verborgen tot de stelling ervoor met meer dan 'Helemaal niet' is beantwoord
        extra = ' data-vervolg="s%d" hidden' % (nr - 1) if j in t.get('vervolg', []) else ''
        keuzes = ''.join('<label><input type="radio" name="s%d" value="%d"><span class="n">%d</span><span class="t">%s</span></label>' % (nr, k + 1, k + 1, SCHAAL[k]) for k in range(5))
        st += ('          <div class="vm-stelling"%s role="radiogroup" aria-labelledby="vm-s%d">\n            <p id="vm-s%d"><span class="vm-nr">%d</span>%s</p>\n'
               '            <div class="vm-keuzes">%s</div>\n            <p class="vm-uiteinden" aria-hidden="true"><span>Helemaal niet</span><span>Helemaal</span></p>\n          </div>\n') % (extra, nr, nr, nr, E(s), keuzes)
    themas += ('        <fieldset class="vm-thema vm-t%d" data-thema="%s"%s>\n          <legend><span class="vm-rond">%s</span><span><span class="vm-thema-nr">Thema %d van 6</span><span class="vm-thema-naam">%s</span><span class="vm-thema-vraag">%s</span></span></legend>\n'
               '          <p class="vm-uitleg">Kies bij elke stelling in hoeverre die klopt voor jouw organisatie of afdeling.</p>\n%s        </fieldset>\n') % (i + 1, t['id'], '' if i == 0 else ' hidden', ico(t['id']), i + 1, E(t['naam']), E(t['vraag']), st)
assert nr == AANTAL == 26

DATA = dict(themas=[dict(id=t['id'], naam=t['naam'], laag=t['laag'], midden=t['midden'], hoog=t['hoog'], stappen=t['stappen'], links=t['links'], ico=ICO[t['id']]) for t in THEMAS],
            totaal=TOTAAL, niveaus=dict(laag='Hier ligt werk', midden='In ontwikkeling', hoog='Staat stevig'))

MAIN = '''<main>
  <section class="sectie vm-kop">
    <div class="wrap">
      <div>
        <h1>Vitaliteitsmeter voor organisaties</h1>
        <p class="intro">Hoe vitaal is jouw organisatie? Beantwoord %(aantal)d stellingen en zie direct waar je staat en welk thema aandacht vraagt.</p>
        <ul class="vm-feiten">
          <li><strong>%(aantal)d</strong> stellingen</li>
          <li><strong>5</strong> minuten</li>
          <li><strong>6</strong> thema's</li>
        </ul>
        <div class="hero-knoppen"><a class="knop" href="#meter">Begin met de meter</a></div>
      </div>
      %(meter_kop)s
    </div>
  </section>

  <section class="sectie wit" id="meter">
    <div class="wrap">
      <noscript><p class="vm-melding">Voor de vitaliteitsmeter moet JavaScript aan staan in je browser.</p></noscript>
      <form class="vm" id="vm-form" novalidate>
        <div class="vm-voortgang" aria-hidden="true">%(bolletjes)s</div>
%(themas)s        <p class="vm-fout" role="alert" hidden>Beantwoord eerst alle stellingen van dit thema.</p>
        <div class="vm-knoppen">
          <button type="button" class="knop omlijnd" id="vm-vorige" hidden>Vorige</button>
          <button type="button" class="knop" id="vm-volgende">Volgende thema</button>
        </div>
      </form>

      <div class="vm-uitslag" id="vm-uitslag" hidden tabindex="-1">
        <h2>Je uitslag</h2>
        <div class="vm-totaal">
          %(meter_uitslag)s
          <div>
            <p class="vm-totaal-score"><span id="vm-totaal">0</span><span class="vm-van"> van 100</span></p>
            <p class="vm-niveau" id="vm-totaal-niveau"></p>
            <p id="vm-totaal-tekst"></p>
          </div>
        </div>
        <h3>Je score per thema</h3>
        <ul class="vm-balken" id="vm-balken"></ul>
        <p class="vm-aandacht" id="vm-aandacht"></p>

        <div class="vm-poort" id="vm-poort">
          <div>
            <h3>Wat zijn je eerste stappen?</h3>
            <p>Laat je gegevens achter. Je ziet dan direct per thema drie eerste stappen. Met artikelen, whitepapers en trainingen die erbij passen.</p>
          </div>
          <form class="contactformulier" id="vm-gegevens" action="/verstuur" method="POST">
            <input type="hidden" name="soort" value="meter">
            <input type="text" name="_honey" class="verborgen" tabindex="-1" autocomplete="off" aria-hidden="true">
            <div class="veld-rij">
              <div class="veld"><label for="vm-naam">Naam</label><input id="vm-naam" type="text" name="naam" autocomplete="name" required></div>
              <div class="veld"><label for="vm-organisatie">Organisatie</label><input id="vm-organisatie" type="text" name="organisatie" autocomplete="organization" required></div>
            </div>
            <div class="veld-rij">
              <div class="veld"><label for="vm-email">E-mailadres</label><input id="vm-email" type="email" name="email" autocomplete="email" required></div>
              <div class="veld"><label for="vm-functie">Functie <span class="optioneel">(optioneel)</span></label><input id="vm-functie" type="text" name="functie" autocomplete="organization-title"></div>
            </div>
            <label class="vinkje"><input type="checkbox" name="nieuwsbrief" value="Ja"> Ik ontvang ook graag nieuwe artikelen per e-mail</label>
            <button class="knop" type="submit">Bekijk je eerste stappen</button>
            <p class="klein">Je antwoorden blijven in je browser. Ik ontvang je naam, organisatie, e-mailadres en de scores per thema. Ik kan je een keer benaderen over de uitslag. Lees meer in de <a href="privacy">privacyverklaring</a>.</p>
          </form>
        </div>

        <div class="vm-rapport" id="vm-rapport" hidden tabindex="-1">
          <h2>Je eerste stappen per thema</h2>
          <p>De thema's staan op volgorde. Bovenaan het thema dat nu de meeste aandacht vraagt.</p>
          <div id="vm-kaarten"></div>
          <div class="nieuwsbrief-band">
            <div>
              <h2>De uitslag bespreken?</h2>
              <p>In een gratis gesprek van 30 minuten kijken we naar je scores en naar waar je begint.</p>
              <p class="vm-alleen-print">Walter Montenarie | waltermontenarie.com | 06 5168 6865 | walter@waltermontenarie.com</p>
            </div>
            <div class="hero-knoppen">
              <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
              <button type="button" class="knop omlijnd" id="vm-print">Print of bewaar als pdf</button>
            </div>
          </div>
        </div>
        <p class="vm-opnieuw"><button type="button" class="vm-link" id="vm-opnieuw">Opnieuw invullen</button></p>
      </div>
    </div>
  </section>

  <section class="sectie vm-over">
    <div class="wrap">
      <h2>Waar is de meter op gebaseerd?</h2>
      <p>De stellingen komen voort uit vier modellen waar ik mee werk.</p>
      <div class="bouwblokken vier">
        <div><strong>Het JD-R-model</strong><span>Werkdruk en andere stressbronnen kosten energie. Energiebronnen vullen de batterij. <a href="tools#jdr-model">Bekijk het model</a></span></div>
        <div><strong>Het ABC van bevlogenheid</strong><span>Autonomie, binding en competentie. <a href="artikelen/bevlogenheid-is-geen-luxe">Lees het artikel</a></span></div>
        <div><strong>Zes bouwblokken</strong><span>Wat vitaliteitsbeleid laat werken volgens onderzoek in Harvard Business Review. <a href="artikelen/zes-bouwblokken-vitaliteitsbeleid">Lees het artikel</a></span></div>
        <div><strong>Het model van Kotter</strong><span>Acht stappen om een verandering te laten slagen. <a href="tools#kotter">Bekijk het model</a></span></div>
      </div>
      <p class="noot">De vitaliteitsmeter geeft een indicatie. Het is geen gevalideerd meetinstrument. De grenzen tussen de drie niveaus heb ik zelf gekozen: tot 40 ligt er werk, van 40 tot 70 is het in ontwikkeling en vanaf 70 staat het stevig. Er is geen vergelijking met andere organisaties.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over de vitaliteitsmeter</h2>
%(vragen)s
      </section>
    </div>
  </section>
</main>
'''

SCRIPT = '''<script>
(function () {
  var DATA = %(data)s;
  var form = document.getElementById('vm-form');
  if (!form) return;
  var themas = Array.prototype.slice.call(form.querySelectorAll('.vm-thema'));
  var bollen = form.querySelectorAll('.vm-voortgang span');
  var vorige = document.getElementById('vm-vorige'), volgende = document.getElementById('vm-volgende');
  var fout = form.querySelector('.vm-fout'), uitslag = document.getElementById('vm-uitslag');
  var stap = 0, scores = null;
  function maak(tag, klasse, tekst) { var e = document.createElement(tag); if (klasse) e.className = klasse; if (tekst != null) e.textContent = tekst; return e; }
  function niveau(s) { return s < 40 ? 'laag' : s < 70 ? 'midden' : 'hoog'; }
  function naar(el) { if (el.scrollIntoView) el.scrollIntoView({ block: 'start' }); if (el.focus) el.focus({ preventScroll: true }); }

  // Gekozen antwoord markeren (ook voor browsers zonder :has)
  form.addEventListener('change', function (e) {
    if (!e.target.matches('input[type="radio"]')) return;
    var groep = e.target.closest('.vm-keuzes');
    groep.querySelectorAll('label').forEach(function (l) { l.classList.toggle('gekozen', l.querySelector('input').checked); });
    e.target.closest('.vm-stelling').classList.remove('open');
    fout.hidden = true;
    vervolg();
  });

  // Vervolgstellingen: alleen in beeld als de stelling ervoor met meer dan 'Helemaal niet' is beantwoord.
  // Een verborgen stelling telt niet mee in de score. De nummers lopen daarna weer door.
  function vervolg() {
    form.querySelectorAll('.vm-stelling[data-vervolg]').forEach(function (s) {
      var bron = form.querySelector('input[name="' + s.getAttribute('data-vervolg') + '"]:checked');
      var weg = !bron || +bron.value < 2;
      if (weg && !s.hidden) {
        s.querySelectorAll('input').forEach(function (i) { i.checked = false; });
        s.querySelectorAll('.gekozen').forEach(function (l) { l.classList.remove('gekozen'); });
        s.classList.remove('open');
      }
      s.hidden = weg;
    });
    var n = 0;
    form.querySelectorAll('.vm-stelling').forEach(function (s) { if (!s.hidden) s.querySelector('.vm-nr').textContent = ++n; });
  }

  function toon() {
    themas.forEach(function (t, i) { t.hidden = i !== stap; });
    bollen.forEach(function (b, i) { b.className = i < stap ? 'klaar' : i === stap ? 'nu' : ''; });
    vorige.hidden = stap === 0;
    volgende.textContent = stap === themas.length - 1 ? 'Bekijk je uitslag' : 'Volgende thema';
    fout.hidden = true;
  }
  function compleet(t) {
    var ok = true, eerste = null;
    t.querySelectorAll('.vm-stelling').forEach(function (s) {
      if (s.hidden) return;
      var gekozen = !!s.querySelector('input:checked');
      s.classList.toggle('open', !gekozen);
      if (!gekozen) { ok = false; if (!eerste) eerste = s; }
    });
    if (eerste) { fout.hidden = false; eerste.scrollIntoView({ block: 'center' }); }
    return ok;
  }
  volgende.addEventListener('click', function () {
    if (!compleet(themas[stap])) return;
    if (stap < themas.length - 1) { stap++; toon(); naar(form); return; }
    reken();
  });
  vorige.addEventListener('click', function () { if (stap > 0) { stap--; toon(); naar(form); } });

  function reken() {
    scores = themas.map(function (t) {
      var som = 0, n = 0;
      t.querySelectorAll('input:checked').forEach(function (i) { som += +i.value; n++; });
      return Math.round((som / n - 1) / 4 * 100);
    });
    var totaal = Math.round(scores.reduce(function (a, b) { return a + b; }, 0) / scores.length);
    var tn = niveau(totaal);
    document.getElementById('vm-totaal').textContent = totaal;
    var chip = document.getElementById('vm-totaal-niveau'); chip.textContent = DATA.niveaus[tn]; chip.className = 'vm-niveau ' + tn;
    document.getElementById('vm-totaal-tekst').textContent = DATA.totaal[tn];
    uitslag.querySelector('.vm-naald').style.transform = 'rotate(' + (totaal * 1.8 - 90) + 'deg)';

    var lijst = document.getElementById('vm-balken'); lijst.textContent = '';
    var laagste = 0;
    DATA.themas.forEach(function (t, i) {
      if (scores[i] < scores[laagste]) laagste = i;
      var n = niveau(scores[i]);
      var li = maak('li', 'vm-t' + (i + 1));
      var kop = maak('div', 'vm-balk-kop');
      kop.appendChild(maak('strong', null, t.naam));
      kop.appendChild(maak('span', 'vm-niveau ' + n, DATA.niveaus[n]));
      kop.appendChild(maak('span', 'vm-score', scores[i]));
      li.appendChild(kop);
      var spoor = maak('div', 'vm-spoor'); var balk = maak('i'); balk.style.width = Math.max(scores[i], 2) + '%%'; spoor.appendChild(balk); li.appendChild(spoor);
      li.appendChild(maak('p', null, t[n]));
      lijst.appendChild(li);
    });
    document.getElementById('vm-aandacht').textContent = 'Het thema dat nu de meeste aandacht vraagt: ' + DATA.themas[laagste].naam + '.';
    form.hidden = true; uitslag.hidden = false; naar(uitslag);
    if (window.console) console.log('Vitaliteitsmeter: uitslag getoond');
  }

  function rapport() {
    var vak = document.getElementById('vm-kaarten'); vak.textContent = '';
    var volgorde = DATA.themas.map(function (t, i) { return i; }).sort(function (a, b) { return scores[a] - scores[b] || a - b; });
    volgorde.forEach(function (i) {
      var t = DATA.themas[i], n = niveau(scores[i]);
      var kaart = maak('section', 'vm-kaart vm-t' + (i + 1));
      var kop = maak('div', 'vm-balk-kop');
      kop.appendChild(maak('h3', null, t.naam));
      kop.appendChild(maak('span', 'vm-niveau ' + n, DATA.niveaus[n]));
      kop.appendChild(maak('span', 'vm-score', scores[i]));
      kaart.appendChild(kop);
      kaart.appendChild(maak('p', null, t[n]));
      kaart.appendChild(maak('p', 'vm-kopje', n === 'hoog' ? 'Zo houd je het vast' : 'Eerste stappen'));
      var ol = maak('ol'); t.stappen.forEach(function (s) { ol.appendChild(maak('li', null, s)); }); kaart.appendChild(ol);
      kaart.appendChild(maak('p', 'vm-kopje', 'Verder lezen'));
      var links = maak('p', 'dienst-links');
      t.links.forEach(function (l) { var a = maak('a', null, l[0]); a.href = l[1]; links.appendChild(a); });
      kaart.appendChild(links);
      vak.appendChild(kaart);
    });
    document.getElementById('vm-poort').hidden = true;
    var r = document.getElementById('vm-rapport'); r.hidden = false; naar(r);
  }

  var gegevens = document.getElementById('vm-gegevens'), bezig = false;
  gegevens.addEventListener('submit', function (e) {
    e.preventDefault();
    if (bezig || !scores) return;
    if (!gegevens.reportValidity()) return;
    bezig = true;
    var knop = gegevens.querySelector('button[type="submit"]'); knop.disabled = true; knop.textContent = 'Bezig';
    var klaar = function () { bezig = false; knop.disabled = false; knop.textContent = 'Bekijk je eerste stappen'; rapport(); };
    if (!window.fetch || !window.URLSearchParams || !window.FormData) { klaar(); return; }
    var p = new URLSearchParams(new FormData(gegevens));
    p.set('totaal', document.getElementById('vm-totaal').textContent);
    DATA.themas.forEach(function (t, i) { p.set('score_' + t.id, scores[i]); });
    var stop = window.AbortController ? new AbortController() : null;
    var klok = setTimeout(function () { if (stop) stop.abort(); }, 10000);
    // Het rapport komt altijd in beeld, ook als het versturen niet lukt
    fetch(gegevens.getAttribute('action'), { method: 'POST', headers: { 'Accept': 'application/json' }, body: p, signal: stop ? stop.signal : undefined })
      .then(function (r) { return r.json(); })
      .then(function (d) { if (window.console && d && !d.ok) console.log('Vitaliteitsmeter: ' + (d.fout || 'niet verstuurd')); })
      .catch(function () {})
      .then(function () { clearTimeout(klok); klaar(); });
  });

  document.getElementById('vm-print').addEventListener('click', function () { window.print(); });
  document.getElementById('vm-opnieuw').addEventListener('click', function () {
    form.reset(); form.querySelectorAll('.gekozen').forEach(function (l) { l.classList.remove('gekozen'); });
    scores = null; stap = 0; vervolg(); toon();
    document.getElementById('vm-rapport').hidden = true; document.getElementById('vm-poort').hidden = false;
    uitslag.hidden = true; form.hidden = false; naar(form);
  });
  vervolg(); toon();
})();
</script>
<script src="js/menu.js" defer></script>
</body>
</html>
'''

basis = open(W + 'tools.html', encoding='utf-8').read()
kop = basis[:basis.index('<main>')]
voet = basis[basis.index('</main>') + len('</main>'):basis.index('<script>')]
kop = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITEL, kop)
kop = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % E(BESCHR), kop)
kop = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="Vitaliteitsmeter voor organisaties">', kop)
kop = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % E(BESCHR), kop)
kop = kop.replace('https://waltermontenarie.com/tools"', 'https://waltermontenarie.com/vitaliteitsmeter"')
assert kop.count('waltermontenarie.com/vitaliteitsmeter') == 2
faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": v, "acceptedAnswer": {"@type": "Answer", "text": a}} for v, a in VRAGEN]}
kop = kop.replace('<link rel="icon"', '<script type="application/ld+json">%s</script>\n<link rel="icon"' % json.dumps(faq, ensure_ascii=False), 1)
assert '<a href="vitaliteitsmeter">Vitaliteitsmeter</a>' in kop
kop = kop.replace('<a href="vitaliteitsmeter">Vitaliteitsmeter</a>', '<a href="vitaliteitsmeter" aria-current="page">Vitaliteitsmeter</a>')

main = MAIN % dict(aantal=AANTAL, meter_kop=meter(' data-stand="62"'), meter_uitslag=meter(), themas=themas,
                   bolletjes=''.join('<span></span>' for _ in THEMAS),
                   vragen='\n'.join('        <h3>%s</h3>\n        <p>%s</p>' % (E(v), E(a)) for v, a in VRAGEN))
script = SCRIPT % dict(data=json.dumps(DATA, ensure_ascii=False).replace('</', '<\\/'))
uit = W + 'vitaliteitsmeter.html'
open(uit, 'w', encoding='utf-8').write(kop + main + voet + script)
for teken in ('—', '–'):
    assert teken not in main and teken not in script
print('geschreven', uit, len(kop + main + voet + script))
