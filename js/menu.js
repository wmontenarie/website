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

/* Venster rechtsonder dat een passende whitepaper onder de aandacht brengt */
(function () {
  var script = document.currentScript;
  if (!script || document.documentElement.lang !== 'nl') return;
  var pad = location.pathname;
  if (/whitepaper|bedankt|privacy/.test(pad)) return;
  var SLEUTEL = 'wp-venster';
  var geheugen = null;
  function lees() { try { return localStorage.getItem(SLEUTEL) || localStorage.getItem('wp-businesscase'); } catch (e) { return geheugen; } }
  function schrijf(w) { geheugen = w; try { localStorage.setItem(SLEUTEL, w); } catch (e) {} }
  if (lees()) return;

  var keuzes = [
    { als: /werkdruk|werkstress/, img: 'werkdruk', pagina: 'whitepaper-werkdruk-verlagen.html', titel: 'Werkdruk verlagen', tekst: 'Hoe verlaag je de werkdruk in je team? Download de gratis handleiding.' },
    { als: /burn-out|bevlogenheid/, img: 'burn-out', pagina: 'whitepaper-burn-out-signaleren.html', titel: 'Burn-out signaleren', tekst: 'Hoe herken je de signalen en voer je het gesprek? Download de gratis gespreksgids.' },
    { als: /vitaliteitsbeleid|bouwblokken|duurzame-inzetbaarheid|kotter/, img: 'vitaliteitsbeleid', pagina: 'whitepaper-vitaliteitsbeleid-opzetten.html', titel: 'Vitaliteitsbeleid opzetten', tekst: 'Van losse activiteiten naar beleid dat werkt. Download het gratis stappenplan.' }
  ];
  var keuze = { img: 'businesscase', pagina: 'whitepaper-businesscase-vitaliteit.html', titel: 'De businesscase voor vitaliteit', tekst: 'Wat kost verzuim en wanneer verdient investeren zich terug? Download de gratis whitepaper.' };
  for (var i = 0; i < keuzes.length; i++) { if (keuzes[i].als.test(pad)) { keuze = keuzes[i]; break; } }

  var basis = new URL('..', script.src).href;
  var getoond = false;
  function toon() {
    if (getoond || lees()) return;
    getoond = true;
    var v = document.createElement('aside');
    v.className = 'wp-venster';
    v.setAttribute('aria-label', 'Gratis whitepaper');
    v.innerHTML =
      '<button class="sluit" type="button" aria-label="Sluiten">\u00d7</button>' +
      '<img src="' + basis + 'img/whitepaper-' + keuze.img + '-omslag.webp" width="560" height="793" alt="">' +
      '<p class="titel">' + keuze.titel + '</p>' +
      '<p class="tekst">' + keuze.tekst + '</p>' +
      '<a class="knop" href="' + basis + keuze.pagina + '">Gratis download</a>';
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

// Inschrijven voor de nieuwsbrief zonder de pagina te verlaten
(function () {
  var form = document.querySelector('.nb-formulier');
  if (!form || !window.fetch || !window.URLSearchParams || !window.FormData) return;
  var blok = form.closest ? form.closest('.nb-blok') : null;
  var melding = form.querySelector('.nb-melding');
  var knop = form.querySelector('button[type="submit"]');
  var tekst = knop.textContent;
  var bezig = false;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (bezig) return;
    bezig = true;
    knop.disabled = true;
    knop.textContent = 'Een moment';
    melding.hidden = true;
    var mislukt = function () {
      melding.textContent = 'Het inschrijven lukt nu niet. Probeer het later opnieuw of stuur een mail naar walter@waltermontenarie.com.';
      melding.hidden = false;
      knop.disabled = false;
      knop.textContent = tekst;
      bezig = false;
    };
    fetch(form.getAttribute('action'), {
      method: 'POST',
      headers: { 'Accept': 'application/json' },
      body: new URLSearchParams(new FormData(form))
    }).then(function (r) { return r.json(); })
      .then(function (d) {
        if (!d || !d.ok) { mislukt(); return; }
        melding.textContent = 'Bedankt voor je inschrijving. Je ontvangt het volgende artikel in je mailbox.';
        melding.hidden = false;
        if (blok) blok.classList.add('klaar');
      })
      .catch(mislukt);
  });
})();

// Link van het artikel kopiëren
(function () {
  var knop = document.querySelector('.deel-kopieer');
  if (!knop) return;
  var melding = knop.closest('.deel').querySelector('.deel-melding');
  knop.addEventListener('click', function () {
    var url = knop.getAttribute('data-url') || location.href;
    var klaar = function (gelukt) {
      melding.textContent = gelukt ? 'De link is gekopieerd.' : 'Kopiëren lukt niet. De link is: ' + url;
      setTimeout(function () { melding.textContent = ''; }, gelukt ? 4000 : 12000);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(function () { klaar(true); }, function () { klaar(false); });
    } else { klaar(false); }
  });
})();
