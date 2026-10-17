# Bouwt het artikel over mentale gezondheid op het werk en de rol van de leidinggevende.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'mentale-gezondheid-werk-leidinggevende'
TITEL = 'Mentale gezondheid op het werk: rol van de leidinggevende'
H1 = 'Mentale gezondheid op het werk is ook jouw zaak'
BESCHR = 'Bijna de helft van de werkenden loopt op het werk risico voor de mentale gezondheid. Wat jij als leidinggevende in een gewone werkweek kunt doen.'

VRAGEN = [
 ('Wat kan een leidinggevende doen voor de mentale gezondheid van het team?', 'Het onderwerp gewoon maken in het werkoverleg, in elk één-op-één gesprek vragen hoe het gaat en wat energie kost, en kijken naar het werk zelf: tijdsdruk, waardering en samenwerking. Daarnaast signalen opmerken, het gesprek aangaan en op tijd doorverwijzen naar de bedrijfsarts.'),
 ('Ben je als leidinggevende verantwoordelijk voor de mentale gezondheid van medewerkers?', 'Je bent geen hulpverlener. Maar de werkgever moet volgens de Arbowet beleid voeren om psychosociale arbeidsbelasting, zoals werkdruk, te voorkomen of te beperken. In de praktijk ben jij als leidinggevende degene die ziet wat er in het werk gebeurt en die er iets aan kan doen.'),
 ('Helpt een training voor leidinggevenden over mentale gezondheid?', 'Ja, daar zijn aanwijzingen voor. In een Australisch onderzoek kregen leidinggevenden een training van vier uur. Het verzuim door werk daalde daarna in hun teams, en de opbrengst was bijna tien keer de investering. De Wereldgezondheidsorganisatie raadt zo\'n training sinds 2022 aan.'),
 ('Wat is de Europese Week voor Veiligheid en Gezondheid op het Werk?', 'Een jaarlijkse week van het Europees Agentschap voor veiligheid en gezondheid op het werk. In 2026 is de week van 19 tot en met 24 oktober. Het is de start van een campagne over mentale gezondheid op het werk die tot en met 2028 loopt.'),
]
ICO = {
 'mens': '<circle cx="12" cy="7" r="4"/><path d="M4 21v-1a7 7 0 0 1 16 0v1"/>',
 'klok': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'oog': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'batterij': '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M5 10v4"/>',
 'gesprek': '<path d="M21 12a8 8 0 0 1-11.5 7.2L4 21l1.8-5.5A8 8 0 1 1 21 12z"/>',
 'team': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 5.2a3 3 0 0 1 0 5.6M18 14.3c1.8.9 3 2.7 3 5.7"/>',
 'werk': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">17 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Van 19 tot en met 24 oktober is de Europese Week voor Veiligheid en Gezondheid op het Werk. Dit jaar gaat die over mentale gezondheid. Misschien denk je: dat is iets voor HR, de bedrijfsarts of de psycholoog. Maar de meeste oorzaken van stress zitten in het werk zelf. En daar heb jij als leidinggevende invloed op. Elke week weer.</p>

      <h2>Hoe staat het ervoor?</h2>
      <p>Het Europees Agentschap voor veiligheid en gezondheid op het werk startte op 13 oktober een campagne die tot en met 2028 loopt. Het motto: samen voor mentale gezondheid op het werk. De cijfers laten zien waarom.</p>
      <figure class="infographic">
        <figcaption><strong>Mentale gezondheid op het werk in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_mens)s<span class="getal">45%%</span><span>van de werkenden in de EU loopt op het werk risico voor de mentale gezondheid</span></div>
          <div>%(i_klok)s<span class="getal">ruim 40%%</span><span>van de werkenden in de EU ervaart ernstige tijdsdruk</span></div>
          <div>%(i_oog)s<span class="getal">1 op 3</span><span>heeft het gevoel dat de eigen inzet niet wordt gezien</span></div>
          <div>%(i_batterij)s<span class="getal">20%%</span><span>van de werknemers in Nederland heeft burn-outklachten</span></div>
        </div>
        <p class="bron-regel">Bronnen: EU-OSHA, campagne 2026 tot 2028 en OSH Pulse 2025. TNO, factsheet werkstress 2025</p>
      </figure>
      <p>In Nederland gaat het om 1,7 miljoen werknemers met burn-outklachten. Werknemers verzuimden in een jaar 14,3 miljoen dagen door psychosociale arbeidsbelasting, zoals werkdruk, emotioneel zwaar werk en conflicten.</p>

      <h2>Waarom jij het verschil maakt</h2>
      <p>Kijk nog eens naar de cijfers. Tijdsdruk, inzet die niet wordt gezien, slechte samenwerking. Dat zijn geen privéproblemen van medewerkers. Het zijn kenmerken van het werk. En jij bepaalt mee hoe het werk is ingericht, hoe het team samenwerkt en of iemand zich gezien voelt.</p>
      <p>Dat is ook de reden dat de Wereldgezondheidsorganisatie en de Internationale Arbeidsorganisatie in 2022 voor het eerst adviseerden om leidinggevenden te trainen in mentale gezondheid. Het doel: stress in het werk voorkomen en goed reageren als een medewerker het moeilijk heeft.</p>
      <p>Dat het werkt, laat een Australisch onderzoek bij de brandweer zien. Leidinggevenden kregen een training van vier uur over mentale gezondheid. In hun teams daalde het verzuim dat met het werk te maken had. Bij de teams van leidinggevenden zonder training steeg het juist. De opbrengst was bijna tien keer de investering. Het is één onderzoek, maar de richting is duidelijk: een leidinggevende die weet wat te doen, maakt verschil.</p>

      <h2>Wat kun je doen?</h2>
      <p>Je hoeft geen psycholoog te zijn. Het gaat om gewone dingen die je vaak en vanzelfsprekend doet.</p>
      <figure class="infographic">
        <figcaption><strong>Vijf dingen die je als leidinggevende kunt doen</strong></figcaption>
        <ol class="stappen">
          <li><strong>Maak het gewoon om erover te praten</strong><p>Zet energie en werkdruk vast op de agenda van het werkoverleg. Niet als zwaar onderwerp, maar als vraag die erbij hoort.</p></li>
          <li><strong>Vraag in elk één-op-één gesprek hoe het echt gaat</strong><p>Vraag wat energie kost en wat energie geeft. En luister naar het antwoord zonder meteen met oplossingen te komen.</p></li>
          <li><strong>Kijk naar het werk</strong><p>Waar zit de tijdsdruk? Wie krijgt nooit een compliment? Waar loopt de samenwerking vast? Pak één ding aan, samen met het team.</p></li>
          <li><strong>Let op signalen en ga het gesprek aan</strong><p>Iemand die stiller wordt, vaker fouten maakt, kort is of juist veel overwerkt. Benoem wat je ziet en vraag hoe het gaat.</p></li>
          <li><strong>Ken je grens en verwijs op tijd door</strong><p>Jij bent geen hulpverlener. Wijs de weg naar de bedrijfsarts, de vertrouwenspersoon of de huisarts. En blijf contact houden.</p></li>
        </ol>
      </figure>
      <p>Hoe je signalen herkent en het gesprek voert, lees je uitgebreider in <a href="burn-out-voorkomen-in-je-team">Burn-out voorkomen in je team</a>.</p>

      <h2>Begin bij jezelf</h2>
      <p>Je team kijkt naar wat je doet, niet naar wat je zegt. Een leidinggevende die zelf geen pauze neemt, 's avonds mailt en nooit zegt dat het even te veel is, maakt het voor anderen moeilijk om dat wel te doen. Wie goed voor zichzelf zorgt, geeft anderen de ruimte om dat ook te doen. Dat is geen zachte kant van leiderschap. Het is de basis.</p>

      <h2>Wat zegt de wet?</h2>
      <p>De Arbowet noemt het psychosociale arbeidsbelasting. Daar vallen werkdruk, werkstress, ongewenst gedrag en emotioneel zwaar werk onder. De werkgever moet beleid voeren om dit te voorkomen of te beperken. De risico's horen in de RI&amp;E, de maatregelen in het plan van aanpak, en medewerkers moeten weten welke risico's er zijn en wat eraan wordt gedaan. De werkgever moet dat ook kunnen laten zien.</p>
      <p>Beleid op papier is een begin. Of het werkt, merk je in het team. En daar ben jij.</p>

      <h2>Drie dingen voor deze week</h2>
      <figure class="infographic">
        <figcaption><strong>Doe het deze week</strong></figcaption>
        <div class="kenmerken">
          <div>%(i_team)s<strong>Werkoverleg</strong><span>Vraag het team: wat kostte deze week de meeste energie?</span></div>
          <div>%(i_gesprek)s<strong>Eén-op-één</strong><span>Vraag één medewerker hoe het echt gaat. En luister.</span></div>
          <div>%(i_werk)s<strong>Het werk</strong><span>Kies één ding dat stress geeft en spreek af wat jullie eraan doen.</span></div>
        </div>
      </figure>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over mentale gezondheid op het werk</h2>
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
          <li><a href="burn-out-voorkomen-in-je-team">Burn-out voorkomen in je team: signalen en wat je als leidinggevende kunt doen</a></li>
          <li><a href="herstel-en-rust-op-het-werk">Herstel is geen luxe: rust inbouwen in een volle werkweek</a></li>
          <li><a href="moet-je-je-druk-maken-over-werkdruk">Moet je je druk maken over werkdruk?</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Zelf het goede voorbeeld geven?</h2>
        <p>In de training vitaal leiderschap werk je aan je eigen energie en aan een team dat bevlogen en gezond blijft. Of bespreek eerst in een gratis gesprek van 30 minuten wat jouw team nodig heeft.</p>
        <div class="hero-knoppen">
          <a class="knop" href="../training-vitaal-leiderschap">Bekijk de training</a>
          <a class="knop omlijnd" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://osha.europa.eu/en/highlights/healthy-workplaces-campaign-launch-improving-mental-health-workers-eu-starts-here">EU-OSHA: Healthy Workplaces campaign 2026 to 2028, together for mental health at work (2026)</a></li>
          <li><a href="https://osha.europa.eu/en/highlights/world-mental-health-day-29-eu-workers-suffer-stress-depression-or-anxiety">EU-OSHA: OSH Pulse 2025, 29%% of EU workers suffer stress, depression or anxiety (2025)</a></li>
          <li><a href="https://publications.tno.nl/publication/34645173/TN4nayzz/TNO-2025-werkstress.pdf">TNO: Factsheet werkstress, Week van de Werkstress (2025)</a></li>
          <li><a href="https://www.who.int/news/item/28-09-2022-who-and-ilo-call-for-new-measures-to-tackle-mental-health-issues-at-work">WHO en ILO: Call for new measures to tackle mental health issues at work (2022)</a></li>
          <li><a href="https://www.unsw.edu.au/newsroom/news/2017/10/training-managers-can-improve-workers--mental-health">Milligan-Saville en collega's: Workplace mental health training for managers and its effect on sick leave in employees, Lancet Psychiatry (2017)</a></li>
          <li><a href="https://www.arboportaal.nl/onderwerpen/psychosociale-arbeidsbelasting/werkdruk/wat-zegt-de-wet">Arboportaal: Wat zegt de wet over werkdruk?</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-17', uit=sys.argv[1] if len(sys.argv) > 1 else None)
