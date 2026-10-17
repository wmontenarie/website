# Bouwt het artikel over herstel en rust in een volle werkweek.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'herstel-en-rust-op-het-werk'
TITEL = 'Herstel is geen luxe: rust inbouwen in een volle werkweek'
H1 = 'Herstel is geen luxe: rust inbouwen in een volle werkweek'
BESCHR = 'Wie nooit loskomt van het werk, raakt uitgeput. Wat onderzoek zegt over herstel, en hoe je als leidinggevende rust inbouwt in de werkweek.'

VRAGEN = [
 ('Waarom is herstel belangrijk voor werkenden?', 'Wie na het werk niet loskomt van het werk, is vaker uitgeput, slaapt slechter en is minder tevreden. Dat blijkt uit een overzicht van 86 publicaties met ruim 38.000 werknemers. Herstel is dus geen luxe, maar een voorwaarde om energie te houden voor werk en privé.'),
 ('Helpen korte pauzes echt?', 'Ja. Een overzicht van 22 onderzoeken liet zien dat pauzes van maximaal tien minuten zorgen voor meer energie en minder vermoeidheid. Het effect is klein maar duidelijk. Na zwaar werk is tien minuten vaak te kort.'),
 ('Hoe zorg je dat medewerkers na werktijd niet bereikbaar hoeven te zijn?', 'Maak duidelijke afspraken over wanneer je reactie verwacht, en houd je er als leidinggevende zelf aan. Onderzoek laat zien dat vooral de verwachting dat je buiten werktijd reageert uitputtend werkt, ook voor de partner thuis.'),
 ('Wanneer is de Dag van de Stilte?', 'De Dag van de Stilte is elk jaar op de laatste zondag van oktober, de dag dat de klok een uur teruggaat. In 2026 is dat zondag 25 oktober.'),
]
ICO = {
 'batterij': '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M5 10v4"/>',
 'druk': '<path d="M12 3a9 9 0 1 0 9 9"/><path d="M12 12l5-5"/><circle cx="12" cy="12" r="1.5"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 'klok': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'deur': '<path d="M14 3h5a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1h-5"/><path d="M10 17l5-5-5-5M15 12H3"/>',
 'maan': '<path d="M20 14.5A8 8 0 1 1 9.5 4 6.5 6.5 0 0 0 20 14.5z"/>',
 'groei': '<path d="M3 17l6-6 4 4 8-8"/><path d="M14 7h7v7"/>',
 'kompas': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">17 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Op zondag 25 oktober gaat de klok een uur terug. Het is ook de Dag van de Stilte: een dag om stil te staan bij rust in een drukke tijd. Een extra uur. Wat zou je ermee doen? Voor veel leidinggevenden is het antwoord: werk inhalen. Juist daarom gaat dit artikel over herstel. Niet in het weekend of op vakantie, maar elke dag.</p>

      <h2>Waarom herstel geen luxe is</h2>
      <p>Energie is als een batterij. Werk kost energie, en dat is niet erg. Het wordt pas een probleem als de batterij niet meer oplaadt. Dan kom je 's avonds uitgeput thuis, slaap je slechter en begin je de volgende dag al half leeg.</p>
      <figure class="infographic">
        <figcaption><strong>Rust in een volle werkweek in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_druk)s<span class="getal">4 op 10</span><span>werknemers moet vaak of altijd heel veel werk doen</span></div>
          <div>%(i_batterij)s<span class="getal">20,7%%</span><span>van de werknemers heeft burn-outklachten</span></div>
          <div>%(i_klok)s<span class="getal">63%%</span><span>werkt weleens buiten de gewone werktijden</span></div>
          <div>%(i_mail)s<span class="getal">42%%</span><span>is vaak of altijd bereikbaar buiten werktijd</span></div>
        </div>
        <p class="bron-regel">Bronnen: CBS, dashboard arbeidsomstandigheden 2025. RIVM, Monitor Mentale Gezondheid 2025. CBS en TNO, NEA 2023</p>
      </figure>
      <p>Een overzicht van 86 publicaties met ruim 38.000 werknemers laat zien wat er gebeurt als je na het werk mentaal loskomt van het werk. Mensen die dat goed kunnen, zijn minder uitgeput, slapen beter en zijn tevredener met hun leven. Herstel is dus geen beloning voor als het werk af is. Het is de voorwaarde om goed te kunnen blijven werken.</p>

      <h2>Vier manieren om te herstellen</h2>
      <p>De Duitse onderzoeker Sabine Sonnentag onderscheidt vier soorten herstel. Ze zijn allemaal nodig, en ze vragen allemaal iets anders.</p>
      <figure class="infographic">
        <figcaption><strong>Vier soorten herstel</strong> Naar Sonnentag en Fritz</figcaption>
        <div class="bouwblokken vier">
          <div>%(i_deur)s<strong>Loskomen</strong><span>Niet aan werk denken als je niet werkt. Geen mail op de bank, geen werk in je hoofd tijdens het eten.</span></div>
          <div>%(i_maan)s<strong>Ontspannen</strong><span>Iets doen dat weinig energie kost. Wandelen, lezen, muziek, stilte.</span></div>
          <div>%(i_groei)s<strong>Uitdaging buiten het werk</strong><span>Iets leren of doen waar je goed in wilt worden. Sport, een instrument, een cursus.</span></div>
          <div>%(i_kompas)s<strong>Zelf bepalen</strong><span>Zelf kiezen wat je met je vrije tijd doet. Geen agenda die anderen voor je vullen.</span></div>
        </div>
        <p class="bron-regel">Bron: Sonnentag en Fritz, The Recovery Experience Questionnaire, 2007</p>
      </figure>

      <h2>Herstel tijdens de werkdag</h2>
      <p>Herstel begint niet om vijf uur. Het begint om negen uur. Twee dingen helpen volgens onderzoek.</p>
      <ul>
        <li><strong>Korte pauzes.</strong> Een overzicht van 22 onderzoeken liet zien dat pauzes van maximaal tien minuten zorgen voor meer energie en minder vermoeidheid. Het effect is klein maar duidelijk. Na zwaar werk is tien minuten vaak niet genoeg.</li>
        <li><strong>Ruimte tussen vergaderingen.</strong> Microsoft mat de hersenactiviteit van mensen tijdens vier vergaderingen achter elkaar. Bij vergaderingen zonder pauze stapelde de stress zich op. Met tien minuten pauze ertussen kon het brein zich herstellen. Vooral de overgang van de ene naar de andere vergadering gaf veel stress.</li>
      </ul>

      <h2>Herstel na werktijd</h2>
      <p>Bijna de helft van de werknemers is vaak of altijd bereikbaar buiten werktijd. Onderzoek laat zien dat niet zozeer het mailen zelf het probleem is, maar de verwachting dat je reageert. Die verwachting maakt het moeilijk om los te komen, en dat put uit. Ook de partner thuis merkt het: in Amerikaans onderzoek leed ook de gezondheid en de relatie van partners onder de spanning rond werkmail.</p>
      <p>Het goede nieuws: een verwachting kun je veranderen. Door haar uit te spreken.</p>

      <h2>Jij bent het voorbeeld</h2>
      <p>Een Duits onderzoek onder 75 leidinggevenden en 237 medewerkers liet zien dat het gedrag van de leidinggevende doorwerkt. Medewerkers van leidinggevenden die werk en privé goed scheiden, waren minder uitgeput en meer betrokken. De onderzoekers noemen leidinggevenden de poortwachters van een cultuur waarin werk en privé goed samengaan.</p>
      <p>Dat betekent: wat jij doet, telt meer dan wat je zegt. Een mail om elf uur 's avonds met de toevoeging dat het geen haast heeft, zegt toch: ik werk om elf uur 's avonds. Wie zelf goed herstelt, geeft anderen toestemming om dat ook te doen. En wie zelf energie heeft, kan er ook voor anderen zijn.</p>

      <h2>Zes afspraken voor een werkweek met rust erin</h2>
      <figure class="infographic">
        <figcaption><strong>Rust inbouwen in zes afspraken</strong></figcaption>
        <ol class="stappen">
          <li><strong>Vergaderingen duren 25 of 50 minuten</strong><p>Dan zit er altijd tijd tussen. Zet het als standaard in de agenda.</p></li>
          <li><strong>Elke dag een echte pauze</strong><p>Weg van het scherm, liefst naar buiten. En als leidinggevende neem je hem zelf ook.</p></li>
          <li><strong>Spreek af wanneer je reactie verwacht</strong><p>Bijvoorbeeld: mail na zes uur 's avonds hoeft pas de volgende werkdag beantwoord te worden. Bij spoed bel je.</p></li>
          <li><strong>Verstuur later</strong><p>Werk je zelf 's avonds? Plan je mail dan in voor de volgende ochtend.</p></li>
          <li><strong>Blokken voor geconcentreerd werk</strong><p>Een paar uur per week zonder overleg en meldingen. Dat geeft rust en meer gedaan.</p></li>
          <li><strong>Praat over energie</strong><p>Vraag in het werkoverleg niet alleen wat er af moet, maar ook hoe het met de energie staat.</p></li>
        </ol>
      </figure>

      <p>Wil je meer weten over hoe energie en bevlogenheid samenhangen? Lees dan <a href="bevlogenheid-die-je-team-kan-volhouden">Bevlogenheid die je team kan volhouden</a>.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over herstel en rust op het werk</h2>
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
          <li><a href="bevlogenheid-die-je-team-kan-volhouden">Bevlogenheid die je team kan volhouden</a></li>
          <li><a href="mentale-gezondheid-werk-leidinggevende">Mentale gezondheid op het werk is ook jouw zaak</a></li>
          <li><a href="vitaliteit-op-de-werkvloer">Vitaliteit op de werkvloer: wat werkt en elf tips</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Zelf energie houden en het goede voorbeeld geven?</h2>
        <p>In de training vitaal leiderschap leer je hoe je je energie de hele dag op peil houdt, en hoe je dat voorleeft aan je team. Of bespreek eerst in een gratis gesprek van 30 minuten wat bij jou past.</p>
        <div class="hero-knoppen">
          <a class="knop" href="../training-vitaal-leiderschap">Bekijk de training</a>
          <a class="knop omlijnd" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://dagvandestilte.nl/dag-van-de-stilte-2026-ontdek-de-stilte-in-jouw-omgeving/">Dag van de Stilte 2026</a></li>
          <li><a href="https://www.cbs.nl/nl-nl/visualisaties/dashboard-arbeidsmarkt/werkenden/arbeidsomstandigheden">CBS: Dashboard arbeidsmarkt, arbeidsomstandigheden (2025)</a></li>
          <li><a href="https://www.rivm.nl/mentale-gezondheid/monitor/werkenden/burn-out-klachten">RIVM: Monitor Mentale Gezondheid, burn-outklachten bij werkenden (2025)</a></li>
          <li><a href="https://www.cbs.nl/-/media/_pdf/2024/20/nea2023-vogelvlucht.pdf">CBS en TNO: NEA 2023 in vogelvlucht (2024)</a></li>
          <li><a href="https://frontiersin.org/articles/10.3389/fpsyg.2016.02072/full">Wendsche en Lohmann-Haislah: A meta-analysis on antecedents and outcomes of detachment from work, Frontiers in Psychology (2017)</a></li>
          <li><a href="https://kops.uni-konstanz.de/entities/publication/901f4299-e3f5-46af-99cb-a27bdd4bca71">Sonnentag en Fritz: The Recovery Experience Questionnaire, Journal of Occupational Health Psychology (2007)</a></li>
          <li><a href="https://doaj.org/article/c6f37b6ba159469296b2cb968b65505f">Albulescu en collega's: Give me a break! A systematic review and meta-analysis on the efficacy of micro-breaks, PLOS ONE (2022)</a></li>
          <li><a href="https://www.microsoft.com/en-us/worklab/work-trend-index/brain-research">Microsoft WorkLab: Research proves your brain needs breaks (2021)</a></li>
          <li><a href="https://news.lehigh.edu/the-negative-impact-of-after-hours-work-email">Belkin, Becker en Conroy: Exhausted, but unable to disconnect (2017)</a></li>
          <li><a href="https://vtechworks.lib.vt.edu/handle/10919/96394">Becker en collega's: Killing me softly, electronic communications monitoring and employee and spouse well-being, Journal of Management (2019)</a></li>
          <li><a href="https://cris.uni-muenster.de/portal/publication/20444224">Koch en Binnewies: Setting a good example, Journal of Occupational Health Psychology (2015)</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-17', uit=sys.argv[1] if len(sys.argv) > 1 else None)
