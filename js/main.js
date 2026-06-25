// Keith Christman portfolio — tiny vanilla JS. No dependencies, no build.
// Note: nothing here gates content visibility. If this file never loads, the
// site still renders completely — JS only adds the lightbox and the year.
(function () {
  // current year in footer
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  // lightbox for figures
  var lb = document.getElementById('lb');
  var lbimg = document.getElementById('lbimg');
  var lbx = document.getElementById('lbx');
  function open(src, alt) {
    if (!lb) return;
    lbimg.src = src; lbimg.alt = alt || '';
    lb.classList.add('open'); document.body.style.overflow = 'hidden';
  }
  function close() {
    if (!lb) return;
    lb.classList.remove('open'); lbimg.src = ''; document.body.style.overflow = '';
  }
  document.querySelectorAll('figure.fig .imgwrap img').forEach(function (img) {
    img.addEventListener('click', function () {
      open(img.getAttribute('data-full') || img.src, img.alt);
    });
  });
  if (lbx) lbx.addEventListener('click', close);
  if (lb) lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });
})();
