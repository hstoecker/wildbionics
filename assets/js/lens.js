// Lens switcher: turns stacked lens panels into an accessible tab set
// (WAI-ARIA Authoring Practices "Tabs with automatic activation").
// Markup: a [role=tablist][data-lens-tabs] whose tabs point to panels via aria-controls.
// Without JavaScript the tab bar stays hidden and all panels remain visible.
// A URL hash such as #lens-math opens that lens directly.
document.querySelectorAll("[data-lens-tabs]").forEach((tablist) => {
  const tabs = [...tablist.querySelectorAll('[role="tab"]')];
  const panels = tabs.map((tab) => document.getElementById(tab.getAttribute("aria-controls")));
  if (panels.includes(null)) return;

  function select(index, { focus = false, updateHash = false } = {}) {
    tabs.forEach((tab, i) => {
      const active = i === index;
      tab.setAttribute("aria-selected", String(active));
      tab.tabIndex = active ? 0 : -1;
      panels[i].hidden = !active;
    });
    if (focus) tabs[index].focus();
    if (updateHash) history.replaceState(null, "", "#" + panels[index].id);
  }

  tabs.forEach((tab, i) => {
    tab.addEventListener("click", () => select(i, { updateHash: true }));
    tab.addEventListener("keydown", (event) => {
      const last = tabs.length - 1;
      const next = { ArrowRight: i === last ? 0 : i + 1, ArrowLeft: i === 0 ? last : i - 1, Home: 0, End: last }[event.key];
      if (next === undefined) return;
      event.preventDefault();
      select(next, { focus: true, updateHash: true });
    });
  });

  // Open the lens named in the URL, e.g. …/#lens-cs (also when the hash points inside a panel).
  function fromHash() {
    const target = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1)));
    const index = target ? panels.findIndex((panel) => panel.contains(target)) : -1;
    return index;
  }
  window.addEventListener("hashchange", () => {
    const index = fromHash();
    if (index >= 0) select(index);
  });

  panels.forEach((panel) => { panel.tabIndex = 0; });
  tablist.hidden = false;
  const initial = fromHash();
  select(initial >= 0 ? initial : 0);
});
