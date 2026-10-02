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
