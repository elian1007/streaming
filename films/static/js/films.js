const API_URL = 'http://127.0.0.1:8000/api/films';


const HTMLResponse = document.querySelector("#app")
const tpl = document.createDocumentFragment()

fetch(`${API_URL}`)
.then((response)=> response.json())
.then((users)=>{


    const tpl= users.map((user) =>`<li>${user.name} ,${user.genre} ,${user.type}</li>`)
    HTMLResponse.innerHTML = `<u>${tpl}</u>`
})



  
  const state = {
    randomFav: null,
    favorites: API_URL
  }
  
  // Como Math.random genera un número decimal pues le aplico Math.floor para redondear al menor entero más cercano
  const random = () => Math.floor(Math.random() * state.favorites.length)
  
  function getRandomItem() {
    const index = random();
    
    if (state.randomFav === index) {
      return getRandomItem();
    }
    state.randomFav = index;
    return state.favorites[index];
  }
  
  console.log(getRandomItem())


