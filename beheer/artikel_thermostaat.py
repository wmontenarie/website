# Bouwt het artikel over het voorbeeld van de leidinggevende en werkstress in het team.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'leidinggevende-voorbeeld-werkstress'
TITEL = 'Werkstress in je team: jouw voorbeeld als leidinggevende'
H1 = 'Jij bent de thermostaat van je team'
BESCHR = 'Hoe jij met druk, pauzes en mail na werktijd omgaat, bepaalt mee hoeveel stress je team ervaart. Wat onderzoek zegt en wat je morgen anders doet.'

VRAGEN = [
 ('Heeft de stress van een leidinggevende invloed op het team?', 'Ja, daar zijn duidelijke aanwijzingen voor. Een overzicht van 49 studies vond een verband tussen het welzijn en gedrag van leidinggevenden en de stress van medewerkers. En een meta-analyse van 88 studies laat zien dat leidinggevenden die gestrest of uitgeput zijn vaker negatief leiderschapsgedrag laten zien.'),
 ('Hoe geef je als leidinggevende het goede voorbeeld bij werkstress?', 'Door zelf te doen wat je van je team vraagt. Neem zichtbaar pauze, ga op tijd naar huis, zeg nee tegen werk dat niet past en zet in een mail buiten werktijd dat het antwoord pas later hoeft. En praat open over je eigen energie, ook op dagen dat het minder gaat.'),
 ('Wat is gezondheidsgericht leiderschap?', 'Leiderschap waarbij je zowel goed voor jezelf zorgt als voor je team. Onderzoek laat zien dat medewerkers zich het gezondst voelen als de leidinggevende goed voor zichzelf zorgt, oog heeft voor het team en medewerkers ook zelf goed voor zichzelf zorgen.'),
 ('Wanneer is de Week van de Werkstress?', 'In 2026 is de Week van de Werkstress van maandag 9 tot en met vrijdag 13 november. Het is een goed moment om met je team te bespreken hoe jullie met druk en herstel omgaan.'),
]
ICO = {
 'meter': '<path d="M12 3a9 9 0 1 0 9 9"/><path d="M12 12l5-5"/><circle cx="12" cy="12" r="1.5"/>',
 'mens': '<circle cx="12" cy="7" r="4"/><path d="M4 21v-1a7 7 0 0 1 16 0v1"/>',
 'batterij': '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M5 10v4"/>',
 'team': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 5.2a3 3 0 0 1 0 5.6M18 14.3c1.8.9 3 2.7 3 5.7"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">26 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Je zegt tegen je team dat ze op tijd naar huis moeten. En om tien uur 's avonds stuur je zelf nog een mail. Je team hoort wat je zegt, maar doet wat je doet. Van 9 tot en met 13 november is het de Week van de Werkstress. Een goed moment om niet alleen naar je team te kijken, maar ook naar jezelf.</p>

      <h2>Waarom jij de temperatuur bepaalt</h2>
      <p>Een thermostaat meet niet alleen de temperatuur, hij stelt hem in. Zo werkt het ook in een team. Hoe jij met druk omgaat, wordt de norm. Ben jij gejaagd, dan wordt het team gejaagd. Neem jij rust, dan mag rust.</p>
      <p>Onderzoek bevestigt dat beeld. Volgens Gallup verklaart de leidinggevende minstens 70 procent van de verschillen in betrokkenheid tussen teams. Een overzicht van 49 studies vond een verband tussen het welzijn en het gedrag van leidinggevenden en de stress van hun medewerkers. En uit een experiment blijkt dat de stemming van de leider aanstekelijk is: groepen met een leider in een goede stemming werkten beter samen en hadden minder moeite nodig.</p>
      <figure class="infographic">
        <figcaption><strong>De leidinggevende en werkstress in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_meter)s<span class="getal">70%%</span><span>van de verschillen in betrokkenheid tussen teams komt door de leidinggevende</span></div>
          <div>%(i_mens)s<span class="getal">30%%</span><span>van de Nederlandse werknemers had de vorige dag veel stress</span></div>
          <div>%(i_batterij)s<span class="getal">21%%</span><span>van de werknemers in Nederland heeft burn-outklachten</span></div>
          <div>%(i_team)s<span class="getal">27%%</span><span>van de managers wereldwijd is nog betrokken bij het werk, was 30%%</span></div>
        </div>
        <p class="bron-regel">Bronnen: Gallup, 2015 en State of the Global Workplace 2025 en 2026. TNO en CBS, NEA 2025</p>
      </figure>

      <h2>Een uitgeputte leider geeft slechter leiding</h2>
      <p>Het gaat niet alleen om wat je laat zien. Het gaat ook om hoe het met je gaat. Een meta-analyse van 88 studies met meer dan 12.000 deelnemers laat zien dat leidinggevenden die zich goed voelen vaker constructief leidinggeven. Leidinggevenden die gestrest of emotioneel uitgeput zijn, laten vaker negatief gedrag zien. Ze zijn korter, ongeduldiger of trekken zich terug. Ook dat terugtrekken is volgens de onderzoekers niet neutraal: een team zonder leiding raakt ook onder druk.</p>
      <p>En juist leidinggevenden staan onder druk. Volgens Gallup daalde de betrokkenheid van managers wereldwijd van 30 naar 27 procent, en managers lieten de grootste daling in welzijn zien. Een leidinggevende die zelf op reserve rijdt, kan zijn team moeilijk opladen.</p>

      <h2>Zorg voor jezelf is geen egoïsme</h2>
      <p>Duits onderzoek naar gezondheidsgericht leiderschap laat zien wanneer medewerkers zich het gezondst voelen. Dat is als drie dingen samen gaan: de leidinggevende zorgt goed voor zichzelf, heeft oog voor het team, en medewerkers zorgen ook zelf goed voor zichzelf. Ontbreekt dat, dan zijn spanning en klachten het hoogst.</p>
      <p>Zelfzorg is dus geen luxe en geen privézaak. Het is een deel van je werk als leidinggevende. Wie energie heeft en goed herstelt, kan ook iets dragen voor een ander.</p>

      <h2>Zes dingen die je team van jou overneemt</h2>
      <figure class="infographic">
        <figcaption><strong>Het goede voorbeeld in zes gewoontes</strong></figcaption>
        <ol class="stappen">
          <li><strong>Neem zichtbaar pauze</strong><p>Loop 's middags een rondje, eet niet achter je scherm. Als jij het doet, durft je team het ook.</p></li>
          <li><strong>Zeg wanneer je antwoord verwacht</strong><p>Uit acht experimenten blijkt dat ontvangers van een mail na werktijd denken dat er sneller antwoord moet komen dan de afzender bedoelt. Zet erbij: dit hoeft pas maandag.</p></li>
          <li><strong>Respecteer grenzen</strong><p>Bel niet in de avond of op een vrije dag, tenzij het echt niet anders kan. In een dagboekstudie kwamen medewerkers dan beter los van het werk en voelden ze zich 's ochtends beter hersteld.</p></li>
          <li><strong>Praat over je eigen energie</strong><p>Zeg ook eens dat je een zware week hebt en wat je doet om bij te tanken. Dat maakt het gewoon om erover te praten.</p></li>
          <li><strong>Kies wat niet hoeft</strong><p>Werkdruk daalt niet door harder te werken. Bespreek met je team wat er kan vervallen, verschuiven of eenvoudiger.</p></li>
          <li><strong>Vraag feedback op jezelf</strong><p>Vraag je team: wat doe ik dat druk geeft? Het antwoord zegt vaak meer dan een enquête.</p></li>
        </ol>
      </figure>

      <h2>Gebruik de Week van de Werkstress voor een spiegel</h2>
      <p>Veel organisaties vullen de Week van de Werkstress met een workshop voor medewerkers. Dat is mooi, maar de grootste hefboom zit bij de leiding. Neem in het werkoverleg van die week tien minuten voor een eerlijke vraag: welk gedrag van mij helpt jullie om energie te houden, en welk gedrag niet? Spreek daarna één ding af dat je anders gaat doen. En kom er over een maand op terug.</p>
      <p>Echt leiderschap begint bij het goede voorbeeld. Niet in een cursus, maar in hoe je elke dag werkt en leeft.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over leidinggevenden en werkstress</h2>
%(vragen)s
      </section>
%(deel)s
      <aside class="wp-tip" aria-label="Whitepaper">
        <img src="../img/whitepaper-werkdruk-omslag.webp" width="560" height="793" alt="Omslag van de whitepaper Werkdruk verlagen" loading="lazy">
        <div>
          <p class="podcast-label">Gratis whitepaper</p>
          <p class="podcast-titel">Werkdruk verlagen</p>
          <p>Oorzaken vinden, het gesprek voeren en met je team aan de slag. Met een teamgesprek in zes stappen en een werkdruk-check.</p>
          <a class="knop" href="../whitepaper-werkdruk-verlagen">Download de whitepaper</a>
        </div>
      </aside>

      <aside class="lees-ook" aria-label="Lees ook">
        <h2>Lees ook</h2>
        <ul>
          <li><a href="week-zonder-werkstress-ideeen">Week van de Werkstress 2026: ideeën voor je team</a></li>
          <li><a href="herstel-en-rust-op-het-werk">Herstel is geen luxe: rust inbouwen in een volle werkweek</a></li>
          <li><a href="stress-bespreekbaar-maken">Stress bespreekbaar maken: het gesprek dat je vaker moet voeren</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Zelf het goede voorbeeld geven?</h2>
        <p>In de training vitaal leiderschap ontdek je hoe je je eigen energie op peil houdt en hoe je dat voorleeft aan je team. Of bespreek eerst in een gratis gesprek van 30 minuten wat bij jou past.</p>
        <div class="hero-knoppen">
          <a class="knop" href="../training-vitaal-leiderschap">Bekijk de training</a>
          <a class="knop omlijnd" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://news.gallup.com/businessjournal/182792/managers-account-variance-employee-engagement.aspx">Gallup: Managers account for 70%% of variance in employee engagement (2015)</a></li>
          <li><a href="https://www.gallup.com/file/workplace/660197/State-of-the-Global-Workplace-Global-Press-Release-2025.pdf">Gallup: State of the Global Workplace 2025, persbericht</a></li>
          <li><a href="https://www.gallup.com/workplace/706490/state-global-workplace-netherlands-country-level-data.aspx">Gallup: State of the Global Workplace 2026, cijfers Nederland</a></li>
          <li><a href="https://monitorarbeid.tno.nl/wp-content/uploads/sites/16/2026/04/Factsheet-NEA2025.pdf">TNO en CBS: Factsheet Nationale Enquête Arbeidsomstandigheden 2025</a></li>
          <li><a href="https://research-portal.uea.ac.uk/en/publications/are-leaders-well-being-behaviours-and-style-associated-with-the-a/">Skakon e.a.: Are leaders' well-being, behaviours and style associated with the affective well-being of their employees? Work &amp; Stress (2010)</a></li>
          <li><a href="https://idw-online.de/en/news718463">Universiteit Kiel: meta-analyse van Kaluza e.a. naar welzijn en gedrag van leidinggevenden, Work &amp; Stress (2019)</a></li>
          <li><a href="https://synapsesocial.com/papers/W2058531065">Sy, Côté en Saavedra: The contagious leader, Journal of Applied Psychology (2005)</a></li>
          <li><a href="https://doaj.org/article/6f5fd02eee434c138d407a5a10b3f66a">Klug, Felfe en Krick: Caring for oneself or for others? Frontiers in Psychology (2019)</a></li>
          <li><a href="https://fis.leuphana.de/en/publications/leader-support-for-recovery-a-multi-level-approach-to-employee-ps/">Sonnentag, Kark en Venz: Leader support for recovery, Journal of Occupational and Organizational Psychology (2024)</a></li>
          <li><a href="https://news.cornell.edu/node/322477">Cornell University: onderzoek van Giurge en Bohns naar mail na werktijd (2021)</a></li>
          <li><a href="https://deweekvandewerkstress.nl/">De Week van de Werkstress</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-26', uit=sys.argv[1] if len(sys.argv) > 1 else None)
