# Bouwt het artikel over volhouden na de Week van de Werkstress.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'werkstress-aanpakken-na-de-week'
TITEL = 'Na de Week van de Werkstress: hoe hou je het vol?'
H1 = 'Na de Week van de Werkstress: hoe hou je het vol?'
BESCHR = 'Een week aandacht voor werkstress is een goed begin. Zo maak je er een vaste gewoonte van, met je team en in het werk zelf.'

VRAGEN = [
 ('Wanneer is de Week van de Werkstress 2026?', 'Van maandag 9 tot en met vrijdag 13 november 2026. De rode draad dit jaar is verbinding.'),
 ('Waarom werkt een losse actie tegen werkstress niet?', 'Omdat de oorzaken meestal in het werk zitten en blijven bestaan als de week voorbij is. Een groot Brits onderzoek onder ruim 46.000 werknemers vond geen verbetering van het welzijn door individuele programma\'s zoals mindfulness of veerkrachttraining. Aanpakken die het werk veranderen zijn kansrijker.'),
 ('Hoe lang duurt het voordat iets een gewoonte is?', 'In een bekend onderzoek duurde het gemiddeld 66 dagen voordat een nieuw gedrag vanzelf ging. Bij sommige mensen was dat 18 dagen, bij anderen naar schatting 254. Eén keer overslaan maakte weinig uit. Reken dus op een paar maanden volhouden.'),
 ('Moet werkstress in de RI&amp;E?', 'Ja. Psychosociale arbeidsbelasting, waaronder werkdruk, hoort in de risico-inventarisatie en -evaluatie. Maatregelen om werkdruk te voorkomen horen in het plan van aanpak. Medewerkers moeten weten welke risico\'s er zijn en wat eraan wordt gedaan.'),
]
ICO = {
 'pct': '<path d="M19 5L5 19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
 'batterij': '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M5 10v4"/>',
 'kalender': '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
 'euro': '<path d="M17 6.5A7 7 0 1 0 17 17.5"/><path d="M4 10h9M4 14h9"/>',
 'herhaal': '<path d="M4 12a8 8 0 0 1 14-5.3L20 9M20 4v5h-5M20 12a8 8 0 0 1-14 5.3L4 15M4 20v-5h5"/>',
 'team': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 5.2a3 3 0 0 1 0 5.6M18 14.3c1.8.9 3 2.7 3 5.7"/>',
 'werk': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">17 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Van 9 tot en met 13 november is de Week van de Werkstress. Veel organisaties doen mee met een workshop, een lunch of een gesprek in het team. Dat is goed. Maar op maandag 16 november is het werk nog net zo vol als ervoor. Hoe zorg je dat de aandacht niet wegzakt? Dit artikel gaat over de weken na de week.</p>

      <h2>Waarom het na een week wegzakt</h2>
      <p>Werkstress ontstaat meestal in het werk zelf. Te veel taken, te weinig tijd, weinig ruimte om zelf te kiezen, onduidelijke prioriteiten. Die oorzaken zijn er na de themaweek nog steeds. Een week aandacht verandert daar weinig aan als er daarna niets volgt.</p>
      <figure class="infographic">
        <figcaption><strong>Werkstress in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_batterij)s<span class="getal">20%%</span><span>van de werknemers heeft burn-outklachten</span></div>
          <div>%(i_pct)s<span class="getal">38%%</span><span>van de werknemers vindt extra maatregelen tegen werkstress nodig</span></div>
          <div>%(i_kalender)s<span class="getal">14,3 mln</span><span>verzuimdagen per jaar door werkdruk en andere psychosociale belasting</span></div>
          <div>%(i_euro)s<span class="getal">&euro;4,9 mld</span><span>aan verzuimkosten per jaar voor werkgevers</span></div>
        </div>
        <p class="bron-regel">Bron: TNO, factsheet werkstress 2025 (cijfers over 2023 en 2024)</p>
      </figure>
      <p>Daar komt bij dat losse acties voor de medewerker weinig opleveren. Een onderzoek van de Universiteit van Oxford onder ruim 46.000 werknemers vond geen verbetering van het welzijn door individuele programma's zoals mindfulness en veerkrachttraining. De onderzoeker vatte het zo samen: organisaties moeten de werkplek veranderen, niet alleen de werknemer.</p>

      <h2>Wat wel werkt</h2>
      <p>Drie dingen komen in onderzoek steeds terug.</p>
      <ul>
        <li><strong>Pak het werk aan.</strong> Een overzicht van 39 studies vond dat ongeveer de helft van de aanpakken in de organisatie effect had op de gezondheid. Aanpakken die tegelijk het werk, de organisatie en de werktijden veranderden, waren kansrijker.</li>
        <li><strong>Doe het samen met het team.</strong> In een Nederlands onderzoek op 29 afdelingen oncologie werkten teams in een reeks bijeenkomsten zelf aan wat stress gaf. Medewerkers waren daarna minder emotioneel uitgeput, en dat was na zes maanden nog zo. Een Deens onderzoek bij de post liet zien dat vooral meedoen als team telt, meer dan de inzet van één persoon.</li>
        <li><strong>Houd een vast ritme aan.</strong> Een nieuwe gewoonte heeft tijd nodig. In een bekend onderzoek duurde het gemiddeld 66 dagen voordat nieuw gedrag vanzelf ging. Eén keer overslaan maakte weinig uit. Vaak overslaan wel.</li>
      </ul>

      <h2>Zo hou je het vol: een plan voor de eerste 66 dagen</h2>
      <p>Gebruik de themaweek als start, niet als hoogtepunt. Dit plan past in een gewone werkweek.</p>
      <figure class="infographic">
        <figcaption><strong>Van één week naar een vaste gewoonte</strong></figcaption>
        <ol class="stappen">
          <li><strong>Kies één thema uit de week</strong><p>Wat kwam in de Week van de Werkstress het vaakst terug? Te veel vergaderingen, onduidelijke prioriteiten, altijd bereikbaar zijn? Kies er één.</p></li>
          <li><strong>Laat het team zelf de oplossing bedenken</strong><p>Zij weten waar het knelt. Spreek één concrete afspraak af die direct kan ingaan.</p></li>
          <li><strong>Schrap iets</strong><p>Een overleg, een rapportage, een regel. Nieuwe afspraken werken beter als er ook iets af gaat.</p></li>
          <li><strong>Maak er een vast agendapunt van</strong><p>Vraag elke twee weken in het werkoverleg: hoe staat het met de werkdruk, en houden we ons aan de afspraak? Vijf minuten is genoeg.</p></li>
          <li><strong>Meet drie keer</strong><p>Bij de start, na zes weken en na drie maanden. Een simpele vraag volstaat: hoe druk was het, van 1 tot 10, en wat hielp?</p></li>
          <li><strong>Leg het vast</strong><p>Zet de afspraken in het plan van aanpak van de RI&amp;E. Dan blijven ze bestaan, ook als het team of de leidinggevende wisselt.</p></li>
        </ol>
      </figure>

      <h2>Jouw rol als leidinggevende</h2>
      <p>Een gewoonte in een team staat of valt met de leidinggevende. Vraag zelf naar de afspraak als niemand het doet. Houd je er zelf ook aan. En geef het niet op als het een keer misgaat. Eén keer overslaan is geen probleem, zolang je de volgende keer weer oppakt.</p>
      <figure class="infographic">
        <figcaption><strong>Drie vaste momenten</strong></figcaption>
        <div class="kenmerken">
          <div>%(i_herhaal)s<strong>Elke twee weken</strong><span>Vijf minuten werkdruk in het werkoverleg</span></div>
          <div>%(i_team)s<strong>Na zes weken</strong><span>Samen terugkijken: wat werkt en wat niet?</span></div>
          <div>%(i_werk)s<strong>Na drie maanden</strong><span>Afspraken vastleggen en een nieuw thema kiezen</span></div>
        </div>
      </figure>

      <h2>Wat zegt de wet?</h2>
      <p>Werkdruk valt in de Arbowet onder psychosociale arbeidsbelasting. De werkgever moet die risico's in de RI&amp;E opnemen en maatregelen in het plan van aanpak zetten. Volgens TNO heeft 64 procent van de werkgevers een RI&amp;E en heeft 78 procent daarvan een plan van aanpak. Een themaweek is dus ook een goed moment om te kijken of werkdruk daar al in staat.</p>

      <p>Zoek je nog ideeën voor de week zelf? Lees dan <a href="week-zonder-werkstress-ideeen">Week van de Werkstress 2026: ideeën voor je team</a>.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over werkstress aanpakken</h2>
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
          <li><a href="moet-je-je-druk-maken-over-werkdruk">Moet je je druk maken over werkdruk?</a></li>
          <li><a href="mentale-gezondheid-werk-leidinggevende">Mentale gezondheid op het werk is ook jouw zaak</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Werkdruk structureel aanpakken?</h2>
        <p>In de training werkdruk verlagen leren teams oorzaken vinden en zelf afspraken maken die blijven. Of bespreek eerst in een gratis gesprek van 30 minuten waar je het beste kunt beginnen.</p>
        <div class="hero-knoppen">
          <a class="knop" href="../trainingen#werkdruk">Bekijk de training</a>
          <a class="knop omlijnd" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://deweekvandewerkstress.nl/">Week van de Werkstress 2026</a></li>
          <li><a href="https://publications.tno.nl/publication/34645173/TN4nayzz/TNO-2025-werkstress.pdf">TNO: Factsheet werkstress, Week van de Werkstress (2025)</a></li>
          <li><a href="https://wellbeing.hmc.ox.ac.uk/news/more-ambition-needed-to-improve-workplace-wellbeing/">Fleming: Employee well-being outcomes from individual-level mental health interventions, Industrial Relations Journal (2024)</a></li>
          <li><a href="https://bmcpublichealth.biomedcentral.com/track/pdf/10.1186/1471-2458-14-135">Montano, Hoven en Siegrist: Effects of organisational-level interventions at work on employees' health, BMC Public Health (2014)</a></li>
          <li><a href="https://psycnet.apa.org/doi/10.1037/0021-9010.92.1.213">Le Blanc en collega's: Take care! The evaluation of a team-based burnout intervention program for oncology care providers, Journal of Applied Psychology (2007)</a></li>
          <li><a href="https://ueaeprints.uea.ac.uk/79240/1/Work_and_stress_accepted.pdf">Nielsen en collega's: Is it me or us? The impact of individual and collective participation, Work &amp; Stress (2021)</a></li>
          <li><a href="https://bps.org.uk/research-digest/how-form-habit">Lally en collega's: How are habits formed, European Journal of Social Psychology (2010)</a></li>
          <li><a href="https://www.arboportaal.nl/onderwerpen/psychosociale-arbeidsbelasting/werkdruk/wat-zegt-de-wet">Arboportaal: Wat zegt de wet over werkdruk?</a></li>
          <li><a href="https://www.arboportaal.nl/actueel/nieuws/2024/11/15/steeds-meer-werkgevers-pakken-arbeidsrisicos-aan-met-een-rie">Arboportaal: Steeds meer werkgevers pakken arbeidsrisico's aan met een RI&amp;E (2024)</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-17', uit=sys.argv[1] if len(sys.argv) > 1 else None)
