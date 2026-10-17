# Bouwt het artikel over werkende mantelzorgers.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'mantelzorger-in-je-team'
TITEL = 'De mantelzorger in je team: onzichtbaar en overbelast'
H1 = 'De mantelzorger in je team: onzichtbaar en overbelast'
BESCHR = 'Miljoenen werkenden zorgen naast hun baan voor een naaste. Vaak weet de leidinggevende het niet. Zo herken je het en voer je het gesprek.'

VRAGEN = [
 ('Hoeveel werkenden zijn mantelzorger?', 'Volgens het Sociaal en Cultureel Planbureau combineerden in 2024 2,7 miljoen mensen een betaalde baan met mantelzorg. Vrouwen geven vaker mantelzorg naast hun werk dan mannen.'),
 ('Op welk verlof heeft een werkende mantelzorger recht?', 'Op kortdurend zorgverlof van maximaal twee keer de wekelijkse werkuren per twaalf maanden, met minimaal 70 procent van het loon. Op langdurend zorgverlof van maximaal zes keer de wekelijkse werkuren, onbetaald. En bij een noodgeval op calamiteitenverlof met behoud van loon.'),
 ('Hoe begin je het gesprek met een medewerker die mantelzorger is?', 'Vraag in een gewoon één-op-één gesprek of er buiten het werk iets is dat veel tijd of energie kost. Leg uit dat je het vraagt omdat je samen naar een oplossing wilt zoeken, niet om te controleren. Bespreek wat iemand nodig heeft en spreek af wanneer je er opnieuw over praat.'),
 ('Wanneer is de Dag van de Mantelzorg?', 'Elk jaar op 10 november. Het is een dag om mantelzorgers te waarderen. Voor werkgevers is het een goed moment om het onderwerp bespreekbaar te maken.'),
]
ICO = {
 'team': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 5.2a3 3 0 0 1 0 5.6M18 14.3c1.8.9 3 2.7 3 5.7"/>',
 'druk': '<path d="M12 3a9 9 0 1 0 9 9"/><path d="M12 12l5-5"/><circle cx="12" cy="12" r="1.5"/>',
 'oog': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'gesprek': '<path d="M21 12a8 8 0 0 1-11.5 7.2L4 21l1.8-5.5A8 8 0 1 1 21 12z"/>',
 'klok': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'kalender': '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
 'huis': '<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/>',
 'alarm': '<path d="M12 3l9 16H3z"/><path d="M12 10v4M12 17v.01"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">17 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Een medewerker die vaker thuiswerkt, wat eerder weg moet en in vergaderingen met het hoofd ergens anders lijkt. Misschien zorgt zij elke avond voor haar moeder. Of hij gaat elke week mee naar het ziekenhuis met zijn partner. Je weet het vaak niet. Op 10 november is het de Dag van de Mantelzorg. Een goed moment om stil te staan bij de mantelzorgers in je team.</p>

      <h2>Hoeveel mantelzorgers werken er?</h2>
      <p>Meer dan je denkt. In 2024 combineerden 2,7 miljoen mensen een betaalde baan met mantelzorg. Het aantal mantelzorgers in Nederland groeit: van 33 procent van de volwassenen in 2014 naar 39 procent in 2024. Dat zijn ruim 5,5 miljoen mensen. Met een ouder wordende bevolking en een zorg die steeds meer een beroep doet op familie, wordt dat aantal niet kleiner.</p>
      <figure class="infographic">
        <figcaption><strong>Werk en mantelzorg in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_team)s<span class="getal">2,7 mln</span><span>werkenden combineren hun baan met mantelzorg</span></div>
          <div>%(i_druk)s<span class="getal">1 op 4</span><span>werkende mantelzorgers heeft problemen met die combinatie</span></div>
          <div>%(i_oog)s<span class="getal">ruim 30%%</span><span>van de leidinggevenden weet niet van de mantelzorg van medewerkers</span></div>
          <div>%(i_gesprek)s<span class="getal">80%%</span><span>komt tot een goede oplossing na een gesprek met de leidinggevende</span></div>
        </div>
        <p class="bron-regel">Bronnen: SCP, 2025 en 2026. Stichting Werk&amp;Mantelzorg, 2025</p>
      </figure>

      <h2>Waarom je het niet ziet</h2>
      <p>Veel werkgevers verwachten dat medewerkers het zelf melden. Maar veel medewerkers doen dat niet. Het Sociaal en Cultureel Planbureau noemt twee redenen: angst dat het hun loopbaan schaadt, en schuldgevoel tegenover collega's. Dus houden ze het vol. Tot het niet meer gaat.</p>
      <p>Signalen die kunnen wijzen op een zware zorgtaak:</p>
      <ul>
        <li>Vaker kort verzuim of verlof op het laatste moment.</li>
        <li>Veel bellen of berichten tijdens werktijd, vaak met dezelfde persoon.</li>
        <li>Moeite met concentreren, vermoeid of prikkelbaar.</li>
        <li>Een vraag om minder uren of andere werktijden, zonder duidelijke reden.</li>
        <li>Minder zin in extra taken, uitjes of overwerk.</li>
      </ul>
      <p>Geen van die signalen bewijst iets. Maar ze zijn een reden om het gesprek aan te gaan.</p>

      <h2>Wat het kost als je wegkijkt</h2>
      <p>Mantelzorg en werk combineren gaat lang goed, tot de zorg zwaarder wordt. Ongeveer een kwart van de werkende mantelzorgers heeft er enige tot veel problemen mee. In een peiling van vakbond CNV onder 800 werkende mantelzorgers zei 1 op de 5 tegen een burn-out aan te zitten. Een kwart was minder gaan werken en 1 op de 10 dacht erover om helemaal te stoppen.</p>
      <p>Vooral bij vrouwen gaat intensieve mantelzorg samen met kortere werkweken. Voor je organisatie betekent dat verzuim, minder uren en het risico dat ervaren mensen vertrekken. Terwijl een open gesprek en wat ruimte vaak genoeg zijn om iemand gezond aan het werk te houden.</p>

      <h2>Wat helpt: het gesprek</h2>
      <p>Als een medewerker en leidinggevende samen in gesprek gaan, komt 80 procent tot een goede oplossing. Dat blijkt uit cijfers van Stichting Werk&amp;Mantelzorg. Het gesprek is dus geen extra werk. Het is de oplossing.</p>
      <figure class="infographic">
        <figcaption><strong>Het gesprek in vijf stappen</strong></figcaption>
        <ol class="stappen">
          <li><strong>Vraag het gewoon</strong><p>Is er buiten je werk iets dat veel tijd of energie kost? Je hoeft het woord mantelzorg niet te gebruiken. Veel mensen zien zichzelf ook niet zo.</p></li>
          <li><strong>Leg uit waarom je het vraagt</strong><p>Je wilt samen kijken wat nodig is om het vol te houden. Niet om te controleren of te oordelen.</p></li>
          <li><strong>Luister naar wat er speelt</strong><p>Hoeveel tijd kost het? Is het voorspelbaar of komt het onverwacht? Wat is het lastigst?</p></li>
          <li><strong>Zoek samen naar ruimte</strong><p>Andere werktijden, thuiswerken, tijdelijk minder uren, taken ruilen of verlof. Kies wat past.</p></li>
          <li><strong>Spreek af wanneer je het opnieuw bespreekt</strong><p>Zorg verandert. Wat nu werkt, past over drie maanden misschien niet meer.</p></li>
        </ol>
      </figure>

      <h2>Wat de wet regelt</h2>
      <p>Medewerkers met een zorgtaak hebben recht op verlof en kunnen vragen om andere werktijden. Het helpt als jij die regels kent, zodat je ze in het gesprek kunt noemen.</p>
      <figure class="infographic">
        <figcaption><strong>Verlof voor mantelzorgers</strong></figcaption>
        <div class="bouwblokken vier">
          <div>%(i_klok)s<strong>Kortdurend zorgverlof</strong><span>Maximaal twee keer de wekelijkse werkuren per twaalf maanden. Minimaal 70 procent van het loon.</span></div>
          <div>%(i_kalender)s<strong>Langdurend zorgverlof</strong><span>Maximaal zes keer de wekelijkse werkuren per twaalf maanden. Onbetaald. Twee weken van tevoren schriftelijk aanvragen.</span></div>
          <div>%(i_alarm)s<strong>Calamiteitenverlof</strong><span>Bij een noodgeval direct vrij, met behoud van loon. Een redelijk verzoek mag je niet weigeren.</span></div>
          <div>%(i_huis)s<strong>Wet flexibel werken</strong><span>Een verzoek om andere uren, tijden of werkplek. Weigeren mag alleen bij een zwaarwegend bedrijfsbelang.</span></div>
        </div>
        <p class="bron-regel">Bronnen: Rijksoverheid en Ondernemersplein, 2026</p>
      </figure>
      <p>Het kabinet wil de regels voor verlof eenvoudiger maken. Volgens het plan worden kort en langdurend zorgverlof één regeling van acht weken. Dat is nog geen wet.</p>

      <h2>Wat je als organisatie kunt doen</h2>
      <ul>
        <li><strong>Maak het zichtbaar.</strong> Noem mantelzorg in het werkoverleg, op intranet en in het jaargesprek. Wat genoemd wordt, mag besproken worden.</li>
        <li><strong>Geef leidinggevenden de ruimte.</strong> Laat ze binnen afspraken zelf beslissen over werktijden en thuiswerken. Dat werkt sneller dan een aanvraag via HR.</li>
        <li><strong>Draag het uit.</strong> Medewerkers ervaren het als helpend als leidinggevenden actief laten zien dat mantelzorg en werk samen kunnen.</li>
        <li><strong>Gebruik de Dag van de Mantelzorg.</strong> Een kaartje of attentie is mooi. Een gesprek is beter.</li>
      </ul>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over mantelzorg en werk</h2>
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
          <li><a href="wat-is-duurzame-inzetbaarheid">Wat is duurzame inzetbaarheid en hoe begin je ermee?</a></li>
          <li><a href="burn-out-voorkomen-in-je-team">Burn-out voorkomen in je team</a></li>
          <li><a href="overgang-op-het-werk">De overgang op het werk: waarom je als werkgever niet kunt wegkijken</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Mantelzorg een plek geven in je beleid?</h2>
        <p>Ik help je mantelzorg op te nemen in je beleid voor duurzame inzetbaarheid, en leidinggevenden te trainen in het gesprek. Bespreek in een gratis gesprek van 30 minuten waar je kunt beginnen.</p>
        <div class="hero-knoppen">
          <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
          <a class="knop omlijnd" href="../diensten#strategisch-advies">Bekijk strategisch advies</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://www.scp.nl/actueel/nieuws/2026/06/30/druk-op-werkende-mantelzorgers-vraagt-om-betere-samenwerking-tussen-professionele-zorg-werknemers-en-werkgevers">SCP: Druk op werkende mantelzorgers vraagt om betere samenwerking (2026)</a></li>
          <li><a href="https://www.scp.nl/actueel/nieuws/2026/05/21/stijgend-aantal-ernstig-belaste-mantelzorgers-maakt-ondersteuning-belangrijker-dan-ooit">SCP: Mantelzorg in beweging, kerncijfers en trends 2014 tot 2024 (2026)</a></li>
          <li><a href="https://www.scp.nl/actueel/nieuws/2025/05/13/veel-werkgevers-met-werknemers-in-gesprek-als-combinatie-werk-en-mantelzorg-lastig-is">SCP: Veel werkgevers met werknemers in gesprek als combinatie werk en mantelzorg lastig is (2025)</a></li>
          <li><a href="https://www.werkenmantelzorg.nl/wp-content/uploads/2025/11/Werk-en-Mantelzorg-10-misverstanden.pdf">Stichting Werk&amp;Mantelzorg: Tien misverstanden over werk en mantelzorg (2025)</a></li>
          <li><a href="https://www.cnv.nl/nieuws/cnv-onderzoek-1-op-5-werkende-mantelzorgers-zit-tegen-een-burn-out-aan/">CNV: 1 op 5 werkende mantelzorgers zit tegen een burn-out aan (2023)</a></li>
          <li><a href="https://www.rijksoverheid.nl/vraag-en-antwoord/zorgverlof/duur-zorgverlof">Rijksoverheid: Hoe lang duurt zorgverlof?</a></li>
          <li><a href="https://ondernemersplein.overheid.nl/wetten-en-regels/verlofregelingen-voor-werknemers/">Ondernemersplein: Verlofregelingen voor werknemers</a></li>
          <li><a href="https://www.rijksoverheid.nl/onderwerpen/arbeidsovereenkomst-en-cao/vraag-en-antwoord/wanneer-mag-ik-meer-of-minder-uren-werken">Rijksoverheid: Wanneer mag ik meer of minder uren werken?</a></li>
          <li><a href="https://www.rijksoverheid.nl/actueel/nieuws/2026/06/29/het-kabinet-komt-met-overzichtelijkere-regels-in-verlofwet">Rijksoverheid: Het kabinet komt met overzichtelijkere regels in Verlofwet (2026)</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-17', uit=sys.argv[1] if len(sys.argv) > 1 else None)
