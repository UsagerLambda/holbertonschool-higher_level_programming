async function getFilms() {
  const reponse = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
  const data = await reponse.json();
  return data.results;
}

getFilms().then(films => {
  const list = document.getElementById("list_movies");
  films.forEach(film => {
      const item = document.createElement('li');
      item.textContent = film.title;
      list.appendChild(item);
  });
});

