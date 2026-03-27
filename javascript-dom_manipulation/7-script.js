document.addEventListener("DOMContentLoaded", () => {
  const movieList = document.getElementById("list_movies");
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      data.results.forEach((movie) => {
        const listItem = document.createElement("li");
        listItem.textContent = movie.title;
        movieList.appendChild(listItem);
      });
    })
    .catch((error) => {
      console.error("Error fetching the movies:", error);
    });
});
