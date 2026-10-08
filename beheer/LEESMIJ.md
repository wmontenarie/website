# Beheer

Deze map hoort niet bij de website zelf. De scripts hier bouwen een paar pagina's op uit lijsten met inhoud.
De map staat in `.assetsignore` en wordt dus niet als onderdeel van de site getoond.

Elk script draai je vanuit de hoofdmap van de repository:

| Script | Bouwt | Inhoud aanpassen in |
|---|---|---|
| `python3 beheer/kalender.py` | `kalender.html` | de lijsten EVENTS, EVENTS_VOLGT, DAGEN en DAGEN_VOLGT bovenin `kalender.py` |
| `python3 beheer/meter_pagina.py` | `vitaliteitsmeter.html` | `meter_inhoud.py` (thema's, stellingen, uitslagteksten) |
| `python3 beheer/artikel_businesscase.py` | `artikelen/businesscase-vitaliteit-maken.html` | het script zelf |
| `python3 beheer/artikel_rendement.py` | `artikelen/rendement-vitaliteitsprogramma-hbr-onderzoek.html` | het script zelf |
| `python3 beheer/artikel_werkvloer.py` | `artikelen/vitaliteit-op-de-werkvloer.html` | het script zelf |
| `python3 beheer/artikel_verzuim.py` | `artikelen/verzuim-terugdringen-maatregelen.html` | het script zelf |

Belangrijk:

- Pas deze pagina's niet met de hand aan. Wijzig de inhoud in het script en bouw de pagina opnieuw. Anders gaat de wijziging bij de volgende keer bouwen verloren.
- De kop met het menu en de voet komen uit een bestaande pagina (`tools.html` of een artikel). Verandert het menu, bouw deze pagina's dan opnieuw.
- `kalender.py` controleert zelf een aantal datums (weekdagen, volgorde). Faalt een controle, dan klopt er iets niet in de lijst.
- Zet in de kalender alleen datums die op de site van de organisator staan. Is de datum niet bekend, zet het item dan in de lijst "datum volgt".
- Werk bij een wijziging van de kalender ook `GECONTROLEERD` bij in `kalender.py`.
