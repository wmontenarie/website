# Bouwt het artikel over verzuim terugdringen op basis van een bestaand artikel als sjabloon.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'verzuim-terugdringen-maatregelen'
TITEL = 'Verzuim terugdringen: zeven maatregelen die werken'
H1 = 'Verzuim terugdringen: zeven maatregelen die werken'
BESCHR = 'Zo dring je verzuim terug. Zeven maatregelen op basis van onderzoek: van je cijfers kennen tot werkdruk, leidinggevenden en terugkeer naar werk.'

VRAGEN = [
 ('Hoe kun je verzuim terugdringen?', 'Door drie dingen samen aan te pakken: grip op je cijfers en het verzuimproces, het werk zelf en de rol van leidinggevenden. Losse maatregelen zoals strengere controle of een vitaliteitsprogramma doen alleen weinig.'),
 ('Wat is het gemiddelde ziekteverzuim in Nederland?', 'In 2025 was het ziekteverzuim 5,4 procent. In het eerste kwartaal van 2026 was het 5,8 procent. Dat is hoger dan het gemiddelde van de afgelopen dertig jaar. Bij organisaties met 100 of meer medewerkers was het in dat kwartaal 6,8 procent.'),
 ('Mag je als werkgever vragen waarom iemand ziek is?', 'Nee. Je mag niet vragen naar de aard of de oorzaak van de ziekte. Je mag wel vragen hoe lang het verzuim naar verwachting duurt, welke afspraken en werkzaamheden er lopen en hoe je de medewerker kunt bereiken. De medewerker vertelt de aard van de klachten aan de bedrijfsarts.'),
 ('Wat doet een leidinggevende bij verzuim?', 'Contact houden vanaf de eerste dag, praten over wat iemand nog wel kan en een patroon van vaak ziek zijn bespreken. Daarnaast kijkt een goede leidinggevende naar wat in het werk energie kost. Onderzoek laat zien dat de kwaliteit van leiderschap samenhangt met minder verzuim.'),
]
ICO = {
 'pct': '<path d="M19 5L5 19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
 'werk': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
 'druk': '<path d="M12 3a9 9 0 1 0 9 9"/><path d="M12 12l5-5"/><circle cx="12" cy="12" r="1.5"/>',
 'brein': '<path d="M9.5 3a3.5 3.5 0 0 0-3.4 4.3A3.5 3.5 0 0 0 5 14a3.5 3.5 0 0 0 4.5 6V3zM14.5 3a3.5 3.5 0 0 1 3.4 4.3A3.5 3.5 0 0 1 19 14a3.5 3.5 0 0 1-4.5 6V3z"/>',
 'gebouw': '<path d="M3 21h18M5 21V8l6-3v16M11 21V11l8 3v7M8 10v.01M8 14v.01M15 17v.01"/>',
 'kompas': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 'mens': '<circle cx="12" cy="7" r="4"/><path d="M4 21v-1a7 7 0 0 1 16 0v1"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">8 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Het ziekteverzuim in Nederland is hoger dan het gemiddelde van de afgelopen dertig jaar. Veel organisaties reageren met strengere controle of met een vitaliteitsprogramma. Allebei doen ze alleen weinig. Verzuim daalt pas als je drie dingen samen aanpakt: je cijfers en het verzuimproces, het werk zelf en de rol van leidinggevenden.</p>

      <h2>Hoe hoog is het verzuim nu?</h2>
      <p>Het ziekteverzuim was in 2025 gemiddeld 5,4 procent. In het eerste kwartaal van 2026 was het 5,8 procent. Bij organisaties met 100 of meer medewerkers was het in dat kwartaal 6,8 procent.</p>
      <p>Het meeste verzuim komt door griep en verkoudheid. Daar kun je als werkgever weinig aan doen. Maar bijna een kwart van de werknemers die verzuimden zegt dat het verzuim geheel of gedeeltelijk door het werk kwam. Werkdruk was daarbij de belangrijkste oorzaak. En psychische klachten zijn de oorzaak van vier op de tien gevallen van langdurig verzuim. Daar ligt je invloed.</p>
      <figure class="infographic">
        <figcaption><strong>Verzuim in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_pct)s<span class="getal">5,8%%</span><span>ziekteverzuim in het eerste kwartaal van 2026</span></div>
          <div>%(i_werk)s<span class="getal">23%%</span><span>van wie verzuimde zegt dat het werk een oorzaak was</span></div>
          <div>%(i_druk)s<span class="getal">28%%</span><span>van dat werkgerelateerde verzuim komt door werkdruk</span></div>
          <div>%(i_brein)s<span class="getal">4 op 10</span><span>gevallen van langdurig verzuim komt door psychische klachten</span></div>
        </div>
        <p class="bron-regel">Bronnen: CBS (2026), VZinfo (2023)</p>
      </figure>
      <p>Wat dat verzuim jouw organisatie kost bereken je met de <a href="../tools#rekentool-kop">verzuimrekentool</a>.</p>

      <h2>Zeven maatregelen</h2>
      <p>Dit zijn de zeven maatregelen. Daaronder licht ik ze toe.</p>
      <figure class="infographic">
        <figcaption><strong>Verzuim terugdringen in zeven maatregelen</strong></figcaption>
        <ol class="stappen">
          <li><strong>Ken je cijfers</strong><p>Niet alleen het percentage, ook hoe vaak, hoe lang en waar.</p></li>
          <li><strong>Houd contact vanaf dag één</strong><p>De leidinggevende belt en vraagt wat iemand nog wel kan.</p></li>
          <li><strong>Bespreek vaak verzuim</strong><p>Een gesprek over het patroon en niet over de ziekte.</p></li>
          <li><strong>Pak werkdruk aan bij de bron</strong><p>Met de RI&amp;E en met teams die zelf oorzaken benoemen.</p></li>
          <li><strong>Investeer in leidinggevenden</strong><p>Hun gedrag hangt samen met minder verzuim.</p></li>
          <li><strong>Maak de bedrijfsarts makkelijk bereikbaar</strong><p>Ook voordat iemand ziek is.</p></li>
          <li><strong>Pas het werk aan bij terugkeer</strong><p>Aangepast werk verkort het verzuim.</p></li>
        </ol>
      </figure>

      <h3>1. Ken je cijfers</h3>
      <p>Een verzuimpercentage zegt weinig over waar het verzuim zit. Kijk ook naar hoe vaak mensen zich ziek melden, hoe lang het verzuim duurt en het verschil tussen kort en lang verzuim. Vergelijk afdelingen en functies. Bijna de helft van de werknemers verzuimt een heel jaar niet. Het verzuim zit dus vaak bij een kleinere groep. Lees daarover meer in <a href="gemiddeld-verzuim-is-niet-normaal">Gemiddeld verzuim is niet normaal</a>.</p>

      <h3>2. Houd contact vanaf dag één</h3>
      <p>Het eerste contact bepaalt veel. Laat de leidinggevende bellen en niet alleen HR of de arbodienst. Vraag hoe het gaat, hoe lang het verzuim naar verwachting duurt en wat er aan werk ligt. Vraag niet naar de aard of de oorzaak van de ziekte. Dat mag niet. De medewerker bespreekt zijn klachten met de bedrijfsarts.</p>
      <p>Duurt het verzuim langer, dan gelden de stappen van de Wet verbetering poortwachter. Rond week 6 maakt de bedrijfsarts een probleemanalyse. Uiterlijk in week 8 maak je samen met de medewerker een plan van aanpak.</p>

      <h3>3. Bespreek vaak verzuim</h3>
      <p>Meldt iemand zich vaak kort ziek, bespreek dan het patroon. Het gaat niet om de ziekte maar om wat er speelt. Soms zit de oorzaak in het werk, soms thuis en soms in de combinatie. Een open gesprek helpt meer dan een waarschuwing.</p>

      <h3>4. Pak werkdruk aan bij de bron</h3>
      <p>Werkdruk is de belangrijkste oorzaak van werkgerelateerd verzuim. Elke werkgever moet een risico-inventarisatie en -evaluatie (RI&amp;E) hebben en daarin hoort ook psychosociale arbeidsbelasting, zoals werkdruk. Bij de RI&amp;E hoort een plan van aanpak. Pak een risico eerst bij de bron aan.</p>
      <p>Een RI&amp;E alleen is niet genoeg. Laat teams zelf benoemen waar de druk vandaan komt en wat ze kunnen schrappen of anders doen. Hoe dat gaat lees je in <a href="moet-je-je-druk-maken-over-werkdruk">Moet je je druk maken over werkdruk?</a></p>

      <h3>5. Investeer in leidinggevenden</h3>
      <p>Een overzicht van 27 studies vond dat goed leiderschap samengaat met 27 procent minder ziekteverzuim en 46 procent minder arbeidsongeschiktheid. In een Deens onderzoek onder ruim 53.000 werknemers hadden medewerkers die hun leidinggevende het laagst beoordeelden ongeveer 60 procent meer kans op verzuim van zes weken of langer.</p>
      <p>Leidinggevenden hoeven geen hulpverlener te zijn. Ze moeten signalen herkennen, het gesprek durven voeren en weten wat in het werk energie kost. Dat kun je leren. Lees ook <a href="burn-out-voorkomen-in-je-team">Burn-out voorkomen in je team</a>.</p>

      <h3>6. Maak de bedrijfsarts makkelijk bereikbaar</h3>
      <p>Medewerkers mogen de bedrijfsarts bezoeken voordat ze ziek zijn, ook zonder toestemming van hun werkgever. Je moet als werkgever die mogelijkheid bieden, bijvoorbeeld met een open spreekuur. Vertel medewerkers dat het spreekuur er is en dat het vertrouwelijk is. Zo kan iemand met klachten op tijd hulp vragen.</p>

      <h3>7. Pas het werk aan bij terugkeer</h3>
      <p>Een Cochrane-overzicht van 14 gerandomiseerde studies laat zien dat aanpassingen op de werkplek het totale verzuim verminderen. Medewerkers keren ook eerder terug. Het sterkste bewijs is er bij klachten aan spieren en gewrichten. Bij psychische klachten keerden mensen eerder terug, maar bleef de terugkeer niet altijd blijvend. Bouw daarom rustig op en blijf in gesprek.</p>
      <p>Denk aan andere taken, minder uren, een andere werkplek of meer regelruimte. Bespreek met de medewerker en de bedrijfsarts wat helpt.</p>

      <h2>Wat weinig oplevert</h2>
      <ul>
        <li><strong>Alleen strenger controleren.</strong> Het lost de oorzaak niet op. Mensen gaan ziek of uitgeput aan het werk. Dat heet presenteïsme. Onderzoek wijst erop dat het productiviteitsverlies daardoor minstens zo groot is als door verzuim. Lees meer in <a href="presenteisme-onbekende-productiviteitskiller">het artikel over presenteïsme</a>.</li>
        <li><strong>Een los vitaliteitsprogramma.</strong> In een Amerikaans experiment kregen bijna 33.000 medewerkers door loting wel of geen programma. Na anderhalf jaar was er geen verschil in verzuim. Een programma werkt alleen als het werk en het leiderschap meeveranderen.</li>
        <li><strong>Sturen op het gemiddelde.</strong> Een gemiddeld verzuimcijfer verbergt de teams waar het misgaat.</li>
      </ul>

      <h2>Van maatregelen naar beleid</h2>
      <p>Zeven losse maatregelen worden pas een aanpak als ze samenhangen en als je ze volhoudt. Begin met een meting. Met de gratis <a href="../vitaliteitsmeter">vitaliteitsmeter</a> zie je in vijf minuten waar je organisatie staat. Wil je de directie overtuigen, maak dan een <a href="businesscase-vitaliteit-maken">businesscase</a>. Hoe je de verandering in de cultuur verankert lees je in <a href="van-verzuim-naar-energie-kotter">Cultuurverandering met het 8-stappenmodel van Kotter</a>.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over verzuim terugdringen</h2>
%(vragen)s
      </section>
%(deel)s
      <aside class="wp-tip" aria-label="Whitepaper">
        <img src="../img/whitepaper-burn-out-omslag.webp" width="560" height="793" alt="Omslag van de whitepaper Burn-out signaleren" loading="lazy">
        <div>
          <p class="podcast-label">Gratis whitepaper</p>
          <p class="podcast-titel">Burn-out signaleren</p>
          <p>Voor leidinggevenden: signalen herkennen, het gesprek voeren en weten wat je wel en niet doet.</p>
          <a class="knop" href="../whitepaper-burn-out-signaleren">Download de whitepaper</a>
        </div>
      </aside>

      <aside class="lees-ook" aria-label="Lees ook">
        <h2>Lees ook</h2>
        <ul>
          <li><a href="gemiddeld-verzuim-is-niet-normaal">Gemiddeld verzuim is niet normaal</a></li>
          <li><a href="businesscase-vitaliteit-maken">Businesscase vitaliteit maken in vijf stappen</a></li>
          <li><a href="van-verzuim-naar-energie-kotter">Cultuurverandering met het 8-stappenmodel van Kotter</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Wil je het verzuim in jouw organisatie terugdringen?</h2>
        <p>In een gratis gesprek van 30 minuten kijken we naar je cijfers en naar waar de winst ligt. Of begin met een training werkdruk verlagen voor je teams.</p>
        <div class="hero-knoppen">
          <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
          <a class="knop omlijnd" href="../trainingen#werkdruk">Bekijk de training</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://www.cbs.nl/nl-nl/nieuws/2026/23/ziekteverzuim-in-eerste-kwartaal-hoger-dan-gemiddeld-in-afgelopen-30-jaar">CBS: Ziekteverzuim in eerste kwartaal hoger dan gemiddeld in afgelopen 30 jaar (2026)</a></li>
          <li><a href="https://www.awvn.nl/arbeidsongeschiktheid/publicaties/psychische-klachten-werk-verzuim/">AWVN: Het groeiende probleem van psychische klachten (2026), met cijfers van VZinfo</a></li>
          <li><a href="https://www.voion.nl/media/ytupsdnx/nea-2023-resultaten-in-vogelvlucht-alle-sectoren-tno-2024.pdf">TNO: Nationale Enquête Arbeidsomstandigheden 2023 (2024)</a></li>
          <li><a href="https://www.awvn.nl/privacy/hr-van-a-tot-z/privacy-zieke-werknemers/">AWVN: Privacy zieke werknemers</a></li>
          <li><a href="https://www.uwv.nl/nl/ervaringsverhalen/stappenplan-wet-verbetering-poortwachter">UWV: Stappenplan Wet verbetering poortwachter</a></li>
          <li><a href="https://www.awvn.nl/arbeidsongeschiktheid/hr-van-a-tot-z/risico-inventarisatie-en-evaluatie-rie/">AWVN: Risico-inventarisatie en -evaluatie (RI&amp;E)</a></li>
          <li><a href="https://www.ehstoday.com/safety/article/21904368/leaderships-effects-on-employee-health-well-being">Kuoppala en collega's: Leadership, job well-being and health effects, Journal of Occupational and Environmental Medicine (2008)</a></li>
          <li><a href="https://acoem.org/Press-Center/Low-Leadership-Quality-Predicts-High-Risk-of-Long-Term-Sickness-Absence">Sørensen en collega's: Leadership quality and risk of long-term sickness absence, Journal of Occupational and Environmental Medicine (2020)</a></li>
          <li><a href="https://www.dirkzwager.nl/kennis/artikelen/wijzigingen-arbowet-grote-re-rol-voor-de-bedrijfsarts">Dirkzwager: Wijzigingen Arbowet, grotere rol voor de bedrijfsarts</a></li>
          <li><a href="https://www.cochrane.org/evidence/CD006955_changes-workplace-preventing-disability-workers-sick-leave">Van Vilsteren en collega's: Workplace interventions to prevent work disability, Cochrane (2015)</a></li>
          <li><a href="https://jamanetwork.com/journals/jama/fullarticle/2730614">Song en Baicker: Effect of a workplace wellness program on employee health and economic outcomes, JAMA (2019)</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-08', uit=sys.argv[1] if len(sys.argv) > 1 else None)
