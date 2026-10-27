/* Keep checkpoint explanations available in print, restoring the reader's choices. */
(() => {
  let expandedForPrint = [];
  window.addEventListener('beforeprint', () => {
    expandedForPrint = [...document.querySelectorAll('.bd-article details:not([open])')];
    expandedForPrint.forEach(detail => { detail.open = true; });
  });
  window.addEventListener('afterprint', () => {
    expandedForPrint.forEach(detail => { detail.open = false; });
    expandedForPrint = [];
  });
})();

/* Wide diagrams remain readable and keyboard-scrollable on narrow screens. */
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.bd-article figure').forEach(figure => {
    figure.tabIndex = 0;
    figure.setAttribute('role', 'group');
    figure.setAttribute('aria-label', 'Diagram and caption; scroll horizontally on narrow screens');
  });
});
