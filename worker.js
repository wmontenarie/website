// Dit script doet twee dingen:
// 1. Het stuurt bezoekers van het oude adres en van www door naar het hoofdadres.
// 2. Het verstuurt de formulieren van de website als e-mail naar Walter.
// Alle andere verzoeken gaan ongewijzigd naar de bestanden van de website.
import { EmailMessage } from 'cloudflare:email';

const HOOFD = 'waltermontenarie.com';
const DOORSTUREN = ['www.waltermontenarie.com', 'website.walter-montenarie.workers.dev'];
const VAN = 'website@waltermontenarie.com';
const NAAR = 'walter.montenarie@gmail.com';

const WHITEPAPERS = {
  'businesscase-vitaliteit': 'De businesscase voor vitaliteit',
  'werkdruk-verlagen': 'Werkdruk verlagen',
  'vitaliteitsbeleid-opzetten': 'Vitaliteitsbeleid opzetten',
  'burn-out-signaleren': 'Burn-out signaleren'
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (DOORSTUREN.includes(url.hostname)) {
      url.hostname = HOOFD;
      url.protocol = 'https:';
      url.port = '';
      return Response.redirect(url.toString(), 301);
    }
    if (url.pathname === '/verstuur') return verstuur(request, env, url);

    const antwoord = await env.ASSETS.fetch(request);
    // De whitepapers zelf hoeven niet in Google te komen, de downloadpagina's wel
    if (url.pathname.startsWith('/downloads/')) {
      const kopie = new Response(antwoord.body, antwoord);
      kopie.headers.set('X-Robots-Tag', 'noindex');
      return kopie;
    }
    return antwoord;
  }
};

// Eén regel tekst: geen regeleinden of stuurtekens, begrensde lengte
function regel(waarde, max) {
  return String(waarde || '').replace(/[\u0000-\u001f\u007f]+/g, ' ').trim().slice(0, max);
}
function tekst(waarde, max) {
  return String(waarde || '').replace(/\r\n?/g, '\n').replace(/[\u0000-\u0008\u000b-\u001f\u007f]/g, '').trim().slice(0, max);
}
function base64(s) {
  const bytes = new TextEncoder().encode(s);
  let bin = '';
  for (let i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
  return btoa(bin);
}
// Onderwerpregel met accenten, in stukjes zoals de e-mailstandaard voorschrijft
function kopwoord(s) {
  const delen = [];
  let deel = '', lengte = 0;
  for (const teken of s) {
    const n = new TextEncoder().encode(teken).length;
    if (lengte + n > 45) { delen.push(deel); deel = ''; lengte = 0; }
    deel += teken; lengte += n;
  }
  if (deel) delen.push(deel);
  return delen.map((d) => '=?UTF-8?B?' + base64(d) + '?=').join('\r\n ');
}
function eigenSite(request, url) {
  const bron = request.headers.get('Origin') || request.headers.get('Referer');
  if (!bron) return false;
  try { return new URL(bron).host === url.host; } catch (e) { return false; }
}

async function verstuur(request, env, url) {
  const json = (request.headers.get('Accept') || '').includes('application/json');
  const klaar = (ok, pad, status, fout) => json
    ? new Response(JSON.stringify(fout ? { ok: ok, fout: fout } : { ok: ok }), {
        status: status,
        headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' }
      })
    : Response.redirect(url.origin + pad, 303);

  if (request.method !== 'POST') return Response.redirect(url.origin + '/contact', 303);

  let f;
  try { f = await request.formData(); } catch (e) { return klaar(false, '/contact?mislukt=1#formulier', 400, 'formulier'); }
  const v = (naam, max) => regel(f.get(naam), max || 200);

  const slug = v('whitepaper', 60);
  const isWhitepaper = v('soort', 20) === 'whitepaper' && Object.prototype.hasOwnProperty.call(WHITEPAPERS, slug);
  const goed = isWhitepaper ? '/bedankt-' + slug : '/contact?verzonden=1#formulier';
  // Bij een whitepaper krijgt de bezoeker de download ook als het versturen mislukt
  const mis = isWhitepaper ? goed : '/contact?mislukt=1#formulier';

  if (!eigenSite(request, url)) return klaar(false, mis, 403, 'herkomst');
  // Onzichtbaar veld dat alleen spamrobots invullen: doe alsof het gelukt is
  if (v('_honey', 50)) return klaar(true, goed, 200);

  const naam = v('naam', 120);
  const email = v('email', 200);
  if (!naam || !/^[^\s@<>"',;]+@[^\s@<>"',;]+\.[^\s@<>"',;]+$/.test(email)) return klaar(false, mis, 400, 'invoer');

  const rijen = [];
  const rij = (label, waarde) => { if (waarde) rijen.push(label + ': ' + waarde); };
  let onderwerp, lang = '';
  if (isWhitepaper) {
    const organisatie = v('organisatie', 160);
    onderwerp = 'Whitepaper gedownload: ' + WHITEPAPERS[slug] + ' (' + naam + (organisatie ? ', ' + organisatie : '') + ')';
    rij('Whitepaper', WHITEPAPERS[slug]);
    rij('Naam', naam);
    rij('Organisatie', organisatie);
    rij('Functie', v('functie', 160));
    rij('E-mail', email);
    rij('Telefoon', v('telefoon', 40));
    rij('Wil artikelen per e-mail', f.get('nieuwsbrief') ? 'Ja' : 'Nee');
    lang = tekst(f.get('uitdagingen'), 4000);
    if (lang) lang = 'Uitdagingen en waar diegene naar op zoek is:\n' + lang;
  } else {
    const waarover = v('onderwerp', 80) || 'Bericht';
    onderwerp = 'Nieuw bericht via de website: ' + waarover + ' (' + naam + ')';
    rij('Onderwerp', waarover);
    rij('Naam', naam);
    rij('Organisatie', v('organisatie', 160));
    rij('E-mail', email);
    rij('Telefoon', v('telefoon', 40));
    lang = tekst(f.get('bericht'), 6000);
    if (!lang) return klaar(false, mis, 400, 'invoer');
    lang = 'Bericht:\n' + lang;
  }
  const inhoud = rijen.join('\n') + (lang ? '\n\n' + lang : '') +
    '\n\n--\nVerstuurd via het formulier op ' + url.host + '. Beantwoord deze mail om ' + naam + ' te antwoorden.\n';

  const kop = [
    'From: "Website Walter Montenarie" <' + VAN + '>',
    'To: <' + NAAR + '>',
    'Reply-To: <' + email + '>',
    'Subject: ' + kopwoord(onderwerp.slice(0, 180)),
    'Message-ID: <' + crypto.randomUUID() + '@' + HOOFD + '>',
    'Date: ' + new Date().toUTCString().replace('GMT', '+0000'),
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: base64'
  ];
  const ruw = kop.join('\r\n') + '\r\n\r\n' + base64(inhoud).replace(/(.{76})/g, '$1\r\n') + '\r\n';

  try {
    await env.MAIL.send(new EmailMessage(VAN, NAAR, ruw));
  } catch (e) {
    console.error('Versturen mislukt:', e && e.message);
    return klaar(false, mis, 502, 'mail: ' + regel(e && e.message, 200));
  }
  return klaar(true, goed, 200);
}
