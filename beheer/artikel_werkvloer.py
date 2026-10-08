# Bouwt het artikel over vitaliteit op de werkvloer op basis van een bestaand artikel als sjabloon.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'vitaliteit-op-de-werkvloer'
TITEL = 'Vitaliteit op de werkvloer: wat werkt en tien tips'
H1 = 'Vitaliteit op de werkvloer: wat werkt en tien tips'
BESCHR = 'Vitaliteit op de werkvloer is meer dan fruit en een sportweek. Wat volgens onderzoek werkt, en tien tips voor werkgevers en leidinggevenden.'

VRAGEN = [
 ('Wat is vitaliteit op de werkvloer?', 'De energie, veerkracht en motivatie waarmee mensen hun werk doen. Die hangt af van het werk zelf, van de leidinggevende en van de leefstijl van de medewerker.'),
 ('Hoe verbeter je vitaliteit op de werkvloer?', 'Begin bij het werk: vraag teams waar energie weglekt en pak dat aan. Zorg dat leidinggevenden het goede voorbeeld geven en regelruimte bieden. Een leefstijlaanbod helpt als aanvulling, niet als oplossing.'),
 ('Werkt een vitaliteitsprogramma?', 'Een los programma naast het werk levert weinig op. In een Amerikaans experiment met bijna 33.000 medewerkers was na anderhalf jaar geen verschil in verzuim. Een Brits onderzoek onder ruim 46.000 werknemers vond geen verbetering van het welzijn door individuele programma\'s zoals mindfulness en veerkrachttraining.'),
 ('Wat kan een leidinggevende doen voor vitaliteit?', 'Het goede voorbeeld geven, in elk werkoverleg vragen wat energie kost en wat energie geeft, en mensen ruimte geven om zelf te bepalen hoe ze hun werk doen.'),
]
ICO = {
 'batterij': '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M5 10v4"/>',
 'druk': '<path d="M12 3a9 9 0 1 0 9 9"/><path d="M12 12l5-5"/><circle cx="12" cy="12" r="1.5"/>',
 'slot': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 'stoel': '<path d="M7 3v9h10M7 12v9M17 12v9M5 12h14"/>',
 'gebouw': '<path d="M3 21h18M5 21V8l6-3v16M11 21V11l8 3v7M8 10v.01M8 14v.01M15 17v.01"/>',
 'kompas': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 'mens': '<circle cx="12" cy="7" r="4"/><path d="M4 21v-1a7 7 0 0 1 16 0v1"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">8 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Fruit op tafel, een fietsplan, een vitaliteitsweek. Het is goed bedoeld en mensen waarderen het. Maar vitaliteit op de werkvloer ontstaat vooral in het werk zelf. In hoe druk het is, hoeveel ruimte mensen hebben en hoe de leidinggevende het voorbeeld geeft. Wat werkt er volgens onderzoek, en wat kun je morgen doen?</p>

      <h2>Wat is vitaliteit op de werkvloer?</h2>
      <p>Vitaliteit op de werkvloer gaat over de energie, veerkracht en motivatie waarmee mensen hun werk doen. Een vitale medewerker begint met zin aan de dag, kan tegen een stootje en herstelt na een drukke periode.</p>
      <p>Die energie komt uit drie bronnen. Het werk zelf: hoeveel er moet, hoe snel en met hoeveel ruimte. De leidinggevende: wat die voorleeft en waar die aandacht voor heeft. En de medewerker: slaap, bewegen, voeding en omgaan met stress. Wie alleen aan de laatste bron werkt, laat de eerste twee liggen.</p>

      <h2>Hoe vitaal is de werkvloer nu?</h2>
      <p>De cijfers van de Nationale Enquête Arbeidsomstandigheden laten zien waar de energie weglekt.</p>
      <figure class="infographic">
        <figcaption><strong>De werkvloer in vier cijfers</strong> Werknemers in Nederland, 2025</figcaption>
        <div class="kerncijfers">
          <div>%(i_batterij)s<span class="getal">21%%</span><span>heeft burn-outklachten</span></div>
          <div>%(i_druk)s<span class="getal">31%%</span><span>heeft te maken met hoge taakeisen</span></div>
          <div>%(i_slot)s<span class="getal">43%%</span><span>heeft weinig zeggenschap over het eigen werk</span></div>
          <div>%(i_stoel)s<span class="getal">21%%</span><span>zit acht uur of meer per dag</span></div>
        </div>
        <p class="bron-regel">Bron: TNO en CBS, Nationale Enquête Arbeidsomstandigheden 2025</p>
      </figure>
      <p>Daar komt bij dat maar 44 procent van de volwassenen genoeg beweegt volgens de beweegrichtlijn. Die vraagt 150 minuten matig intensief bewegen per week, verspreid over de week.</p>

      <h2>Wat werkt en wat niet?</h2>
      <p>Onderzoek is daar vrij duidelijk over. Losse programma's voor de medewerker leveren weinig op.</p>
      <ul>
        <li><strong>Individuele programma's.</strong> Een onderzoek van de Universiteit van Oxford onder ruim 46.000 werknemers bij 233 Britse organisaties vond geen verbetering van het welzijn door mindfulness, veerkrachttraining, stressmanagement, ontspanningslessen of welzijnsapps.</li>
        <li><strong>Een los vitaliteitsprogramma.</strong> In een Amerikaans experiment kregen bijna 33.000 medewerkers door loting wel of geen programma. Na anderhalf jaar zeiden deelnemers gezonder te leven. In verzuim, zorgkosten en gemeten gezondheid was geen verschil.</li>
      </ul>
      <p>Wat wel helpt, zit dichter bij het werk:</p>
      <ul>
        <li><strong>Korte pauzes.</strong> Een overzicht van 22 onderzoeken laat zien dat korte pauzes tot tien minuten samengaan met meer energie en minder vermoeidheid.</li>
        <li><strong>Minder zitten.</strong> Medewerkers met een zit-sta-bureau zaten 84 tot 116 minuten per werkdag minder dan collega's met een gewoon bureau. Het bewijs is nog zwak.</li>
        <li><strong>Goed leiderschap.</strong> Een overzicht van 27 studies vond dat goed leiderschap samengaat met 27 procent minder ziekteverzuim.</li>
      </ul>
      <p>De les is niet dat leefstijl er niet toe doet. De les is dat een aanbod voor de medewerker weinig verandert als het werk en het leiderschap hetzelfde blijven. In <a href="https://www.hr2day.com/nieuws/vitaliteit-op-de-werkvloer-vraagt-meer-dan-een-fruitschaal-en-een-welzijnsweek/" target="_blank" rel="noopener">de podcast van HR2day</a> vertelde ik daar meer over.</p>

      <h2>Tien tips voor vitaliteit op de werkvloer</h2>
      <p>De tips zijn verdeeld over de drie bronnen van energie.</p>
      <figure class="infographic">
        <figcaption><strong>Tien tips</strong> Op drie niveaus</figcaption>
        <div class="kenmerken">
          <div>%(i_gebouw)s<strong>Organisatie</strong><span>Tip 1 tot en met 5</span></div>
          <div>%(i_kompas)s<strong>Leiding&shy;gevende</strong><span>Tip 6 tot en met 8</span></div>
          <div>%(i_mens)s<strong>Medewerker</strong><span>Tip 9 en 10</span></div>
        </div>
      </figure>

      <h3>Organisatie</h3>
      <ol>
        <li><strong>Vraag teams waar energie weglekt.</strong> Wat kost energie en wat geeft energie? De antwoorden zijn je agenda.</li>
        <li><strong>Schrap iets.</strong> Elk team kiest één overleg, rapportage of regel die kan stoppen of korter kan.</li>
        <li><strong>Maak pauzes normaal.</strong> Plan geen vergaderingen van een uur achter elkaar. Laat ze vijf of tien minuten eerder eindigen.</li>
        <li><strong>Maak staan en bewegen makkelijk.</strong> Zit-sta-bureaus, wandeloverleg, een trap die je wilt nemen. Dan hoeft niemand daar apart tijd voor te maken.</li>
        <li><strong>Meet waar je staat.</strong> Begin met een meting, dan weet je later wat het heeft opgeleverd. Met de gratis <a href="../vitaliteitsmeter">vitaliteitsmeter</a> heb je in vijf minuten een eerste beeld.</li>
      </ol>
      <h3>Leidinggevende</h3>
      <ol start="6">
        <li><strong>Geef het goede voorbeeld.</strong> Een leidinggevende die zelf pauze neemt en 's avonds niet mailt, maakt het voor het team normaal.</li>
        <li><strong>Vraag naar energie.</strong> Maak het een vaste vraag in het werkoverleg en in het één-op-één gesprek. Vroege signalen herken je zo eerder.</li>
        <li><strong>Geef regelruimte.</strong> Laat mensen zelf bepalen hoe ze hun werk doen en wanneer. Bijna de helft heeft daar nu te weinig ruimte voor.</li>
      </ol>
      <h3>Medewerker</h3>
      <ol start="9">
        <li><strong>Bied leefstijl aan als aanvulling.</strong> Een inspiratiesessie over slaap, bewegen of stress helpt mensen op weg. Maar het is een aanvulling op tip 1 tot en met 8, geen vervanging.</li>
        <li><strong>Laat medewerkers meedenken.</strong> Vraag wat zij nodig hebben. Zij weten het best waar het knelt.</li>
      </ol>

      <h2>Van tips naar beleid</h2>
      <p>Tien tips zijn een begin. Ze worden pas beleid als ze samenhangen, een doel hebben en iemand er eigenaar van is. Hoe je dat aanpakt lees je in <a href="vitaliteitsbeleid-opzetten-stappenplan">Vitaliteitsbeleid opzetten: stappenplan en voorbeeld</a>. Welke onderdelen er volgens onderzoek in horen lees je in <a href="zes-bouwblokken-vitaliteitsbeleid">Vitaliteitsbeleid: zes bouwblokken die werken</a>.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over vitaliteit op de werkvloer</h2>
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
          <li><a href="vitaliteitsbeleid-opzetten-stappenplan">Vitaliteitsbeleid opzetten: stappenplan en voorbeeld</a></li>
          <li><a href="moet-je-je-druk-maken-over-werkdruk">Moet je je druk maken over werkdruk?</a></li>
          <li><a href="verzuim-terugdringen-maatregelen">Verzuim terugdringen: zeven maatregelen die werken</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Meer vitaliteit op jouw werkvloer?</h2>
        <p>Begin met een inspiratiesessie van een uur voor je medewerkers, of met de training werkdruk verlagen voor je teams. Of bespreek eerst in een gratis gesprek van 30 minuten waar de winst ligt.</p>
        <div class="hero-knoppen">
          <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
          <a class="knop omlijnd" href="../trainingen#workshops">Bekijk de inspiratiesessies</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://monitorarbeid.tno.nl/wp-content/uploads/sites/16/2026/04/Factsheet-NEA2025.pdf">TNO en CBS: Factsheet Nationale Enquête Arbeidsomstandigheden 2025 (2026)</a></li>
          <li><a href="https://www.rivm.nl/nieuws/deel-nederlanders-beweegt-voldoende-maar-te-weinig-verspreid-over-week">RIVM: Deel Nederlanders beweegt voldoende maar te weinig verspreid over week (2024)</a></li>
          <li><a href="https://wellbeing.hmc.ox.ac.uk/news/more-ambition-needed-to-improve-workplace-wellbeing/">Fleming: Employee well-being outcomes from individual-level mental health interventions, Industrial Relations Journal (2024)</a></li>
          <li><a href="https://jamanetwork.com/journals/jama/fullarticle/2730614">Song en Baicker: Effect of a workplace wellness program on employee health and economic outcomes, JAMA (2019)</a></li>
          <li><a href="https://journals.plos.org/plosone/article?id=10.1371%%2Fjournal.pone.0272460">Albulescu en collega's: Give me a break! A systematic review and meta-analysis on the efficacy of micro-breaks, PLOS ONE (2022)</a></li>
          <li><a href="https://www.cochrane.org/about-us/news/featured-review-workplace-interventions-reducing-time-spent-sitting-work">Shrestha en collega's: Workplace interventions for reducing sitting at work, Cochrane (2018)</a></li>
          <li><a href="https://www.ehstoday.com/safety/article/21904368/leaderships-effects-on-employee-health-well-being">Kuoppala en collega's: Leadership, job well-being and health effects, Journal of Occupational and Environmental Medicine (2008)</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-08', uit=sys.argv[1] if len(sys.argv) > 1 else None)
