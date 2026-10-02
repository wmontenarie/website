(function () {
  var groepen = Array.prototype.slice.call(document.querySelectorAll('.menu-groep'));
  if (!groepen.length) return;
  function zet(groep, open) {
    var knop = groep.querySelector('.menu-knop');
    groep.classList.toggle('open', open);
    if (knop) knop.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  function sluitAlle(behalve) {
    groepen.forEach(function (g) { if (g !== behalve) zet(g, false); });
  }
  groepen.forEach(function (groep) {
    var knop = groep.querySelector('.menu-knop');
    if (!knop) return;
    knop.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = !groep.classList.contains('open');
      sluitAlle(groep);
      zet(groep, open);
    });
    groep.querySelectorAll('.submenu a').forEach(function (a) {
      a.addEventListener('click', function () { zet(groep, false); });
    });
  });
  document.addEventListener('click', function (e) {
    groepen.forEach(function (g) { if (!g.contains(e.target)) zet(g, false); });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    groepen.forEach(function (g) {
      if (g.classList.contains('open')) { zet(g, false); g.querySelector('.menu-knop').focus(); }
    });
  });
})();

/* Venster rechtsonder dat de whitepaper onder de aandacht brengt */
(function () {
  var script = document.currentScript;
  if (!script || document.documentElement.lang !== 'nl') return;
  if (/whitepaper|privacy/.test(location.pathname)) return;
  var SLEUTEL = 'wp-businesscase';
  var geheugen = null;
  function lees() { try { return localStorage.getItem(SLEUTEL); } catch (e) { return geheugen; } }
  function schrijf(w) { geheugen = w; try { localStorage.setItem(SLEUTEL, w); } catch (e) {} }
  if (lees()) return;

  var basis = new URL('..', script.src).href;
  var getoond = false;
  function toon() {
    if (getoond || lees()) return;
    getoond = true;
    var v = document.createElement('aside');
    v.className = 'wp-venster';
    v.setAttribute('aria-label', 'Gratis whitepaper');
    v.innerHTML =
      '<button class="sluit" type="button" aria-label="Sluiten">×</button>' +
      '<img src="' + basis + 'img/whitepaper-businesscase-omslag.webp" width="560" height="793" alt="">' +
      '<p class="titel">De businesscase voor vitaliteit</p>' +
      '<p class="tekst">Wat kost verzuim en wanneer verdient investeren zich terug? Download de gratis whitepaper.</p>' +
      '<a class="knop" href="' + basis + 'whitepapers.html">Gratis download</a>';
    v.querySelector('.sluit').addEventListener('click', function () { schrijf('gesloten'); v.hidden = true; });
    v.querySelector('.knop').addEventListener('click', function () { schrijf('geklikt'); });
    document.body.appendChild(v);
  }
  var klok = setTimeout(toon, 6000);
  window.addEventListener('scroll', function opScroll() {
    var hoogte = document.documentElement.scrollHeight - window.innerHeight;
    if (hoogte > 0 && window.scrollY / hoogte > 0.3) { clearTimeout(klok); window.removeEventListener('scroll', opScroll); toon(); }
  }, { passive: true });
})();
