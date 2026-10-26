# Beheer

Deze map hoort niet bij de website zelf. De scripts hier bouwen een paar pagina's op uit lijsten met inhoud.
De map staat in `.assetsignore` en wordt dus niet als onderdeel van de site getoond.

Elk script draai je vanuit de hoofdmap van de repository:

| Script | Bouwt | Inhoud aanpassen in |
|---|---|---|
| `python3 beheer/kalender.py` | `kalender.html` | de lijsten EVENTS, EVENTS_VOLGT, DAGEN en DAGEN_VOLGT bovenin `kalender.py` |
| `python3 beheer/llms.py` | `llms.txt` (samenvatting van de site voor AI-zoekmachines) | de teksten in het script; de artikelen komen uit `artikelen.html`. Draai dit opnieuw na elk nieuw artikel |
| `python3 beheer/meter_pagina.py` | `vitaliteitsmeter.html` | `meter_inhoud.py` (thema's, stellingen, uitslagteksten) |
| `python3 beheer/artikel_businesscase.py` | `artikelen/businesscase-vitaliteit-maken.html` | het script zelf |
| `python3 beheer/artikel_rendement.py` | `artikelen/rendement-vitaliteitsprogramma-hbr-onderzoek.html` | het script zelf |
| `python3 beheer/artikel_werkvloer.py` | `artikelen/vitaliteit-op-de-werkvloer.html` | het script zelf |
| `python3 beheer/artikel_verzuim.py` | `artikelen/verzuim-terugdringen-maatregelen.html` | het script zelf |
| `python3 beheer/artikel_chronisch.py` | `artikelen/werken-met-chronische-aandoening.html` | het script zelf |
| `python3 beheer/artikel_mentaal.py` | `artikelen/mentale-gezondheid-werk-leidinggevende.html` | het script zelf |
| `python3 beheer/artikel_werkstress_volhouden.py` | `artikelen/werkstress-aanpakken-na-de-week.html` | het script zelf |
| `python3 beheer/artikel_mantelzorg.py` | `artikelen/mantelzorger-in-je-team.html` | het script zelf |
| `python3 beheer/artikel_overgang.py` | `artikelen/overgang-op-het-werk.html` | het script zelf |
| `python3 beheer/artikel_herstel.py` | `artikelen/herstel-en-rust-op-het-werk.html` | het script zelf |
| `python3 beheer/artikel_thermostaat.py` | `artikelen/leidinggevende-voorbeeld-werkstress.html` | het script zelf |
| `python3 beheer/artikel_stress_gesprek.py` | `artikelen/stress-bespreekbaar-maken.html` | het script zelf |
| `python3 beheer/artikel_mantelzorgbeleid.py` | `artikelen/mantelzorgvriendelijk-werkgeverschap.html` | het script zelf |
| `python3 beheer/artikel_mannen.py` | `artikelen/mannen-stress-gezondheid-werk.html` | het script zelf |
| `python3 beheer/artikel_diabetes.py` | `artikelen/diabetes-type-2-voorkomen-werk.html` | het script zelf |
| `python3 beheer/artikel_krapte.py` | `artikelen/psychisch-verzuim-krapte-arbeidsmarkt.html` | het script zelf |
| `python3 beheer/artikel_extra.py` | kruimelpad, leestijd en blok over de auteur in alle artikelen, plus de leestijd op de kaarten in `artikelen.html` | `AUTEUR` in het script; het thema per artikel in `themas.py`. De artikelscripts doen dit zelf; draai het na een artikel dat met de hand is gemaakt |
| `python3 beheer/thema_paginas.py` | `werkdruk.html`, `burn-out-en-verzuim.html`, `vitaliteitsbeleid.html`, `cultuurverandering.html` | `themas.py`. De kaarten komen uit `artikelen.html`, dus draai dit opnieuw na een nieuw artikel |
| `python3 beheer/training_cultuurverandering.py` | `training-cultuurverandering.html` | het script zelf |
| `python3 beheer/nieuwsbrief_voorbeeld.py` | `nieuwsbrief-voorbeeld.html` | het script zelf |

Belangrijk:

- Een nieuw artikel hoort bij een thema. Zet het in `themas.py`, anders stopt het bouwen met een melding.

- Pas deze pagina's niet met de hand aan. Wijzig de inhoud in het script en bouw de pagina opnieuw. Anders gaat de wijziging bij de volgende keer bouwen verloren.
- De kop met het menu en de voet komen uit een bestaande pagina (`tools.html` of een artikel). Verandert het menu, bouw deze pagina's dan opnieuw.
- `kalender.py` controleert zelf een aantal datums (weekdagen, volgorde). Faalt een controle, dan klopt er iets niet in de lijst.
- Zet in de kalender alleen datums die op de site van de organisator staan. Is de datum niet bekend, zet het item dan in de lijst "datum volgt".
- Werk bij een wijziging van de kalender ook `GECONTROLEERD` bij in `kalender.py`.
