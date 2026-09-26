// Lens switcher: turns the stacked lens panels into an accessible tab set
// (WAI-ARIA Authoring Practices "Tabs with automatic activation").
// Without JavaScript all panels stay visible, one below the other.
document.querySelectorAll("[data-lens]").forEach((lens) => {
  const tablist = lens.querySelector('[role="tablist"]');
  const tabs = [...tablist.querySelectorAll('[role="tab"]')];
  const panels = tabs.map((tab) => document.getElementById(tab.getAttribute("aria-controls")));

  function select(index, focus) {
    tabs.forEach((tab, i) => {
      const active = i === index;
      tab.setAttribute("aria-selected", String(active));
      tab.tabIndex = active ? 0 : -1;
      panels[i].hidden = !active;
    });
    if (focus) tabs[index].focus();
  }

  tabs.forEach((tab, i) => {
    tab.addEventListener("click", () => select(i, false));
    tab.addEventListener("keydown", (event) => {
      const last = tabs.length - 1;
      const next = { ArrowRight: i === last ? 0 : i + 1, ArrowLeft: i === 0 ? last : i - 1, Home: 0, End: last }[event.key];
      if (next === undefined) return;
      event.preventDefault();
      select(next, true);
    });
  });

  panels.forEach((panel) => { panel.tabIndex = 0; });
  tablist.hidden = false;
  lens.classList.add("is-enhanced");
  select(0, false);
});
