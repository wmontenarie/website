# Bouwt het artikel over psychisch verzuim en de krapte op de arbeidsmarkt (onderzoek Acture, oktober 2026).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'psychisch-verzuim-krapte-arbeidsmarkt'
TITEL = 'Psychisch verzuim vergroot de krapte: wat je eraan doet'
H1 = 'Psychisch verzuim is het personeelstekort dat je zelf kunt verkleinen'
BESCHR = 'Verzuimdagen door psychische klachten stegen in drie jaar met 73 procent. In een krappe arbeidsmarkt is dat capaciteit die je niet terugkrijgt. Wat werkt.'

VRAGEN = [
 ('Hoeveel is het verzuim door psychische klachten gestegen?', 'Volgens een analyse van Acture van ruim 300.000 verzuimdossiers steeg het aantal verzuimdagen door psychische klachten tussen 2022 en 2025 met 73 procent. In 2025 ging het om ongeveer 4 procent van de verzuimgevallen, maar om bijna 22 procent van alle verzuimdagen.'),
 ('Hoe lang duurt verzuim door psychische klachten?', 'Volgens Acture verzuimden medewerkers met psychische klachten in 2025 gemiddeld 77 dagen, tegen 71 dagen in 2022. Bij burn-out ligt de duur volgens arbodiensten nog veel hoger, gemiddeld ruim 300 dagen.'),
 ('Wat heeft psychisch verzuim met de krapte op de arbeidsmarkt te maken?', 'Openstaande vacatures leggen meer werk bij de mensen die er wel zijn. Dat verhoogt de werkdruk en daarmee de kans op uitval. En wie uitvalt, is in een krappe arbeidsmarkt moeilijk te vervangen. Zo versterken krapte en verzuim elkaar.'),
 ('Wat kunnen werkgevers doen tegen psychisch verzuim?', 'Eerder signaleren en het gesprek voeren, leidinggevenden daarin trainen, de werkdruk samen met het team aanpakken en herstel een vaste plek geven in de werkweek. De meeste mensen die uitvallen met psychische klachten voelden het volgens Acture al maanden aankomen.'),
]
ICO = {
 'pijl': '<path d="M3 17l6-6 4 4 8-8"/><path d="M14 7h7v7"/>',
 'klok': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'kalender': '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
 'oog': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">26 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Organisaties steken veel tijd en geld in het vinden van nieuwe mensen. Vacatureteksten, recruiters, wervingsbonussen. Maar ondertussen loopt aan de andere kant van de organisatie capaciteit weg. Nieuw onderzoek laat zien hoe snel dat gaat: het verzuim door psychische klachten groeit hard. In een krappe arbeidsmarkt is dat werk dat blijft liggen, en mensen die je niet zomaar vervangt.</p>

      <h2>Wat het onderzoek laat zien</h2>
      <p>Verzuimspecialist Acture analyseerde ruim 300.000 verzuimdossiers uit de jaren 2022 tot en met 2025. Het totale aantal verzuimdagen daalde in 2025 licht. Maar het aantal verzuimdagen door psychische klachten steeg in een jaar met 7 procent, en in drie jaar met 73 procent.</p>
      <p>Psychisch verzuim komt niet het vaakst voor, maar duurt wel het langst. Het gaat om ongeveer 4 procent van de verzuimgevallen, maar om bijna 22 procent van alle verzuimdagen. Wie uitvalt met psychische klachten, was in 2025 gemiddeld 77 dagen afwezig. In 2022 was dat nog 71 dagen.</p>
      <figure class="infographic">
        <figcaption><strong>Psychisch verzuim in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_pijl)s<span class="getal">+73%%</span><span>meer verzuimdagen door psychische klachten tussen 2022 en 2025</span></div>
          <div>%(i_kalender)s<span class="getal">22%%</span><span>van alle verzuimdagen komt door psychische klachten</span></div>
          <div>%(i_klok)s<span class="getal">77 dagen</span><span>duurt psychisch verzuim gemiddeld, een week langer dan in 2022</span></div>
          <div>%(i_oog)s<span class="getal">1 op 3</span><span>verzuimdagen kan in 2030 psychisch zijn als de trend doorzet</span></div>
        </div>
        <p class="bron-regel">Bron: Acture, Toekomst zonder verzuim, 2026</p>
      </figure>
      <p>Acture rekende ook drie scenario's door tot 2030. Daarin stijgt het aantal psychische verzuimdagen met 27 tot 42 procent. In het middelste scenario is dan ongeveer een op de drie verzuimdagen psychisch. Acture noemt het nadrukkelijk scenario's en geen voorspelling. Maar de richting is duidelijk.</p>

      <h2>Krapte en verzuim versterken elkaar</h2>
      <p>Het is een vicieuze cirkel. Een vacature die lang openstaat, legt meer werk bij de collega's die er wel zijn. De werkdruk stijgt en de kans op uitval ook. Valt iemand uit, dan komt er weer meer werk bij de rest. En in de zorg, het onderwijs en de techniek, waar de krapte het grootst is, vind je geen vervanger.</p>
      <p>Uitzendbureau Randstad zag hetzelfde. Sinds 2022 steeg het aantal mensen dat niet werkt door ziekte of arbeidsongeschiktheid met 10 procent. Het aantal werkenden groeide in dezelfde tijd met 4 procent. Volgens Randstad is uitval daarmee een van de grootste problemen op de arbeidsmarkt.</p>
      <p>De les is eenvoudig: elke medewerker die je gezond aan het werk houdt, is een vacature die je niet hoeft te vullen. Behoud is de goedkoopste werving.</p>

      <h2>Het begint niet bij de ziekmelding</h2>
      <p>Het meest hoopgevende uit het onderzoek is misschien dit. Volgens Acture voelde ongeveer 70 procent van de mensen die zich ziek melden met psychische klachten het al maanden aankomen. Er was dus tijd om in te grijpen. Maar volgens Acture herkent maar een op de elf leidinggevenden het signaal en gaat daar ook echt het gesprek over aan.</p>
      <p>Daar zit de winst. Niet in een beter verzuimproces na de ziekmelding, maar in de maanden ervoor.</p>

      <h2>Wat je als organisatie kunt doen</h2>
      <figure class="infographic">
        <figcaption><strong>Vijf stappen om psychisch verzuim voor te zijn</strong></figcaption>
        <ol class="stappen">
          <li><strong>Leer leidinggevenden signalen zien</strong><p>Iemand die stiller wordt, vaker fouten maakt of juist steeds overwerkt. Leidinggevenden die weten waar ze op letten, zien het eerder.</p></li>
          <li><strong>Maak het gesprek gewoon</strong><p>Vraag in elk één-op-één gesprek hoe het echt gaat en wat energie kost. Niet pas als het misgaat, maar altijd.</p></li>
          <li><strong>Pak de werkdruk aan met het team</strong><p>Juist in een krappe arbeidsmarkt is de verleiding groot om meer werk bij dezelfde mensen te leggen. Bespreek samen wat kan vervallen, verschuiven of eenvoudiger.</p></li>
          <li><strong>Bouw herstel in</strong><p>Niet alleen in het weekend of op vakantie, maar elke werkdag. Pauzes, rustige blokken zonder vergaderingen en geen mail in de avond.</p></li>
          <li><strong>Meet en stuur bij</strong><p>Kijk niet alleen naar het verzuimpercentage, maar ook naar energie, werkdruk en bevlogenheid. Dan zie je de trend voordat hij in het verzuim zichtbaar wordt.</p></li>
        </ol>
      </figure>

      <h2>Van kostenpost naar strategie</h2>
      <p>Psychisch verzuim wordt vaak gezien als iets van HR en de arbodienst. Maar als een op de drie verzuimdagen psychisch wordt, en je die mensen niet kunt vervangen, is het een vraag voor de directie. Het gaat over continuïteit, productiviteit en of je je beloftes aan klanten kunt waarmaken. Een organisatie die investeert in leiderschap, werkdruk en herstel, wint twee keer: minder verzuim en een werkgever waar mensen willen blijven.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over psychisch verzuim en krapte</h2>
%(vragen)s
      </section>
%(deel)s
      <aside class="wp-tip" aria-label="Whitepaper">
        <img src="../img/whitepaper-businesscase-omslag.webp" width="560" height="793" alt="Omslag van de whitepaper De businesscase voor vitaliteit" loading="lazy">
        <div>
          <p class="podcast-label">Gratis whitepaper</p>
          <p class="podcast-titel">De businesscase voor vitaliteit</p>
          <p>Bereken wat verzuim je organisatie kost en laat zien wat investeren in vitaliteit oplevert.</p>
          <a class="knop" href="../whitepaper-businesscase-vitaliteit">Download de whitepaper</a>
        </div>
      </aside>

      <aside class="lees-ook" aria-label="Lees ook">
        <h2>Lees ook</h2>
        <ul>
          <li><a href="stress-bespreekbaar-maken">Stress bespreekbaar maken: het gesprek dat je vaker moet voeren</a></li>
          <li><a href="burn-out-voorkomen-in-je-team">Burn-out voorkomen in je team</a></li>
          <li><a href="gemiddeld-verzuim-is-niet-normaal">Gemiddeld verzuim is niet normaal</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Wat kost psychisch verzuim jouw organisatie?</h2>
        <p>Bereken het in een minuut met de verzuimrekentool. Of bespreek in een gratis gesprek van 30 minuten waar in jouw organisatie de winst ligt.</p>
        <div class="hero-knoppen">
          <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
          <a class="knop omlijnd" href="../tools#rekentool-kop">Naar de verzuimrekentool</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://acture.nl/inzichten/toekomst-zonder-verzuim/">Acture: Toekomst zonder verzuim (2026)</a></li>
          <li><a href="https://www.hrmorgen.nl/2026/10/psychisch-verzuim-groeit-door-terwijl-totaal-verzuim-daalt">HRMorgen: Psychisch verzuim groeit door, terwijl totaal verzuim daalt (2026)</a></li>
          <li><a href="https://wnl.tv/2026/10/07/psychisch-verzuim-loopt-op-maar-werkgevers-missen-signalen-slechts-een-op-de-elf-leidinggevenden-herkent-het">WNL: Psychisch verzuim loopt op, werkgevers missen signalen (2026)</a></li>
          <li><a href="https://www.accountant.nl/nieuws/2026/6/randstad-zorgen-over-meer-zieke-werknemers-door-burn-out/">Accountant.nl: Randstad bezorgd over meer zieke werknemers door burn-out (2026)</a></li>
          <li><a href="https://www.howdengroup.com/nl-nl/nieuws/ziekteverzuim-2024-lichte-daling-psychisch-verzuim-neemt-toe-howden">Howden: verzuimcijfers 2024 van ArboNed en HumanCapitalCare (2025)</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-26', uit=sys.argv[1] if len(sys.argv) > 1 else None)
