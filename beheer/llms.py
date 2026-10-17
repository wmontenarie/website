# Bouwt llms.txt: een korte samenvatting van de site voor AI-zoekmachines zoals ChatGPT, Perplexity en Claude.
# De lijst met artikelen komt uit artikelen.html. Opnieuw uitvoeren na een nieuw artikel.
import re, html, os
W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')
B = 'https://waltermontenarie.com'

def tekst(s): return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

s = open(W + 'artikelen.html', encoding='utf-8').read()
artikelen = re.findall(r'<a href="(artikelen/[a-z0-9-]+)">.*?<h2>(.*?)</h2>\s*<p>(.*?)</p>', s, re.S)
assert len(artikelen) >= 20, len(artikelen)

regels = ['# Walter Montenarie, adviseur duurzame inzetbaarheid', '',
 '> Walter Montenarie is een adviseur, coach, trainer en spreker uit Den Haag. Hij helpt werkgevers, leidinggevenden, directeuren en HR in heel Nederland aan minder verzuim, minder werkstress en meer energie en plezier in het werk. Zijn aanpak gaat uit van het werk zelf en de rol van de leidinggevende, met modellen als het Job Demands-Resources-model en het 8-stappenmodel van Kotter. Hij heeft ruim 30 jaar ervaring in gezondheidscoaching, management en strategie en is ervaringsdeskundige bij burn-out.', '',
 'Talen: Nederlands, Engels en Duits. Contact: walter@waltermontenarie.com, +31 6 51 68 68 65.', '',
 '## Over en contact', '',
 '- [Over Walter Montenarie](%s/over-mij): achtergrond, ervaring en werkwijze' % B,
 '- [Contact](%s/contact): gratis kennismakingsgesprek van 30 minuten plannen' % B, '',
 '## Diensten', '',
 '- [Diensten](%s/diensten): strategisch advies over vitaliteit en duurzame inzetbaarheid, coaching, trainingen, inspiratiesessies, spreker en interim-management' % B,
 '- [Trainingen](%s/trainingen): werkdruk verlagen, stress verminderen en bevlogenheid verhogen, cultuurverandering met Kotter, inspiratiesessies' % B,
 '- [Training vitaal leiderschap](%s/training-vitaal-leiderschap): voor leidinggevenden en directeuren, in 2 of 4 dagdelen' % B,
 '- [Spreker](%s/spreker): keynote, interactieve lezing, webinar of dagvoorzitter over vitaliteit, verzuim, werkstress en burn-out' % B, '',
 '## Gratis hulpmiddelen', '',
 '- [Tools](%s/tools): rekentool verzuimkosten, het JD-R-model en het 8-stappenmodel van Kotter' % B,
 '- [Vitaliteitsmeter](%s/vitaliteitsmeter): 24 stellingen over vitaliteit in je organisatie, met uitslag per thema' % B,
 '- [Vitaliteitskalender](%s/kalender): evenementen en dagen en weken over gezondheid en werk in Nederland' % B,
 '- [Whitepapers](%s/whitepapers): businesscase vitaliteit, werkdruk verlagen, vitaliteitsbeleid opzetten en burn-out signaleren' % B, '',
 '## Artikelen', '']
for href, titel, uitleg in artikelen:
    regels.append('- [%s](%s/%s): %s' % (tekst(titel), B, href, tekst(uitleg)))
regels.append('')
uit = '\n'.join(regels)
for teken in ('—', '–'):
    assert teken not in uit
open(W + 'llms.txt', 'w', encoding='utf-8').write(uit)
print('llms.txt geschreven met', len(artikelen), 'artikelen')
