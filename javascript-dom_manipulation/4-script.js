document.getElementById('add_item').onclick = () => {
  const newItem = document.createElement("li");
  newItem.textContent = "Item";
  const myList = document.querySelector(".my_list");
  myList.appendChild(newItem);
}
