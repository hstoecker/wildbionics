// WildBionics knowledge graph: loads /graph.json and draws an interactive SVG.
// No dependencies – a small deterministic force layout:
//   · the four dimensions are fixed anchors (corners), their terms cluster around them,
//   · articles sit between the clusters, organisms and lenses orbit their articles.
// Accessible: article nodes are real links, all other nodes are focusable buttons that
// announce their connections; a complete list of connections is rendered server-side.
(() => {
  const stage = document.querySelector("[data-graph]");
  if (!stage) return;
  const svg = stage.querySelector(".graph-svg");
  const info = stage.querySelector(".graph-info");
  const lang = stage.dataset.lang;
  const NS = "http://www.w3.org/2000/svg";
  const DIMS = ["time", "space", "physics", "adjacent_sciences"];
  const typeLabel = {
    article: stage.dataset.labelArticle,
    being: stage.dataset.labelBeing,
    "thought-experiment": stage.dataset.labelThoughtExperiment,
  };
  const dimLabel = Object.fromEntries(DIMS.map((d) => [d, stage.dataset["label" + d.split("_").map((w) => w[0].toUpperCase() + w.slice(1)).join("")]]));

  // Node sizes and preferred edge lengths (in viewBox units).
  const RADIUS = { dimension: 28, article: 20, being: 11, "thought-experiment": 11, term: 7 };
  const LENGTH = { contains: 78, about: 120 };
  const ARTICLE_TERM = 210;

  let data, nodes, edges, byId, layoutKind, pinned = null;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const nameTpl = stage.dataset.nodeName || "%NAME% (%TYPE%), %N%";
  const nameDimTpl = stage.dataset.nodeNameDim || "%NAME%, %N%";

  // ---------------------------------------------------------------------------
  // Layout
  // ---------------------------------------------------------------------------
  function frame(kind) {
    // Landscape for wide screens, portrait for phones – labels stay readable.
    return kind === "portrait"
      ? { w: 640, h: 1080, fan: 170, anchors: { time: [150, 110], space: [490, 110], physics: [490, 930], adjacent_sciences: [150, 930] } }
      : { w: 1100, h: 720, fan: 150, anchors: { time: [170, 110], space: [930, 110], physics: [930, 610], adjacent_sciences: [170, 610] } };
  }

  function seeded(i) {           // deterministic pseudo-random in [-1, 1]
    const x = Math.sin(i * 12.9898 + 78.233) * 43758.5453;
    return (x - Math.floor(x)) * 2 - 1;
  }

  function layout(kind) {
    const f = frame(kind);
    const cx = f.w / 2, cy = f.h / 2;
    nodes.forEach((n, i) => {
      if (n.type === "dimension") {
        [n.x, n.y] = f.anchors[n.dim];
        n.fixed = true;
      } else if (n.type === "term") {
        const [ax, ay] = f.anchors[n.dim];
        n.x = ax + seeded(i) * 90; n.y = ay + seeded(i + 99) * 90;
      } else {
        n.x = cx + seeded(i) * 120; n.y = cy + seeded(i + 7) * 90;
      }
      n.vx = n.vy = 0;
    });

    for (let step = 0, alpha = 1; step < 600; step++, alpha *= 0.992) {
      // Repulsion between all node pairs
      for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
          const a = nodes[i], b = nodes[j];
          let dx = b.x - a.x, dy = b.y - a.y;
          let d2 = dx * dx + dy * dy;
          if (d2 < 1) { dx = seeded(i + j); dy = seeded(i - j); d2 = 1; }
          // Terms need room for their labels, which sit beside them; articles for their long titles
          const labelRoom = a.type === "article" && b.type === "article" ? 140 : a.type === "term" && b.type === "term" ? 48 : 26;
          const min = RADIUS[a.type] + RADIUS[b.type] + labelRoom;
          const force = (min * min * 2.2) / d2 * alpha;
          const d = Math.sqrt(d2);
          const fx = (dx / d) * force, fy = (dy / d) * force;
          a.vx -= fx; a.vy -= fy; b.vx += fx; b.vy += fy;
        }
      }
      // Springs along edges
      edges.forEach((e) => {
        const a = e.s, b = e.t;
        const target = LENGTH[e.type] || ARTICLE_TERM;
        const strength = e.type === "contains" || e.type === "about" ? 0.08 : 0.012;
        const dx = b.x - a.x, dy = b.y - a.y;
        const d = Math.sqrt(dx * dx + dy * dy) || 1;
        const k = ((d - target) / d) * strength * alpha;
        a.vx += dx * k; a.vy += dy * k; b.vx -= dx * k; b.vy -= dy * k;
      });
      // Terms stay near their dimension, everything else drifts to the centre; integrate
      nodes.forEach((n) => {
        if (n.fixed) { n.vx = n.vy = 0; return; }
        // Terms fan out on the inner side of their dimension (towards the centre), which
        // keeps the outer side free for the dimension label and the canvas edge free of labels.
        let tx = cx, ty = cy, pull = 0.002;
        if (n.type === "term") {
          const [ax, ay] = f.anchors[n.dim];
          const ux = cx - ax, uy = cy - ay, ul = Math.hypot(ux, uy);
          tx = ax + (ux / ul) * f.fan; ty = ay + (uy / ul) * f.fan;
          pull = 0.03;
        }
        n.vx += (tx - n.x) * pull * alpha;
        n.vy += (ty - n.y) * pull * alpha;
        n.x += n.vx; n.y += n.vy;
        n.vx *= 0.6; n.vy *= 0.6;
        const r = RADIUS[n.type] + (n.type === "term" ? 70 : 40);
        n.x = Math.max(r, Math.min(f.w - r, n.x));
        n.y = Math.max(r, Math.min(f.h - r, n.y));
      });
    }
    svg.setAttribute("viewBox", `0 0 ${f.w} ${f.h}`);
  }

  // ---------------------------------------------------------------------------
  // Rendering
  // ---------------------------------------------------------------------------
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  const el = (name, attrs = {}, parent) => {
    const node = document.createElementNS(NS, name);
    Object.entries(attrs).forEach(([k, v]) => node.setAttribute(k, v));
    if (parent) parent.appendChild(node);
    return node;
  };

  function describe(n) {
    if (n.type === "dimension") return dimLabel[n.dim];
    if (n.type === "term") return dimLabel[n.dim] + (n.used ? "" : " · " + stage.dataset.labelUnused);
    return typeLabel[n.type];
  }

  function render() {
    svg.textContent = "";
    // tap area of at least 22 px radius on screen, whatever the scale of the drawing
    const ctm = svg.getScreenCTM();          // real scale, also when max-height letterboxes the drawing
    const scale = (ctm && ctm.a) || 1;
    const hitRadius = 22 / scale;
    const gEdges = el("g", { class: "edges" }, svg);
    const gNodes = el("g", { class: "nodes" }, svg);

    edges.forEach((e) => {
      e.line = el("line", { class: `edge edge--${e.type}${e.lens ? " edge--lens" : ""}`, "data-dim": e.s.dim || e.t.dim || "" }, gEdges);
    });

    nodes.forEach((n) => {
      const label = n.label[lang] || n.label.en;
      const count = n.links.length;
      // "Mechanics (Rules), 3 connections" – dimension nodes without the repeated type
      const name = (n.type === "dimension" ? nameDimTpl : nameTpl)
        .replace("%NAME%", label).replace("%TYPE%", describe(n)).replace("%N%", count);
      let g;
      if (n.type === "article") {
        g = el("a", { href: n.url[lang] || n.url.en, class: "node node--article", "aria-label": name }, gNodes);
      } else {
        g = el("g", { class: `node node--${n.type}${n.used === false ? " is-unused" : ""}`, tabindex: "0", role: "button", "aria-pressed": "false", "aria-label": name }, gNodes);
      }
      if (n.dim) g.setAttribute("data-dim", n.dim);
      el("circle", { class: "node-hit", r: Math.max(RADIUS[n.type], hitRadius) }, g);
      el("circle", { r: RADIUS[n.type] }, g);
      // Term labels point away from their dimension (radially), others sit below the node.
      let attrs = { class: "node-label", "text-anchor": "middle", y: RADIUS[n.type] + 15 };
      if (n.type === "dimension") {
        // Outer side: above for the top row, below for the bottom row
        attrs.y = n.y < svg.viewBox.baseVal.height / 2 ? -RADIUS.dimension - 12 : RADIUS.dimension + 24;
      }
      if (n.type === "term") {
        // Labels point towards the middle of the canvas, so they never run off its edge.
        const right = n.x < svg.viewBox.baseVal.width / 2;
        attrs = { class: "node-label", "text-anchor": right ? "start" : "end", x: right ? RADIUS.term + 6 : -RADIUS.term - 6, y: 4 };
      }
      const text = el("text", attrs, g);
      text.textContent = label;
      n.g = g;

      g.addEventListener("pointerenter", () => { if (!pinned) highlight(n); });
      g.addEventListener("pointerleave", () => { if (!pinned) highlight(null); });
      g.addEventListener("focus", () => highlight(n));
      g.addEventListener("blur", () => { if (!pinned) highlight(null); });
      if (n.type !== "article") {
        const toggle = () => {
          pinned = pinned === n ? null : n;
          nodes.forEach((m) => { if (m.g.getAttribute("role") === "button") m.g.setAttribute("aria-pressed", String(pinned === m)); });
          highlight(pinned || n);
          // on phones the info panel sits below the drawing – bring it into view
          if (pinned && window.matchMedia("(max-width: 640px)").matches) {
            info.scrollIntoView({ block: "nearest", behavior: reduceMotion ? "auto" : "smooth" });
          }
        };
        g.addEventListener("click", toggle);
        g.addEventListener("keydown", (ev) => { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); toggle(); } });
      }
      enableDrag(n);
    });
    relaxLabels();
    position();
  }

  function visibleBox(g) {
    const parts = [...g.children].filter((c) => !c.classList.contains("node-hit")).map((c) => c.getBBox());
    const x0 = Math.min(...parts.map((p) => p.x)), y0 = Math.min(...parts.map((p) => p.y));
    const x1 = Math.max(...parts.map((p) => p.x + p.width)), y1 = Math.max(...parts.map((p) => p.y + p.height));
    return { x: x0, y: y0, width: x1 - x0, height: y1 - y0 };
  }

  // Second pass: the force layout only knows circles. Measure the real label boxes and
  // push overlapping terms, organisms and articles apart (dimensions stay where they are).
  function relaxLabels() {
    const vb = svg.viewBox.baseVal;
    nodes.forEach((n) => {
      n.g.setAttribute("transform", `translate(${n.x} ${n.y})`);
      const b = visibleBox(n.g);   // circle + label, not the invisible tap area
      const pad = 3;
      n.box = { x0: b.x - pad, y0: b.y - pad, x1: b.x + b.width + pad, y1: b.y + b.height + pad };
      n.movable = n.type !== "dimension";
    });
    for (let iter = 0; iter < 200; iter++) {
      let moved = false;
      for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
          const a = nodes[i], b = nodes[j];
          if (!a.movable && !b.movable) continue;
          const ox = Math.min(a.x + a.box.x1, b.x + b.box.x1) - Math.max(a.x + a.box.x0, b.x + b.box.x0);
          const oy = Math.min(a.y + a.box.y1, b.y + b.box.y1) - Math.max(a.y + a.box.y0, b.y + b.box.y0);
          if (ox <= 0 || oy <= 0) continue;
          const dir = a.y < b.y || (a.y === b.y && i < j) ? -1 : 1;   // a goes up, b down
          const shift = oy + 1;
          if (a.movable && b.movable) { a.y += (dir * shift) / 2; b.y -= (dir * shift) / 2; }
          else if (a.movable) a.y += dir * shift;
          else b.y -= dir * shift;
          moved = true;
        }
      }
      nodes.forEach((n) => {
        if (!n.movable) return;
        n.y = Math.max(-n.box.y0, Math.min(vb.height - n.box.y1, n.y));
        n.x = Math.max(-n.box.x0, Math.min(vb.width - n.box.x1, n.x));
      });
      if (!moved) break;
    }
  }

  function position() {
    edges.forEach((e) => {
      e.line.setAttribute("x1", e.s.x.toFixed(1)); e.line.setAttribute("y1", e.s.y.toFixed(1));
      e.line.setAttribute("x2", e.t.x.toFixed(1)); e.line.setAttribute("y2", e.t.y.toFixed(1));
    });
    nodes.forEach((n) => n.g.setAttribute("transform", `translate(${n.x.toFixed(1)} ${n.y.toFixed(1)})`));
  }

  function highlight(n) {
    stage.classList.toggle("has-active", !!n);
    const near = new Set(n ? [n, ...n.links] : []);
    nodes.forEach((m) => m.g.classList.toggle("is-active", near.has(m)));
    edges.forEach((e) => e.line.classList.toggle("is-active", !!n && (e.s === n || e.t === n)));
    if (!n) { info.hidden = true; return; }
    const label = n.label[lang] || n.label.en;
    const items = n.links.map((m) => {
      const l = m.label[lang] || m.label.en;
      return m.type === "article" ? `<li><a href="${esc(m.url[lang] || m.url.en)}">${esc(l)}</a></li>` : `<li>${esc(l)}</li>`;
    }).join("");
    info.innerHTML = `<p class="graph-info__type">${esc(describe(n))}</p><p class="graph-info__title">${esc(label)}</p>` +
      (n.taxon ? `<p class="graph-info__taxon"><i>${esc(n.taxon)}</i></p>` : "") +
      (n.type === "article" ? `<p><a href="${esc(n.url[lang] || n.url.en)}">${esc(n.title[lang] || n.title.en)} →</a></p>` : "") +
      (items ? `<ul>${items}</ul>` : "");
    info.hidden = false;
  }

  function enableDrag(n) {
    let start = null;
    n.g.addEventListener("pointerdown", (ev) => {
      start = { x: ev.clientX, y: ev.clientY, nx: n.x, ny: n.y, moved: false };
      n.g.setPointerCapture(ev.pointerId);
    });
    n.g.addEventListener("pointermove", (ev) => {
      if (!start) return;
      const ctm = svg.getScreenCTM();
      const dx = (ev.clientX - start.x) / ctm.a, dy = (ev.clientY - start.y) / ctm.d;
      if (Math.abs(dx) + Math.abs(dy) > 4) start.moved = true;
      if (!start.moved) return;
      n.x = start.nx + dx; n.y = start.ny + dy;
      position();
    });
    n.g.addEventListener("pointerup", () => {
      if (start && start.moved) n.g.addEventListener("click", (e) => { e.preventDefault(); e.stopImmediatePropagation(); }, { once: true, capture: true });
      start = null;
    });
  }

  // ---------------------------------------------------------------------------
  // Filters, stats, start
  // ---------------------------------------------------------------------------
  function applyFilter() {
    const on = new Set([...stage.querySelectorAll(".graph-filter input:checked")].map((i) => i.value));
    nodes.forEach((n) => { if (n.dim) n.g.classList.toggle("is-hidden", !on.has(n.dim)); });
    edges.forEach((e) => {
      const dim = e.s.dim || e.t.dim;
      e.line.classList.toggle("is-hidden", !!dim && !on.has(dim));
    });
  }

  function build() {
    const kind = stage.clientWidth < 640 ? "portrait" : "landscape";
    if (kind === layoutKind) return;
    layoutKind = kind;
    layout(kind);
    render();
    applyFilter();
  }

  fetch(stage.dataset.graph)
    .then((r) => r.json())
    .then((json) => {
      data = json;
      nodes = data.nodes.map((n) => ({ ...n, links: [] }));
      byId = Object.fromEntries(nodes.map((n) => [n.id, n]));
      const merged = new Map();
      data.edges.forEach((e) => {
        const key = e.source + ">" + e.target;
        if (merged.has(key)) { merged.get(key).lens = merged.get(key).lens || e.lens; return; }
        merged.set(key, { ...e, s: byId[e.source], t: byId[e.target] });
      });
      edges = [...merged.values()].filter((e) => e.s && e.t);
      edges.forEach((e) => { e.s.links.push(e.t); e.t.links.push(e.s); });

      const stats = document.querySelector("[data-graph-stats]");
      if (stats) {
        stats.textContent = stats.dataset.template
          .replace("%A%", nodes.filter((n) => n.type === "article").length)
          .replace("%T%", nodes.filter((n) => n.type === "term").length)
          .replace("%E%", edges.length);
      }
      stage.classList.add("is-ready");
      build();
      const list = document.querySelector("[data-graph-list]");
      if (list) list.open = false;   // the drawing replaces the list; it stays one click away
      stage.querySelectorAll(".graph-filter input").forEach((i) => i.addEventListener("change", applyFilter));
      let t;
      window.addEventListener("resize", () => { clearTimeout(t); t = setTimeout(build, 200); });
      document.addEventListener("keydown", (ev) => {
        if (ev.key === "Escape" && pinned) {
          pinned = null;
          nodes.forEach((m) => { if (m.g.getAttribute("role") === "button") m.g.setAttribute("aria-pressed", "false"); });
          highlight(null);
        }
      });
    })
    .catch(() => stage.classList.add("is-failed"));
})();
