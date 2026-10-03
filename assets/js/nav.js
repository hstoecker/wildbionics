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

// Contact addresses (_includes/email.html): built here so harvesters reading the HTML find none.
document.querySelectorAll("[data-email]").forEach((el) => {
  const address = `${el.dataset.email}@${el.dataset.domain}`;
  const link = document.createElement("a");
  link.href = `mailto:${address}`;
  link.textContent = address;
  if (el.dataset.class) link.className = el.dataset.class;
  el.replaceWith(link);
});
