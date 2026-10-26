# Bouwt het artikel over mannen, stress en gezondheid op het werk.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'mannen-stress-gezondheid-werk'
TITEL = 'Mannen, stress en gezondheid op het werk: wat je doet'
H1 = 'Waarom mannen in je team pas laat aan de bel trekken'
BESCHR = 'Mannen melden minder klachten en gaan minder vaak naar huisarts of psycholoog. Wat dat betekent voor je team, en hoe je mannen wel bereikt.'

VRAGEN = [
 ('Hebben mannen minder vaak stress of burn-outklachten?', 'Mannen melden minder klachten. In 2025 had 18 procent van de mannelijke werknemers burn-outklachten, tegen 23,5 procent van de vrouwelijke werknemers. Dat betekent niet zonder meer dat mannen minder klachten hebben. Ze gaan ook minder vaak naar de huisarts of een psycholoog.'),
 ('Hoe begin je een gesprek met een man in je team die het moeilijk lijkt te hebben?', 'Kies een rustig moment en een gewone plek, bijvoorbeeld tijdens een wandeling of in de auto. Vraag hoe het gaat of zeg dat hij niet zichzelf lijkt. Luister zonder op te lossen, vraag wat zou helpen en kom er een paar dagen later op terug. Movember noemt dit de ALEC-aanpak: ask, listen, encourage action en check in.'),
 ('Waarom praten mannen op het werk minder over mentale gezondheid?', 'In onderzoek van Movember onder Australische mannen uit 2019 was een derde van de werkende mannen bang zijn baan te riskeren als hij op het werk over mentale gezondheid praat. 4 op de 10 dachten dat het hun promotie zou kosten. Ook in Nederland noemen werknemers schaamte en angst voor hun loopbaan als reden om te zwijgen.'),
 ('Wanneer is Internationale Mannendag?', 'Elk jaar op 19 november. In 2026 valt die op donderdag. In de hele maand november vraagt Movember aandacht voor de gezondheid van mannen.'),
]
ICO = {
 'arts': '<path d="M6 3v6a6 6 0 0 0 12 0V3"/><path d="M12 15v2a4 4 0 0 0 8 0v-2"/><circle cx="20" cy="13" r="2"/>',
 'gesprek': '<path d="M21 12a8 8 0 0 1-11.5 7.2L4 21l1.8-5.5A8 8 0 1 1 21 12z"/>',
 'batterij': '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M5 10v4"/>',
 'hart': '<path d="M20.8 5.6a5 5 0 0 0-7.1 0L12 7.3l-1.7-1.7a5 5 0 0 0-7.1 7.1L12 21.5l8.8-8.8a5 5 0 0 0 0-7.1z"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">26 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Hij werkt hard, klaagt nooit en is er altijd. Tot hij op een maandag niet meer komt. Veel leidinggevenden herkennen dat verhaal. In november laten mannen een snor staan voor Movember, en op 19 november is het Internationale Mannendag. Een goed moment om stil te staan bij een vraag: waarom horen we het bij mannen vaak pas als het te laat is?</p>

      <h2>Mannen melden minder</h2>
      <p>De cijfers laten een patroon zien. Mannen gaan minder vaak naar de huisarts dan vrouwen. Ze gaan minder vaak naar een psycholoog, psychiater of psychotherapeut. En ze geven minder vaak aan dat ze zich angstig of somber voelen. Ook op het werk melden mannen minder burn-outklachten dan vrouwen.</p>
      <figure class="infographic">
        <figcaption><strong>Mannen en gezondheid in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_arts)s<span class="getal">66%% tegen 72%%</span><span>van de mannen ging in een jaar naar de huisarts, tegenover vrouwen</span></div>
          <div>%(i_gesprek)s<span class="getal">10%% tegen 14%%</span><span>van de mannen bezocht een psycholoog, psychiater of psychotherapeut, tegenover vrouwen</span></div>
          <div>%(i_batterij)s<span class="getal">18%% tegen 23,5%%</span><span>van de mannelijke werknemers meldt burn-outklachten, tegenover vrouwelijke werknemers</span></div>
          <div>%(i_hart)s<span class="getal">80,7 jaar</span><span>is de levensverwachting van mannen, tegen 83,5 jaar voor vrouwen</span></div>
        </div>
        <p class="bron-regel">Bronnen: CBS, Gezondheidsenquête 2025 en sterftecijfers 2025. RIVM, Monitor Mentale Gezondheid, 2025</p>
      </figure>
      <p>Minder melden is niet hetzelfde als minder hebben. Het kan ook betekenen dat klachten langer onder de radar blijven. Voor een leidinggevende is dat het lastige: je ziet het pas als iemand al ver over zijn grens is.</p>

      <h2>Waarom mannen zwijgen</h2>
      <p>Movember vroeg in 2019 aan werkende mannen in Australië waarom ze op het werk niet over mentale gezondheid praten. Een derde was bang dat het zijn baan zou kosten. 4 op de 10 dachten dat het hun promotie in de weg zou zitten. En bijna de helft was bang voor opmerkingen van collega's. Het zijn geen Nederlandse cijfers, maar het beeld is herkenbaar. Ook Nederlandse werknemers noemen schaamte en angst voor hun loopbaan als reden om te zwijgen.</p>
      <p>Daar komt bij dat veel mannen geleerd hebben dat je problemen zelf oplost. Doorwerken voelt als sterk zijn. Vragen om hulp voelt als zwak. Op de werkvloer wordt dat beeld vaak bevestigd, zonder dat iemand het zo bedoelt.</p>

      <h2>Wat jij als leidinggevende kunt doen</h2>
      <figure class="infographic">
        <figcaption><strong>Zo bereik je de mannen in je team</strong></figcaption>
        <ol class="stappen">
          <li><strong>Praat naast elkaar, niet tegenover elkaar</strong><p>Een wandeling, een autorit of samen koffie halen. Veel mannen praten makkelijker als ze niet recht tegenover je zitten.</p></li>
          <li><strong>Vraag, en vraag nog een keer</strong><p>Op de eerste vraag volgt vaak: prima. Zeg wat je ziet, bijvoorbeeld dat hij niet zichzelf lijkt, en vraag opnieuw hoe het echt gaat.</p></li>
          <li><strong>Luister zonder op te lossen</strong><p>Movember noemt dit de belangrijkste stap. Laat de stilte er zijn. Vraag pas daarna wat zou helpen: slaap, een gesprek met iemand, even minder werk.</p></li>
          <li><strong>Kom erop terug</strong><p>Stuur na een paar dagen een berichtje of loop even langs. Dat laat zien dat je het meende.</p></li>
          <li><strong>Haal de angst weg</strong><p>Zeg hardop dat praten over stress geen gevolgen heeft voor iemands beoordeling of loopbaan. En laat het ook zo zijn.</p></li>
        </ol>
        <p class="bron-regel">Naar de ALEC-aanpak van Movember: ask, listen, encourage action, check in</p>
      </figure>

      <h2>Begin bij jezelf</h2>
      <p>Het sterkste signaal geef je zelf. Een mannelijke leidinggevende die vertelt dat hij naar de huisarts is geweest, dat hij slecht slaapt in een drukke periode of dat hij hulp heeft gezocht, doet meer dan welke campagne ook. Daarmee laat je zien dat sterk zijn en voor jezelf zorgen samengaan. Gebruik Movember en Internationale Mannendag als aanleiding. Niet voor een grap over snorren, maar voor een gesprek.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over mannen en gezondheid op het werk</h2>
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
          <li><a href="stress-bespreekbaar-maken">Stress bespreekbaar maken: het gesprek dat je vaker moet voeren</a></li>
          <li><a href="burn-out-voorkomen-in-je-team">Burn-out voorkomen in je team</a></li>
          <li><a href="overgang-op-het-werk">De overgang op het werk: waarom je als werkgever niet kunt wegkijken</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Gezondheid bespreekbaar maken in je team?</h2>
        <p>In de training vitaal leiderschap ontdek je hoe je het goede voorbeeld geeft, ook als het om je eigen gezondheid gaat. Of bespreek eerst in een gratis gesprek van 30 minuten wat bij jullie past.</p>
        <div class="hero-knoppen">
          <a class="knop" href="../training-vitaal-leiderschap">Bekijk de training</a>
          <a class="knop omlijnd" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://www.cbs.nl/nl-nl/nieuws/2026/10/vrouwen-ongezonder-en-vaker-naar-dokter-dan-mannen">CBS: Vrouwen ongezonder en vaker naar dokter dan mannen (2026)</a></li>
          <li><a href="https://www.cbs.nl/nl-nl/nieuws/2026/11/173-duizend-mensen-overleden-in-2025">CBS: 173 duizend mensen overleden in 2025 (2026)</a></li>
          <li><a href="https://www.rivm.nl/mentale-gezondheid/monitor/werkenden/burn-out-klachten">RIVM: Monitor Mentale Gezondheid, burn-outklachten bij werkenden</a></li>
          <li><a href="https://cdn.movember.com/uploads/files/Media%%20Room/AU/Movember%%20WSPD%%20Mental%%20Health%%20at%%20Work_FINAL.pdf">Movember en Ipsos MORI: Mental health at work, onderzoek onder Australische mannen (2019)</a></li>
          <li><a href="https://movember.com/articles/mental-health-conversations">Movember: How to have a conversation about mental health</a></li>
          <li><a href="https://www.hrpraktijk.nl/medewerker/duurzame-inzetbaarheid/kwart-nederlandse-werknemers-zou-psychische-problemen-niet-met-leidinggevende-bespreken/">HR Praktijk: onderzoek van Tilburg University naar psychische problemen bespreken (2020)</a></li>
          <li><a href="https://nl.movember.com/">Movember Nederland</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-26', uit=sys.argv[1] if len(sys.argv) > 1 else None)
