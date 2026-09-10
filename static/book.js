// Turns pages in place. Every link still works as a plain link without this file.
(function () {
  const book = document.getElementById("book");
  if (!book) return;

  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");
  const narrow = matchMedia("(max-width: 760px)");
  const turnTime = parseFloat(getComputedStyle(document.documentElement).getPropertyValue("--turn-time")) || 900;
  let busy = false;

  function currentSpread() {
    return book.querySelector(".spread");
  }

  async function fetchSpread(url) {
    const separator = url.includes("?") ? "&" : "?";
    const response = await fetch(url + separator + "fragment=1", { headers: { "X-Requested-With": "book" } });
    if (!response.ok) throw new Error("no page at " + url);
    const html = await response.text();
    const doc = new DOMParser().parseFromString(html, "text/html");
    return doc.querySelector(".spread");
  }

  function pageFace(spread, which) {
    // The right-hand slot holds the recto, or the cover when the book is closed.
    const pages = spread.querySelectorAll(":scope > .page");
    const page = which === "left" ? pages[0] : pages[1];
    return page.cloneNode(true);
  }

  function swapNav(spread) {
    const nav = document.querySelector(".turn");
    const index = Number(spread.dataset.index);
    const back = nav.querySelector(".turn-back");
    const forward = nav.querySelector(".turn-forward");
    const slugs = JSON.parse(book.dataset.slugs);
    if (back) back.remove();
    if (forward) forward.remove();
    if (index > 0) {
      const a = document.createElement("a");
      a.className = "turn-back";
      a.rel = "prev";
      a.href = index - 1 === 0 ? "/" : "/" + slugs[index - 1];
      a.textContent = "Previous page";
      nav.prepend(a);
    }
    if (index + 1 < slugs.length) {
      const a = document.createElement("a");
      a.className = "turn-forward";
      a.rel = "next";
      a.href = "/" + slugs[index + 1];
      a.textContent = "Next page";
      nav.append(a);
    }
  }

  function finish(next) {
    document.title = next.dataset.title;
    swapNav(next);
    busy = false;
  }

  async function turnTo(url, push) {
    if (busy) return;
    busy = true;
    let next;
    try {
      next = await fetchSpread(url);
    } catch (_error) {
      location.href = url;
      return;
    }
    const current = currentSpread();
    const forward = Number(next.dataset.index) > Number(current.dataset.index);
    if (push) history.pushState({ index: Number(next.dataset.index) }, "", url);

    if (reduceMotion.matches || narrow.matches) {
      current.replaceWith(next);
      finish(next);
      return;
    }

    const leaf = document.createElement("div");
    leaf.className = "leaf " + (forward ? "forward" : "backward");
    const front = document.createElement("div");
    front.className = "face front";
    front.append(pageFace(current, forward ? "right" : "left"));
    const back = document.createElement("div");
    back.className = "face back";
    back.append(pageFace(next, forward ? "left" : "right"));
    leaf.append(front, back);

    // The page the leaf lands on stays hidden until it arrives.
    next.classList.add("incoming");
    const landing = next.querySelectorAll(":scope > .page")[forward ? 0 : 1];
    landing.classList.add("hidden-until-landed");
    // The page the leaf lifts off is covered by the leaf's front, so the incoming page beneath shows.
    const lifted = current.querySelectorAll(":scope > .page")[forward ? 1 : 0];
    lifted.classList.add("hidden-until-landed");

    book.classList.add("turning");
    current.after(next);
    book.append(leaf);

    requestAnimationFrame(() => requestAnimationFrame(() => leaf.classList.add("turning")));
    setTimeout(() => {
      landing.classList.remove("hidden-until-landed");
      next.classList.remove("incoming");
      current.remove();
      leaf.remove();
      book.classList.remove("turning");
      finish(next);
    }, turnTime + 30);
  }

  document.addEventListener("click", (event) => {
    const link = event.target.closest("a");
    if (!link || link.origin !== location.origin || link.target) return;
    if (!/^\/[a-z-]*$/.test(link.pathname)) return;
    if (link.pathname === location.pathname) return;
    event.preventDefault();
    turnTo(link.pathname, true);
  });

  document.addEventListener("keydown", (event) => {
    if (event.altKey || event.ctrlKey || event.metaKey) return;
    const rel = event.key === "ArrowRight" ? "next" : event.key === "ArrowLeft" ? "prev" : null;
    if (!rel) return;
    const link = document.querySelector('.turn a[rel="' + rel + '"]');
    if (link) turnTo(link.pathname, true);
  });

  addEventListener("popstate", () => {
    turnTo(location.pathname, false);
  });
})();
