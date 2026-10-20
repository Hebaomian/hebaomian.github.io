(() => {
  "use strict";
  const list = document.querySelector("#publication-list");
  const papers = window.PUBLICATIONS || [];
  const escape = value => String(value).replace(/[&<>"']/g, char => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[char]));
  const renderPaper = paper => `<article class="publication" data-topic="${paper.topic}" id="paper-${paper.id}">
    <div class="publication-meta"><span class="venue-badge ${paper.group === "Preprints" ? "preprint" : ""}">${escape(paper.badge)}</span><span class="paper-year">${paper.year}</span></div>
    <div class="publication-content">
      <h4><a href="${escape(paper.url)}" target="_blank" rel="noopener">${escape(paper.title)}</a></h4>
      <p class="authors">${paper.authors.map(name => name === "Zishuo Zhao" ? `<strong>${name}</strong>` : escape(name)).join(", ")}</p>
      <p class="paper-venue">${escape(paper.venue)}</p>
      <div class="paper-links">
        <a href="${escape(paper.url)}" target="_blank" rel="noopener">${paper.searchLink ? "FIND PAPER" : paper.group === "Preprints" ? "ARXIV" : "PAPER"} ↗</a>
        ${paper.pdf ? `<a href="${escape(paper.pdf)}" target="_blank" rel="noopener">PDF ↗</a>` : ""}
        <button data-disclosure="${paper.id}-summary" aria-expanded="false" aria-controls="${paper.id}-summary">${paper.abstract ? "ABSTRACT" : "OVERVIEW"}</button>
        <button data-disclosure="${paper.id}-bib" aria-expanded="false" aria-controls="${paper.id}-bib">BIBTEX</button>
      </div>
      <div class="paper-details" id="${paper.id}-summary" hidden><p>${escape(paper.abstract || paper.summary)}</p></div>
      <div class="paper-details bibtex-wrap" id="${paper.id}-bib" hidden><button class="copy-bib" data-copy="${paper.id}" aria-label="Copy citation for ${escape(paper.title)}">Copy citation</button><pre>${escape(paper.bibtex)}</pre></div>
    </div>
  </article>`;
  for (const group of [...new Set(papers.map(paper => paper.group))]) {
    const section = document.createElement("section");
    section.className = "publication-group";
    const groupId = group.toLowerCase().replaceAll(" ", "-");
    section.setAttribute("aria-labelledby", groupId);
    section.innerHTML = `<h3 id="${groupId}">${escape(group)}</h3>${papers.filter(paper => paper.group === group).map(renderPaper).join("")}`;
    list.append(section);
  }

  function setFilter(filter) {
    document.querySelectorAll("[data-filter]").forEach(button => {
      const selected = button.dataset.filter === filter;
      button.classList.toggle("selected", selected);
      button.setAttribute("aria-pressed", String(selected));
    });
    let count = 0;
    document.querySelectorAll(".publication").forEach(paper => {
      paper.hidden = filter !== "all" && paper.dataset.topic !== filter;
      if (!paper.hidden) count++;
    });
    document.querySelectorAll(".publication-group").forEach(group => {
      group.hidden = [...group.querySelectorAll(".publication")].every(paper => paper.hidden);
    });
    document.querySelector(".filter-result").textContent = `${count} ${count === 1 ? "publication" : "publications"} shown.`;
  }
  document.querySelectorAll("[data-filter]").forEach(button => button.addEventListener("click", () => setFilter(button.dataset.filter)));
  document.querySelectorAll("[data-research-filter]").forEach(link => link.addEventListener("click", () => setFilter(link.dataset.researchFilter)));

  let toastTimer;
  function toast(message) {
    const element = document.querySelector(".toast");
    element.textContent = message;
    element.classList.add("visible");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => element.classList.remove("visible"), 2400);
  }
  list.addEventListener("click", async event => {
    const disclosure = event.target.closest("[data-disclosure]");
    if (disclosure) {
      const panel = document.getElementById(disclosure.dataset.disclosure);
      panel.hidden = !panel.hidden;
      disclosure.setAttribute("aria-expanded", String(!panel.hidden));
    }
    const copy = event.target.closest("[data-copy]");
    if (copy) {
      const paper = papers.find(paper => paper.id === copy.dataset.copy);
      try {
        await navigator.clipboard.writeText(paper.bibtex);
        toast("Citation copied to clipboard.");
      } catch {
        const range = document.createRange();
        range.selectNodeContents(copy.parentElement.querySelector("pre"));
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        toast("Citation selected. Press Ctrl+C or ⌘C to copy.");
      }
    }
  });

  const menu = document.querySelector(".menu-toggle");
  const navigation = document.querySelector("#navigation");
  menu.addEventListener("click", () => {
    const open = navigation.classList.toggle("open");
    menu.setAttribute("aria-expanded", String(open));
    menu.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
  });
  navigation.querySelectorAll("a").forEach(link => link.addEventListener("click", () => {
    navigation.classList.remove("open");
    menu.setAttribute("aria-expanded", "false");
    menu.setAttribute("aria-label", "Open navigation");
  }));
  document.addEventListener("keydown", event => {
    if (event.key === "Escape") {
      navigation.classList.remove("open");
      menu.setAttribute("aria-expanded", "false");
      menu.setAttribute("aria-label", "Open navigation");
    }
  });
  const sections = [...document.querySelectorAll("#home,main>.page-section")];
  const navLinks = [...navigation.querySelectorAll('a[href^="#"]')];
  let scheduled = false;
  const updateActive = () => {
    let activeId = "home";
    for (const section of sections) if (section.getBoundingClientRect().top <= 150) activeId = section.id;
    navLinks.forEach(link => {
      const active = link.getAttribute("href") === `#${activeId}`;
      link.classList.toggle("active", active);
      if (active) link.setAttribute("aria-current", "location"); else link.removeAttribute("aria-current");
    });
    scheduled = false;
  };
  window.addEventListener("scroll", () => { if (!scheduled) { scheduled = true; requestAnimationFrame(updateActive); } }, {passive:true});
  updateActive();
})();
