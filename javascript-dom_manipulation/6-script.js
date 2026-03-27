document.addEventListener("DOMContentLoaded", () => {
  const characterDiv = document.getElementById("character");
  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      characterDiv.textContent = data.name;
    })
    .catch((error) => {
      console.error("Error fetching the character:", error);
    });
});
