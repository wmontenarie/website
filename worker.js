// Stuurt bezoekers van het oude adres en van www door naar het hoofdadres.
// Alle andere verzoeken gaan ongewijzigd naar de bestanden van de website.
const HOOFD = 'waltermontenarie.com';
const DOORSTUREN = ['www.waltermontenarie.com', 'website.walter-montenarie.workers.dev'];

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (DOORSTUREN.includes(url.hostname)) {
      url.hostname = HOOFD;
      url.protocol = 'https:';
      url.port = '';
      return Response.redirect(url.toString(), 301);
    }
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
