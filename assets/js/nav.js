// Mobile menu (<details class="menu">): works without JavaScript; this only closes it after a
// link is chosen (same-page anchors keep the page), on Escape and on a tap outside.
(() => {
  const menu = document.querySelector("[data-menu]");
  if (!menu) return;
  const summary = menu.querySelector("summary");
  const close = (focus) => {
    if (!menu.open) return;
    menu.open = false;
    if (focus) summary.focus();
  };
  menu.addEventListener("click", (e) => { if (e.target.closest("a")) close(false); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") close(menu.contains(document.activeElement)); });
  document.addEventListener("click", (e) => { if (!menu.contains(e.target)) close(false); });
})();
