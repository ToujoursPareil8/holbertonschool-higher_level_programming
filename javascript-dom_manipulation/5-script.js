document.addEventListener("DOMContentLoaded", () => {
  const updateHeaderButton = document.getElementById("update_header");
  const headerElement = document.querySelector("header");

  updateHeaderButton.addEventListener("click", () => {
    headerElement.textContent = "New Header!!!";
  });
});
