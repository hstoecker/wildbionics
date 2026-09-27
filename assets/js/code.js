// Copy buttons for code blocks: every highlighted block in .prose and the .code-card on the home
// page. Pure enhancement – without JavaScript the code stays selectable. Where the Clipboard API
// is missing or denied, the code is selected and copied the old way (or left selected for Ctrl+C).
// Labels come from _data/i18n.yml via data attributes on the <script> tag.
(() => {
  const labels = document.currentScript.dataset;
  const status = document.createElement("p");
  status.className = "visually-hidden";
  status.setAttribute("role", "status");
  document.body.appendChild(status);

  async function copy(code) {
    const text = code.textContent.replace(/\s+$/, "") + "\n";
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
  }

  // Code that scrolls sideways (Python keeps its indentation) must be reachable by keyboard.
  const markScrollable = () => document.querySelectorAll(".prose .highlight pre, .code-card pre").forEach((pre) => {
    if (pre.scrollWidth > pre.clientWidth + 1) pre.setAttribute("tabindex", "0");
    else pre.removeAttribute("tabindex");
  });
  markScrollable();
  window.addEventListener("resize", markScrollable);

  const blocks = document.querySelectorAll(".prose div.highlighter-rouge, .code-card");
  blocks.forEach((block) => {
    const code = block.querySelector("pre code");
    if (!code) return;
    const button = document.createElement("button");
    button.type = "button";
    button.className = "code-copy";
    button.setAttribute("aria-label", labels.copyLabel);
    button.innerHTML = '<svg aria-hidden="true" focusable="false"><use href="#icon-copy"/></svg><span aria-hidden="true"></span>';
    const text = button.querySelector("span");
    text.textContent = labels.copy;
    let timer;
    button.addEventListener("click", async () => {
      if (!(await copy(code))) return; // code is left selected
      button.classList.add("is-done");
      text.textContent = labels.copied;
      status.textContent = labels.copiedStatus;
      clearTimeout(timer);
      timer = setTimeout(() => {
        button.classList.remove("is-done");
        text.textContent = labels.copy;
        status.textContent = "";
      }, 2000);
    });
    const bar = block.querySelector(".code-card__bar");
    if (bar) {
      bar.appendChild(button);
    } else {
      block.classList.add("has-copy");
      block.prepend(button);
    }
  });
})();
