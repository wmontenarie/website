# Bouwt kalender.html uit de lijsten hieronder. Opnieuw uitvoeren na het bijwerken van de lijsten.
import datetime as dt, html, re, json

import os
W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')
GECONTROLEERD = '6 oktober 2026'
MND = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']
MK = ['jan', 'feb', 'mrt', 'apr', 'mei', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec']

# ---------------------------------------------------------------- 1. Evenementen
# (start, eind, soort, naam, plaats, beschrijving, voor wie, link)
# soort: werk = werk en vitaliteit, leefstijl = leefstijl en preventie, zorg = zorg en innovatie
EVENTS = [
 ('2026-10-07', '2026-10-07', 'werk', 'RNVC Jaarcongres 2026', 'Barneveld, Midden Nederland Hallen', 'Jaarcongres voor casemanagers verzuim en re-integratie. Thema: van proces naar mens.', 'Casemanagers verzuim en HR', 'https://rnvc.nl/jaarcongres-2026/'),
 ('2026-10-07', '2026-10-08', 'werk', 'Safety&Health@Work', 'Rotterdam, Ahoy', 'Vakbeurs over veilig en gezond werken met exposanten en kennissessies.', 'Preventiemedewerkers en arboprofessionals', 'https://www.safetyandhealthatwork.nl/en'),
 ('2026-10-08', '2026-10-08', 'leefstijl', 'Hét Leefstijl Symposium', 'Almelo, Erve Asito en online', 'Symposium over leefstijl in de dagelijkse zorgpraktijk, met onder meer ademhaling, slaap en vrouwengezondheid.', 'Zorgprofessionals en leefstijlcoaches', 'https://www.leefstijlsymposium.nl/'),
 ('2026-10-10', '2026-10-10', 'leefstijl', 'Slaapsymposium DREAMING', 'Maarssen, InnStyle', 'Nascholing over slaap en slaapzorg.', 'Zorgprofessionals en bedrijfsartsen', 'https://events.slaapoefentherapie.nl/'),
 ('2026-10-20', '2026-10-23', 'leefstijl', 'Sleep Europe 2026', 'Maastricht, MECC', 'Europees wetenschappelijk congres over slaaponderzoek en slaapgeneeskunde. Engelstalig.', 'Onderzoekers en artsen', 'https://www.mecc.nl/events/sleep-europe-2026/'),
 ('2026-10-30', '2026-10-30', 'leefstijl', 'Congres Voeding', 'Ede, ReeHorst', 'Congres over voeding bij het voorkomen en behandelen van chronische ziekten.', 'Huisartsen, diëtisten en andere zorgprofessionals', 'https://congressen.huisarts.bsl.nl/event/congres-voeding/'),
 ('2026-10-30', '2026-10-30', 'leefstijl', 'Congres Slaapstoornissen', 'Veenendaal, Van der Valk', 'Congres over wat werkt bij slaapproblemen in verschillende levensfasen.', 'Artsen, bedrijfsartsen, psychologen en leefstijlcoaches', 'https://congressen.huisarts.bsl.nl/event/slaapstoornissen/'),
 ('2026-10-30', '2026-10-30', 'leefstijl', 'Leefstijlcongres Van Vragen naar Doen', 'Den Haag', 'Regionaal congres over leefstijl in de paramedische praktijk.', 'Paramedici en leefstijlcoaches in Haaglanden', 'https://www.fysiogroephaaglanden.nl/leefstijlcongres-van-vragen-naar-doen'),
 ('2026-11-02', '2026-11-05', 'leefstijl', 'Kennisweek Sport & Bewegen', 'Utrecht en online', 'Kennisweek over bewegen in het dagelijks leven, beleid en gedragsverandering.', 'Beleidsadviseurs, leefstijlcoaches en buurtsportcoaches', 'https://www.beweegalliantie.nl/actueel/agenda/kennisweek-sport-bewegen'),
 ('2026-11-03', '2026-11-03', 'werk', 'Nationaal Arbocongres', 'Baarn, Vuursche Lodge', 'Congres over arbowetgeving, de RI&E, psychosociale arbeidsbelasting en psychische klachten op het werk.', 'Arboprofessionals, preventiemedewerkers, HR en OR', 'https://www.rendementco.nl/id94-nationaal-arbo-congres.html'),
 ('2026-11-04', '2026-11-04', 'zorg', 'Mobile Healthcare Event', 'Rotterdam, Ahoy', 'Congres over digitale zorg en de juiste zorg op de juiste plek.', 'Bestuurders, managers en artsen in de zorg', 'https://www.mobilehealthcareplatform.nl/congres/info/'),
 ('2026-11-04', '2026-11-05', 'leefstijl', 'Nationaal Prehabilitatie Congres', 'Drachten, De Lawei', 'Congres over patiënten fitter maken voor een ingreep met beweging, voeding en mentale voorbereiding.', 'Artsen, fysiotherapeuten en diëtisten', 'https://congresscare.com/en/congress/6e-nationaal-prehabilitatie-congres-2026'),
 ('2026-11-09', '2026-11-09', 'leefstijl', 'Jaarevent Beweegalliantie en JOGG', 'Baarn, Vuursche Lodge', 'Middag over een leefomgeving die uitnodigt tot bewegen, met voorbeelden uit de praktijk.', 'Gemeenten, organisaties en bedrijven', 'https://www.beweegalliantie.nl/actueel/agenda/jaarevent-hoe-maken-we-bewegen-in-onze-leefomgeving-vanzelfsprekend'),
 ('2026-11-14', '2026-11-15', 'leefstijl', 'HOLOLIFE Summit Amsterdam', 'Halfweg, SugarFactory', 'Tweedaags Engelstalig evenement over langer gezond leven, voeding en technologie voor gezondheid.', 'Publiek, artsen en ondernemers', 'https://ams2026.hololifesummit.com/'),
 ('2026-11-20', '2026-11-20', 'werk', 'WAOP Conference 2026', 'Rotterdam, Postillion WTC', 'Wetenschappelijke conferentie over werk en welzijn. Thema: Making Minds Matter at Work. Engelstalig.', 'Onderzoekers, A&O-psychologen en HR', 'https://www.eventbrite.com/e/waop-conference-2026-tickets-1984780347448'),
 ('2026-11-24', '2026-11-24', 'werk', 'HR, Arbo en Salarisnet Kennisfestival', 'Nieuwegein, NBC Congrescentrum', 'Kennisdag met sessies over onder meer vitaliteit, verzuim, het voorkomen van burn-out en de RI&E.', 'HR, arboprofessionals, leidinggevenden en OR', 'https://arbo-academy.nl/events/arbo-kennisfestival'),
 ('2026-12-01', '2026-12-01', 'leefstijl', 'Congres Bouwen aan de Sociale Riolering', 'Den Haag, Provinciehuis', 'Dagcongres van het Institute for Positive Health over Positieve Gezondheid in de woon- en leefomgeving.', 'Gemeenten en maatschappelijke organisaties', 'https://www.iph.nl/evenementen/1-december-2026-congres-bouwen-aan-de-sociale-riolering/'),
 ('2027-01-26', '2027-01-28', 'zorg', 'ICT&health World Conference 2027', 'Maastricht, MECC', 'Driedaagse internationale conferentie over digitale zorg en de verandering van de zorg.', 'Zorgprofessionals, bestuurders en beleidsmakers', 'https://www.icthealth.nl/events/icthealth-world-conference-2027'),
 ('2027-01-29', '2027-01-29', 'leefstijl', 'Jaarcongres Vrouw & Gezondheid', 'Woerden, Van der Valk', 'Congres over de gezondheid van vrouwen, waaronder de overgang, migraine en hart- en vaatziekten.', 'Huisartsen, bedrijfsartsen en praktijkondersteuners', 'https://congressen.huisarts.bsl.nl/event/vrouw-en-gezondheid/'),
 ('2027-02-02', '2027-02-02', 'werk', 'OR Arbo', 'Amersfoort, Leerhotel Het Klooster', 'Arbocongres voor de medezeggenschap met workshops over werkdruk, verzuim, duurzame inzetbaarheid en de RI&E.', 'OR-leden en preventiemedewerkers', 'https://performa-or.nl/product/or-arbo/'),
 ('2027-02-10', '2027-02-10', 'leefstijl', 'Brein college met Erik Scherder', 'Ede, ReeHorst', 'Collegedag over gezonde hersenen, voeding en leefstijl.', 'Zorgprofessionals', 'https://events.bsl.nl/event/brein-college-voorjaar/'),
 ('2027-03-01', '2027-03-04', 'leefstijl', 'Arts en Leefstijl Week', 'Online en Driebergen, Antropia', 'Drie online avonden en een congresdag op 4 maart over leefstijl en preventie in de zorg.', 'Artsen, zorgprofessionals en beleidsmakers', 'https://www.artsenleefstijl.nl/academy/congres'),
 ('2027-03-05', '2027-03-05', 'leefstijl', 'Nationaal Obesitas Congres', 'Barneveld, Midden Nederland Hallen', 'Congres met praktische inzichten voor de zorg bij overgewicht en obesitas.', 'Zorgprofessionals', 'https://www.obesitascongres.nl/'),
 ('2027-03-08', '2027-03-08', 'werk', 'Werkgelukcongres', 'Utrecht', 'Derde editie van het congres voor professionals in werkgeluk, met sprekers en voorbeelden uit de praktijk.', 'HR, leidinggevenden en coaches', 'https://werkgelukcongres.nl/'),
 ('2027-03-11', '2027-03-11', 'leefstijl', 'Nationale Voedingscongres', 'Ede, ReeHorst', 'Jaarlijks congres over voeding en voedingszorg in de praktijk.', 'Diëtisten, verpleegkundigen en artsen', 'https://www.interactiegroep.nl/en/product/nvc/'),
 ('2027-03-11', '2027-03-11', 'zorg', 'Innovation for Health', 'Utrecht, Jaarbeurs', 'Engelstalige conferentie over innovatie in gezondheid en zorg.', 'Ondernemers, onderzoekers en zorgbestuurders', 'https://www.hyphenprojects.nl/i4h/'),
 ('2027-03-12', '2027-03-12', 'werk', 'Nationale Vitaliteitsdag', 'Zeist, Better Meetings', 'Congresdag over leiderschap en de vitale organisatie. Thema: Leiderschap in Balans.', 'HR, directeuren en managers', 'https://www.nationalevitaliteitsdag.nl/'),
 ('2027-03-18', '2027-03-18', 'zorg', 'Health Valley Event', 'Nijmegen, De Vasim', 'Congres en netwerkdag over innovatie in zorg en welzijn.', 'Zorgprofessionals, ondernemers en onderzoekers', 'https://www.healthvalley.nl/nl/events/health-valley-event-2027/'),
 ('2027-03-23', '2027-03-23', 'leefstijl', 'Verbindingsdag Positieve Gezondheid', 'Cuijk, Inspyrium', 'Dag van het Institute for Positive Health om elkaar te ontmoeten en kennis te delen.', 'Professionals die met Positieve Gezondheid werken', 'https://www.iph.nl/evenementen/23-maart-2027-samen-op-pad-met-positieve-gezondheid-verbindingsdag-iph/'),
 ('2027-04-07', '2027-04-08', 'werk', 'NVvA Symposium', 'Locatie volgt', 'Tweedaags symposium over arbeidshygiëne en gezond werken.', 'Arbeidshygiënisten en arboprofessionals', 'https://arbeidshygiene.nl/symposium/'),
 ('2027-04-08', '2027-04-08', 'werk', 'Landelijke VGWM-Dag', 'Nieuwegein, NBC Congrescentrum', 'Dag over veiligheid, gezondheid, welzijn en milieu voor de medezeggenschap.', 'OR-leden en VGWM-commissies', 'https://ornetacademy.nl/events/landelijke-vgwm-dag'),
 ('2027-04-13', '2027-04-15', 'werk', 'Zorg & HR', 'Utrecht, Jaarbeurs', 'Vakbeurs over personeel in de zorg: tekorten, werkdruk, werkplezier, vitaliteit en leiderschap.', 'HR en leidinggevenden in de zorg', 'https://www.zorg-en-hr.nl/'),
 ('2027-04-13', '2027-04-15', 'zorg', 'Zorg & ict', 'Utrecht, Jaarbeurs', 'Driedaagse vakbeurs over technologie en digitale zorg.', 'Zorgprofessionals, ICT en zorgbestuurders', 'https://www.zorg-en-ict.nl/'),
 ('2027-04-21', '2027-04-22', 'werk', 'WorkPlace Xperience', 'Utrecht, Jaarbeurs', 'Beurs over de gezonde en prettige werkomgeving.', 'Facilitair managers en HR', 'https://www.workplacexperience.nl/'),
 ('2027-06-21', '2027-06-24', 'zorg', 'HLTH Europe', 'Amsterdam, RAI', 'Internationaal Engelstalig evenement over innovatie in gezondheid en zorg.', 'Zorgbestuurders, bedrijven en investeerders', 'https://hlth.com/events/europe/'),
 ('2027-09-17', '2027-09-17', 'werk', 'Aftrap Nationale Vitaliteitsweek', 'Eindhoven', 'Bijeenkomst op vrijdagmiddag als start van de Nationale Vitaliteitsweek.', 'Werkgevers, HR en vitaliteitscoördinatoren', 'https://www.nationalevitaliteitsweek.nl/'),
 ('2027-09-28', '2027-09-28', 'werk', 'Jaarcongres HRM in de Zorg', "'s-Hertogenbosch, Congrescentrum 1931", 'Jaarcongres over HR in de zorg, met thema\'s als behoud van personeel, werkdruk en duurzame inzetbaarheid.', 'HR, bestuurders en managers in de zorg', 'https://www.hrmindezorg.nl/'),
]
# (naam, wanneer meestal, organisator, link)
EVENTS_VOLGT = [
 ('BG-dagen voor bedrijfsartsen', 'mei', 'NVAB', 'https://nvab-online.nl/bg-dagen/'),
 ('Landelijk Congres Mentale Gezondheid', 'juni', 'Missie Mentaal', 'https://missiementaal.com/landelijk-congres-mentale-gezondheid'),
 ('Congres Dag van de preventie', 'mei', 'Zorgvisie', 'https://congressen.zorgvisie.nl/event/congres-dag-van-de-preventie/'),
 ('Doorzaam congres over duurzame inzetbaarheid in de uitzendbranche', 'maart', 'Doorzaam', 'https://www.doorzaam.nl/over-doorzaam/congres/'),
 ('Nationaal Sportcongres', 'juni', 'Vereniging Sport en Gemeenten en NOC*NSF', 'https://sportengemeenten.nl/agenda-item/nationaal-sportcongres-2/'),
 ('Congres Van zorg naar bewegen', 'juni', 'Kenniscentrum Sport & Bewegen', 'https://www.kenniscentrumsportenbewegen.nl/congres-van-zorg-naar-bewegen/'),
 ('Nationaal Arbocongres 2027', 'november', 'Rendement', 'https://www.rendementco.nl/id94-nationaal-arbo-congres.html'),
 ('Hét Leefstijl Symposium 2027', 'oktober', 'Stichting TWINZ', 'https://www.leefstijlsymposium.nl/'),
]

# ---------------------------------------------------------------- 2. Dagen en weken van
# (start, eind, vorm, thema, naam, beschrijving, link, intern)
# vorm: dag | week | maand | periode ; thema: werk mentaal leefstijl bewegen voeding slaap zorg ziekte
D = 'dag'
DAGEN = [
 ('2026-10-01', '2026-10-28', 'periode', 'leefstijl', 'Stoptober', 'Landelijke actie waarbij rokers samen 28 dagen stoppen met roken.', 'https://stoptober.nl/doe-mee/'),
 ('2026-10-01', '2026-10-31', 'maand', 'ziekte', 'Borstkankermaand', 'Maand waarin Pink Ribbon aandacht vraagt voor borstkanker.', 'https://www.kwf.nl/nieuws/pink-ribbon-helpt-nederland-woorden-vinden-bij-borstkanker'),
 ('2026-10-03', '2026-10-10', 'week', 'zorg', 'Week van de Palliatieve Zorg', 'Week met activiteiten en voorlichting over zorg in de laatste levensfase.', 'https://overpalliatievezorg.nl/agenda/week-van-de-palliatieve-zorg-2026'),
 ('2026-10-08', '', D, 'ziekte', 'Wereld Dag van het Zicht', 'Aandacht voor gezonde ogen en het voorkomen van slechtziendheid.', 'https://www.iapb.org/world-sight-day/'),
 ('2026-10-10', '', D, 'mentaal', 'Werelddag Psychische Gezondheid', 'Wereldwijde dag om psychische gezondheid bespreekbaar te maken, ook op het werk.', 'https://www.who.int/campaigns/world-mental-health-day'),
 ('2026-10-10', '', D, 'zorg', 'Internationale Dag van de Palliatieve Zorg', 'Aandacht voor goede zorg en steun in de laatste levensfase.', 'https://thewhpca.org/'),
 ('2026-10-12', '', D, 'ziekte', 'Wereld Reumadag', 'Aandacht voor reuma en de gevolgen voor werk en dagelijks leven.', 'https://reumanederland.nl/'),
 ('2026-10-15', '', D, 'ziekte', 'Wereld Handenwasdag', 'Handen wassen met zeep als eenvoudige manier om infecties te voorkomen.', 'https://globalhandwashing.org/global-handwashing-day/'),
 ('2026-10-16', '', D, 'voeding', 'Wereldvoedseldag', 'Aandacht voor gezond en voldoende voedsel voor iedereen.', 'https://www.fao.org/world-food-day'),
 ('2026-10-16', '', D, 'ziekte', 'Wereld Reanimatiedag', 'Oproep om te leren reanimeren en een AED te gebruiken.', 'https://www.ilcor.org/'),
 ('2026-10-18', '', D, 'leefstijl', 'Wereld Menopauzedag', 'Aandacht voor de overgang en wat die betekent voor gezondheid en werk.', 'https://www.imsociety.org/education/world-menopause-day/'),
 ('2026-10-19', '2026-10-24', 'week', 'werk', 'Europese Week voor Veiligheid en Gezondheid op het Werk', 'Europese week over veilig en gezond werken. Dit jaar over mentale gezondheid op het werk.', 'https://osha.europa.eu/en/oshevents'),
 ('2026-10-20', '', D, 'ziekte', 'Wereld Osteoporose Dag', 'Aandacht voor sterke botten en het voorkomen van botontkalking.', 'https://www.worldosteoporosisday.org/'),
 ('2026-10-25', '', D, 'mentaal', 'Dag van de Stilte', 'Dag om stil te staan bij rust en stilte in een drukke tijd.', 'https://dagvandestilte.nl/'),
 ('2026-10-27', '', D, 'zorg', 'Wereld Ergotherapie Dag', 'Aandacht voor ergotherapie en zelfstandig functioneren thuis en op het werk.', 'https://wfot.org/'),
 ('2026-10-29', '', D, 'ziekte', 'Wereld Beroertedag', 'Aandacht voor het herkennen en voorkomen van een beroerte.', 'https://www.world-stroke.org/world-stroke-day-campaign'),
 ('2026-10-29', '', D, 'zorg', 'Internationale Dag van Zorg en Ondersteuning', 'Erkenning van betaalde en onbetaalde zorg voor anderen.', 'https://www.un.org/en/observances/care-and-support-day'),
 ('2026-11-01', '2026-11-30', 'maand', 'ziekte', 'Movember', 'Maand waarin mannen een snor laten staan om aandacht te vragen voor de gezondheid van mannen.', 'https://nl.movember.com/'),
 ('2026-11-01', '', D, 'voeding', 'Wereld Veganisme Dag', 'Aandacht voor plantaardig eten.', 'https://www.vegansociety.com/'),
 ('2026-11-02', '', D, 'werk', 'Dag van de BHV', 'Waardering voor bedrijfshulpverleners die zorgen voor veiligheid op het werk.', 'https://www.101bhv.nl/dag-van-de-bhv/'),
 ('2026-11-04', '', D, 'mentaal', 'International Stress Awareness Day', 'Aandacht voor stress, de signalen en wat je eraan kunt doen.', 'https://isma.org.uk/'),
 ('2026-11-09', '2026-11-13', 'week', 'werk', 'Week van de Werkstress', 'Week waarin organisaties aandacht geven aan werkstress en werkplezier.', 'https://deweekvandewerkstress.nl/', ('artikelen/week-zonder-werkstress-ideeen', 'Lees mijn zeven ideeën voor deze week')),
 ('2026-11-10', '', D, 'zorg', 'Dag van de Mantelzorg', 'Waardering voor mensen die naast werk of gezin voor een naaste zorgen.', 'https://www.mantelzorg.nl/'),
 ('2026-11-14', '', D, 'ziekte', 'Wereld Diabetes Dag', 'Aandacht voor diabetes, vroege herkenning en leefstijl.', 'https://worlddiabetesday.org/'),
 ('2026-11-18', '', D, 'ziekte', 'Wereld COPD Dag', 'Aandacht voor de longziekte COPD en een vroege diagnose.', 'https://goldcopd.org/'),
 ('2026-11-19', '', D, 'leefstijl', 'Internationale Mannendag', 'Aandacht voor de gezondheid en het welzijn van mannen.', 'https://internationalmensday.com/'),
 ('2026-12-01', '', D, 'ziekte', 'Wereld Aids Dag', 'Aandacht voor hiv en aids en voor mensen die ermee leven.', 'https://www.who.int/campaigns/world-aids-day'),
 ('2026-12-03', '', D, 'werk', 'Internationale Dag van Mensen met een Beperking', 'Aandacht voor gelijke kansen en meedoen, ook op de werkvloer.', 'https://www.un.org/en/observances/day-of-persons-with-disabilities'),
 ('2026-12-12', '', D, 'zorg', 'Internationale Dag voor Gezondheidszorg voor Iedereen', 'Pleidooi voor toegankelijke en betaalbare zorg voor iedereen.', 'https://www.un.org/en/observances/universal-health-coverage-day'),
 ('2026-12-21', '', D, 'mentaal', 'Wereld Meditatie Dag', 'Aandacht voor meditatie als hulpmiddel voor rust en mentale gezondheid.', 'https://www.un.org/en/observances/meditation-day'),
 ('2027-01-01', '2027-01-31', 'maand', 'leefstijl', 'Dry January', 'Uitdaging van IkPas om in januari geen alcohol te drinken.', 'https://ikpas.nl/over-ons'),
 ('2027-01-18', '', D, 'mentaal', 'Blue Monday', 'Zogenaamd de somberste dag van het jaar. Niet wetenschappelijk, wel een aanleiding om over somberheid te praten.', 'https://www.beleven.org/feest/blue_monday'),
 ('2027-02-04', '', D, 'ziekte', 'Wereldkankerdag', 'Aandacht voor kanker, preventie en de mensen die ermee te maken hebben.', 'https://wereldkankerdag.nl/'),
 ('2027-02-08', '', D, 'ziekte', 'Internationale Epilepsie Dag', 'Aandacht voor epilepsie en begrip voor mensen die ermee leven.', 'https://internationalepilepsyday.org/'),
 ('2027-02-10', '2027-03-21', 'periode', 'leefstijl', 'IkPas: 40 dagen geen druppel', 'Uitdaging om in de vastentijd veertig dagen geen alcohol te drinken.', 'https://ikpas.nl/over-ons'),
 ('2027-02-28', '', D, 'ziekte', 'Zeldzame Ziektendag', 'Aandacht voor mensen met een zeldzame aandoening.', 'https://www.rarediseaseday.org/'),
 ('2027-02-28', '', D, 'werk', 'Internationale RSI Dag', 'Aandacht voor klachten aan arm, nek en schouder door werk.', 'https://www.rsi-vereniging.nl/'),
 ('2027-03-01', '', D, 'mentaal', 'Nationale Complimentendag', 'Dag om oprechte waardering uit te spreken, ook naar collega\'s.', 'https://www.nationalecomplimentendag.nl/'),
 ('2027-03-03', '', D, 'ziekte', 'Wereld Gehoordag', 'Aandacht voor goed horen en het voorkomen van gehoorschade.', 'https://www.who.int/campaigns/world-hearing-day'),
 ('2027-03-04', '', D, 'ziekte', 'Wereld Obesitas Dag', 'Aandacht voor obesitas als chronische ziekte en voor preventie zonder stigma.', 'https://www.worldobesityday.org/'),
 ('2027-03-04', '', D, 'zorg', 'Dag van de Doktersassistent', 'Waardering voor doktersassistenten, vaak het eerste aanspreekpunt in de zorg.', 'https://www.nvda.nl/dag-van-de-doktersassistent/'),
 ('2027-03-11', '', D, 'ziekte', 'Wereld Nierdag', 'Aandacht voor gezonde nieren en het vroeg opsporen van nierschade.', 'https://www.worldkidneyday.org/'),
 ('2027-03-19', '', D, 'slaap', 'Wereld Slaapdag', 'Aandacht voor het belang van goede slaap voor gezondheid en functioneren.', 'https://worldsleepday.org/'),
 ('2027-03-20', '', D, 'mentaal', 'Internationale Dag van het Geluk', 'Aandacht voor geluk en welzijn als doel voor mens en samenleving.', 'https://www.un.org/en/observances/happiness-day'),
 ('2027-03-20', '', D, 'ziekte', 'Wereld Mondgezondheidsdag', 'Aandacht voor een gezonde mond als onderdeel van je gezondheid.', 'https://www.worldoralhealthday.org/'),
 ('2027-03-21', '', D, 'zorg', 'Wereld Downsyndroomdag', 'Aandacht voor mensen met downsyndroom en hun plek in de samenleving.', 'https://www.un.org/en/observances/down-syndrome-day'),
 ('2027-03-24', '', D, 'werk', 'Bewust Veilig-dag', 'Dag waarop bouw en techniek stilstaan bij veilig werken.', 'https://bewustveilig.com/'),
 ('2027-03-30', '', D, 'mentaal', 'Wereld Bipolaire Dag', 'Aandacht voor de bipolaire stoornis en het doorbreken van het taboe.', 'https://www.worldbipolarday.org/'),
 ('2027-04-02', '', D, 'mentaal', 'Wereld Autisme Dag', 'Aandacht voor autisme en voor meedoen in werk en samenleving.', 'https://www.un.org/en/observances/autism-day'),
 ('2027-04-06', '', D, 'bewegen', 'Internationale Dag van de Sport', 'Aandacht voor wat sport en bewegen betekenen voor gezondheid en verbinding.', 'https://www.un.org/en/observances/sport-day'),
 ('2027-04-07', '', D, 'leefstijl', 'Wereldgezondheidsdag', 'Jaarlijkse dag van de Wereldgezondheidsorganisatie met elk jaar een eigen thema.', 'https://www.who.int/campaigns/world-health-day'),
 ('2027-04-08', '', D, 'bewegen', 'Wandel Tijdens Je Werkdag', 'Oproep aan werkend Nederland om tijdens de werkdag een wandeling te maken.', 'https://www.wandelnet.nl/wandel-tijdens-je-werkdag'),
 ('2027-04-11', '', D, 'ziekte', 'Wereld Parkinsondag', 'Aandacht voor de ziekte van Parkinson en voor onderzoek.', 'https://www.parkinson-vereniging.nl/'),
 ('2027-04-19', '', D, 'mentaal', 'Landelijke Dag tegen Pesten', 'Aandacht voor pesten op school, online en op het werk.', 'https://www.stoppestennu.nl/'),
 ('2027-04-28', '', D, 'werk', 'Werelddag voor Veiligheid en Gezondheid op het Werk', 'Aandacht voor het voorkomen van ongevallen en ziekte door werk.', 'https://www.un.org/en/observances/work-safety-day'),
 ('2027-05-04', '', D, 'ziekte', 'Wereld Astma Dag', 'Aandacht voor astma en een goede behandeling.', 'https://ginasthma.org/'),
 ('2027-05-05', '', D, 'zorg', 'Wereld Handhygiënedag', 'Aandacht voor schone handen in de zorg om infecties te voorkomen.', 'https://www.who.int/campaigns/world-hand-hygiene-day'),
 ('2027-05-05', '', D, 'zorg', 'Internationale Dag van de Verloskundige', 'Waardering voor het werk van verloskundigen.', 'https://internationalmidwives.org/'),
 ('2027-05-12', '', D, 'zorg', 'Dag van de Zorg', 'Waardering voor verpleegkundigen, verzorgenden en andere zorgmedewerkers. Ook bekend als Dag van de Verpleging.', 'https://www.icn.ch/'),
 ('2027-05-17', '', D, 'ziekte', 'Wereld Hypertensie Dag', 'Oproep om je bloeddruk te kennen en hoge bloeddruk te voorkomen.', 'https://www.whleague.org/'),
 ('2027-05-19', '', D, 'zorg', 'Wereld Huisartsendag', 'Waardering voor huisartsen en hun rol in de zorg dicht bij huis.', 'https://www.globalfamilydoctor.com/'),
 ('2027-05-24', '2027-05-28', 'week', 'bewegen', 'Nationale Beweegweek', 'Week van het Ouderenfonds waarin ouderen samen in beweging komen.', 'https://ouderenfonds.nl/activiteit/nationale-beweegweek/'),
 ('2027-05-30', '', D, 'ziekte', 'Wereld MS Dag', 'Aandacht voor multiple sclerose en voor leven en werken met MS.', 'https://worldmsday.org/'),
 ('2027-05-31', '', D, 'leefstijl', 'Wereld Niet Roken Dag', 'Aandacht voor de schade van roken en hulp bij stoppen.', 'https://www.who.int/campaigns/world-no-tobacco-day'),
 ('2027-06-03', '', D, 'bewegen', 'Wereld Fietsdag', 'Aandacht voor de fiets als gezond en duurzaam vervoermiddel.', 'https://www.un.org/en/observances/bicycle-day'),
 ('2027-06-07', '', D, 'voeding', 'Wereld Voedselveiligheidsdag', 'Aandacht voor veilig voedsel en het voorkomen van voedselinfecties.', 'https://www.who.int/campaigns/world-food-safety-day'),
 ('2027-06-14', '', D, 'zorg', 'Wereld Bloeddonordag', 'Dank aan bloeddonoren en een oproep om donor te worden.', 'https://www.who.int/campaigns/world-blood-donor-day'),
 ('2027-06-21', '', D, 'bewegen', 'Internationale Dag van de Yoga', 'Aandacht voor yoga als manier om lichaam en geest gezond te houden.', 'https://www.un.org/en/observances/yoga-day'),
 ('2027-06-26', '', D, 'ziekte', 'Internationale Dag tegen Drugsmisbruik', 'Aandacht voor het voorkomen van verslaving en de gevolgen van drugsgebruik.', 'https://www.un.org/en/observances/end-drug-abuse-day'),
 ('2027-07-24', '', D, 'leefstijl', 'Internationale Dag van de Zelfzorg', 'Aandacht voor wat je zelf elke dag kunt doen voor je gezondheid.', 'https://www.selfcarefederation.org/news-events/happy-international-self-care-day-2026'),
 ('2027-07-28', '', D, 'ziekte', 'Wereld Hepatitis Dag', 'Aandacht voor leverontsteking door hepatitis, testen en behandeling.', 'https://www.who.int/campaigns/world-hepatitis-day'),
 ('2027-09-10', '', D, 'mentaal', 'Wereld Suïcidepreventiedag', 'Aandacht voor het voorkomen van zelfdoding en het bespreekbaar maken ervan.', 'https://www.who.int/campaigns/world-suicide-prevention-day'),
 ('2027-09-11', '', D, 'ziekte', 'Wereld Eerste Hulp Dag', 'Aandacht voor het belang van eerste hulp kunnen verlenen.', 'https://www.rodekruis.nl/'),
 ('2027-09-13', '', D, 'ziekte', 'Wereld Sepsis Dag', 'Aandacht voor het snel herkennen van sepsis, ook wel bloedvergiftiging.', 'https://www.worldsepsisday.org/'),
 ('2027-09-16', '2027-09-22', 'week', 'bewegen', 'Europese Mobiliteitsweek', 'Europese week die lopen, fietsen en schoon vervoer naar werk en school stimuleert.', 'https://mobilityweek.eu/home/'),
 ('2027-09-17', '', D, 'zorg', 'Wereld Patiëntveiligheidsdag', 'Aandacht voor veilige zorg en het voorkomen van vermijdbare schade.', 'https://www.who.int/campaigns/world-patient-safety-day'),
 ('2027-09-20', '2027-09-26', 'week', 'werk', 'Nationale Vitaliteitsweek', 'Dertiende editie van de week waarin werkgevers activiteiten rond vitaliteit organiseren.', 'https://www.nationalevitaliteitsweek.nl/', ('trainingen#workshops', 'Bekijk mijn inspiratiesessies voor deze week')),
 ('2027-09-21', '', D, 'ziekte', 'Wereld Alzheimer Dag', 'Aandacht voor dementie en voor de mensen die ervoor zorgen.', 'https://www.alzheimer-nederland.nl/'),
 ('2027-09-25', '', D, 'zorg', 'Wereld Apothekersdag', 'Waardering voor apothekers en hun bijdrage aan goed medicijngebruik.', 'https://www.fip.org/world-pharmacists-day'),
 ('2027-09-29', '', D, 'ziekte', 'Wereld Hart Dag', 'Aandacht voor een gezond hart en het voorkomen van hart- en vaatziekten.', 'https://world-heart-federation.org/world-heart-day/'),
 ('2027-10-01', '2027-10-28', 'periode', 'leefstijl', 'Stoptober', 'Landelijke actie waarbij rokers samen 28 dagen stoppen met roken.', 'https://stoptober.nl/doe-mee/'),
 ('2027-10-01', '2027-10-31', 'maand', 'ziekte', 'Borstkankermaand', 'Maand waarin Pink Ribbon aandacht vraagt voor borstkanker.', 'https://www.kwf.nl/nieuws/pink-ribbon-helpt-nederland-woorden-vinden-bij-borstkanker'),
 ('2027-10-01', '', D, 'leefstijl', 'Internationale Dag van de Ouderen', 'Aandacht voor de bijdrage en het welzijn van ouderen.', 'https://www.un.org/en/observances/older-persons-day'),
 ('2027-10-01', '', D, 'mentaal', 'Nationale Ouderendag', 'Dag waarop wensen van ouderen in vervulling gaan, tegen eenzaamheid.', 'https://ouderenfonds.nl/activiteit/nationale-ouderendag/'),
 ('2027-10-01', '', D, 'voeding', 'Wereld Vegetarisme Dag', 'Aandacht voor vegetarisch eten.', 'https://www.vegetariers.nl/'),
 ('2027-10-09', '', D, 'zorg', 'Internationale Dag van de Palliatieve Zorg', 'Aandacht voor goede zorg en steun in de laatste levensfase.', 'https://thewhpca.org/'),
 ('2027-10-10', '', D, 'mentaal', 'Werelddag Psychische Gezondheid', 'Wereldwijde dag om psychische gezondheid bespreekbaar te maken, ook op het werk.', 'https://www.who.int/campaigns/world-mental-health-day'),
 ('2027-10-12', '', D, 'ziekte', 'Wereld Reumadag', 'Aandacht voor reuma en de gevolgen voor werk en dagelijks leven.', 'https://reumanederland.nl/'),
 ('2027-10-14', '', D, 'ziekte', 'Wereld Dag van het Zicht', 'Aandacht voor gezonde ogen en het voorkomen van slechtziendheid.', 'https://www.iapb.org/world-sight-day/'),
 ('2027-10-15', '', D, 'ziekte', 'Wereld Handenwasdag', 'Handen wassen met zeep als eenvoudige manier om infecties te voorkomen.', 'https://globalhandwashing.org/global-handwashing-day/'),
 ('2027-10-16', '', D, 'voeding', 'Wereldvoedseldag', 'Aandacht voor gezond en voldoende voedsel voor iedereen.', 'https://www.fao.org/world-food-day'),
 ('2027-10-16', '', D, 'ziekte', 'Wereld Reanimatiedag', 'Oproep om te leren reanimeren en een AED te gebruiken.', 'https://www.ilcor.org/'),
 ('2027-10-18', '', D, 'leefstijl', 'Wereld Menopauzedag', 'Aandacht voor de overgang en wat die betekent voor gezondheid en werk.', 'https://www.imsociety.org/education/world-menopause-day/'),
 ('2027-10-20', '', D, 'ziekte', 'Wereld Osteoporose Dag', 'Aandacht voor sterke botten en het voorkomen van botontkalking.', 'https://www.worldosteoporosisday.org/'),
 ('2027-10-27', '', D, 'zorg', 'Wereld Ergotherapie Dag', 'Aandacht voor ergotherapie en zelfstandig functioneren thuis en op het werk.', 'https://wfot.org/'),
 ('2027-10-29', '', D, 'ziekte', 'Wereld Beroertedag', 'Aandacht voor het herkennen en voorkomen van een beroerte.', 'https://www.world-stroke.org/world-stroke-day-campaign'),
 ('2027-10-29', '', D, 'zorg', 'Internationale Dag van Zorg en Ondersteuning', 'Erkenning van betaalde en onbetaalde zorg voor anderen.', 'https://www.un.org/en/observances/care-and-support-day'),
 ('2027-10-31', '', D, 'mentaal', 'Dag van de Stilte', 'Dag om stil te staan bij rust en stilte in een drukke tijd.', 'https://dagvandestilte.nl/'),
]
# (naam, wanneer meestal, thema, link)
DAGEN_VOLGT = [
 ('Week van het Werkgeluk', 'tweede helft van september', 'werk', 'https://weekvanhetwerkgeluk.nl/'),
 ('Week van de Werkstress 2027', 'november', 'werk', 'https://deweekvandewerkstress.nl/'),
 ('Europese Week voor Veiligheid en Gezondheid op het Werk 2027', 'tweede helft van oktober', 'werk', 'https://osha.europa.eu/en/oshevents'),
 ('Week van de Mentale Gezondheid', 'eerste week van juni', 'mentaal', 'https://missiementaal.com/de-week'),
 ('Week van de Psychiatrie', 'eind maart', 'mentaal', 'https://mindplatform.nl/project/week-van-de-psychiatrie'),
 ('Autismeweek', 'rond 2 april', 'mentaal', 'https://www.ruimtevoorautisme.nl/'),
 ('Week tegen Eenzaamheid', 'eind september', 'mentaal', 'https://www.eentegeneenzaamheid.nl/gemeenten-en-organisaties/week-tegen-eenzaamheid'),
 ('Week van de Overgang', 'april', 'leefstijl', 'https://overacademie.nl/overzicht/'),
 ('Nationale Week Zonder Vlees & Zuivel', 'maart', 'voeding', 'https://issuekalender.nl/issue/nationale-week-zonder-vlees-en-zuivel/'),
 ('Fiets naar je Werk Dag', 'tweede helft van mei', 'bewegen', 'https://fietsnaarjewerkdag.fiscfree.nl/'),
 ('Nationale Sportweek', 'tweede helft van september', 'bewegen', 'https://nocnsf.nl/nationale-sportweek/ontdek/wat-is-de-nationale-sportweek'),
 ('Steptember', 'september', 'bewegen', 'https://cpnederland.nl/steptember-dagelijks-10-000-stappen-voor-mensen-met-cerebrale-parese/'),
 ('Week van de Jonge Mantelzorger', 'begin juni', 'zorg', 'https://www.weekvandejongemantelzorger.nl/'),
 ('Week van de Palliatieve Zorg 2027', 'begin oktober', 'zorg', 'https://overpalliatievezorg.nl/leventothetlaatst'),
 ('Dress Red Day', 'eind september', 'ziekte', 'https://www.hartstichting.nl/hart-en-vaatziekten/vrouwen-en-hart-en-vaatziekten/dress-red-day'),
]

SOORT = {'werk': 'Werk en vitaliteit', 'leefstijl': 'Leefstijl en preventie', 'zorg': 'Zorg en innovatie'}
THEMA = {'werk': 'Werk', 'mentaal': 'Mentaal', 'leefstijl': 'Leefstijl', 'bewegen': 'Bewegen', 'voeding': 'Voeding', 'slaap': 'Slaap', 'zorg': 'Zorg', 'ziekte': 'Ziekte en preventie'}
VORM = {'dag': 'Dag', 'week': 'Week', 'maand': 'Maand', 'periode': 'Actie'}

# ---------------------------------------------------------------- controles
REGELS = {  # naam -> (weekdag ma=0, welke in de maand; -1 = laatste)
 'Wereld Dag van het Zicht': (3, 2), 'Internationale Dag van de Palliatieve Zorg': (5, 2), 'Dag van de Stilte': (6, -1), 'Dag van de BHV': (0, 1),
 'International Stress Awareness Day': (2, 1), 'Wereld COPD Dag': (2, 3), 'Blue Monday': (0, 3), 'Internationale Epilepsie Dag': (0, 2),
 'Dag van de Doktersassistent': (3, 1), 'Wereld Nierdag': (3, 2), 'Wereld Astma Dag': (1, 1), 'Wereld Eerste Hulp Dag': (5, 2), 'Nationale Ouderendag': (4, 1),
}
def nde(jaar, maand, weekdag, n):
    dagen = [dt.date(jaar, maand, d) for d in range(1, 32) if d <= (dt.date(jaar + (maand == 12), maand % 12 + 1, 1) - dt.timedelta(days=1)).day and dt.date(jaar, maand, d).weekday() == weekdag]
    return dagen[n - 1] if n > 0 else dagen[-1]
for r in DAGEN:
    s = dt.date.fromisoformat(r[0]); e = dt.date.fromisoformat(r[1]) if r[1] else s
    assert e >= s, r
    assert dt.date(2026, 10, 1) <= s <= dt.date(2027, 10, 31), r
    assert r[3] in THEMA and r[2] in VORM, r
    if r[4] in REGELS:
        wd, n = REGELS[r[4]]
        assert nde(s.year, s.month, wd, n) == s, ('regel klopt niet', r[4], s, nde(s.year, s.month, wd, n))
assert dt.date(2027, 3, 19).weekday() == 4  # Wereld Slaapdag op vrijdag
assert dt.date(2027, 2, 10) + dt.timedelta(days=46) == dt.date(2027, 3, 28)  # Aswoensdag + 46 = Pasen
for r in EVENTS:
    s = dt.date.fromisoformat(r[0]); e = dt.date.fromisoformat(r[1]); assert e >= s and r[2] in SOORT, r
    assert dt.date(2026, 10, 6) <= s <= dt.date(2027, 10, 31), r
assert EVENTS == sorted(EVENTS, key=lambda r: (r[0], r[1])), 'events niet op datum'
assert [x[0] for x in DAGEN] == sorted(x[0] for x in DAGEN), 'dagen niet op datum'

# ---------------------------------------------------------------- opbouw
E = html.escape
# Pictogrammen (eigen lijntekeningen), één keer in de pagina en daarna hergebruikt
ICONEN = {
 'werk': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
 'leefstijl': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
 'zorg': '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M12 8v8M8 12h8"/>',
 'mentaal': '<circle cx="12" cy="12" r="9"/><path d="M8.5 14.5a4 4 0 0 0 7 0M9 9.5h.01M15 9.5h.01"/>',
 'bewegen': '<path d="M3 12h4l3-7 4 14 3-7h4"/>',
 'voeding': '<path d="M12 7.5c-2-1.6-6-1-6 4 0 4 2.5 8 4.5 8 .8 0 1-.4 1.5-.4s.7.4 1.5.4c2 0 4.5-4 4.5-8 0-5-4-5.6-6-4zM12 7.5c0-2 1-3.5 3-4"/>',
 'slaap': '<path d="M20 14.5A8 8 0 1 1 9.5 4 6.5 6.5 0 0 0 20 14.5z"/>',
 'ziekte': '<path d="M12 3l7 3v6c0 4.500-3 7.500-7 9-4-1.500-7-4.500-7-9V6z"/><path d="M9 12l2 2 4-4"/>',
 'plaats': '<path d="M12 21s-6-5.600-6-10.500a6 6 0 0 1 12 0C18 15.400 12 21 12 21z"/><circle cx="12" cy="10.500" r="2"/>',
 'mensen': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.300 2.700-6 6-6s6 2.700 6 6M16 5.200a3 3 0 0 1 0 5.600M18 14.300c1.800.9 3 2.700 3 5.700"/>',
 'kalender': '<rect x="3.500" y="5" width="17" height="15.500" rx="2.500"/><path d="M3.500 10h17M8 3v4M16 3v4"/>',
 'klok': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'vlag': '<path d="M5 21V4M5 4h12l-2.500 4 2.500 4H5"/>',
 'kaartje': '<path d="M3 9a3 3 0 0 0 0 6v3h18v-3a3 3 0 0 1 0-6V6H3z"/><path d="M14 9v1.500M14 13.500V15"/>',
 'alles': '<rect x="4" y="4" width="6.500" height="6.500" rx="1.500"/><rect x="13.500" y="4" width="6.500" height="6.500" rx="1.500"/><rect x="4" y="13.500" width="6.500" height="6.500" rx="1.500"/><rect x="13.500" y="13.500" width="6.500" height="6.500" rx="1.500"/>',
}
SPRITE = '<svg class="kal-sprite" aria-hidden="true" focusable="false">' + ''.join('<symbol id="i-%s" viewBox="0 0 24 24">%s</symbol>' % (k, v.replace('.500', '.5').replace('.600', '.6').replace('.400', '.4').replace('.300', '.3').replace('.200', '.2').replace('.700', '.7')) for k, v in ICONEN.items()) + '</svg>'
def ic(naam): return '<svg class="kal-ic" aria-hidden="true"><use href="#i-%s"/></svg>' % naam

def tekening():
    # Kalenderblad met gekleurde dagen, als versiering naast de titel
    kleuren = {(0, 2): '#3aa5b2', (0, 5): '#f0a830', (1, 1): '#e8742c', (1, 4): '#7a6bb8', (2, 0): '#4f9d69', (2, 3): '#23406e', (2, 6): '#d2567a', (3, 2): '#f0a830', (3, 5): '#3aa5b2'}
    h = '<svg class="kal-tekening" viewBox="0 0 300 250" aria-hidden="true" focusable="false">'
    h += '<rect x="34" y="40" width="250" height="200" rx="22" fill="#f0a830"/><rect x="16" y="24" width="250" height="200" rx="22" fill="#fff"/>'
    h += '<path d="M16 46a22 22 0 0 1 22-22h206a22 22 0 0 1 22 22v24H16z" fill="#23406e"/>'
    for x in (78, 141, 204):
        h += '<rect x="%d" y="10" width="10" height="30" rx="5" fill="#5b8fc7"/>' % x
    for r in range(4):
        for k in range(7):
            x = 34 + k * 31.5; y = 86 + r * 32
            kl = kleuren.get((r, k))
            h += '<rect x="%.1f" y="%d" width="24" height="24" rx="7" fill="%s"/>' % (x, y, kl or '#e9eef7')
    h += '<path d="M103.5 108.5l3.500 3.500 6.500-7" fill="none" stroke="#fff" stroke-width="2.600" stroke-linecap="round" stroke-linejoin="round"/>'.replace('.500', '.5').replace('.600', '.6')
    h += '<path d="M140.5 169.500s-5.500-3.400-5.500-7.600a3 3 0 0 1 5.500-1.800 3 3 0 0 1 5.500 1.800c0 4.200-5.500 7.600-5.500 7.600z" fill="#fff"/>'.replace('.500', '.5')
    return h + '</svg>'
def datumtekst(s, e, vorm=None):
    s = dt.date.fromisoformat(s); e = dt.date.fromisoformat(e) if e else s
    if vorm == 'maand':
        return 'hele', 'maand'
    if s == e:
        return str(s.day), MK[s.month - 1]
    if s.month == e.month:
        return ('%d en %d' if (e - s).days == 1 else '%d t/m %d') % (s.day, e.day), MK[s.month - 1]
    return '%d %s t/m' % (s.day, MK[s.month - 1]), '%d %s' % (e.day, MK[e.month - 1])
def lang(s, e):
    s = dt.date.fromisoformat(s); e = dt.date.fromisoformat(e) if e else s
    if s == e: return '%d %s %d' % (s.day, MND[s.month - 1], s.year)
    if s.month == e.month: return '%d tot en met %d %s %d' % (s.day, e.day, MND[s.month - 1], s.year)
    return '%d %s tot en met %d %s %d' % (s.day, MND[s.month - 1], e.day, MND[e.month - 1], e.year)

def per_maand(rijen, maak):
    uit = []; huidig = None
    for r in rijen:
        s = dt.date.fromisoformat(r[0]); sleutel = (s.year, s.month)
        if sleutel != huidig:
            if huidig: uit.append('        </ul>\n      </div>')
            uit.append('      <div class="kal-maand">\n        <h3><span class="kal-rond">' + ic('kalender') + '</span>%s <span class="kal-jaar">%d</span></h3>\n        <ul class="kal-lijst">' % (MND[s.month - 1].capitalize(), s.year))
            huidig = sleutel
        uit.append(maak(r))
    uit.append('        </ul>\n      </div>')
    return '\n'.join(uit)

def event_li(r):
    s, e, soort, naam, plaats, tekst, voor, url = r
    a, b = datumtekst(s, e)
    return ('          <li class="kal-item" data-eind="%s" data-groep="%s">\n'
            '            <p class="kal-datum%s" aria-label="%s"><span>%s</span><span>%s</span></p>\n'
            '            <div class="kal-tekst">\n'
            '              <p class="kal-label k-%s">%s%s</p>\n'
            '              <h4><a href="%s" target="_blank" rel="noopener">%s</a></h4>\n'
            '              <p class="kal-plaats">%s<span>%s</span></p>\n'
            '              <p>%s</p>\n'
            '              <p class="kal-voor">%s<span><strong>Voor wie:</strong> %s</span></p>\n'
            '              <p class="kal-link"><a href="%s" target="_blank" rel="noopener">Informatie en aanmelden <span aria-hidden="true">→</span></a></p>\n'
            '            </div>\n          </li>') % (e, soort, ' lang' if len(a) > 2 else '', E(lang(s, e)), a, b, soort, ic(soort), SOORT[soort], E(url), E(naam), ic('plaats'), E(plaats), E(tekst), ic('mensen'), E(voor), E(url))

def dag_li(r):
    s, e, vorm, thema, naam, tekst, url = r[:7]
    intern = r[7] if len(r) > 7 else None
    a, b = datumtekst(s, e, vorm)
    extra = ' <a class="kal-intern" href="%s">%s</a>' % intern if intern else ''
    return ('          <li class="kal-item klein" data-eind="%s" data-groep="%s">\n'
            '            <p class="kal-datum%s" aria-label="%s"><span>%s</span><span>%s</span></p>\n'
            '            <div class="kal-tekst">\n'
            '              <h4><a href="%s" target="_blank" rel="noopener">%s</a> <span class="kal-vorm">%s</span></h4>\n'
            '              <p>%s%s</p>\n'
            '              <p class="kal-label t-%s">%s%s</p>\n'
            '            </div>\n          </li>') % (e or s, thema, ' lang' if len(a) > 2 else '', E(lang(s, e) if vorm != 'maand' else MND[int(s[5:7]) - 1] + ' ' + s[:4]), a, b, E(url), E(naam), VORM[vorm], E(tekst), extra, thema, ic(thema), THEMA[thema])

def knoppen(groepen, naam):
    h = '      <div class="kal-filter" role="group" aria-label="%s">\n        <button type="button" class="actief" aria-pressed="true" data-filter="alles">%sAlles</button>\n' % (naam, ic('alles'))
    for k, v in groepen.items():
        h += '        <button type="button" aria-pressed="false" data-filter="%s">%s%s</button>\n' % (k, ic(k), v)
    return h + '      </div>'

def volgt(rijen, soort):
    h = '      <ul class="kal-volgt">\n'
    for r in rijen:
        if soort == 'event':
            naam, wanneer, org, url = r
            h += '        <li>%s<span class="kal-volgt-tekst"><a href="%s" target="_blank" rel="noopener">%s</a><span>Meestal in %s. Organisator: %s.</span></span></li>\n' % (ic('klok'), E(url), E(naam), wanneer, E(org))
        else:
            naam, wanneer, thema, url = r
            h += '        <li>%s<span class="kal-volgt-tekst"><a href="%s" target="_blank" rel="noopener">%s</a><span>Meestal %s.</span></span></li>\n' % (ic('klok'), E(url), E(naam), ('in ' + wanneer) if wanneer.split()[0] in MND or wanneer in MND else wanneer)
    return h + '      </ul>'

TITEL = 'Vitaliteitskalender 2026 en 2027 | Walter Montenarie'
BESCHR = 'Kalender met evenementen over vitaliteit en gezondheid in Nederland en alle dagen en weken van rond gezondheid. Van oktober 2026 tot en met oktober 2027.'
assert len(TITEL) <= 60 and len(BESCHR) <= 160, (len(TITEL), len(BESCHR))

basis = open(W + 'tools.html', encoding='utf-8').read()
kop = basis[:basis.index('<main>')]
voet = basis[basis.index('</main>') + len('</main>'):basis.index('<script>')]
kop = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITEL, kop)
kop = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % BESCHR, kop)
kop = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="Vitaliteitskalender 2026 en 2027">', kop)
kop = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % BESCHR, kop)
kop = kop.replace('https://waltermontenarie.com/tools"', 'https://waltermontenarie.com/kalender"')
assert kop.count('waltermontenarie.com/kalender') == 2
# In het menu is Kalender de huidige pagina, niet Tools
assert '<a href="tools" aria-current="page">Tools</a>' in kop and '<a class="menu-kal" href="kalender">' in kop
kop = kop.replace('<a href="tools" aria-current="page">Tools</a>', '<a href="tools">Tools</a>').replace('<a class="menu-kal" href="kalender">', '<a class="menu-kal" href="kalender" aria-current="page">')

main = '''<main>
  %s
  <section class="sectie kal-kop">
    <div class="wrap">
      <div class="kal-kop-tekst">
        <h1>Vitaliteitskalender</h1>
        <p class="intro">Wil je je activiteiten laten aansluiten op wat er in het land gebeurt? Hier vind je twee overzichten. De evenementen over vitaliteit en gezondheid in Nederland. En de dagen en weken die met gezondheid te maken hebben. Van oktober 2026 tot en met oktober 2027.</p>
      </div>
      %s
      <div class="kal-sprong">
        <a class="kal-tegel t-ev" href="#evenementen"><span class="kal-rond">%s</span><span class="kal-tegel-tekst"><strong><span data-tel="evenementen">%d</span> evenementen</strong><span>Congressen, beurzen en kennisdagen in Nederland</span></span><span class="kal-pijl" aria-hidden="true">↓</span></a>
        <a class="kal-tegel t-dag" href="#dagen-en-weken"><span class="kal-rond">%s</span><span class="kal-tegel-tekst"><strong><span data-tel="dagen-en-weken">%d</span> dagen en weken van</strong><span>Themadagen, weken en maanden rond gezondheid</span></span><span class="kal-pijl" aria-hidden="true">↓</span></a>
      </div>
    </div>
  </section>

  <section class="sectie wit kal" id="evenementen">
    <div class="wrap">
      <div class="kal-titel t-ev"><span class="kal-rond">%s</span><h2>Evenementen over vitaliteit en gezondheid</h2></div>
      <p>Congressen, beurzen en kennisdagen in Nederland. Klik op een evenement voor informatie en aanmelden bij de organisator.</p>
%s
%s
      <p class="kal-leeg" hidden>Geen evenementen in deze groep.</p>
      <h3 class="kal-volgt-kop">Datum volgt</h3>
      <p>Deze evenementen komen elk jaar terug. De nieuwe datum is nog niet bekend.</p>
%s
    </div>
  </section>

  <section class="sectie kal" id="dagen-en-weken">
    <div class="wrap">
      <div class="kal-titel t-dag"><span class="kal-rond">%s</span><h2>Dagen en weken van</h2></div>
      <p>Landelijke en internationale dagen, weken en maanden die met gezondheid te maken hebben. Handig als haakje voor een sessie, een actie of een bericht aan je team.</p>
%s
%s
      <p class="kal-leeg" hidden>Geen dagen of weken in deze groep.</p>
      <h3 class="kal-volgt-kop">Datum volgt</h3>
      <p>Deze weken en dagen komen elk jaar terug. De nieuwe datum is nog niet bekend.</p>
%s
    </div>
  </section>

  <section class="sectie wit">
    <div class="wrap">
      <p class="noot">De datums zijn gecontroleerd op %s. Organisatoren kunnen een datum of locatie wijzigen. Kijk daarom altijd op de website van de organisator. Mis je een evenement of een dag? <a href="contact">Laat het me weten</a>.</p>
      <div class="nieuwsbrief-band">
        <div>
          <h2>Iets doen met een van deze weken?</h2>
          <p>Ik geef inspiratiesessies en trainingen die je kunt laten aansluiten op een themaweek.</p>
        </div>
        <div class="hero-knoppen">
          <a class="knop" href="trainingen#workshops">Bekijk de inspiratiesessies</a>
          <a class="knop omlijnd" href="https://calendly.com/walter-montenarie/30min" target="_blank" rel="noopener">Plan een gratis gesprek</a>
        </div>
      </div>
    </div>
  </section>
</main>
''' % (SPRITE, tekening(), ic('kaartje'), len(EVENTS), ic('vlag'), len(DAGEN), ic('kaartje'), knoppen(SOORT, 'Kies een soort evenement'), per_maand(EVENTS, event_li), volgt(EVENTS_VOLGT, 'event'),
       ic('vlag'), knoppen(THEMA, 'Kies een thema'), per_maand(DAGEN, dag_li), volgt(DAGEN_VOLGT, 'dag'), GECONTROLEERD)

script = '''<script>
(function () {
  var nu = new Date(); nu.setHours(0, 0, 0, 0);
  // Verberg wat voorbij is en filter per groep
  document.querySelectorAll('.kal').forEach(function (deel) {
    var items = deel.querySelectorAll('.kal-item'), filter = 'alles';
    items.forEach(function (li) {
      var d = li.getAttribute('data-eind').split('-');
      if (new Date(+d[0], +d[1] - 1, +d[2]) < nu) li.setAttribute('data-voorbij', '');
    });
    var tel = document.querySelector('[data-tel="' + deel.id + '"]');
    if (tel) tel.textContent = deel.querySelectorAll('.kal-item:not([data-voorbij])').length;
    function toon() {
      var zichtbaar = 0;
      items.forEach(function (li) {
        var weg = li.hasAttribute('data-voorbij') || (filter !== 'alles' && li.getAttribute('data-groep') !== filter);
        li.hidden = weg; if (!weg) zichtbaar++;
      });
      deel.querySelectorAll('.kal-maand').forEach(function (m) { m.hidden = !m.querySelector('.kal-item:not([hidden])'); });
      deel.querySelector('.kal-leeg').hidden = zichtbaar > 0;
    }
    deel.querySelectorAll('.kal-filter button').forEach(function (knop) {
      knop.addEventListener('click', function () {
        filter = knop.getAttribute('data-filter');
        deel.querySelectorAll('.kal-filter button').forEach(function (k) { var aan = k === knop; k.classList.toggle('actief', aan); k.setAttribute('aria-pressed', aan ? 'true' : 'false'); });
        toon();
      });
    });
    toon();
  });
})();
</script>
<script src="js/menu.js" defer></script>
</body>
</html>
'''
open(W + 'kalender.html', 'w', encoding='utf-8').write(kop + main + voet + script)
print('events', len(EVENTS), 'dagen', len(DAGEN))
