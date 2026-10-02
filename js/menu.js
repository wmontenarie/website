(function () {
  var groep = document.querySelector('.menu-groep');
  if (!groep) return;
  var knop = groep.querySelector('.menu-knop');
  if (!knop) return;
  function zet(open) {
    groep.classList.toggle('open', open);
    knop.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  knop.addEventListener('click', function (e) {
    e.stopPropagation();
    zet(!groep.classList.contains('open'));
  });
  groep.querySelectorAll('.submenu a').forEach(function (a) {
    a.addEventListener('click', function () { zet(false); });
  });
  document.addEventListener('click', function (e) {
    if (!groep.contains(e.target)) zet(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { zet(false); knop.focus(); }
  });
})();
