async function getName() {
  const reponse = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
  const name = await reponse.json();
  return name;
}

getName().then(name => {
  document.getElementById("character").textContent = name.name;
});
