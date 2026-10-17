# Bouwt het artikel over de overgang op het werk.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'overgang-op-het-werk'
TITEL = 'De overgang op het werk: wat kun je als werkgever doen?'
H1 = 'De overgang op het werk: waarom je als werkgever niet kunt wegkijken'
BESCHR = 'Meer dan de helft van de vrouwen in de overgang merkt het in het werk. Weinigen praten erover met hun leidinggevende. Wat je als werkgever kunt doen.'

VRAGEN = [
 ('Hoeveel vrouwen hebben last van de overgang op het werk?', 'Volgens CBS en TNO gaven in 2021 173.000 vrouwelijke werknemers aan dat overgangsklachten weleens invloed hadden op hun werk. Dat is 55 procent van de vrouwelijke werknemers in de overgang. Bij 8 procent was dat dagelijks.'),
 ('Wat kan een werkgever doen voor medewerkers in de overgang?', 'Het onderwerp bespreekbaar maken, leidinggevenden leren het gesprek te voeren, de werkplek aanpassen met bijvoorbeeld ventilatie en een koele werkplek, ruimte geven in werktijden en de bedrijfsarts betrekken. Vaak zijn het kleine aanpassingen die veel verschil maken.'),
 ('Mag je als leidinggevende vragen naar de overgang?', 'Je mag niet vragen naar een diagnose of medische details. Je kunt wel vragen hoe het gaat, wat iemand in het werk merkt en wat zou helpen. Medische vragen horen bij de bedrijfsarts of de huisarts.'),
 ('Wat doet de bedrijfsarts bij overgangsklachten?', 'Volgens de richtlijn Overgang en Werk van de NVAB uit 2026 neemt de bedrijfsarts het voortouw bij het voorkomen van gezondheidsschade door de overgang. De bedrijfsarts adviseert over aanpassingen in het werk en verwijst zo nodig naar de huisarts, gynaecoloog of overgangsconsulent.'),
]
ICO = {
 'team': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 5.2a3 3 0 0 1 0 5.6M18 14.3c1.8.9 3 2.7 3 5.7"/>',
 'werk': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
 'gesprek': '<path d="M21 12a8 8 0 0 1-11.5 7.2L4 21l1.8-5.5A8 8 0 1 1 21 12z"/>',
 'hart': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
 'thermo': '<path d="M14 14.8V5a2 2 0 0 0-4 0v9.8a4 4 0 1 0 4 0z"/>',
 'klok': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'kompas': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 'arts': '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M12 8v8M8 12h8"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">17 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Ze heeft twintig jaar ervaring, kent het vak en de klanten. Maar de laatste tijd slaapt ze slecht, verliest ze de draad in een overleg en krijgt ze midden in een presentatie een opvlieger. Ze zegt er niets over. Op 18 oktober is het Wereld Menopauzedag. Een goed moment om te kijken naar een onderwerp dat op de werkvloer nog vaak een taboe is: de overgang.</p>

      <h2>Waarom dit jou als werkgever aangaat</h2>
      <p>In Nederland zijn ongeveer 1,8 miljoen vrouwen in de levensfase waarin overgangsklachten een grote rol spelen. Ongeveer 80 procent van hen heeft klachten. En steeds meer van hen werken: van de vrouwen tussen 55 en 65 jaar had in 2025 bijna 70 procent werk. In 2013 was dat nog geen 50 procent.</p>
      <p>Het gaat dus om een grote groep ervaren medewerkers. Vaak in een fase van hun loopbaan waarin ze veel kennis en verantwoordelijkheid hebben. Die wil je niet kwijt.</p>
      <figure class="infographic">
        <figcaption><strong>De overgang op het werk in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_werk)s<span class="getal">55%%</span><span>van de werknemers in de overgang merkt de klachten in het werk</span></div>
          <div>%(i_kompas)s<span class="getal">36%%</span><span>vindt dat ze minder goed functioneert</span></div>
          <div>%(i_gesprek)s<span class="getal">35%%</span><span>praat er op het werk met niemand over</span></div>
          <div>%(i_hart)s<span class="getal">57%%</span><span>van wie het merkt in het werk wil meer steun of begrip</span></div>
        </div>
        <p class="bron-regel">Bronnen: CBS, 2022. TNO, De overgang: klachten en de invloed op het werk, 2022</p>
      </figure>

      <h2>Wat merk je ervan in het werk?</h2>
      <p>Opvliegers en nachtelijk zweten zijn de bekendste klachten. Maar ook slecht slapen, vermoeidheid, concentratie- en geheugenproblemen, stemmingswisselingen en pijn in spieren en gewrichten komen veel voor. Het thema van Wereld Menopauzedag is dit jaar ook chronische pijn in de middelbare leeftijd.</p>
      <p>Volgens TNO vindt 36 procent van de vrouwen in de overgang dat ze minder goed functioneert door bijvoorbeeld pijn, vermoeidheid of concentratieproblemen. 31 procent maakt weleens ongemakkelijke situaties mee op de werkvloer, bijvoorbeeld door een opvlieger. Het verband met burn-outklachten is opvallend.</p>
      <figure class="infographic">
        <figcaption><strong>Burn-outklachten bij vrouwen in de overgang</strong> In procenten van de vrouwelijke werknemers</figcaption>
        <div class="balken">
          <div class="balk-rij" title="Geen overgangsklachten: 13,4%%">
            <span class="balk-label">Geen overgangsklachten</span>
            <span class="balk-spoor"><span class="balk" style="width:33.5%%"></span></span>
            <span class="balk-waarde">13,4%%</span>
          </div>
          <div class="balk-rij" title="Soms klachten: 26,3%%">
            <span class="balk-label">Soms klachten</span>
            <span class="balk-spoor"><span class="balk" style="width:65.8%%"></span></span>
            <span class="balk-waarde">26,3%%</span>
          </div>
          <div class="balk-rij" title="Regelmatig klachten: 38,9%%">
            <span class="balk-label">Regelmatig klachten</span>
            <span class="balk-spoor"><span class="balk" style="width:97.3%%"></span></span>
            <span class="balk-waarde">38,9%%</span>
          </div>
        </div>
        <p class="bron-regel">Bron: TNO, De overgang: klachten en de invloed op het werk, 2022</p>
      </figure>
      <p>Ongeveer 2 procent meldt zich weleens ziek door de klachten. Dat lijkt weinig. Maar het grootste verlies zit niet in verzuim. Het zit in mensen die doorwerken terwijl het niet goed gaat, die minder uren gaan werken of die stoppen. In een groot Brits onderzoek dacht 17 procent van de vrouwen erover om te stoppen met werken door gebrek aan steun. 6 procent was al gestopt.</p>

      <h2>Waarom niemand erover begint</h2>
      <p>Van de vrouwen in de overgang met klachten praat 35 procent er op het werk met niemand over. Maar 13 procent bespreekt het met de leidinggevende en nog geen 3 procent met de bedrijfsarts. Tegelijk wil 57 procent van de vrouwen die de klachten in hun werk merken meer steun of begrip. En als ze zeggen van wie, noemen ze het vaakst de leidinggevende.</p>
      <p>Daar zit dus de sleutel. Niet in een groot programma, maar in een leidinggevende die het onderwerp normaal maakt en weet wat hij of zij kan doen.</p>

      <h2>Wat kun je doen?</h2>
      <p>De NVAB, de vereniging van bedrijfsartsen, bracht in maart 2026 een richtlijn uit over overgang en werk. Daarin staan veel praktische maatregelen. Vaak zijn het kleine aanpassingen.</p>
      <figure class="infographic">
        <figcaption><strong>Vier soorten maatregelen</strong></figcaption>
        <div class="bouwblokken vier">
          <div>%(i_thermo)s<strong>De werkplek</strong><span>Goede ventilatie, een koele werkplek of een ventilator, koud drinkwater en makkelijk bereikbare toiletten. Ademende bedrijfskleding als er een uniform is.</span></div>
          <div>%(i_klok)s<strong>Het werk</strong><span>Ruimte om werktijden aan te passen na een slechte nacht, duidelijke taken en invloed op hoe je je werk doet. En voorkomen dat het werk te veel wordt.</span></div>
          <div>%(i_gesprek)s<strong>De leidinggevende</strong><span>Het onderwerp bespreekbaar maken, vragen wat iemand nodig heeft en steun geven. Zonder te vragen naar medische details.</span></div>
          <div>%(i_arts)s<strong>De bedrijfsarts</strong><span>De bedrijfsarts neemt het voortouw bij preventie, adviseert over aanpassingen en verwijst zo nodig door naar huisarts, gynaecoloog of overgangsconsulent.</span></div>
        </div>
        <p class="bron-regel">Bron: NVAB, richtlijn Overgang en Werk, 2026</p>
      </figure>

      <h2>Het gesprek: zo begin je</h2>
      <p>Je hoeft geen kennis van de overgang te hebben om een goed gesprek te voeren. Een paar vragen helpen:</p>
      <ul>
        <li>Hoe gaat het met je, en hoe gaat het met je werk?</li>
        <li>Merk je iets dat het werk lastiger maakt dan vroeger?</li>
        <li>Wat zou je helpen? Denk aan je werkplek, je werktijden of je taken.</li>
        <li>Zou het helpen om met de bedrijfsarts te praten?</li>
      </ul>
      <p>Medische vragen stel je niet. Dat is aan de bedrijfsarts en de huisarts. Jouw rol is ruimte maken en praktisch meedenken.</p>

      <h2>Wat je als organisatie kunt doen</h2>
      <ul>
        <li><strong>Doorbreek het taboe.</strong> Noem het onderwerp in het werkoverleg, op intranet of in een inspiratiesessie. De Stichting van de Arbeid maakte een handreiking met precies dat doel.</li>
        <li><strong>Train leidinggevenden.</strong> Een leidinggevende die weet wat er speelt, voert het gesprek makkelijker en eerder.</li>
        <li><strong>Neem het op in je beleid.</strong> De overgang hoort bij duurzame inzetbaarheid, net als werkdruk en leefstijl. Bijvoorbeeld in een preventief medisch onderzoek met aandacht voor de overgang.</li>
        <li><strong>Gebruik Wereld Menopauzedag.</strong> Een moment om het onderwerp voor het eerst te noemen. Daarna wordt het makkelijker.</li>
      </ul>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over de overgang op het werk</h2>
%(vragen)s
      </section>
%(deel)s
      <aside class="wp-tip" aria-label="Whitepaper">
        <img src="../img/whitepaper-vitaliteitsbeleid-omslag.webp" width="560" height="793" alt="Omslag van de whitepaper Vitaliteitsbeleid opzetten" loading="lazy">
        <div>
          <p class="podcast-label">Gratis whitepaper</p>
          <p class="podcast-titel">Vitaliteitsbeleid opzetten</p>
          <p>Van losse activiteiten naar beleid dat werkt. Met zeven stappen, een jaarplanning en een checklist.</p>
          <a class="knop" href="../whitepaper-vitaliteitsbeleid-opzetten">Download de whitepaper</a>
        </div>
      </aside>

      <aside class="lees-ook" aria-label="Lees ook">
        <h2>Lees ook</h2>
        <ul>
          <li><a href="wat-is-duurzame-inzetbaarheid">Wat is duurzame inzetbaarheid en hoe begin je ermee?</a></li>
          <li><a href="mantelzorger-in-je-team">De mantelzorger in je team: onzichtbaar en overbelast</a></li>
          <li><a href="presenteisme-onbekende-productiviteitskiller">Presenteïsme: het onbekende fenomeen als productiviteitskiller</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>De overgang bespreekbaar maken in jouw organisatie?</h2>
        <p>Begin met een inspiratiesessie van een uur voor leidinggevenden of medewerkers. Of bespreek eerst in een gratis gesprek van 30 minuten hoe je de overgang een plek geeft in je beleid.</p>
        <div class="hero-knoppen">
          <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
          <a class="knop omlijnd" href="../trainingen#workshops">Bekijk de inspiratiesessies</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://nvab-online.nl/app/uploads/2026/03/20260312-NVAB_Richtlijn-Overgang-en-Werk_DEF.pdf">NVAB: Richtlijn Overgang en Werk (2026)</a></li>
          <li><a href="https://www.cbs.nl/nl-nl/nieuws/2022/20/helft-werknemers-in-overgang-ondervindt-hinder-op-werk">CBS: Helft werknemers in overgang ondervindt hinder op werk (2022)</a></li>
          <li><a href="https://publications.tno.nl/publication/34639469/ur01Jm/TNO-2022-R10823.pdf">TNO: De overgang, klachten en de invloed op het werk (2022)</a></li>
          <li><a href="https://publications.tno.nl/publication/34639499/ibBJSJ/TNO-2022-overgang.pdf">TNO: Factsheet De overgang, klachten en invloed op het werk (2022)</a></li>
          <li><a href="https://www.cbs.nl/nl-nl/visualisaties/dashboard-arbeidsmarkt/werkenden/arbeidsparticipatie-naar-leeftijd-en-geslacht">CBS: Arbeidsparticipatie naar leeftijd en geslacht</a></li>
          <li><a href="https://cipd.org/uk/knowledge/reports/menopause-workplace-experiences/">CIPD: Menopause in the workplace, employee experiences in 2023</a></li>
          <li><a href="https://www.awvn.nl/arbeidsongeschiktheid/nieuws/handreiking-moet-taboe-op-overgang-op-het-werk-doorbreken/">AWVN: Handreiking moet taboe op overgang op het werk doorbreken (2023)</a></li>
          <li><a href="https://www.imsociety.org/?p=4180">International Menopause Society: World Menopause Day 2026</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-17', uit=sys.argv[1] if len(sys.argv) > 1 else None)
