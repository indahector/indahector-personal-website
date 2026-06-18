/* Héctor Inda Díaz — site behavior
   - mobile nav toggle
   - contour isoline signature (generated)
   - scroll reveal
   - active nav state + footer year
*/
(function () {
  "use strict";

  /* ---- mobile nav ---- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") links.classList.remove("open");
    });
  }

  /* ---- active nav link ---- */
  var here = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  document.querySelectorAll(".nav-links a").forEach(function (a) {
    var href = (a.getAttribute("href") || "").toLowerCase();
    if (href === here || (here === "" && href === "index.html")) a.classList.add("active");
  });

  /* ---- footer year ---- */
  var y = document.querySelector("[data-year]");
  if (y) y.textContent = new Date().getFullYear();

  /* ---- contour isolines (the signature) ---- */
  var SVGNS = "http://www.w3.org/2000/svg";
  function buildContours(svg) {
    var W = 1000, H = 700;
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    svg.setAttribute("preserveAspectRatio", "xMidYMid slice");
    var stroke = svg.getAttribute("data-stroke") || "#17605c";
    var baseOp = parseFloat(svg.getAttribute("data-opacity") || "0.16");
    var lines = parseInt(svg.getAttribute("data-lines") || "15", 10);

    var g = document.createElementNS(SVGNS, "g");
    g.setAttribute("class", "contour-group");

    // a few sine components per line for an organic, field-like look
    for (var i = 0; i < lines; i++) {
      var t = i / (lines - 1);
      var yBase = -40 + t * (H + 80);
      var a1 = 26 + 30 * Math.sin(i * 0.9);
      var a2 = 14 + 12 * Math.cos(i * 0.6 + 1.3);
      var f1 = 1.1 + 0.5 * Math.sin(i * 0.4);
      var f2 = 2.3 + 0.7 * Math.cos(i * 0.7);
      var ph = i * 0.7;
      var d = "";
      for (var x = -80; x <= W + 80; x += 14) {
        var yy =
          yBase +
          a1 * Math.sin((x / W) * Math.PI * 2 * f1 + ph) +
          a2 * Math.sin((x / W) * Math.PI * 2 * f2 + ph * 1.7);
        d += (x === -80 ? "M" : "L") + x.toFixed(1) + " " + yy.toFixed(1) + " ";
      }
      var p = document.createElementNS(SVGNS, "path");
      p.setAttribute("d", d.trim());
      p.setAttribute("fill", "none");
      p.setAttribute("stroke", stroke);
      p.setAttribute("stroke-width", (0.9 + (i % 3 === 0 ? 0.5 : 0)).toFixed(2));
      // gently fade lines toward the vertical edges of the field
      var edgeFade = 1 - Math.abs(t - 0.5) * 0.7;
      p.setAttribute("stroke-opacity", (baseOp * edgeFade).toFixed(3));
      g.appendChild(p);
    }
    svg.appendChild(g);
  }
  document.querySelectorAll(".js-contours").forEach(buildContours);

  /* ---- scroll reveal ---- */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealEls = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  }
})();
