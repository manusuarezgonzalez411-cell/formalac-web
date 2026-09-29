// Menú móvil
document.addEventListener('DOMContentLoaded', function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.querySelector('.nav-links');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
  }
  // Submenú calculadoras en móvil
  var hasMenu = document.querySelector('.has-menu > a');
  if (hasMenu) {
    hasMenu.addEventListener('click', function (e) {
      if (window.innerWidth <= 640) {
        e.preventDefault();
        hasMenu.parentElement.classList.toggle('open');
      }
    });
  }
});

// Utilidad: redondear a n decimales
function fmt(n, d) {
  if (d === undefined) d = 1;
  return Number(n).toLocaleString('es-ES', { minimumFractionDigits: d, maximumFractionDigits: d });
}
