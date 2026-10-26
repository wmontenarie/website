# Bouwt het artikel over mantelzorgvriendelijk werkgeverschap.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'mantelzorgvriendelijk-werkgeverschap'
TITEL = 'Mantelzorgvriendelijk werkgeverschap in vijf afspraken'
H1 = 'Mantelzorgvriendelijk werkgeverschap in vijf afspraken'
BESCHR = 'Mantelzorg hangt samen met bijna een vijfde van het verzuim. Met vijf afspraken maak je er als organisatie beleid van, in plaats van toeval.'

VRAGEN = [
 ('Wat is mantelzorgvriendelijk werkgeverschap?', 'Een organisatie waarin medewerkers met een zorgtaak dat kunnen bespreken, weten welke ruimte er is en die ruimte ook krijgen. Dat vraagt om beleid op papier, leidinggevenden die het gesprek kunnen voeren en afspraken die je regelmatig bekijkt.'),
 ('Hoeveel verzuim heeft met mantelzorg te maken?', 'Volgens onderzoek van HRM CZ en GfK hangt ongeveer 18 procent van het ziekteverzuim samen met mantelzorg. Het SCP vond dat 18 procent van de werkende mantelzorgers twee weken of langer per jaar ziek is, tegen 10 procent van de werkenden zonder zorgtaak.'),
 ('Komt er meer zorgverlof?', 'Het kabinet wil kort en langdurend zorgverlof samenvoegen tot één regeling van acht weken. Daarvan zijn de eerste twee weken betaald tegen 70 procent van het loon. Het doel is dat de nieuwe Verlofwet in 2028 ingaat. De SER adviseert om alle acht weken te betalen.'),
 ('Kan ik nog een erkenning als mantelzorgvriendelijke werkgever krijgen?', 'De Erkenning van Stichting Werk&Mantelzorg kan alleen in 2026 nog worden aangevraagd en stopt na afronding van de lopende trajecten. De vier pijlers van de stichting, bespreken, beschrijven, bekwamen en borgen, zijn wel een goede leidraad voor je beleid.'),
]
ICO = {
 'pols': '<path d="M3 12h4l3-8 4 16 3-8h4"/>',
 'bed': '<path d="M3 18V8M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="2"/>',
 'zon': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 'team': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 5.2a3 3 0 0 1 0 5.6M18 14.3c1.8.9 3 2.7 3 5.7"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">26 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Op 10 november is het de Dag van de Mantelzorg. Veel organisaties sturen dan een bloemetje of een kaartje. Mooi gebaar. Maar de mantelzorger in je team heeft meer aan iets anders: weten waar hij of zij aan toe is. Of de ruimte er is, mag niet afhangen van welke leidinggevende je toevallig hebt. Daar is beleid voor nodig.</p>

      <h2>Waarom het een zaak is voor de directie</h2>
      <p>Mantelzorg lijkt een privézaak, maar het raakt je organisatie direct. Ongeveer 18 procent van het ziekteverzuim hangt samen met mantelzorg. Werkende mantelzorgers zijn vaker langdurig ziek: 18 procent is twee weken of langer per jaar ziek, tegen 10 procent van de werkenden zonder zorgtaak.</p>
      <p>In 2023 hadden 807.000 werknemers te maken met een langdurige zorgsituatie. 243.000 van hen pasten hun werk aan. Ze gingen op andere tijden werken, vaker thuis, of minder uren. 14.000 stopten tijdelijk met werken. Opvallend: wie verlof nam, gebruikte vooral de eigen vakantiedagen. Dus de vakantie die bedoeld is om te herstellen, gaat op aan zorg.</p>
      <figure class="infographic">
        <figcaption><strong>Mantelzorg en werk in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_pols)s<span class="getal">18%%</span><span>van het ziekteverzuim hangt samen met mantelzorg</span></div>
          <div>%(i_bed)s<span class="getal">18%% tegen 10%%</span><span>van de mantelzorgers is twee weken of langer ziek per jaar, tegenover werkenden zonder zorgtaak</span></div>
          <div>%(i_team)s<span class="getal">243.000</span><span>werknemers pasten hun werk aan voor de zorg voor een naaste</span></div>
          <div>%(i_zon)s<span class="getal">158.000</span><span>werknemers namen vakantiedagen op om voor een naaste te zorgen</span></div>
        </div>
        <p class="bron-regel">Bronnen: HRM CZ en GfK, 2017. SCP, 2022. CBS, 2023, via SER, 2026</p>
      </figure>

      <h2>De vijf afspraken</h2>
      <p>Stichting Werk&amp;Mantelzorg werkt met vier pijlers: bespreken, beschrijven, bekwamen en borgen. Ik voeg daar één aan toe: de ruimte echt geven. Samen zijn het vijf afspraken die je als organisatie kunt maken.</p>
      <figure class="infographic">
        <figcaption><strong>Vijf afspraken voor mantelzorgvriendelijk werkgeverschap</strong></figcaption>
        <ol class="stappen">
          <li><strong>We maken het bespreekbaar</strong><p>Mantelzorg is een vast onderwerp in het jaargesprek en het werkoverleg. Wie het noemt, wordt niet als minder inzetbaar gezien.</p></li>
          <li><strong>We zetten het op papier</strong><p>Beschrijf welke ruimte er is: verlof, flexibele uren, thuiswerken, tijdelijk minder uren met de garantie dat je terug kunt. Zet het op intranet, zodat niemand ernaar hoeft te raden.</p></li>
          <li><strong>We leren leidinggevenden het gesprek</strong><p>Een gesprek tussen medewerker en leidinggevende leidt in de meeste gevallen tot een oplossing. Train leidinggevenden daarin en geef ze binnen afspraken de ruimte om zelf te beslissen.</p></li>
          <li><strong>We geven echte ruimte</strong><p>Denk verder dan de wet. Laat collega's verlofuren aan elkaar geven. Bij PGGM kunnen medewerkers verlof doneren aan collega's met een zorgtaak, en de werkgever verdubbelt die uren. Of ruil nachtdiensten voor dagdiensten, zoals zorgorganisatie Charim doet.</p></li>
          <li><strong>We kijken elk jaar of het werkt</strong><p>Vraag na hoeveel mensen een zorgtaak hebben, wat ze gebruiken en wat ze missen. Pas het beleid aan als dat nodig is. Zorg verandert, en beleid moet meebewegen.</p></li>
        </ol>
        <p class="bron-regel">Naar de vier pijlers van Stichting Werk&amp;Mantelzorg</p>
      </figure>

      <h2>Wat er verandert in de wet</h2>
      <p>Het kabinet wil kort en langdurend zorgverlof samenvoegen tot één regeling van acht weken. De eerste twee weken worden betaald tegen 70 procent van het loon, de andere zes zijn onbetaald. Het doel is dat de nieuwe Verlofwet in 2028 ingaat. De SER gaat verder en adviseert om alle acht weken te betalen, met een uitkering van de overheid. Ook vraagt de SER om mantelzorg vaker aan de cao-tafel te bespreken.</p>
      <p>Wacht daar niet op. De wet regelt het minimum. Wat een medewerker echt helpt, is een organisatie waarin de zorgtaak gezien wordt en waarin de ruimte vanzelfsprekend is.</p>

      <h2>Begin op 10 november</h2>
      <p>Gebruik de Dag van de Mantelzorg als startpunt. Vraag in het managementteam: weten we hoeveel mantelzorgers er bij ons werken? Staat ergens wat ze kunnen verwachten? Weten onze leidinggevenden hoe ze het gesprek voeren? Is het antwoord drie keer nee, dan weet je waar je begint.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over mantelzorgvriendelijk werkgeverschap</h2>
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
          <li><a href="mantelzorger-in-je-team">De mantelzorger in je team: onzichtbaar en overbelast</a></li>
          <li><a href="vitaliteitsbeleid-opzetten-stappenplan">Vitaliteitsbeleid opzetten: stappenplan en voorbeeld</a></li>
          <li><a href="wat-is-duurzame-inzetbaarheid">Wat is duurzame inzetbaarheid en hoe begin je ermee?</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Mantelzorg een vaste plek geven in je beleid?</h2>
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
          <li><a href="https://www.ser.nl/-/media/ser/downloads/adviezen/2026/mantelzorg-en-werk.pdf">SER: advies Mantelzorg en werk (2026)</a></li>
          <li><a href="https://www.werkenmantelzorg.nl/feiten-cijfers-2">Stichting Werk&amp;Mantelzorg: feiten en cijfers</a></li>
          <li><a href="https://www.werkenmantelzorg.nl/aan-de-slag/de-4-pijlers/">Stichting Werk&amp;Mantelzorg: de vier pijlers</a></li>
          <li><a href="https://www.werkenmantelzorg.nl/wp-content/uploads/2025/06/Werk-en-Mantelzorg-Publicatie-Zorg-en-Welzijn_HR.pdf">Stichting Werk&amp;Mantelzorg: publicatie zorg en welzijn (2025)</a></li>
          <li><a href="https://www.hrpraktijk.nl/medewerker/arbo/ser-totaalpakket-mantelzorg-nodig-met-belangrijke-bijdrage-werkgevers-voorbeelden-uit-de-praktijk/">HR Praktijk: SER wil totaalpakket voor mantelzorg, met voorbeelden uit de praktijk (2026)</a></li>
          <li><a href="https://www.rijksoverheid.nl/actueel/nieuws/2026/06/29/het-kabinet-komt-met-overzichtelijkere-regels-in-verlofwet">Rijksoverheid: Het kabinet komt met overzichtelijkere regels in Verlofwet (2026)</a></li>
          <li><a href="https://www.mantelzorg.nl/campagne/dag-van-de-mantelzorg">MantelzorgNL: Dag van de Mantelzorg</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-26', uit=sys.argv[1] if len(sys.argv) > 1 else None)
