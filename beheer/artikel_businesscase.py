# Bouwt het artikel over de businesscase voor vitaliteit op basis van een bestaand artikel als sjabloon.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'businesscase-vitaliteit-maken'
TITEL = 'Businesscase vitaliteit maken in vijf stappen'
H1 = 'Businesscase vitaliteit: zo maak je hem in vijf stappen'
BESCHR = 'Zo maak je een businesscase voor vitaliteit. Bereken wat verzuim kost, bepaal je investering en zie bij welke daling je die terugverdient.'

VRAGEN = [
 ('Wat is een businesscase voor vitaliteit?', 'Een onderbouwing in euro\'s. Hij laat zien wat verzuim nu kost, wat je investeert en bij welke daling van het verzuim die investering is terugverdiend.'),
 ('Wat levert investeren in vitaliteit op?', 'Dat hangt af van wat je doet. Een los programma naast het werk verandert weinig. Een aanpak die het werk, het leiderschap en de gezondheid van medewerkers samen aanpakt is kansrijker. Reken daarom met je eigen cijfers en niet met een rendement uit een rapport.'),
 ('Wat kost een verzuimdag?', 'In de regel 400 tot 600 euro. In het rekenvoorbeeld in dit artikel is het 386 euro bij een gemiddeld bruto jaarsalaris van 45.000 euro. Daarin zitten loonkosten, begeleiding, vervanging en de tijd van leidinggevenden en HR.'),
 ('Wanneer heb je een investering in vitaliteit terugverdiend?', 'Dat laat het omslagpunt zien. Je deelt de investering per jaar door de waarde van één procentpunt verzuim. In het rekenvoorbeeld is de investering terugverdiend als het verzuim 0,3 procentpunt daalt.'),
 ('Hoe snel zie je resultaat?', 'In het eerste jaar meet je, begin je en zie je vooral vroege signalen zoals deelname en werkplezier. Het effect op verzuim en verloop volgt later. Spreek daarom af dat je de aanpak minstens twee tot drie jaar volhoudt.'),
]
ICO = {
 'pct': '<path d="M19 5L5 19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
 'gebouw': '<path d="M3 21h18M5 21V8l6-3v16M11 21V11l8 3v7M8 10v.01M8 14v.01M15 17v.01"/>',
 'werk': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
 'euro': '<path d="M17 6.5A6.5 6.5 0 1 0 17 17.500M4 10h9M4 14h8"/>'.replace('.500', '.5'),
 'kompas': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 'mens': '<circle cx="12" cy="7" r="4"/><path d="M4 21v-1a7 7 0 0 1 16 0v1"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">7 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Vitaliteit staat bij veel organisaties op de agenda. Toch blijft het budget klein en verdwijnt het vaak bij de eerste bezuiniging. Dat komt zelden door onwil. Het komt doordat de onderbouwing ontbreekt. Met een businesscase verander je dat.</p>

      <h2>Wat is een businesscase voor vitaliteit?</h2>
      <p>Een businesscase voor vitaliteit is een onderbouwing in euro's. Hij beantwoordt drie vragen. Wat kost verzuim ons nu? Wat gaan we investeren? En bij welk resultaat hebben we die investering terugverdiend?</p>
      <p>Een goede businesscase belooft geen rendement. Hij laat zien wat er nodig is om de investering terug te verdienen. Zo praat je in de taal van de directie: kosten, opbrengsten en risico's.</p>

      <h2>Waarom je er nu een nodig hebt</h2>
      <p>Het ziekteverzuim in Nederland was in 2025 gemiddeld 5,4 procent. In het eerste kwartaal van 2026 liep het op naar 5,8 procent. Bij organisaties met 100 of meer medewerkers was het in dat kwartaal 6,8 procent.</p>
      <p>Volgens TNO hangt ongeveer de helft van het verzuim samen met het werk. Alleen al de loondoorbetaling daarvan kostte werkgevers in 2023 ruim 8,3 miljard euro. Op dat deel heb je als werkgever invloed.</p>
      <figure class="infographic">
        <figcaption><strong>Vier cijfers om mee te beginnen</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_pct)s<span class="getal">5,4%%</span><span>ziekteverzuim in Nederland in 2025</span></div>
          <div>%(i_gebouw)s<span class="getal">6,8%%</span><span>bij organisaties met 100 of meer medewerkers in het eerste kwartaal van 2026</span></div>
          <div>%(i_werk)s<span class="getal">51%%</span><span>van het verzuim hangt samen met het werk</span></div>
          <div>%(i_euro)s<span class="getal">€ 8,3 mld</span><span>loondoorbetaling bij werkgerelateerd verzuim in 2023</span></div>
        </div>
        <p class="bron-regel">Bronnen: CBS (2026), TNO Arbobalans 2024</p>
      </figure>

      <h2>De businesscase in vijf stappen</h2>
      <p>Dit zijn de vijf stappen. Daaronder werk ik ze uit met een rekenvoorbeeld.</p>
      <figure class="infographic">
        <figcaption><strong>Businesscase vitaliteit in vijf stappen</strong></figcaption>
        <ol class="stappen">
          <li><strong>Bereken wat verzuim nu kost</strong><p>Met je eigen verzuimpercentage, aantal fte en gemiddelde salaris.</p></li>
          <li><strong>Zoek uit waar het zit</strong><p>Welke afdelingen, functies en oorzaken? Daar ligt ook de winst.</p></li>
          <li><strong>Kies maatregelen en bepaal de investering</strong><p>Op drie niveaus: organisatie, leiderschap en medewerker.</p></li>
          <li><strong>Bereken het omslagpunt</strong><p>Bij welke daling van het verzuim is de investering terugverdiend?</p></li>
          <li><strong>Reken scenario's door en spreek af wat je meet</strong><p>Voorzichtig, gemiddeld en ambitieus. Met vaste momenten om te rapporteren.</p></li>
        </ol>
      </figure>

      <h3>Stap 1: bereken wat verzuim nu kost</h3>
      <p>De meeste organisaties kennen hun verzuimpercentage. Weinig organisaties weten wat dat percentage in euro's betekent. Een verzuimdag kost meer dan het loon. Er komen kosten bij voor begeleiding, vervanging en de tijd van leidinggevenden en HR.</p>
      <p>Neem een organisatie met 500 medewerkers in voltijd, 220 werkdagen per jaar en een verzuim van 5,4 procent. Bij een gemiddeld bruto jaarsalaris van 45.000 euro kost een verzuimdag 386 euro. Dat is 266 euro aan loonkosten inclusief werkgeverslasten. Daar komt 120 euro bij: 25 euro voor verzuimbegeleiding en arbodienst, 20 euro voor de tijd van leidinggevende en HR, 60 euro voor vervanging en 15 euro voor werving en selectie. De <a href="../tools#rekentool-kop">verzuimrekentool</a> rekent met dezelfde opbouw.</p>
      <figure class="infographic">
        <figcaption><strong>Rekenvoorbeeld</strong> Organisatie met 500 medewerkers bij gemiddeld verzuim</figcaption>
        <div class="rekensom">
          <div><span class="getal">500</span><span>medewerkers</span></div>
          <span class="teken" aria-hidden="true">×</span>
          <div><span class="getal">220</span><span>werkdagen</span></div>
          <span class="teken" aria-hidden="true">×</span>
          <div><span class="getal">5,4%%</span><span>verzuim</span></div>
          <span class="teken" aria-hidden="true">=</span>
          <div><span class="getal">5.940</span><span>verzuimdagen</span></div>
          <span class="teken" aria-hidden="true">×</span>
          <div><span class="getal">€ 386</span><span>per verzuimdag</span></div>
          <span class="teken" aria-hidden="true">=</span>
          <div class="uitkomst"><span class="getal">€ 2,3 mln</span><span>per jaar</span></div>
        </div>
        <p class="bron-regel">Eigen berekening. Bij deeltijd reken je met fte in plaats van medewerkers.</p>
      </figure>
      <p>Dat is ongeveer 4.600 euro per medewerker per jaar. Elk procentpunt verzuim staat in dit voorbeeld voor 1.100 verzuimdagen en ruim 420.000 euro per jaar. Dat bedrag heb je in stap 4 nodig.</p>
      <p>Reken het daar voor je eigen organisatie uit. Reken alleen met kosten die je kunt onderbouwen.</p>

      <h3>Stap 2: zoek uit waar het zit</h3>
      <p>Bijna de helft van de werknemers verzuimt een heel jaar niet. Wie wel verzuimt is gemiddeld 17 dagen afwezig. Het verzuim zit dus bij een deel van je mensen en vaak bij een kleine groep met langdurige klachten. Een gemiddeld cijfer verbergt dat. Lees daarover meer in <a href="gemiddeld-verzuim-is-niet-normaal">Gemiddeld verzuim is niet normaal</a>.</p>
      <p>Kijk naar afdelingen, functiegroepen en leeftijden. Kijk ook naar het verschil tussen kort en lang verzuim en naar de oorzaken. Gebruik de verzuimcijfers, de RI&amp;E, het PMO en het medewerkersonderzoek. Vul dat aan met gesprekken met leidinggevenden, HR, de bedrijfsarts en medewerkers.</p>

      <h3>Stap 3: kies maatregelen en bepaal de investering</h3>
      <p>Onderzoek laat twee kanten zien. In 2010 beschreven drie onderzoekers in Harvard Business Review tien organisaties waar het vitaliteitsprogramma aantoonbaar iets opleverde. Johnson &amp; Johnson verdiende van 2002 tot 2008 elke dollar 2,71 keer terug. Wat deze organisaties gemeen hadden lees je in <a href="rendement-vitaliteitsprogramma-hbr-onderzoek">Rendement van een vitaliteitsprogramma</a>.</p>
      <p>Daar staat een Amerikaans experiment uit 2019 tegenover. Bijna 33.000 medewerkers kregen door loting wel of geen vitaliteitsprogramma aangeboden. Na anderhalf jaar zeiden deelnemers gezonder te leven. In verzuim, zorgkosten en gemeten gezondheid was geen verschil te zien.</p>
      <p>Een Brits overzicht van Deloitte kwam uit op gemiddeld 4,70 pond opbrengst per pond die werkgevers in mentale gezondheid investeren. Vroege maatregelen voor de hele organisatie leverden meer op dan late hulp aan individuen.</p>
      <p>De les is dat een los programma naast het werk weinig verandert. Kies daarom maatregelen op drie niveaus die passen bij wat je in stap 2 hebt gevonden.</p>
      <figure class="infographic">
        <figcaption><strong>Een aanpak op drie niveaus</strong></figcaption>
        <div class="kenmerken">
          <div>%(i_gebouw)s<strong>Organisatie</strong><span>Werkdruk, prioriteiten, bezetting en een gezonde werkomgeving</span></div>
          <div>%(i_kompas)s<strong>Leiderschap</strong><span>Voorbeeldgedrag, signalen herkennen en het goede gesprek voeren</span></div>
          <div>%(i_mens)s<strong>Medewerker</strong><span>Leefstijl, omgaan met stress, herstel en eigen regie</span></div>
        </div>
      </figure>
      <p>Tel alle kosten mee: externe begeleiding, interne coördinatie en de tijd van medewerkers en leidinggevenden. Hoe je van maatregelen beleid maakt lees je in <a href="vitaliteitsbeleid-opzetten-stappenplan">Vitaliteitsbeleid opzetten: een stappenplan</a>.</p>

      <h3>Stap 4: bereken het omslagpunt</h3>
      <p>Het omslagpunt is de daling van het verzuim waarbij de investering is terugverdiend. Je deelt de investering per jaar door de waarde van één procentpunt verzuim.</p>
      <p>De organisatie uit het voorbeeld investeert 250 euro per medewerker per jaar. Dat is 125.000 euro. Eén procentpunt verzuim is 424.500 euro waard.</p>
      <figure class="infographic">
        <figcaption><strong>Het omslagpunt</strong> Organisatie met 500 medewerkers</figcaption>
        <div class="rekensom">
          <div><span class="getal">€ 125.000</span><span>investering per jaar</span></div>
          <span class="teken" aria-hidden="true">:</span>
          <div><span class="getal">€ 424.500</span><span>waarde van één procentpunt verzuim</span></div>
          <span class="teken" aria-hidden="true">=</span>
          <div class="uitkomst"><span class="getal">0,3 procentpunt</span><span>minder verzuim en de investering is terugverdiend</span></div>
        </div>
      </figure>
      <p>Daalt het verzuim van 5,4 naar 5,1 procent dan is de investering terugverdiend. De vraag aan de directie wordt daarmee een andere. Niet: geloven we in vitaliteit? Wel: achten we een daling van 0,3 procentpunt haalbaar met deze aanpak?</p>

      <h3>Stap 5: reken scenario's door en spreek af wat je meet</h3>
      <p>Laat zien wat een voorzichtig, een gemiddeld en een ambitieus resultaat oplevert.</p>
      <figure class="infographic">
        <figcaption><strong>Drie scenario's</strong> Netto resultaat per jaar bij een investering van € 125.000</figcaption>
        <div class="kerncijfers rijen">
          <div><span class="getal">€ 2.350</span><span><strong>Voorzichtig.</strong> Het verzuim daalt 0,3 procentpunt naar 5,1 procent. Dat scheelt € 127.350 aan verzuimkosten.</span></div>
          <div><span class="getal">€ 129.700</span><span><strong>Gemiddeld.</strong> Het verzuim daalt 0,6 procentpunt naar 4,8 procent. Dat scheelt € 254.700 aan verzuimkosten.</span></div>
          <div><span class="getal">€ 299.500</span><span><strong>Ambitieus.</strong> Het verzuim daalt 1,0 procentpunt naar 4,4 procent. Dat scheelt € 424.500 aan verzuimkosten.</span></div>
        </div>
        <p class="bron-regel">Dit zijn rekenvoorbeelden en geen voorspellingen. Welke daling haalbaar is hangt af van je uitgangspositie en je aanpak.</p>
      </figure>
      <p>Leg vooraf vast welke cijfers je volgt en wanneer je rapporteert. Vroege signalen zie je binnen maanden: deelname aan maatregelen, werkdruk en herstel in het medewerkersonderzoek en werkplezier. Resultaten volgen later: het verzuimpercentage, hoe vaak mensen zich ziek melden, de duur van het verzuim en het verloop.</p>
      <p>Reken op een aanloop. In het eerste jaar meet je en begin je. Het effect op verzuim en verloop volgt later. Spreek daarom vooraf af dat je de aanpak minstens twee tot drie jaar volhoudt en elk half jaar rapporteert.</p>

      <h2>Wat je niet meerekent maakt de case sterker</h2>
      <p>Het verzuimcijfer is een ondergrens. Drie kostenposten staan er niet in.</p>
      <ul>
        <li><strong>Ziek doorwerken.</strong> Studies schatten de kosten van presenteïsme 1,8 tot 3 keer zo hoog als de kosten van verzuim. Het is lastig te meten en de schattingen lopen uiteen. Daarom reken ik het in de businesscase niet mee. Lees meer in <a href="presenteisme-onbekende-productiviteitskiller">het artikel over presenteïsme</a>.</li>
        <li><strong>Verloop.</strong> Een overzicht van dertig praktijkstudies schat de kosten van het vervangen van een medewerker op ongeveer 20 procent van een jaarsalaris.</li>
        <li><strong>Arbeidsongeschiktheid.</strong> Middelgrote en grote werkgevers betalen een WGA-premie die afhangt van hoeveel van hun eigen medewerkers arbeidsongeschikt raken. Langdurig verzuim werkt dus nog jaren door in de loonkosten.</li>
      </ul>
      <p>Noem deze posten wel in je voorstel. Ze laten zien dat je voorzichtig hebt gerekend en dat de uitkomst een ondergrens is.</p>

      <h2>Van businesscase naar besluit</h2>
      <p>Een directie beslist op vijf vragen. Zorg dat je voorstel ze alle vijf beantwoordt.</p>
      <ol>
        <li><strong>Wat kost het ons nu?</strong> De verzuimkosten in euro's en wat je niet hebt meegerekend.</li>
        <li><strong>Waar zit het?</strong> De groepen en oorzaken waar de winst ligt.</li>
        <li><strong>Wat gaan we doen en waarom dat?</strong> De maatregelen en de onderbouwing.</li>
        <li><strong>Wanneer is het terugverdiend?</strong> Het omslagpunt en de scenario's.</li>
        <li><strong>Hoe weten we of het werkt?</strong> De cijfers die je volgt en de momenten waarop je rapporteert.</li>
      </ol>

      <h2>Vijf valkuilen</h2>
      <ul>
        <li><strong>Rekenen met het rendement van een ander.</strong> Een percentage uit een rapport overtuigt geen financieel directeur. Je eigen cijfers wel.</li>
        <li><strong>Te mooi rekenen.</strong> Reken voorzichtig en benoem wat je niet meerekent.</li>
        <li><strong>Beginnen bij de oplossing.</strong> Eerst de vraag en dan de maatregel.</li>
        <li><strong>Geen nulmeting.</strong> Zonder beginpunt weet je later niet wat het heeft opgeleverd.</li>
        <li><strong>De tijd van je eigen mensen vergeten.</strong> Die tijd bepaalt vaak of het lukt.</li>
      </ul>
      <p>Vitaliteit is geen kostenpost en ook geen wondermiddel. Het is een investering die je net zo zakelijk kunt onderbouwen als elke andere. Begin bij je eigen cijfers. Reken voorzichtig. Kies een aanpak die het werk zelf raakt.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over de businesscase voor vitaliteit</h2>
%(vragen)s
      </section>
%(deel)s
      <aside class="wp-tip" aria-label="Whitepaper">
        <img src="../img/whitepaper-businesscase-omslag.webp" width="560" height="793" alt="Omslag van de whitepaper De businesscase voor vitaliteit" loading="lazy">
        <div>
          <p class="podcast-label">Gratis whitepaper</p>
          <p class="podcast-titel">De businesscase voor vitaliteit</p>
          <p>De uitgebreide versie van dit artikel. Met de opbouw van de kosten per verzuimdag, vijf studies naast elkaar en een werkblad voor je eigen businesscase.</p>
          <a class="knop" href="../whitepaper-businesscase-vitaliteit">Download de whitepaper</a>
        </div>
      </aside>

      <aside class="lees-ook" aria-label="Lees ook">
        <h2>Lees ook</h2>
        <ul>
          <li><a href="gemiddeld-verzuim-is-niet-normaal">Gemiddeld verzuim is niet normaal</a></li>
          <li><a href="presenteisme-onbekende-productiviteitskiller">Presenteïsme: het onbekende fenomeen als productiviteitskiller</a></li>
          <li><a href="rendement-vitaliteitsprogramma-hbr-onderzoek">Rendement van een vitaliteitsprogramma: lessen van tien organisaties</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Wil je de businesscase voor jouw organisatie maken?</h2>
        <p>Ik reken hem graag met je door. In een gratis gesprek van 30 minuten kijken we naar je cijfers en naar waar de winst ligt.</p>
        <div class="hero-knoppen">
          <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
          <a class="knop omlijnd" href="../tools#rekentool-kop">Bereken je verzuimkosten</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://www.cbs.nl/nl-nl/nieuws/2026/23/ziekteverzuim-in-eerste-kwartaal-hoger-dan-gemiddeld-in-afgelopen-30-jaar">CBS: Ziekteverzuim in eerste kwartaal hoger dan gemiddeld in afgelopen 30 jaar (2026)</a></li>
          <li><a href="https://publications.tno.nl/publication/34644281/tJVhoMUv/TNO-2025-R11108.pdf">TNO: Arbobalans 2024 (2025)</a></li>
          <li><a href="https://www.voion.nl/media/ytupsdnx/nea-2023-resultaten-in-vogelvlucht-alle-sectoren-tno-2024.pdf">TNO: Nationale Enquête Arbeidsomstandigheden 2023 (2024)</a></li>
          <li><a href="https://hbr.org/2010/12/whats-the-hard-return-on-employee-wellness-programs">Berry, Mirabito en Baun: What's the Hard Return on Employee Wellness Programs?, Harvard Business Review (2010)</a></li>
          <li><a href="https://jamanetwork.com/journals/jama/fullarticle/2730614">Song en Baicker: Effect of a workplace wellness program on employee health and economic outcomes, JAMA (2019)</a></li>
          <li><a href="https://www.deloitte.com/uk/en/about/press-room/poor-mental-health-costs-uk-employers-51-billion-a-year-for-employees.html">Deloitte: Mental health and employers (2024)</a></li>
          <li><a href="https://oshwiki.osha.europa.eu/en/themes/presenteeism-overview">EU-OSHA: Presenteeism, an overview</a></li>
          <li><a href="https://www.americanprogress.org/article/there-are-significant-business-costs-to-replacing-employees/">Boushey en Glynn: There are significant business costs to replacing employees, Center for American Progress (2012)</a></li>
          <li><a href="https://www.mkbservicedesk.nl/personeel/verzuim-reintegratie/alles-over-de-wga-premie">MKB Servicedesk: Alles over de WGA-premie</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, uit=sys.argv[1] if len(sys.argv) > 1 else None)
