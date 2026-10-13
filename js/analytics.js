// Google Analytics met toestemming.
// Analytics laadt pas nadat de bezoeker op "Akkoord" klikt. De keuze wordt in de browser bewaard.
// Een link of knop met data-cookiekeuze (bijvoorbeeld op de privacypagina) opent de vraag opnieuw.
(function () {
  var ID = 'G-C3EMWN7TVR';
  var SLEUTEL = 'analytics-keuze';
  var en = (document.documentElement.lang || '').toLowerCase().indexOf('en') === 0;
  var T = en ? {
    vraag: 'May I measure how this site is used? I use Google Analytics to see which pages are visited. This places cookies.',
    meer: 'Privacy statement',
    ja: 'Accept',
    nee: 'No thanks'
  } : {
    vraag: 'Mag ik meten hoe deze site gebruikt wordt? Ik gebruik Google Analytics om te zien welke pagina’s bezocht worden. Dat plaatst cookies.',
    meer: 'Privacyverklaring',
    ja: 'Akkoord',
    nee: 'Liever niet'
  };

  function lees() {
    try { return localStorage.getItem(SLEUTEL); } catch (e) { return null; }
  }
  function bewaar(w) {
    try { localStorage.setItem(SLEUTEL, w); } catch (e) {}
  }

  var geladen = false;
  function laad() {
    if (geladen) return;
    geladen = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', ID);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID;
    document.head.appendChild(s);
  }

  function wisCookies() {
    document.cookie.split(';').forEach(function (c) {
      var naam = c.split('=')[0].trim();
      if (naam.indexOf('_ga') !== 0) return;
      var host = location.hostname.replace(/^www\./, '');
      ['', '; domain=.' + host, '; domain=' + location.hostname].forEach(function (d) {
        document.cookie = naam + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d;
      });
    });
  }

  var balk = null;
  function toon() {
    if (balk) return;
    balk = document.createElement('div');
    balk.className = 'cookiebalk';
    balk.setAttribute('role', 'dialog');
    balk.setAttribute('aria-label', en ? 'Cookies' : 'Cookies');
    var p = document.createElement('p');
    p.textContent = T.vraag + ' ';
    var a = document.createElement('a');
    a.href = en ? '/privacy.html' : '/privacy.html';
    a.textContent = T.meer;
    p.appendChild(a);
    var knoppen = document.createElement('div');
    knoppen.className = 'cookiebalk-knoppen';
    var ja = document.createElement('button');
    ja.type = 'button';
    ja.className = 'knop';
    ja.textContent = T.ja;
    var nee = document.createElement('button');
    nee.type = 'button';
    nee.className = 'knop omlijnd';
    nee.textContent = T.nee;
    knoppen.appendChild(ja);
    knoppen.appendChild(nee);
    balk.appendChild(p);
    balk.appendChild(knoppen);
    document.body.appendChild(balk);
    ja.addEventListener('click', function () { bewaar('ja'); sluit(); laad(); });
    nee.addEventListener('click', function () {
      var wasAan = geladen;
      bewaar('nee'); sluit(); wisCookies();
      if (wasAan) location.reload();
    });
  }
  function sluit() {
    if (balk) { balk.remove(); balk = null; }
  }

  var keuze = lees();
  if (keuze === 'ja') laad();

  function start() {
    if (keuze !== 'ja' && keuze !== 'nee') toon();
    document.querySelectorAll('[data-cookiekeuze]').forEach(function (el) {
      el.addEventListener('click', function (e) { e.preventDefault(); toon(); });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
