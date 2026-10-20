# Bouwt training-cultuurverandering.html. Pas de inhoud hier aan en draai: python3 beheer/training_cultuurverandering.py
import sys, os, re, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pagina_basis import maak_pagina

PRIJS = 2995
MIN_GROEP, MAX_GROEP = 6, 10
def euro(n): return '€&nbsp;' + '{:,}'.format(n).replace(',', '.')
INCL = round(PRIJS * 1.21)
PP_LAAG, PP_HOOG = round(PRIJS / MAX_GROEP), round(PRIJS / MIN_GROEP)

VRAGEN = [
    ('Wat is cultuurverandering?', 'Cultuur is hoe het bij jullie gaat als niemand kijkt. Wat normaal is, wat mag en wat niet. Bij cultuurverandering verander je die vanzelfsprekendheden. Bijvoorbeeld hoe je omgaat met werkdruk, met herstel of met een collega die uitvalt.'),
    ('Waarom het model van Kotter en niet ADKAR of De Caluwé?', 'ADKAR kijkt vooral naar de verandering bij één persoon. De Caluwé helpt je kiezen hoe je verandert. Kotter geeft een managementteam een duidelijke volgorde om een organisatie mee te nemen, van urgentie tot verankering. Dat past bij een team dat samen een plan wil maken. Ik gebruik het als leidraad, niet als recept.'),
    ('Hoe ga je om met weerstand?', 'Weerstand is informatie. Mensen hebben vaak een goede reden om te twijfelen. In dagdeel 3 leer je die redenen te achterhalen en weg te nemen wat in de weg zit, in plaats van harder te duwen.'),
    ('Is de training geschikt voor de zorg en het onderwijs?', 'Ja. Juist daar zijn werkdruk en verzuim hoog en lopen veranderingen vaak vast. Kan je organisatie de btw niet terugvragen? Dan kost de training %s inclusief btw.' % euro(INCL).replace('&nbsp;', ' ')),
    ('Hoe lang duurt een cultuurverandering?', 'Langer dan vier dagdelen. Een cultuur verander je niet in een training. Wel zet je de eerste stappen en ga je naar huis met een plan voor het jaar daarna.'),
    ('Wat levert het op voor verzuim en werkdruk?', 'Dat hangt af van wat je verandert. De training richt zich op de oorzaken: werkdruk, leiderschap en hoe je met herstel omgaat. Daarom meten we aan het begin waar je staat, zodat je later kunt zien wat er veranderd is.'),
    ('Wat is het verschil met een masterclass?', 'Een masterclass volg je alleen, met mensen uit andere organisaties. Deze training doe je met je eigen team, over je eigen verandering. Je gaat naar huis met een plan, niet alleen met kennis.'),
    ('Wat kost de training?', '%s per groep van %d tot %d deelnemers, exclusief btw en reiskosten. Dat is %s tot %s per deelnemer.' % (euro(PRIJS), MIN_GROEP, MAX_GROEP, euro(PP_LAAG), euro(PP_HOOG))),
]
vragen_html = '\n'.join('            <dt>%s</dt><dd>%s</dd>' % (v, a) for v, a in VRAGEN)

MAIN = f'''<main>
  <section class="sectie">
    <div class="wrap">
      <p class="kruimel"><a href="trainingen">Trainingen</a> <span aria-hidden="true">›</span> Cultuurverandering</p>
      <article class="aanbod vl-pagina" id="cultuurverandering">
        <div class="aanbod-kop">
          <h1>Training cultuurverandering</h1>
          <p class="vl-invalshoek">Van verzuim naar energie met het 8-stappenmodel van Kotter.</p>
          <p class="herken-regel"><strong>Herken je dit?</strong> Je bent een verandering begonnen en die blijft steken.</p>
          <p>In deze training cultuurverandering maakt je managementteam in vier dagdelen een eigen veranderplan. Bijvoorbeeld om vitaliteitsbeleid in te voeren, werkdruk aan te pakken of anders leiding te geven. We volgen de acht stappen van Kotter, twee per dagdeel. Tussen de dagdelen zet je de stappen in je eigen organisatie.</p>
        </div>
        <ul class="vl-zinnen">
          <li>Een verandering die niemand voelt, is geen verandering.</li>
          <li>Cultuur verander je met gedrag, niet met een memo.</li>
          <li>Begin klein. Laat zien dat het werkt. Bouw daarop voort.</li>
          <li>Een plan waar je team achter staat, loopt ook na de training door.</li>
        </ul>
        <div class="vl-vragen">
          <p class="vl-vragen-kop">Stel jezelf deze vragen</p>
          <ul>
            <li>Weet iedereen in je organisatie waarom het anders moet?</li>
            <li>Wie trekt de verandering als jij er niet bij bent?</li>
            <li>Welk succes kun je over drie maanden laten zien?</li>
            <li>Wat gebeurt er met je plan als de aandacht verschuift?</li>
          </ul>
          <p>Twijfel je bij een van deze vragen? Dan is deze training voor jou.</p>
        </div>
        <nav class="anker-menu" aria-label="Op deze pagina">
          <a href="#programma">Programma</a> <a href="#investering">Investering</a> <a href="#waarom-kotter">Waarom Kotter</a> <a href="#vragen">Veelgestelde vragen</a>
        </nav>
        <dl class="aanbod-feiten" id="investering">
          <div><dt>Voor wie</dt><dd>Directie, managementteams en leidinggevenden</dd></div>
          <div><dt>Opzet</dt><dd>Incompany, met je eigen team. Kennis, oefeningen en tussenopdrachten in de praktijk</dd></div>
          <div><dt>Resultaat</dt><dd>Een veranderplan waar het team achter staat en dat na de training doorloopt</dd></div>
          <div><dt>Duur</dt><dd>4 dagdelen</dd></div>
          <div><dt>Groepsgrootte</dt><dd>{MIN_GROEP} tot {MAX_GROEP} deelnemers</dd></div>
          <div><dt>Investering</dt><dd>{euro(PRIJS)} per groep<br>{euro(PP_LAAG)} tot {euro(PP_HOOG)} per deelnemer<br>Excl. btw en reiskosten<br>Zorg en onderwijs zonder btw-aftrek: {euro(INCL)} incl. btw</dd></div>
        </dl>
        <div class="aanbod-meer">
          <h2 id="programma">Programma: twee stappen per dagdeel</h2>
          <p>Elk dagdeel behandelt twee stappen van Kotter. Je past ze direct toe op jullie eigen verandering. Aan het begin meten we kort waar je staat, met de <a href="vitaliteitsmeter">vitaliteitsmeter</a> of jullie eigen cijfers.</p>
          <ol class="vl-dagdelen">
            <li><span class="sub">Dagdeel 1 | Stap 1 en 2</span><strong>Urgentie en een sterk kernteam</strong><span>Waarom moet het anders, en waarom nu? Je maakt zichtbaar wat verzuim en werkdruk kosten, in geld en in mensen. Daarna bepaal je wie de verandering samen met jou trekt.</span><span class="opdracht"><b>Tussenopdracht</b>Verzamel cijfers en verhalen uit je eigen team. Vraag twee of drie mensen voor het kernteam.</span></li>
            <li><span class="sub">Dagdeel 2 | Stap 3 en 4</span><strong>Een visie en het verhaal</strong><span>Wat wil je bereiken en hoe weet je dat het gelukt is? Je maakt de visie concreet met twee of drie meetbare doelen. En je oefent het verhaal, want het belangrijkste kanaal is je eigen gedrag.</span><span class="opdracht"><b>Tussenopdracht</b>Vertel het verhaal in je eigen team en haal de reacties op.</span></li>
            <li><span class="sub">Dagdeel 3 | Stap 5 en 6</span><strong>Obstakels weg en snelle successen</strong><span>Wat houdt de verandering tegen? Je leert weerstand te begrijpen en weg te nemen wat in de weg zit. Met het <a class="geen-breuk" href="tools#jdr-model">JD-R-model</a> zie je wat energie kost en wat energie geeft. Je kiest een eerste verbetering die binnen een paar maanden zichtbaar is.</span><span class="opdracht"><b>Tussenopdracht</b>Start de eerste verbetering met een team dat wil.</span></li>
            <li><span class="sub">Dagdeel 4 | Stap 7 en 8</span><strong>Doorzetten en verankeren</strong><span>We halen de oogst op. Wat werkte en wat niet? Je bepaalt hoe je de resultaten gebruikt om anderen mee te nemen. En je verankert de verandering in de gesprekscyclus, het inwerkprogramma en de rapportages.</span><span class="opdracht"><b>Na de training</b>Je hebt een veranderplan voor het komende jaar. Je kernteam voert het uit.</span></li>
          </ol>
          <h2 id="waarom-kotter">Waarom het 8-stappenmodel van Kotter?</h2>
          <p>Kotter ontwikkelde zijn model op basis van onderzoek naar veranderingen die wel en niet slaagden. Het is praktisch en een managementteam kan er direct mee aan de slag. Veel trainingen noemen Kotter naast andere modellen. In deze training bouwen we het hele programma eromheen, zodat je het echt leert gebruiken.</p>
          <p>Onderzoek ondersteunt de meeste afzonderlijke stappen. De vaste volgorde past niet altijd. Daarom gebruik ik het model als leidraad en niet als recept. Lees meer in <a href="artikelen/van-verzuim-naar-energie-kotter">Cultuurverandering met het 8-stappenmodel van Kotter</a>.</p>
          <h2>Wat deze training anders maakt</h2>
          <ul>
            <li><strong>Cultuurverandering en vitaliteit samen.</strong> We kijken naar werkdruk, herstel en leiderschap. Want daar loopt een verandering vaak op vast.</li>
            <li><strong>Met je eigen team.</strong> Geen open inschrijving met vreemden. Je werkt aan jullie eigen verandering.</li>
            <li><strong>Een vaste prijs per groep.</strong> Hoe groter de groep, hoe lager de prijs per deelnemer.</li>
            <li><strong>Het blijft niet bij praten.</strong> Na elk dagdeel zet je een stap in je eigen organisatie. In het volgende dagdeel bespreken we wat werkte.</li>
          </ul>
          <h2>Mijn rol en jouw rol</h2>
          <p>Ik heb twintig jaar teams geleid, vaak onder hoge druk. Ik inspireer je, geef je kennis en help je bij de verandering. Jij en je team bepalen wat er verandert en jullie doen het werk.</p>
          <h2 id="vragen">Veelgestelde vragen over de training cultuurverandering</h2>
          <dl class="vragen-kort">
{vragen_html}
          </dl>
          <p class="noot">Quotes van deelnemers volgen na de eerste groepen.</p>
        </div>
        <p class="klein wp-regel">Gratis whitepaper: <a href="whitepaper-vitaliteitsbeleid-opzetten">Vitaliteitsbeleid opzetten</a></p>
        <p class="klein">Meer achtergrond: <a href="artikelen/van-verzuim-naar-energie-kotter">Cultuurverandering met het 8-stappenmodel van Kotter</a>, <a href="artikelen/zes-bouwblokken-vitaliteitsbeleid">Zes bouwblokken voor vitaliteitsbeleid dat werkt</a>, <a href="cultuurverandering">alles over cultuurverandering</a> en <a href="tools#kotter">het 8-stappenmodel op de pagina Tools</a></p>
        <div class="hero-knoppen">
          <a class="knop" href="contact#offerte">Vraag een offerte aan</a>
          <a class="knop omlijnd" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Bespreek het in een gratis gesprek</a>
        </div>
      </article>
      <p class="klein vl-andere">Bekijk ook de <a href="trainingen">andere trainingen</a>, zoals <a href="training-vitaal-leiderschap">vitaal leiderschap</a> en <a href="trainingen#werkdruk">werkdruk verlagen</a>.</p>
    </div>
  </section>
</main>
'''

URL = 'https://waltermontenarie.com/training-cultuurverandering'
BESCHR = 'Training cultuurverandering voor managementteams: in vier dagdelen een eigen veranderplan met het 8-stappenmodel van Kotter. € 2.995 per groep.'
schoon = lambda t: html.unescape(re.sub(r'<[^>]+>', '', t))
LD = [
    {"@context": "https://schema.org", "@type": "Course", "name": "Training cultuurverandering", "description": BESCHR, "url": URL, "inLanguage": "nl",
     "educationalLevel": "Directie, managementteams en leidinggevenden",
     "about": ["cultuurverandering", "verandermanagement", "8-stappenmodel van Kotter", "weerstand", "vitaliteit", "werkdruk", "verzuim"],
     "provider": {"@type": "Person", "@id": "https://waltermontenarie.com/over-mij#walter", "name": "Walter Montenarie", "url": "https://waltermontenarie.com/over-mij"},
     "offers": [{"@type": "Offer", "name": "4 dagdelen, per groep", "price": str(PRIJS), "priceCurrency": "EUR", "category": "Paid", "url": URL}],
     "hasCourseInstance": [{"@type": "CourseInstance", "courseMode": "Onsite", "location": "Op locatie bij de opdrachtgever"}]},
    {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": v, "acceptedAnswer": {"@type": "Answer", "text": schoon(a)}} for v, a in VRAGEN]},
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://waltermontenarie.com/"},
        {"@type": "ListItem", "position": 2, "name": "Trainingen", "item": "https://waltermontenarie.com/trainingen"},
        {"@type": "ListItem", "position": 3, "name": "Training cultuurverandering", "item": URL}]},
]
maak_pagina('training-cultuurverandering', 'Training cultuurverandering met Kotter | Walter Montenarie', BESCHR,
            'Training cultuurverandering: van verzuim naar energie met Kotter', MAIN, LD=LD)
