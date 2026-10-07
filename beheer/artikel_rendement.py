# Bouwt het artikel over het HBR-onderzoek naar het rendement van vitaliteitsprogramma's.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'rendement-vitaliteitsprogramma-hbr-onderzoek'
TITEL = 'Rendement vitaliteitsprogramma: het onderzoek van HBR'
H1 = 'Rendement van een vitaliteitsprogramma: lessen van tien organisaties'
BESCHR = 'Wat levert een vitaliteitsprogramma op? Harvard Business Review onderzocht tien organisaties. De cijfers, zes bouwblokken en vier kanttekeningen.'

VRAGEN = [
 ('Wat is het rendement van een vitaliteitsprogramma?', 'Dat verschilt per organisatie. In het artikel in Harvard Business Review verdiende Johnson & Johnson van 2002 tot 2008 elke dollar 2,71 keer terug. Een experiment uit 2019 vond na anderhalf jaar geen effect op verzuim en zorgkosten. Het rendement hangt af van de aanpak.'),
 ('Wat zijn de zes bouwblokken uit Harvard Business Review?', 'Leiderschap op alle niveaus, aansluiting op identiteit en cultuur, scope, relevantie en kwaliteit, toegankelijkheid, goede partners en communicatie.'),
 ('Geldt het onderzoek ook voor Nederland?', 'Voor een deel. Veel besparingen in het artikel gaan over zorgkosten die Amerikaanse werkgevers betalen. In Nederland zit de winst voor een werkgever vooral in minder verzuim, hogere productiviteit en behoud van mensen. De zes bouwblokken zijn wel bruikbaar.'),
 ('Wie deden het onderzoek?', 'Leonard Berry, Ann Mirabito en William Baun. Hun artikel What\'s the Hard Return on Employee Wellness Programs? verscheen in december 2010 in Harvard Business Review.'),
]
ICO = {
 'gebouw': '<path d="M3 21h18M5 21V8l6-3v16M11 21V11l8 3v7M8 10v.01M8 14v.01M15 17v.01"/>',
 'mensen': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 5.2a3 3 0 0 1 0 5.6M18 14.3c1.8.9 3 2.700 3 5.7"/>'.replace('.700', '.7'),
 'blok': '<rect x="4" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="1.5"/>',
 'kalender': '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
 'euro': '<path d="M17 6.5A6.5 6.5 0 1 0 17 17.5M4 10h9M4 14h8"/>',
 'werk': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
 'hart': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
 'deur': '<path d="M14 4h4a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-4M10 16l4-4-4-4M14 12H4"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">7 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Levert investeren in de gezondheid van medewerkers geld op? In 2010 zochten drie onderzoekers dat uit voor Harvard Business Review. Hun artikel wordt nog steeds veel aangehaald. Dit is wat ze vonden en wat je er vandaag mee kunt.</p>

      <figure class="infographic">
        <figcaption><strong>Wat het opleverde</strong> Drie soorten opbrengst bij de onderzochte organisaties</figcaption>
        <div class="rendement">
          <div class="vm-t1">
            <span class="rend-kop"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 6.5A6.5 6.5 0 1 0 17 17.5M4 10h9M4 14h8"/></svg><span>Lagere zorgkosten</span></span>
            <span class="rend-getal">$ 2,71</span>
            <span class="rend-tekst"><span>terug per dollar bij Johnson &amp; Johnson, van 2002 tot 2008</span><span class="rend-extra"><b>$ 6</b> per dollar in een studie onder 185 medewerkers en partners</span></span>
          </div>
          <div class="vm-t3">
            <span class="rend-kop"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4M9 15l2 2 4-4"/></svg><span>Minder verzuim</span></span>
            <span class="rend-getal">80%%</span>
            <span class="rend-tekst"><span>minder verloren werkdagen bij MD Anderson Cancer Center, binnen zes jaar</span><span class="rend-extra"><b>64%%</b> minder dagen met aangepast werk</span></span>
          </div>
          <div class="vm-t6">
            <span class="rend-kop"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 5.2a3 3 0 0 1 0 5.6M18 14.3c1.8.9 3 2.7 3 5.7"/></svg><span>Mensen blijven</span></span>
            <span class="rend-getal">9%%<small>tegen 15%%</small></span>
            <span class="rend-tekst"><span>vrijwillig vertrek bij een effectief en bij een weinig effectief programma</span><span class="rend-extra"><b>19%% naar 9%%</b> verloop bij Biltmore, van 2005 tot 2009</span></span>
          </div>
        </div>
        <p class="bron-regel">Bron: Berry, Mirabito en Baun, Harvard Business Review (2010). Een deel van de cijfers komt van de organisaties zelf.</p>
      </figure>

      <h2>Het onderzoek in het kort</h2>
      <p>Het artikel heet What's the Hard Return on Employee Wellness Programs? De schrijvers zijn Leonard Berry, Ann Mirabito en William Baun. Het verscheen in december 2010.</p>
      <p>Zij bekeken bestaand onderzoek en bezochten tien Amerikaanse organisaties waar het vitaliteitsprogramma aantoonbaar resultaat had. Daaronder waren Johnson &amp; Johnson, Chevron, softwarebedrijf SAS en het ziekenhuis MD Anderson Cancer Center. Ze spraken ongeveer 300 mensen: directeuren, financieel directeuren, leidinggevenden en medewerkers die wel en niet meededen.</p>
      <figure class="infographic">
        <figcaption><strong>Het onderzoek in vier cijfers</strong></figcaption>
        <div class="kerncijfers compact">
          <div>%(i_gebouw)s<span class="getal">10</span><span>organisaties bezocht</span></div>
          <div>%(i_mensen)s<span class="getal">300</span><span>mensen gesproken, ongeveer</span></div>
          <div>%(i_blok)s<span class="getal">6</span><span>bouwblokken die bij alle tien terugkwamen</span></div>
          <div>%(i_kalender)s<span class="getal">2010</span><span>verschenen in Harvard Business Review</span></div>
        </div>
        <p class="bron-regel">Bron: Berry, Mirabito en Baun, Harvard Business Review (2010)</p>
      </figure>

      <h2>Wat leverde het op?</h2>
      <p>De onderzoekers beschrijven drie soorten opbrengst.</p>

      <h3>Lagere zorgkosten</h3>
      <p>De leiding van Johnson &amp; Johnson schatte dat het programma in tien jaar ongeveer 250 miljoen dollar aan zorgkosten had bespaard. Van 2002 tot 2008 leverde elke dollar 2,71 dollar op. Sinds 1995 was het aandeel rokers onder medewerkers met meer dan twee derde gedaald. Het aandeel met hoge bloeddruk of te weinig beweging was meer dan gehalveerd.</p>
      <p>Het artikel haalt ook een studie aan onder 185 medewerkers en partners van één werkgever. Zij volgden zes maanden een programma met hartrevalidatie en beweegtraining. Hartpatiënt waren zij niet. Van de deelnemers met een hoog gezondheidsrisico ging 57 procent naar een laag risico. De zorgkosten daalden met 1.421 dollar per deelnemer. In de controlegroep gebeurde dat niet. Elke dollar leverde zes dollar op.</p>

      <h3>Minder verzuim</h3>
      <p>MD Anderson Cancer Center richtte in 2001 een eigen team in voor medewerkers met letsel of klachten door het werk. Binnen zes jaar daalde het aantal verloren werkdagen met 80 procent. Het aantal dagen met aangepast werk daalde met 64 procent. De besparing was 1,5 miljoen dollar. De premie voor de verzekering tegen arbeidsongevallen halveerde.</p>
      <p>De onderzoekers wijzen ook op presenteïsme: medewerkers die er wel zijn maar door ziekte of stress minder kunnen. In een studie onder 50.000 werknemers bij tien werkgevers waren de kosten van verloren productiviteit 2,3 keer zo hoog als de kosten van zorg en medicijnen. Lees meer in <a href="presenteisme-onbekende-productiviteitskiller">het artikel over presenteïsme</a>.</p>

      <h3>Mensen blijven</h3>
      <p>Het artikel haalt onderzoek aan van Towers Watson en de National Business Group on Health. Organisaties met een effectief programma hadden minder vrijwillig vertrek: 9 procent tegen 15 procent bij organisaties met een weinig effectief programma. Bij Biltmore daalde het verloop van 19 procent in 2005 naar 9 procent in 2009. De onderzoekers noemen ook trots, vertrouwen en betrokkenheid. Die opbrengst ontbreekt vaak in de berekeningen.</p>

      <h2>De zes bouwblokken</h2>
      <p>De tien organisaties verschilden in grootte en sector. Toch kwamen zes dingen steeds terug.</p>
      <figure class="infographic">
        <figcaption><strong>De zes bouwblokken</strong> Wat de tien organisaties gemeen hadden</figcaption>
[[WIEL]]        <p class="blokken-voet">Geen van de zes werkt op zichzelf.</p>
        <p class="bron-regel">Naar Berry, Mirabito en Baun, Harvard Business Review (2010)</p>
      </figure>
      <p>Ik werk ze uit in <a href="zes-bouwblokken-vitaliteitsbeleid">Zes bouwblokken voor vitaliteitsbeleid dat werkt</a>.</p>

      <h2>Vier kanttekeningen</h2>
      <ul>
        <li><strong>De onderzoekers kozen organisaties waar het werkte.</strong> Het artikel zegt niets over organisaties waar het programma niets opleverde.</li>
        <li><strong>Veel cijfers komen van de organisaties zelf.</strong> De 250 miljoen dollar van Johnson &amp; Johnson is een schatting van de eigen leiding.</li>
        <li><strong>Het gaat om Amerikaanse werkgevers.</strong> Zij betalen vaak de zorgverzekering van hun medewerkers. Een groot deel van de besparingen gaat over zorgkosten. In Nederland zit de winst voor een werkgever vooral in minder verzuim, hogere productiviteit en behoud van mensen.</li>
        <li><strong>Later onderzoek is minder positief.</strong> In een experiment uit 2019 kregen bijna 33.000 medewerkers door loting wel of geen vitaliteitsprogramma. Na anderhalf jaar was er geen verschil in verzuim, zorgkosten en gemeten gezondheid.</li>
      </ul>
      <p>De schrijvers zijn daar zelf ook eerlijk over. Zij schrijven dat een aantoonbaar rendement niet zeker is en dat de weg ernaartoe zwaar kan zijn.</p>

      <h2>Wat kun je er vandaag mee?</h2>
      <p>Het artikel bewijst niet dat elk vitaliteitsprogramma rendeert. Het laat wel zien onder welke voorwaarden het kan. Drie dingen kun je er direct mee doen.</p>
      <ul>
        <li><strong>Maak je eigen som.</strong> Reken niet met het rendement van Johnson &amp; Johnson. Lees hoe je dat doet in <a href="businesscase-vitaliteit-maken">Businesscase vitaliteit: zo maak je hem in vijf stappen</a>.</li>
        <li><strong>Toets je aanpak aan de zes bouwblokken.</strong> Met de <a href="../vitaliteitsmeter">vitaliteitsmeter</a> zie je in vijf minuten waar je organisatie staat.</li>
        <li><strong>Kijk verder dan zorgkosten.</strong> Neem verzuim, productiviteit en behoud van mensen mee. Bereken eerst wat verzuim nu kost met de <a href="../tools#rekentool-kop">verzuimrekentool</a>.</li>
      </ul>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over het rendement van vitaliteit</h2>
%(vragen)s
      </section>
%(deel)s
      <aside class="wp-tip" aria-label="Whitepaper">
        <img src="../img/whitepaper-businesscase-omslag.webp" width="560" height="793" alt="Omslag van de whitepaper De businesscase voor vitaliteit" loading="lazy">
        <div>
          <p class="podcast-label">Gratis whitepaper</p>
          <p class="podcast-titel">De businesscase voor vitaliteit</p>
          <p>Wat kost verzuim en wanneer verdient investeren zich terug? Met vijf studies naast elkaar, een rekenvoorbeeld en een werkblad.</p>
          <a class="knop" href="../whitepaper-businesscase-vitaliteit">Download de whitepaper</a>
        </div>
      </aside>

      <aside class="lees-ook" aria-label="Lees ook">
        <h2>Lees ook</h2>
        <ul>
          <li><a href="businesscase-vitaliteit-maken">Businesscase vitaliteit: zo maak je hem in vijf stappen</a></li>
          <li><a href="zes-bouwblokken-vitaliteitsbeleid">Zes bouwblokken voor vitaliteitsbeleid dat werkt</a></li>
          <li><a href="gemiddeld-verzuim-is-niet-normaal">Gemiddeld verzuim is niet normaal</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Wat kan vitaliteit jouw organisatie opleveren?</h2>
        <p>Ik reken het graag met je door. In een gratis gesprek van 30 minuten kijken we naar je cijfers en naar waar de winst ligt.</p>
        <div class="hero-knoppen">
          <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
          <a class="knop omlijnd" href="../vitaliteitsmeter">Doe de vitaliteitsmeter</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://hbr.org/2010/12/whats-the-hard-return-on-employee-wellness-programs">Berry, Mirabito en Baun: What's the Hard Return on Employee Wellness Programs?, Harvard Business Review (2010)</a></li>
          <li><a href="https://jamanetwork.com/journals/jama/fullarticle/2730614">Song en Baicker: Effect of a workplace wellness program on employee health and economic outcomes, JAMA (2019)</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''
# Infographic: wiel met zes segmenten, de namen staan links en rechts ernaast
import math
BLOKKEN = [
 ('Leiderschap op alle niveaus', 'Directie en leidinggevenden geven het goede voorbeeld.', '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/>', '#3d6fb5', '#fff'),
 ('Identiteit en cultuur', 'Vitaliteit hoort bij de bedrijfsvoering en niet bij een project.', '<path d="M4 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16M16 9h2a2 2 0 0 1 2 2v10M3 21h18M8 7h4M8 11h4M8 15h4"/>', '#e8742c', '#fff'),
 ('Scope, relevantie en kwaliteit', 'Een aanbod dat past bij wat medewerkers nodig hebben.', '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>', '#3aa5b2', '#fff'),
 ('Toegankelijkheid', 'Meedoen is makkelijk en kost weinig of niets.', '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h7M10 12h11M18 9l3 3-3 3"/>', '#7a6bb8', '#fff'),
 ('Goede partners', 'Specialistische kennis waar dat nodig is.', '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>', '#f0a830', '#18213a'),
 ('Communicatie', 'Vaak en via verschillende kanalen.', '<path d="M3 10v4a1 1 0 0 0 1 1h3l6 4V5L7 9H4a1 1 0 0 0-1 1zM17 8a5 5 0 0 1 0 8"/>', '#4f9d69', '#fff'),
]
def wiel():
    cx = cy = 110; R = 104; r = 56; spleet = 2.2
    punt = lambda straal, graden: (cx + straal * math.sin(math.radians(graden)), cy - straal * math.cos(math.radians(graden)))
    h = '        <div class="wiel6">\n          <svg class="wiel6-beeld" viewBox="0 0 220 220" aria-hidden="true" focusable="false">'
    for i, (naam, tekst, pad, kleur, lijn) in enumerate(BLOKKEN):
        a0 = i * 60 + spleet; a1 = (i + 1) * 60 - spleet
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = punt(R, a0), punt(R, a1), punt(r, a1), punt(r, a0)
        h += '<path d="M%.1f %.1fA%d %d 0 0 1 %.1f %.1fL%.1f %.1fA%d %d 0 0 0 %.1f %.1fZ" fill="%s"/>' % (x0, y0, R, R, x1, y1, x2, y2, r, r, x3, y3, kleur)
        mx, my = punt((R + r) / 2, i * 60 + 30)
        h += '<g transform="translate(%.1f %.1f) scale(1.05)" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (mx - 12.6, my - 12.6, lijn, pad)
    h += '<circle cx="110" cy="110" r="47" fill="#23406e"/><text x="110" y="105" text-anchor="middle" font-family="Schibsted Grotesk, system-ui, sans-serif" font-size="14.5" font-weight="700" fill="#fff">Vitaliteit</text><text x="110" y="123" text-anchor="middle" font-family="Schibsted Grotesk, system-ui, sans-serif" font-size="14.5" font-weight="700" fill="#f0a830">die werkt</text>'
    h += '</svg>\n          <ol class="wiel6-lijst">\n'
    for i, (naam, tekst, pad, kleur, lijn) in enumerate(BLOKKEN):
        h += '            <li class="vm-t%d"><span class="wiel6-nr">%d</span><span class="wiel6-tekst"><strong>%s</strong><span>%s</span></span></li>\n' % (i + 1, i + 1, naam, tekst)
    return h + '          </ol>\n        </div>\n'
MAIN = MAIN.replace('[[WIEL]]', wiel())
assert '%' not in wiel()
maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, uit=sys.argv[1] if len(sys.argv) > 1 else None)
