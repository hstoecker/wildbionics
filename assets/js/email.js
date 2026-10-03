// Contact addresses (_includes/email.html): the mailto links are built here, so harvesters reading
// the HTML find no address. Without JavaScript the text fallback with its <noscript> hint stays.
document.querySelectorAll("[data-email]").forEach((el) => {
  const address = `${el.dataset.email}@${el.dataset.domain}`;
  const link = document.createElement("a");
  link.href = `mailto:${address}`;
  link.textContent = address;
  if (el.dataset.class) link.className = el.dataset.class;
  el.replaceWith(link);
});
