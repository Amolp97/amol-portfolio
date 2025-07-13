// Typing effect
const text = "Hi, I'm Amol Patil";
let index = 0;
function type() {
  if (index < text.length) {
    document.getElementById("typed-text").innerHTML += text.charAt(index);
    index++;
    setTimeout(type, 100);
  }
}
type();

// Scroll reveal
const sections = document.querySelectorAll(".reveal");
function revealOnScroll() {
  const windowHeight = window.innerHeight;
  sections.forEach((section) => {
    const sectionTop = section.getBoundingClientRect().top;
    if (sectionTop < windowHeight - 50) {
      section.classList.add("visible");
    }
  });
}
window.addEventListener("scroll", revealOnScroll);
window.addEventListener("load", revealOnScroll);

// Scroll to top
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// Dark mode toggle
document.getElementById("theme-toggle").addEventListener("change", () => {
  document.body.classList.toggle("dark-mode");
});

// Load projects from API
async function loadProjects() {
  const response = await fetch("/api/projects");
  const projects = await response.json();
  const container = document.getElementById("project-container");

  projects.forEach(proj => {
    const card = document.createElement("div");
    card.className = "project-card";
    card.innerHTML = `
      <h3>${proj.title}</h3>
      <p>${proj.description}</p>
      <a href="${proj.link}" target="_blank" class="btn-neon">View Project</a>
    `;
    container.appendChild(card);
  });
}
loadProjects();
