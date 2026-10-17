# Bouwt het artikel over werken met een chronische aandoening op basis van een bestaand artikel als sjabloon.
# Gebaseerd op ESB (14 oktober 2026): Onze arbeidsmarkt kan gezonder en veel inclusiever.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artikel_basis import maak
SLUG = 'werken-met-chronische-aandoening'
TITEL = 'Werken met een chronische aandoening: acht maatregelen'
H1 = 'Werken met een chronische aandoening: acht maatregelen voor werkgevers'
BESCHR = 'Ruim 400.000 fte blijft onbenut omdat mensen met een chronische aandoening minder werken. Acht maatregelen om talent te behouden en te vinden.'

VRAGEN = [
 ('Hoeveel mensen in Nederland hebben een chronische aandoening?', 'In 2025 hadden 11,1 miljoen mensen in Nederland minstens één chronische aandoening. Het RIVM verwacht dat dit groeit naar ongeveer 12 miljoen in 2050. Het gaat om lichamelijke en psychische aandoeningen die lang duren, zoals diabetes, rugklachten, migraine of een depressie.'),
 ('Kun je werken met een chronische aandoening?', 'Vaak wel. Van de mensen met een chronische beperking of een langdurige psychische aandoening heeft 60 procent betaald werk. Bij mensen zonder zo\'n diagnose is dat 82 procent. Of iemand kan werken hangt niet alleen af van de aandoening. Het hangt ook af van hoe het werk is ingericht en of er op tijd hulp is.'),
 ('Wat kan een werkgever doen voor een medewerker met een chronische aandoening?', 'Praat op tijd over wat iemand nodig heeft. Pas het werk aan, bijvoorbeeld met andere taken, andere werktijden of meer regelruimte. Maak de bedrijfsarts makkelijk bereikbaar. En wacht bij uitval niet te lang met kijken naar ander passend werk.'),
 ('Hoe lang betaalt een werkgever het loon door bij ziekte?', 'In Nederland twee jaar. Dat is internationaal gezien lang. In Duitsland en de Scandinavische landen betaalt de werkgever veel korter door. Daarna regelt de overheid of een collectieve verzekering het inkomen.'),
]
ICO = {
 'mensen': '<circle cx="9" cy="7" r="3.5"/><path d="M2 21v-1a7 7 0 0 1 14 0v1M16 3.5a3.5 3.5 0 0 1 0 7M22 21v-1a7 7 0 0 0-4-6.3"/>',
 'werk': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
 'fte': '<path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 5-6"/>',
 'klok': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
}

MAIN = '''<main>
  <article class="sectie artikel">
    <div class="wrap">
      <p class="artikel-meta">17 oktober 2026 | Walter Montenarie</p>
      <h1>%(h1)s</h1>
      <p class="intro">Je zoekt mensen en je vindt ze moeilijk. Tegelijk staan honderdduizenden mensen langs de kant of werken ze minder dan ze willen. Vaak omdat ze een chronische aandoening hebben. Een deel van hen kan en wil wel werken. Als werkgever heb je meer invloed dan je denkt. In dit artikel lees je wat er speelt en welke acht maatregelen helpen.</p>
      <p>Dit artikel is gebaseerd op een artikel in het economenvakblad ESB van Anthony Stigter (VNO-NCW en MKB-Nederland), Lidewij Renaud (TNO), Iris de Vries (huisarts) en Ton Wilthagen (Tilburg University). Zij schrijven over beleid voor de overheid. Ik vertaal het naar wat jij als leidinggevende, directeur of HR-professional kunt doen.</p>

      <h2>Wat is het probleem?</h2>
      <p>De meeste Nederlanders hebben één of meer chronische aandoeningen. Denk aan rugklachten, diabetes, migraine, een hartaandoening of een depressie. Dat aantal groeit, want we worden ouder en werken langer door.</p>
      <p>Een chronische aandoening betekent niet dat iemand niet kan werken. Toch werken deze mensen minder vaak. Volgens de auteurs komt dat deels door hoe we werk, zorg en sociale zekerheid hebben ingericht. Dat deel kun je dus voorkomen.</p>
      <figure class="infographic">
        <figcaption><strong>Werken met een chronische aandoening in vier cijfers</strong></figcaption>
        <div class="kerncijfers">
          <div>%(i_mensen)s<span class="getal">11,1 mln</span><span>Nederlanders met minstens één chronische aandoening in 2025</span></div>
          <div>%(i_werk)s<span class="getal">60%%</span><span>van de mensen met een chronische beperking heeft betaald werk, tegen 82%% van de anderen</span></div>
          <div>%(i_fte)s<span class="getal">415.000</span><span>fte blijft maximaal onbenut bij mensen met een chronische aandoening</span></div>
          <div>%(i_klok)s<span class="getal">2 jaar</span><span>loondoorbetaling bij ziekte, internationaal gezien lang</span></div>
        </div>
        <p class="bron-regel">Bron: Stigter en collega's in ESB (2026), met cijfers van VZinfo, CBS en TNO</p>
      </figure>

      <h2>Waar zit het verlies?</h2>
      <p>TNO berekende hoeveel werk we mislopen. Het gaat om maximaal 415.000 fte. Dat verlies zit op vier plekken:</p>
      <ul>
        <li><strong>Verzuim.</strong> Mensen met een chronische aandoening verzuimen vaker. Dat kost 142.000 fte.</li>
        <li><strong>Eerder stoppen.</strong> Werkenden van 45 jaar en ouder stoppen eerder met werken. Dat kost 73.000 fte.</li>
        <li><strong>Minder uren.</strong> Mensen werken iets minder uren per week. Dat kost 17.000 fte.</li>
        <li><strong>Niet aan het werk.</strong> Mensen zonder werk die zeggen dat hun gezondheid ze niet of maar een beetje belemmert. Daar ligt 183.000 fte.</li>
      </ul>
      <p>Niet iedereen met een chronische aandoening kan werken. Maar ook als je maar een deel terugwint, gaat het om veel mensen. Twee van de vier plekken liggen bij je eigen medewerkers: verzuim en eerder stoppen. Daar heb je als werkgever direct invloed op.</p>

      <h2>Werk is ook goed voor je gezondheid</h2>
      <p>Werk geeft meer dan inkomen. Het geeft structuur, zin en contact met anderen. Volgens de auteurs gebruiken mensen met werk minder medicijnen, gaan ze minder vaak naar de huisarts en zijn ze gelukkiger. Dat geldt wel alleen voor werk dat gezond en veilig is.</p>
      <p>Wie door zijn gezondheid uitvalt, verliest dus twee keer. Hij verliest zijn werk en ook een bron van herstel. Iemand aan het werk houden is daarom vaak ook goed voor zijn gezondheid.</p>

      <h2>Acht maatregelen</h2>
      <p>Dit zijn de acht maatregelen. Daaronder licht ik ze toe.</p>
      <figure class="infographic">
        <figcaption><strong>Talent met een chronische aandoening behouden in acht maatregelen</strong></figcaption>
        <ol class="stappen">
          <li><strong>Kijk naar wat iemand kan</strong><p>Niet naar de diagnose.</p></li>
          <li><strong>Praat over werk en gezondheid voordat iemand uitvalt</strong><p>In het gewone gesprek tussen leidinggevende en medewerker.</p></li>
          <li><strong>Pas het werk aan</strong><p>Andere taken, andere tijden of meer regelruimte.</p></li>
          <li><strong>Maak de bedrijfsarts makkelijk bereikbaar</strong><p>Ook voordat iemand ziek is.</p></li>
          <li><strong>Zorg voor één aanspreekpunt</strong><p>Iemand die zorg, werk en terugkeer verbindt.</p></li>
          <li><strong>Kijk eerder naar ander werk</strong><p>Binnen of buiten je organisatie.</p></li>
          <li><strong>Houd oudere medewerkers vitaal</strong><p>Zodat ze niet eerder stoppen dan nodig.</p></li>
          <li><strong>Investeer in gezond werken</strong><p>Voorkomen is beter dan herstellen.</p></li>
        </ol>
      </figure>

      <h3>1. Kijk naar wat iemand kan</h3>
      <p>Werkgevers aarzelen soms om iemand met een gezondheidsprobleem aan te nemen. Ze zijn bang voor kosten, voor minder productiviteit of ze weten niet welke aanpassingen nodig zijn. Dat blijkt uit onderzoek dat de auteurs aanhalen. Vaak valt het mee. Vraag in een sollicitatie niet naar de aandoening, want dat mag niet. Vraag wel wat iemand nodig heeft om goed te werken. Zo vind je talent dat anderen laten liggen.</p>

      <h3>2. Praat over werk en gezondheid voordat iemand uitvalt</h3>
      <p>Nu komt werk vaak pas ter sprake als iemand al langer ziek is. Dan is het eigenlijk te laat. Maak gezondheid en energie een gewoon onderwerp in het werkoverleg en in het één-op-ééngesprek. Vraag wat iemand energie geeft en wat energie kost. Je hoeft niet te weten wat iemand mankeert. Je wilt weten wat iemand helpt om goed te blijven werken.</p>

      <h3>3. Pas het werk aan</h3>
      <p>Aanpassingen op de werkplek verkorten het verzuim en helpen mensen eerder terug te keren. Dat blijkt uit verschillende overzichtsstudies. Een aanpassing hoeft niet groot te zijn. Denk aan andere taken, minder uren, later beginnen, vaker thuiswerken, een andere stoel of meer vrijheid om je dag in te delen. Bespreek met de medewerker en de bedrijfsarts wat werkt.</p>

      <h3>4. Maak de bedrijfsarts makkelijk bereikbaar</h3>
      <p>In Nederland zijn de gewone zorg en de bedrijfsgezondheidszorg twee aparte werelden. De huisarts en de specialist kijken vooral naar de ziekte en de behandeling. Werk komt pas in beeld als iemand langer verzuimt en bij de bedrijfsarts komt. Je kunt die afstand als werkgever kleiner maken. Bied een open spreekuur bij de bedrijfsarts aan en vertel medewerkers dat het er is en dat het vertrouwelijk is.</p>

      <h3>5. Zorg voor één aanspreekpunt</h3>
      <p>Een medewerker met een chronische aandoening heeft te maken met de huisarts, een specialist, de bedrijfsarts, HR en zijn leidinggevende. Iemand die dat bij elkaar brengt maakt verschil. Onderzoek laat zien dat zo'n coördinator het verzuim kan verkorten en de terugkeer naar werk kan versnellen. In de Scandinavische landen is die verbinding tussen zorg en werk beter geregeld dan bij ons.</p>

      <h3>6. Kijk eerder naar ander werk</h3>
      <p>Ons systeem richt zich lang op terugkeer in het eigen werk. Ander werk, bij jou of bij een andere werkgever, komt vaak pas laat in beeld. Dan is iemand al lang uit het werk en is de stap groter. Kijk dus eerder wat mogelijk is. Ook als het eigen werk niet meer gaat, kan iemand vaak nog prima ander werk doen.</p>
      <p>Let ook op flexwerkers. Hun risico om in de WIA te komen is twee tot drie keer zo groot als bij mensen met een vast contract. Vaak hebben ze bij ziekte geen werkgever meer en dus ook geen contact met het werk.</p>

      <h3>7. Houd oudere medewerkers vitaal</h3>
      <p>Chronische aandoeningen komen vaker voor op latere leeftijd. Werkenden van 45 jaar en ouder met gezondheidsproblemen stoppen eerder met werken. Dat kost veel kennis en ervaring. Praat met oudere medewerkers over hoe ze gezond en met plezier kunnen blijven werken. Denk aan ander werk binnen je organisatie, minder zware taken of het delen van kennis met jongere collega's. Lees meer in <a href="wat-is-duurzame-inzetbaarheid">Wat is duurzame inzetbaarheid?</a></p>

      <h3>8. Investeer in gezond werken</h3>
      <p>Een gezondere bevolking helpt om meer mensen aan het werk te houden. Daar ligt een taak voor de overheid. De auteurs laten zien dat Nederland zijn eigen doelen bij overgewicht niet haalt. Maar ook als werkgever kun je veel doen. Pak werkdruk aan bij de bron, geef ruimte voor herstel tijdens de werkdag en geef als leidinggevende zelf het goede voorbeeld. Een fruitschaal en een sportweek zijn daarbij niet genoeg. Lees wat wel werkt in <a href="vitaliteit-op-de-werkvloer">Vitaliteit op de werkvloer</a>.</p>

      <h2>Wat de overheid volgens de auteurs moet doen</h2>
      <p>De auteurs doen ook voorstellen voor de overheid. Ze zijn goed om te kennen, omdat ze jouw risico's als werkgever veranderen:</p>
      <ul>
        <li><strong>Kortere loondoorbetaling.</strong> Twee jaar loon doorbetalen bij ziekte is een groot risico, vooral voor kleine werkgevers. Daardoor nemen werkgevers minder snel iemand aan met een gezondheidsprobleem. Eerder is al geadviseerd om de periode te verkorten naar één jaar.</li>
        <li><strong>Eerder hulp bij terugkeer.</strong> Meer en eerdere steun bij aanpassingen en bij terugkeer naar werk, ook bij een andere werkgever.</li>
        <li><strong>Zorg en werk verbinden.</strong> Huisartsen en specialisten moeten vanaf het begin met de patiënt over werk praten. Een vaste richtlijn raadt dat al aan. De auteurs pleiten voor scholing van zorgverleners zodat ze dat ook doen.</li>
        <li><strong>Gezondheidsdoelen bewaken.</strong> Doelen voor bijvoorbeeld roken en overgewicht koppelen aan metingen en extra maatregelen als het resultaat achterblijft.</li>
      </ul>
      <p>Op die maatregelen hoef je niet te wachten. Alles wat in de acht maatregelen staat kun je morgen al doen.</p>

      <h2>Waar begin je?</h2>
      <p>Begin bij je leidinggevenden. Zij voeren het gesprek, zien de signalen en bepalen of iemand ruimte krijgt om het werk aan te passen. En ze laten zelf zien hoe je gezond werkt. Wil je weten waar je organisatie nu staat, doe dan de gratis <a href="../vitaliteitsmeter">vitaliteitsmeter</a>. Wil je zien wat verzuim je kost, gebruik dan de <a href="../tools#rekentool-kop">verzuimrekentool</a>.</p>

      <section class="vragen" aria-labelledby="vragen-kop">
        <h2 id="vragen-kop">Veelgestelde vragen over werken met een chronische aandoening</h2>
%(vragen)s
      </section>
%(deel)s
      <aside class="wp-tip" aria-label="Whitepaper">
        <img src="../img/whitepaper-vitaliteitsbeleid-omslag.webp" width="560" height="793" alt="Omslag van de whitepaper Vitaliteitsbeleid opzetten" loading="lazy">
        <div>
          <p class="podcast-label">Gratis whitepaper</p>
          <p class="podcast-titel">Vitaliteitsbeleid opzetten</p>
          <p>Een stappenplan voor beleid dat verder gaat dan losse activiteiten. Met een voorbeeld van een plan van aanpak.</p>
          <a class="knop" href="../whitepaper-vitaliteitsbeleid-opzetten">Download de whitepaper</a>
        </div>
      </aside>

      <aside class="lees-ook" aria-label="Lees ook">
        <h2>Lees ook</h2>
        <ul>
          <li><a href="verzuim-terugdringen-maatregelen">Verzuim terugdringen: zeven maatregelen die werken</a></li>
          <li><a href="wat-is-duurzame-inzetbaarheid">Wat is duurzame inzetbaarheid?</a></li>
          <li><a href="vitaliteit-op-de-werkvloer">Vitaliteit op de werkvloer: wat werkt en elf tips</a></li>
        </ul>
      </aside>
      <div class="artikel-cta">
        <h2>Wil je talent met een chronische aandoening behouden?</h2>
        <p>In een gratis gesprek van 30 minuten kijken we waar in jouw organisatie de winst ligt. Of leer met je leidinggevenden in de training vitaal leiderschap hoe je het goede voorbeeld geeft.</p>
        <div class="hero-knoppen">
          <a class="knop" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
          <a class="knop omlijnd" href="../training-vitaal-leiderschap">Bekijk de training</a>
        </div>
      </div>
%(nb)s
      <section class="bronnen" aria-labelledby="bronnen-kop">
        <h2 id="bronnen-kop">Bronnen</h2>
        <ul>
          <li><a href="https://esb.nu/onze-arbeidsmarkt-kan-gezonder-en-veel-inclusiever/">Stigter, Renaud, De Vries en Wilthagen: Onze arbeidsmarkt kan gezonder en veel inclusiever, ESB (2026)</a>. De cijfers in dit artikel komen uit dit artikel, dat zich baseert op VZinfo, CBS, TNO, RIVM en OCTAS.</li>
          <li><a href="https://www.cochrane.org/evidence/CD006955_changes-workplace-preventing-disability-workers-sick-leave">Van Vilsteren en collega's: Workplace interventions to prevent work disability, Cochrane (2015)</a></li>
        </ul>
      </section>
    </div>
  </article>
</main>
'''

maak(SLUG, TITEL, H1, BESCHR, VRAGEN, MAIN, ICO, DATUM='2026-10-17', uit=sys.argv[1] if len(sys.argv) > 1 else None)
