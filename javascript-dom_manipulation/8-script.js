document.addEventListener("DOMContentLoaded", async () => {
  async function getHello() {
    const reponse = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
    const data = await reponse.json();
    console.log(data)
    return data;
  }

  getHello().then(hello => {
    const list = document.getElementById("hello");
    list.textContent = hello.hello;
  });
});
