/* =========================================================
   FRIG ZONE — main.js
   Menú, carrusel de marcas, formularios y animaciones.
   ========================================================= */
(function () {
  "use strict";

  var WA = "5491173719821";

  /* ---------- Menú móvil ---------- */
  var burger = document.querySelector(".burger");
  var mobileNav = document.getElementById("mobileNav");
  if (burger && mobileNav) {
    burger.addEventListener("click", function () {
      var open = mobileNav.classList.toggle("open");
      burger.setAttribute("aria-expanded", String(open));
      burger.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
    });
    mobileNav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        mobileNav.classList.remove("open");
        burger.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---------- Año ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---------- Reveal ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Carrusel de marcas ---------- */
  var track = document.getElementById("brandsTrack");
  var prev = document.querySelector("[data-brands-prev]");
  var next = document.querySelector("[data-brands-next]");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function step() {
    if (!track) return 320;
    var first = track.querySelector(".brand");
    if (!first) return 320;
    return first.getBoundingClientRect().width + 12;
  }

  if (track) {
    if (prev) prev.addEventListener("click", function () { track.scrollBy({ left: -step() * 2, behavior: "smooth" }); });
    if (next) next.addEventListener("click", function () { track.scrollBy({ left: step() * 2, behavior: "smooth" }); });

    var timer = null;
    var paused = false;

    function tick() {
      if (paused || !track) return;
      var max = track.scrollWidth - track.clientWidth - 2;
      if (track.scrollLeft >= max) {
        track.scrollTo({ left: 0, behavior: "smooth" });
      } else {
        track.scrollBy({ left: step(), behavior: "smooth" });
      }
    }

    function start() {
      if (reduce || timer) return;
      timer = setInterval(tick, 3200);
    }
    function stop() {
      if (timer) { clearInterval(timer); timer = null; }
    }

    track.addEventListener("mouseenter", function () { paused = true; });
    track.addEventListener("mouseleave", function () { paused = false; });
    track.addEventListener("focusin", function () { paused = true; });
    track.addEventListener("focusout", function () { paused = false; });
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) stop(); else start();
    });

    start();
  }

  /* ---------- Formularios -> WhatsApp ---------- */
  function buildMessage(form) {
    var data = new FormData(form);
    var lines = ["Hola Frig Zone, les escribo desde la web."];
    form.querySelectorAll("[data-label]").forEach(function (field) {
      var val = (data.get(field.name) || "").toString().trim();
      if (val) lines.push("• " + field.getAttribute("data-label") + ": " + val);
    });
    return lines.join("\n");
  }

  document.querySelectorAll("form[data-wa-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = buildMessage(form);
      var url = "https://wa.me/" + WA + "?text=" + encodeURIComponent(msg);

      // Guardado local de demostración (sin backend todavía)
      try {
        var leads = JSON.parse(localStorage.getItem("fz_leads") || "[]");
        var obj = {};
        new FormData(form).forEach(function (v, k) { obj[k] = v; });
        obj.fecha = new Date().toISOString();
        obj.pagina = location.pathname;
        leads.push(obj);
        localStorage.setItem("fz_leads", JSON.stringify(leads));
      } catch (err) { /* modo privado */ }

      var msgEl = form.querySelector(".form-msg");
      if (msgEl) {
        msgEl.textContent = "Listo. Abrimos WhatsApp con tu consulta cargada. Si no se abrió, tocá el botón verde.";
        msgEl.classList.add("show");
      }
      window.open(url, "_blank", "noopener");
    });
  });

  /* ---------- FAQ: acordeón exclusivo ---------- */
  document.querySelectorAll(".faq details").forEach(function (d) {
    d.addEventListener("toggle", function () {
      if (!d.open) return;
      d.closest(".faq").querySelectorAll("details").forEach(function (other) {
        if (other !== d) other.open = false;
      });
    });
  });

  /* ---------- Marcadores de scroll activos ---------- */
  var sections = document.querySelectorAll("main [id]");
  var links = document.querySelectorAll('.nav a[href^="#"]');
  if ("IntersectionObserver" in window && sections.length && links.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        links.forEach(function (l) {
          l.classList.toggle("active", l.getAttribute("href") === "#" + en.target.id);
        });
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    sections.forEach(function (s) { spy.observe(s); });
  }
})();
