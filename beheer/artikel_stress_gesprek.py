# Bouwt het artikel over stress bespreekbaar maken als leidinggevende.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'stress-bespreekbaar-maken'
TITEL = 'Stress bespreekbaar maken: tips voor leidinggevenden'
H1 = 'Stress bespreekbaar maken: het gesprek dat je vaker moet voeren'
BESCHR = 'Meer dan een derde van de werknemers praat met de leidinggevende niet over mentale klachten. Zo maak je stress gewoon bespreekbaar, voordat iemand uitvalt.'

VRAGEN = [
 ('Hoe maak je stress bespreekbaar in je team?', 'Door er vaak en gewoon over te praten, niet alleen als het misgaat. Zet energie en werkdruk vast op de agenda van het werkoverleg, vraag in elk één-op-één gesprek hoe het echt gaat en vertel ook eens hoe het met jezelf gaat. Dan wordt het een normaal onderwerp in plaats van een probleem.'),
 ('Hoe begin je een gesprek over stress met een medewerker?', 'Kies een rustig moment en een plek waar niemand meeluistert. Stel een open vraag, zoals: hoe gaat het de laatste tijd? Blijft het antwoord oppervlakkig, benoem dan wat je ziet en vraag of de ander dat herkent. Luister zonder meteen met oplossingen te komen en spreek af wanneer je er opnieuw over praat.'),
 ('Hoe lang duurt verzuim door stress of burn-out?', 'Volgens cijfers van arbodiensten duurt verzuim door stress gemiddeld zo\'n 250 dagen en verzuim door burn-out ruim 300 dagen. Vroeg het gesprek aangaan helpt om het zover niet te laten komen.'),
 ('Wanneer is de Stress Awareness Week?', 'De internationale Stress Awareness Week van ISMA is in 2026 van maandag 2 tot en met vrijdag 6 november. Een week later volgt in Nederland de Week van de Werkstress, van 9 tot en met 13 november.'),
]
ICO = {
 'gesprek': '<path d="M21 12a8 8 0 0 1-11.5 7.2L4 21l1.8-5.5A8 8 0 1 1 21 12z"/>',
 'batterij': '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M5 10v4"/>',
 'les': '<path d="M3 7l9-4 9 4-9 4z"/><path d="M7 9v5c0 1.7 2.2 3 5 3s5-1.3 5-3V9"/>',
 'klok': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">26 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Hoe gaat het? Goed hoor. Druk, maar goed. Je kent het antwoord. En je weet ook dat het vaak niet het hele verhaal is. Van 2 tot en met 6 november is het de internationale Stress Awareness Week. Een week later volgt de Week van de Werkstress. Een goed moment om het gesprek over stress te voeren dat je eigenlijk vaker zou moeten voeren.</p>

      <h2>Waarom medewerkers zwijgen</h2>
      <p>Meer dan een derde van de Nederlandse werknemers brengt mentale gezondheid niet ter sprake in gesprekken met de leidinggevende. Dat bleek uit onderzoek van YouGov voor Indeed. Een kwart voelt zich niet gesteund door de werkgever. In eerder onderzoek van Tilburg University noemden medewerkers twee redenen om te zwijgen: schaamte en angst voor hun loopbaan.</p>
      <p>Tegelijk hebben steeds meer mensen klachten. In tien jaar steeg het aandeel werknemers met burn-outklachten van 13 naar 21 procent. Bij 25 tot 34 jarigen is het zelfs 28 procent.</p>
      <figure class="infographic">
        <figcaption><strong>Stress op het werk in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_gesprek)s<span class="getal">ruim 1 op 3</span><span>werknemers bespreekt mentale gezondheid niet met de leidinggevende</span></div>
          <div>%(i_batterij)s<span class="getal">21%%</span><span>van de werknemers heeft burn-outklachten</span></div>
          <div>%(i_les)s<span class="getal">27%%</span><span>van de leidinggevenden is getraind om signalen van burn-out te herkennen</span></div>
          <div>%(i_klok)s<span class="getal">40%%</span><span>van het langdurig verzuim komt door psychische klachten</span></div>
        </div>
        <p class="bron-regel">Bronnen: YouGov voor Indeed, 2023. TNO en CBS, NEA 2025. Robidus, 2026. AWVN, 2026</p>
      </figure>

      <h2>Ook leidinggevenden vinden het lastig</h2>
      <p>Het ligt niet alleen aan medewerkers. In een peiling onder ruim 500 werkgevers zei 38 procent dat hun leidinggevenden niet goed zijn toegerust om signalen van overbelasting te herkennen. Maar 27 procent van de leidinggevenden is daar structureel in getraind. Dus wachten veel leidinggevenden af tot de medewerker zelf iets zegt. En de medewerker wacht tot het niet meer gaat.</p>
      <p>Dat wachten is duur. Psychische klachten zijn inmiddels de oorzaak van 40 procent van het langdurig verzuim. Verzuim door stress duurt gemiddeld zo'n 250 dagen, door burn-out ruim 300 dagen. Wie eerder het gesprek aangaat, voorkomt vaak dat het zover komt.</p>

      <h2>Het gesprek in vijf stappen</h2>
      <figure class="infographic">
        <figcaption><strong>Zo voer je het gesprek over stress</strong></figcaption>
        <ol class="stappen">
          <li><strong>Kies het moment</strong><p>Niet tussen twee vergaderingen door. Kies een rustige plek waar niemand meeluistert, of maak samen een wandeling. Naast elkaar praat het vaak makkelijker.</p></li>
          <li><strong>Stel een open vraag</strong><p>Vraag: hoe gaat het de laatste tijd? Niet: ben je gestrest? Een open vraag geeft ruimte, een gesloten vraag een kort antwoord.</p></li>
          <li><strong>Benoem wat je ziet</strong><p>Blijft het bij goed hoor, beschrijf dan wat je opvalt. Je lijkt stiller dan anders, je werkt vaak 's avonds. Vraag of de ander dat herkent.</p></li>
          <li><strong>Luister zonder op te lossen</strong><p>De neiging is groot om meteen met tips te komen. Wacht daarmee. Vraag eerst wat energie kost en wat energie geeft.</p></li>
          <li><strong>Spreek samen iets af</strong><p>Een taak die even weg kan, andere uren, of een gesprek met de bedrijfsarts. Spreek af wanneer je erop terugkomt, en doe dat ook.</p></li>
        </ol>
      </figure>

      <h2>Maak het gewoon, niet groot</h2>
      <p>Het beste gesprek over stress is het gesprek dat je al voert voordat er iets aan de hand is. Vraag iedereen regelmatig: zit je nog goed op je plek? Wat heb je nodig om je werk goed te blijven doen? Zet energie en werkdruk vast op de agenda van het werkoverleg. En vertel zelf ook eens dat je een zware week had. Als de leidinggevende het durft, durft het team het ook.</p>
      <p>Twijfel je of iemand meer hulp nodig heeft? Je bent geen hulpverlener. Verwijs op tijd door naar de bedrijfsarts of een vertrouwenspersoon. Dat is geen afschuiven, maar goed leiderschap.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over stress bespreekbaar maken</h2>
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
          <li><a href="burn-out-voorkomen-in-je-team">Burn-out voorkomen in je team</a></li>
          <li><a href="mentale-gezondheid-werk-leidinggevende">Mentale gezondheid op het werk is ook jouw zaak</a></li>
          <li><a href="leidinggevende-voorbeeld-werkstress">Jij bent de thermostaat van je team</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Leidinggevenden leren het gesprek te voeren?</h2>
        <p>In de training verminder stress, verhoog bevlogenheid leert je team wat energie geeft en wat energie kost, en hoe je dat bespreekbaar maakt. Of bespreek eerst in een gratis gesprek van 30 minuten wat bij jullie past.</p>
        <div class="hero-knoppen">
          <a class="knop" href="../trainingen#bevlogenheid">Bekijk de training</a>
          <a class="knop omlijnd" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://isma.org.uk/isma-international-stress-awareness-week">ISMA: International Stress Awareness Week 2026</a></li>
          <li><a href="https://www.hrpraktijk.nl/medewerker/duurzame-inzetbaarheid/een-vijfde-van-de-werknemers-kampt-met-mentale-problemen-zo-maak-je-mentale-gezondheid-onderwerp-van-gesprek/">HR Praktijk: onderzoek van YouGov voor Indeed naar mentale gezondheid op het werk (2023)</a></li>
          <li><a href="https://www.hrpraktijk.nl/medewerker/duurzame-inzetbaarheid/kwart-nederlandse-werknemers-zou-psychische-problemen-niet-met-leidinggevende-bespreken/">HR Praktijk: onderzoek van Tilburg University naar psychische problemen bespreken (2020)</a></li>
          <li><a href="https://monitorarbeid.tno.nl/wp-content/uploads/sites/16/2026/04/Factsheet-NEA2025.pdf">TNO en CBS: Factsheet Nationale Enquête Arbeidsomstandigheden 2025</a></li>
          <li><a href="https://www.awvn.nl/arbeidsongeschiktheid/publicaties/psychische-klachten-werk-verzuim">AWVN: Psychische klachten, werk en verzuim (2026)</a></li>
          <li><a href="https://www.hrpraktijk.nl/medewerker/duurzame-inzetbaarheid/slechts-27-procent-leidinggevenden-getraind-in-herkennen-burn-outsignalen/">HR Praktijk: onderzoek van Robidus naar het herkennen van burn-outsignalen (2026)</a></li>
          <li><a href="https://www.howdengroup.com/nl-nl/nieuws/ziekteverzuim-2024-lichte-daling-psychisch-verzuim-neemt-toe-howden">Howden: verzuimcijfers 2024 van ArboNed en HumanCapitalCare (2025)</a></li>
          <li><a href="https://www.uwv.nl/nl/achtergrond/opinie-kijk-bij-mentale-klachten-ook-naar-iemands-omgeving">UWV: Kijk bij mentale klachten ook naar iemands omgeving (2026)</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-26', uit=sys.argv[1] if len(sys.argv) > 1 else None)
