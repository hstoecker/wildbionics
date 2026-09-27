// Contribution guide: copy buttons for command blocks and a sub-navigation that marks the
// section currently in view. Pure enhancement – without JavaScript the page is complete.
(() => {
  const guide = document.querySelector("[data-guide]");
  if (!guide) return;

  // Copy buttons
  const copyLabel = guide.dataset.copyLabel || "Copy";
  const copiedLabel = guide.dataset.copiedLabel || "Copied";
  guide.querySelectorAll("pre.guide-code").forEach((pre) => {
    if (!navigator.clipboard) return;
    const button = document.createElement("button");
    button.type = "button";
    button.className = "guide-copy";
    button.innerHTML = "<span>" + copyLabel + "</span>";
    button.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(pre.querySelector("code").innerText.trim());
        button.classList.add("is-done");
        button.querySelector("span").textContent = copiedLabel;
        setTimeout(() => {
          button.classList.remove("is-done");
          button.querySelector("span").textContent = copyLabel;
        }, 2000);
      } catch (e) { /* clipboard blocked – the text stays selectable */ }
    });
    pre.appendChild(button);
  });

  // Sub-navigation: mark the section in view
  const links = [...document.querySelectorAll(".guide-subnav a[href^='#']")];
  const sections = links.map((a) => document.getElementById(a.hash.slice(1))).filter(Boolean);
  if (!("IntersectionObserver" in window) || !sections.length) return;
  const mark = (id) => links.forEach((a) => {
    if (a.hash === "#" + id) {
      a.setAttribute("aria-current", "true");
      // keep the active pill visible in the horizontally scrolling bar (never scroll the page)
      const bar = a.closest("ul");
      bar.scrollTo({ left: a.parentElement.offsetLeft - 16, behavior: "smooth" });
    } else {
      a.removeAttribute("aria-current");
    }
  });
  const observer = new IntersectionObserver((entries) => {
    const visible = entries.filter((e) => e.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
    if (visible.length) mark(visible[0].target.id);
  }, { rootMargin: "-30% 0px -60% 0px" });
  sections.forEach((s) => observer.observe(s));
})();
