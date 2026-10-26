# Bouwt het artikel over diabetes type 2 voorkomen en de rol van de werkgever.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'diabetes-type-2-voorkomen-werk'
TITEL = 'Diabetes type 2 voorkomen: wat werkgevers kunnen doen'
H1 = 'Diabetes type 2 voorkomen begint op het werk'
BESCHR = 'Werknemers zitten bijna negen uur per werkdag. Zo werkt leefstijl op het werk mee aan het voorkomen van diabetes type 2, en wat je als werkgever doet.'

VRAGEN = [
 ('Hoeveel mensen in Nederland hebben diabetes type 2?', 'Ongeveer 1,2 miljoen mensen in Nederland hebben diabetes, van wie 9 op de 10 type 2. Daarnaast hebben naar schatting zo\'n 400.000 mensen type 2 zonder het te weten, volgens het Diabetes Fonds.'),
 ('Is diabetes type 2 te voorkomen?', 'Bij mensen met een verhoogd risico vaak wel. In het bekende Amerikaanse Diabetes Prevention Program kregen deelnemers met een leefstijlprogramma 58 procent minder vaak diabetes type 2 dan de groep zonder programma. Het programma richtte zich op meer bewegen en wat gewicht verliezen.'),
 ('Wat kan een werkgever doen tegen diabetes?', 'Lang stilzitten onderbreken, bewegen in het werk inbouwen, gezond eten makkelijk maken en letten op roosters, slaap en werkstress. En medewerkers met diabetes de ruimte geven voor hun zorg, zoals een pauze om te eten of te meten en vrij voor controles.'),
 ('Wanneer is Wereld Diabetes Dag?', 'Elk jaar op 14 november. Het thema van de Wereldgezondheidsorganisatie in 2026 is vroeg ingrijpen bij diabetes.'),
]
ICO = {
 'mens': '<circle cx="12" cy="7" r="4"/><path d="M4 21v-1a7 7 0 0 1 16 0v1"/>',
 'vraag': '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14M12 17v.01"/>',
 'stoel': '<path d="M6 21v-6M18 21v-6M5 15h14M7 15V5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v10"/>',
 'pijl': '<path d="M3 17l6-6 4 4 8-8"/><path d="M14 7h7v7"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">26 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Op 14 november is het Wereld Diabetes Dag. Diabetes klinkt als een onderwerp voor de huisarts. Maar de leefstijl die het risico op diabetes type 2 vergroot, ontstaat voor een groot deel op het werk. Lang zitten, eten tussen twee vergaderingen door, te weinig slaap en veel stress. Als werkgever heb je daar meer invloed op dan je denkt.</p>

      <h2>Hoe groot is het?</h2>
      <p>Ongeveer 1 op de 14 Nederlanders heeft diabetes, en 9 op de 10 van hen hebben type 2. Elk jaar komen er zo'n 54.000 mensen bij. Naar schatting krijgt 1 op de 3 mensen die nu 45 jaar zijn later diabetes type 2. Het is dus geen ziekte van alleen ouderen: ook ruim 18.000 dertigers hebben type 2.</p>
      <figure class="infographic">
        <figcaption><strong>Diabetes in Nederland in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_mens)s<span class="getal">1,2 mln</span><span>mensen in Nederland hebben diabetes, 9 op de 10 type 2</span></div>
          <div>%(i_vraag)s<span class="getal">400.000</span><span>mensen hebben type 2 zonder het te weten</span></div>
          <div>%(i_pijl)s<span class="getal">1,3 tot 1,5 mln</span><span>mensen van 40 tot 75 jaar hebben prediabetes</span></div>
          <div>%(i_stoel)s<span class="getal">8,9 uur</span><span>zitten werknemers gemiddeld op een werkdag</span></div>
        </div>
        <p class="bron-regel">Bronnen: VZinfo, 2025. Diabetes Fonds, 2024. CBS, 2025</p>
      </figure>
      <p>Daarnaast hebben naar schatting 1,3 tot 1,5 miljoen mensen van 40 tot 75 jaar prediabetes: een verhoogde bloedsuiker die nog geen diabetes is. Van hen kreeg 14 procent in ruim acht jaar diabetes type 2, tegen 2 procent van de mensen met een normale bloedsuiker. Juist in die groep, vaak midden in hun loopbaan, valt veel te winnen.</p>

      <h2>Wat het werk ermee te maken heeft</h2>
      <p>Werknemers zitten gemiddeld 8,9 uur per werkdag. Daarvan zitten ze 4,5 uur op het werk, 1,1 uur onderweg en 3,3 uur in hun vrije tijd. Bijna de helft van de werkenden zit tijdens het werk zes uur of langer. Volgens TNO is Nederland Europees kampioen zitten. En maar 47 procent van de mensen beweegt genoeg volgens de beweegrichtlijnen.</p>
      <p>Daar komen werkdruk, onregelmatige diensten en te weinig slaap bij. Ze maken het moeilijker om gezond te eten en te bewegen. Leefstijl is daarom niet alleen een privékeuze. Het werk bepaalt voor een groot deel hoe makkelijk of moeilijk de gezonde keuze is.</p>

      <h2>Preventie werkt</h2>
      <p>Het goede nieuws: bij mensen met een verhoogd risico is diabetes type 2 vaak te voorkomen of uit te stellen. In het bekende Diabetes Prevention Program kregen deelnemers met een leefstijlprogramma 58 procent minder vaak diabetes type 2. Het doel was haalbaar: 150 minuten per week bewegen en 7 procent gewicht verliezen. Een overzicht van tien studies liet zien dat zulke programma's ook op het werk het risico verlagen, zeker als de werkgever meedoet met passende roosters en een passende werkomgeving.</p>
      <p>Wie overgewicht heeft en een verhoogd risico, kan via de huisarts ook een gecombineerde leefstijlinterventie krijgen. Dat programma van twee jaar zit in het basispakket en valt niet onder het eigen risico.</p>

      <h2>Wat je als werkgever kunt doen</h2>
      <figure class="infographic">
        <figcaption><strong>Zes stappen voor een werkplek die helpt</strong></figcaption>
        <ol class="stappen">
          <li><strong>Onderbreek het zitten</strong><p>Sta op bij het bellen, maak van een overleg een wandeloverleg en plan korte pauzes tussen vergaderingen.</p></li>
          <li><strong>Maak bewegen gewoon</strong><p>Fietsen naar het werk, de trap in plaats van de lift, een wandeling in de lunchpauze. Leidinggevenden die het zelf doen, maken het normaal.</p></li>
          <li><strong>Maak gezond eten makkelijk</strong><p>Wat in de kantine en bij vergaderingen standaard staat, wordt gegeten. Maak de gezonde keuze de makkelijkste.</p></li>
          <li><strong>Let op roosters en slaap</strong><p>Onregelmatige diensten en weinig slaap maken gezond leven moeilijker. Kijk of roosters voorspelbaarder kunnen.</p></li>
          <li><strong>Pak werkstress aan</strong><p>Wie onder druk staat, slaat de lunch over en beweegt minder. Werkdruk verlagen is ook preventie.</p></li>
          <li><strong>Geef ruimte aan wie diabetes heeft</strong><p>Een pauze om te eten of te meten en vrij voor controles. In internationaal onderzoek van de IDF kreeg 28 procent van de werknemers met diabetes die ruimte niet.</p></li>
        </ol>
      </figure>

      <h2>Gebruik 14 november als begin</h2>
      <p>Een voorlichtingsbijeenkomst op Wereld Diabetes Dag is een goed begin. Maar de echte winst zit in het gewone werk, elke dag. Vraag je af: maakt onze manier van werken de gezonde keuze makkelijker of moeilijker? Dat antwoord bepaalt meer dan elke campagne.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over diabetes en werk</h2>
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
          <li><a href="vitaliteit-op-de-werkvloer">Vitaliteit op de werkvloer: wat werkt en elf tips</a></li>
          <li><a href="werken-met-chronische-aandoening">Werken met een chronische aandoening: acht maatregelen voor werkgevers</a></li>
          <li><a href="zes-bouwblokken-vitaliteitsbeleid">Vitaliteitsbeleid: zes bouwblokken die werken</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Leefstijl een plek geven in je beleid?</h2>
        <p>Ik help je vitaliteitsbeleid op te zetten waarin werk, leefstijl en leiderschap samenkomen. Bespreek in een gratis gesprek van 30 minuten waar je kunt beginnen, of doe eerst de gratis vitaliteitsscan.</p>
        <div class="hero-knoppen">
          <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
          <a class="knop omlijnd" href="../vitaliteitsmeter">Doe de vitaliteitsscan</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://www.who.int/campaigns/world-diabetes-day/2026">Wereldgezondheidsorganisatie: World Diabetes Day 2026</a></li>
          <li><a href="https://www.vzinfo.nl/diabetes-mellitus">VZinfo: Diabetes mellitus</a></li>
          <li><a href="https://www.diabetesfonds.nl/over-diabetes/wat-is-diabetes/diabetes-in-cijfers">Diabetes Fonds: Diabetes in cijfers</a></li>
          <li><a href="https://www.diabetesfonds.nl/uploads/2025-01/prediabetes_in_nederland_diabetes_fonds_factsheet_20240416.pdf">Diabetes Fonds en Maastricht UMC+: Factsheet prediabetes in Nederland (2024)</a></li>
          <li><a href="https://www.diabetesfonds.nl/nieuws/nieuwe-cijfers-van-nivel-over-diabetes">Diabetes Fonds: Nieuwe cijfers van Nivel over diabetes (2024)</a></li>
          <li><a href="https://www.cbs.nl/nl-nl/nieuws/2025/34/werknemers-zitten-gemiddeld-bijna-9-uur-per-werkdag">CBS: Werknemers zitten gemiddeld bijna 9 uur per werkdag (2025)</a></li>
          <li><a href="https://www.tno.nl/nl/newsroom/2024/02/nederland-europees-kampioen-zitten/">TNO: Nederland Europees kampioen zitten (2024)</a></li>
          <li><a href="https://www.kenniscentrumsportenbewegen.nl/nieuws/sport-en-beweegcijfers-2025-voorzichtig-positieve-trend-zichtbaar/">Kenniscentrum Sport &amp; Bewegen: Sport- en beweegcijfers 2025 (2026)</a></li>
          <li><a href="https://pubmed.ncbi.nlm.nih.gov/11832527/">Diabetes Prevention Program Research Group: New England Journal of Medicine (2002)</a></li>
          <li><a href="https://doaj.org/article/94f870ca6282487ea48086fee6fb9f06">Systematische review naar leefstijlprogramma's tegen diabetes type 2 op het werk, Revista de Saúde Pública (2019)</a></li>
          <li><a href="https://www.zorginstituutnederland.nl/verzekerde-zorg/g/gecombineerde-leefstijlinterventie-gli-zvw">Zorginstituut Nederland: Gecombineerde leefstijlinterventie</a></li>
          <li><a href="https://idf.org/news-and-resources/news/negative-workplace-treatment/">International Diabetes Federation: onderzoek naar diabetes op het werk (2025)</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-26', uit=sys.argv[1] if len(sys.argv) > 1 else None)
