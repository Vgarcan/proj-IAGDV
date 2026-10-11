/**
 * Progressive visual behaviour for the documentation site.
 * The guide remains fully usable when JavaScript is unavailable.
 */
(() => {
  "use strict";

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const hero = document.querySelector("[data-parallax-root]");
  const layers = [...document.querySelectorAll("[data-parallax-layer]")];

  if (!reducedMotion && hero && layers.length) {
    let scheduled = false;
    const render = () => {
      const rect = hero.getBoundingClientRect();
      const travel = Math.max(-rect.height, Math.min(window.innerHeight, -rect.top));
      layers.forEach((layer) => {
        const speed = Number(layer.dataset.speed || 0);
        layer.style.transform = `translate3d(0, ${travel * speed}px, 0)`;
      });
      scheduled = false;
    };
    const requestRender = () => {
      if (!scheduled) {
        window.requestAnimationFrame(render);
        scheduled = true;
      }
    };
    window.addEventListener("scroll", requestRender, { passive: true });
    window.addEventListener("resize", requestRender);
    render();
  }
})();
