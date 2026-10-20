# Bouwt nieuwsbrief-voorbeeld.html: een voorbeeld van de nieuwsbrief, met echte artikelen van de site.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pagina_basis import maak_pagina

MAIN = '''<main>
  <section class="sectie">
    <div class="wrap smal">
      <p class="kruimel"><a href="./">Home</a> <span aria-hidden="true">›</span> Voorbeeld nieuwsbrief</p>
      <h1>Zo ziet de nieuwsbrief eruit</h1>
      <p class="intro">De nieuwsbrief gaat over duurzame inzetbaarheid, vitaliteit en leiderschap. Je krijgt hem als ik iets heb wat je verder helpt: soms twee keer per week, soms pas na een paar weken. Hieronder een voorbeeld.</p>

      <div class="nb-mail" aria-label="Voorbeeld van een nieuwsbrief">
        <div class="nb-mail-kop"><strong>Walter Montenarie</strong><span>Oktober 2026</span></div>
        <div class="nb-mail-romp">
          <h2>Een extra uur. Wat doe je ermee?</h2>
          <p>Op zondag 25 oktober gaat de klok een uur terug. Het is ook de Dag van de Stilte. Voor veel leidinggevenden is het antwoord op die vraag: werk inhalen. Daarom gaat deze nieuwsbrief over herstel. Niet in het weekend, maar elke werkdag.</p>

          <h3>Herstel is geen luxe: rust inbouwen in een volle werkweek</h3>
          <p>Wie de hele dag doorwerkt, komt 's avonds leeg thuis. Korte pauzes en ruimte tussen vergaderingen helpen meer dan je denkt. In het artikel lees je wat onderzoek zegt en zes afspraken die je met je team kunt maken.</p>
          <p><a class="knop" href="artikelen/herstel-en-rust-op-het-werk">Lees het hele artikel</a></p>

          <p class="nb-mail-kern">Plan vergaderingen van 25 of 50 minuten. Dan heeft je brein tijd om te herstellen voor het volgende overleg.</p>

          <h3>Tip voor deze week</h3>
          <p>Kijk morgen in je agenda. Staan er vergaderingen direct achter elkaar? Maak er één korter en gebruik de tijd die overblijft om even naar buiten te gaan.</p>

          <div class="nb-mail-wp">
            <p class="podcast-label">Gratis whitepaper</p>
            <p class="podcast-titel">Werkdruk verlagen</p>
            <p>Een handleiding voor leidinggevenden. Oorzaken vinden, het gesprek voeren en met je team aan de slag.</p>
            <a class="knop" href="whitepaper-werkdruk-verlagen">Download de whitepaper</a>
          </div>

          <h3>In de kalender</h3>
          <p>Op 3 november is het Nationaal Arbocongres in Baarn, over psychosociale arbeidsbelasting en psychische klachten op het werk. Meer evenementen vind je in de <a href="kalender">vitaliteitskalender</a>.</p>

          <p class="nb-mail-groet">Met vriendelijke groet,<br><strong>Walter Montenarie</strong></p>
        </div>
      </div>

      <aside class="nb-blok" id="nieuwsbrief" aria-labelledby="nb-kop">
        <div class="nb-tekst">
          <h2 id="nb-kop">Ook ontvangen?</h2>
          <p>Schrijf je in met je voornaam en e-mailadres. Afmelden kan altijd.</p>
        </div>
        <form class="nb-formulier" action="/verstuur" method="POST">
          <input type="hidden" name="soort" value="nieuwsbrief">
          <input type="text" name="_honey" class="verborgen" tabindex="-1" autocomplete="off" aria-hidden="true">
          <div class="nb-velden">
            <label for="nb-naam">Voornaam<input id="nb-naam" type="text" name="naam" autocomplete="given-name" required></label>
            <label for="nb-email">E-mailadres<input id="nb-email" type="email" name="email" autocomplete="email" required></label>
            <button class="knop" type="submit">Schrijf je in</button>
          </div>
          <p class="nb-klein">Afmelden kan altijd via de link in elke nieuwsbrief. Lees meer in de <a href="privacy">privacyverklaring</a>.</p>
          <p class="nb-melding" role="status" hidden></p>
        </form>
      </aside>
    </div>
  </section>
</main>
'''

maak_pagina('nieuwsbrief-voorbeeld',
            'Voorbeeld van de nieuwsbrief | Walter Montenarie',
            'Zo ziet de nieuwsbrief van Walter Montenarie eruit. Over duurzame inzetbaarheid, vitaliteit en leiderschap, met een artikel, een tip en de kalender.',
            'Voorbeeld van de nieuwsbrief',
            MAIN)
