// Contribution guide: copy buttons for command blocks and a sub-navigation that marks the
// section currently in view. Pure enhancement – without JavaScript the page is complete.
(() => {
  const guide = document.querySelector("[data-guide]");
  if (!guide) return;

  // Copy buttons – placed next to the <pre> (not inside it, so "Copy" never becomes part of the
  // command for screen readers or a manual selection). Clipboard API with a fallback; the result
  // is announced in a status region.
  const copyLabel = guide.dataset.copyLabel || "Copy";
  const copiedLabel = guide.dataset.copiedLabel || "Copied";
  const status = document.createElement("p");
  status.className = "visually-hidden";
  status.setAttribute("role", "status");
  guide.appendChild(status);
  const copy = async (code) => {
    const text = code.innerText.trim();
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch (e) {
      const range = document.createRange();
      range.selectNodeContents(code);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      let copied = false;
      try { copied = document.execCommand("copy"); } catch (e2) { /* stays selected for Ctrl+C */ }
      if (copied) selection.removeAllRanges();
      return copied;
    }
  };
  guide.querySelectorAll("pre.guide-code").forEach((pre) => {
    const code = pre.querySelector("code");
    if (!code) return;
    const wrap = document.createElement("div");
    wrap.className = "guide-code-wrap";
    pre.before(wrap);
    const button = document.createElement("button");
    button.type = "button";
    button.className = "guide-copy";
    button.innerHTML = "<span>" + copyLabel + "</span>";
    let timer;
    button.addEventListener("click", async () => {
      if (!(await copy(code))) return; // left selected
      button.classList.add("is-done");
      button.querySelector("span").textContent = copiedLabel;
      status.textContent = copiedLabel;
      clearTimeout(timer);
      timer = setTimeout(() => {
        button.classList.remove("is-done");
        button.querySelector("span").textContent = copyLabel;
        status.textContent = "";
      }, 2000);
    });
    wrap.append(button, pre);
  });

  // Sub-navigation: mark the section in view
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const links = [...document.querySelectorAll(".guide-subnav a[href^='#']")];
  const sections = links.map((a) => document.getElementById(a.hash.slice(1))).filter(Boolean);
  if (!("IntersectionObserver" in window) || !sections.length) return;
  const mark = (id) => links.forEach((a) => {
    if (a.hash === "#" + id) {
      a.setAttribute("aria-current", "true");
      // keep the active pill visible in the horizontally scrolling bar (never scroll the page)
      const bar = a.closest("ul");
      bar.scrollTo({ left: a.parentElement.offsetLeft - 16, behavior: reduceMotion ? "auto" : "smooth" });
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
