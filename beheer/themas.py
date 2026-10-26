# De vier thema's van de site. Elk artikel hoort bij één hoofdthema (voor het kruimelpad).
# Een thema kan ook artikelen uit een ander thema tonen (lijst 'ook').
# Na een wijziging: python3 beheer/thema_paginas.py en python3 beheer/artikel_extra.py

THEMAS = [
    {
        'slug': 'werkdruk',
        'wat': ('Wat is werkdruk?', 'Werkdruk is de verhouding tussen wat het werk van je vraagt en wat je aankunt. Een drukke week is geen probleem: werkdruk hoort bij werk. Het wordt een probleem als de druk te hoog is en te lang duurt zonder dat je herstelt. Te hoge werkdruk is de meest genoemde oorzaak van verzuim door het werk.'),
        'naam': 'Werkdruk',
        'titel': 'Werkdruk verlagen: artikelen, whitepaper en training',
        'h1': 'Werkdruk',
        'beschr': 'Alles over werkdruk en werkstress: artikelen, een gratis whitepaper, de training werkdruk verlagen en het JD-R-model. Voor leidinggevenden en HR.',
        'intro': 'Werkdruk is een van de grootste oorzaken van verzuim. Hier vind je wat werkdruk is, waar hij vandaan komt en wat je er als leidinggevende samen met je team aan doet.',
        'artikelen': ['moet-je-je-druk-maken-over-werkdruk', 'herstel-en-rust-op-het-werk', 'week-zonder-werkstress-ideeen',
                      'werkstress-aanpakken-na-de-week', 'leidinggevende-voorbeeld-werkstress', 'bevlogenheid-is-geen-luxe', 'bevlogenheid-die-je-team-kan-volhouden'],
        'ook': [],
        'whitepaper': ('whitepaper-werkdruk-verlagen', 'Werkdruk verlagen', 'Een handleiding voor leidinggevenden. Oorzaken vinden, het gesprek voeren en met je team aan de slag.', 'img/whitepaper-werkdruk-omslag.webp'),
        'training': ('trainingen#werkdruk', 'Training werkdruk verlagen', 'Na twee korte sessies weet je team waar de werkdruk vandaan komt en is het al bezig met een eigen plan.'),
        'tool': ('tools#jdr-model', 'Het JD-R-model', 'Zie in één beeld wat energie kost en wat energie geeft in het werk.'),
    },
    {
        'slug': 'burn-out-en-verzuim',
        'wat': ('Wat is het verschil tussen burn-out en verzuim?', 'Verzuim is alle afwezigheid door ziekte. Burn-out is een van de oorzaken: uitputting door langdurige stress zonder herstel. Psychische klachten zoals overspannenheid en burn-out zijn de oorzaak bij vier op de tien gevallen van langdurig verzuim. Ze komen zelden onverwacht, dus wie de signalen herkent kan uitval vaak voorkomen.'),
        'naam': 'Burn-out en verzuim',
        'titel': 'Burn-out en verzuim: artikelen, whitepaper en tools',
        'h1': 'Burn-out en verzuim',
        'beschr': 'Burn-out voorkomen en verzuim terugdringen: artikelen voor leidinggevenden, een gratis gespreksgids, een training en de verzuimrekentool.',
        'intro': 'Uitval komt zelden onverwacht. Hier lees je hoe je signalen herkent, het gesprek voert en wat werkt om verzuim terug te dringen. Ook voor mensen met een chronische aandoening, mantelzorgers en vrouwen in de overgang.',
        'artikelen': ['burn-out-voorkomen-in-je-team', 'stress-bespreekbaar-maken', 'mannen-stress-gezondheid-werk', 'verzuim-terugdringen-maatregelen', 'gemiddeld-verzuim-is-niet-normaal',
                      'presenteisme-onbekende-productiviteitskiller', 'mentale-gezondheid-werk-leidinggevende', 'werken-met-chronische-aandoening',
                      'mantelzorger-in-je-team', 'overgang-op-het-werk', 'onzichtbare-schuld-op-de-balans'],
        'ook': [],
        'whitepaper': ('whitepaper-burn-out-signaleren', 'Burn-out signaleren', 'Een gespreksgids voor leidinggevenden. Signalen herkennen en het gesprek voeren voordat iemand uitvalt.', 'img/whitepaper-burn-out-omslag.webp'),
        'training': ('trainingen#bevlogenheid', 'Verminder stress, verhoog bevlogenheid', 'Je team ontdekt wat in het werk energie geeft en wat energie kost, en maakt afspraken om stress te verlagen.'),
        'tool': ('tools#rekentool-kop', 'Verzuimrekentool', 'Bereken in een minuut wat verzuim je organisatie per jaar kost.'),
    },
    {
        'slug': 'vitaliteitsbeleid',
        'wat': ('Wat is vitaliteitsbeleid?', 'Vitaliteitsbeleid is de manier waarop een organisatie ervoor zorgt dat medewerkers gezond, met energie en met plezier kunnen werken. Het gaat over meer dan leefstijl: werkdruk, leiderschap en cultuur horen er net zo goed bij. Beleid heeft een doel, een eigenaar en een meting. Losse activiteiten zoals fruit op het werk zijn nog geen beleid.'),
        'naam': 'Vitaliteitsbeleid',
        'titel': 'Vitaliteitsbeleid: artikelen, whitepapers en vitaliteitsscan',
        'h1': 'Vitaliteitsbeleid',
        'beschr': 'Vitaliteitsbeleid en duurzame inzetbaarheid: stappenplan, voorbeelden, businesscase, twee gratis whitepapers en de vitaliteitsmeter.',
        'intro': 'Fruit op het werk en een workshop zijn nog geen beleid. Hier lees je hoe je vitaliteitsbeleid opzet dat samenhangt, een doel heeft en laat zien wat het oplevert.',
        'artikelen': ['vitaliteitsbeleid-opzetten-stappenplan', 'vitaliteit-op-de-werkvloer', 'zes-bouwblokken-vitaliteitsbeleid',
                      'wat-is-duurzame-inzetbaarheid', 'mantelzorgvriendelijk-werkgeverschap', 'diabetes-type-2-voorkomen-werk', 'businesscase-vitaliteit-maken', 'rendement-vitaliteitsprogramma-hbr-onderzoek'],
        'ook': [],
        'whitepaper': ('whitepaper-vitaliteitsbeleid-opzetten', 'Vitaliteitsbeleid opzetten', 'Van losse activiteiten naar beleid dat werkt. Met zeven stappen, een jaarplanning en een checklist.', 'img/whitepaper-vitaliteitsbeleid-omslag.webp'),
        'training': ('training-vitaal-leiderschap', 'Training vitaal leiderschap', 'Van zelfzorg tot cultuurverandering. Je ontdekt hoe je een goed voorbeeld bent voor je team.'),
        'tool': ('vitaliteitsmeter', 'Vitaliteitsmeter', 'Gratis vitaliteitsscan: 26 stellingen en je ziet direct waar je organisatie staat.'),
    },
    {
        'slug': 'cultuurverandering',
        'wat': ('Wat is cultuurverandering?', "Cultuur is hoe het in een organisatie gaat als niemand kijkt: wat normaal is, wat mag en wat niet. Bij cultuurverandering verander je die vanzelfsprekendheden, bijvoorbeeld hoe je omgaat met werkdruk en herstel. Het 8-stappenmodel van Kotter helpt om zo'n verandering stap voor stap vorm te geven, van urgentie tot verankering."),
        'naam': 'Cultuurverandering',
        'titel': 'Cultuurverandering: artikelen, model van Kotter en training',
        'h1': 'Cultuurverandering',
        'beschr': 'Cultuurverandering die blijft: het 8-stappenmodel van Kotter, artikelen over beleid dat werkt en de training cultuurverandering voor managementteams.',
        'intro': 'Vitaliteit vraagt vaak een andere cultuur. Anders leidinggeven, anders omgaan met werkdruk en herstel. Hier lees je hoe je zo een verandering laat slagen, stap voor stap.',
        'artikelen': ['van-verzuim-naar-energie-kotter'],
        'ook': ['zes-bouwblokken-vitaliteitsbeleid', 'rendement-vitaliteitsprogramma-hbr-onderzoek', 'bevlogenheid-die-je-team-kan-volhouden'],
        'whitepaper': ('whitepaper-vitaliteitsbeleid-opzetten', 'Vitaliteitsbeleid opzetten', 'Van losse activiteiten naar beleid dat werkt. Met zeven stappen, een jaarplanning en een checklist.', 'img/whitepaper-vitaliteitsbeleid-omslag.webp'),
        'training': ('training-cultuurverandering', 'Training cultuurverandering', 'In vier dagdelen maakt je team met de acht stappen van Kotter een eigen veranderplan.'),
        'tool': ('tools#kotter', 'Het 8-stappenmodel van Kotter', 'De acht stappen op een rij, met wat elke stap van je vraagt.'),
    },
]

def thema_van(slug):
    for t in THEMAS:
        if slug in t['artikelen']:
            return t
    return None

# controle: elk artikel hoort bij precies één thema
if __name__ == '__main__':
    import os, glob
    W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')
    alle = [os.path.basename(p)[:-5] for p in glob.glob(W + 'artikelen/*.html')]
    for a in alle:
        n = sum(a in t['artikelen'] for t in THEMAS)
        print(n, a) if n != 1 else None
