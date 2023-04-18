const btnDarkMode = document.getElementById("btn-dark-mode");
const btnLightMode = document.getElementById("btn-light-mode");

btnDarkMode.addEventListener("click", function() {
  document.body.classList.add("dark-mode");
});

btnLightMode.addEventListener("click", function() {
  document.body.classList.remove("dark-mode");
});