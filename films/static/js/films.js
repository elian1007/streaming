const API_URL = 'http://127.0.0.1:8000/api/mediarandom/';


const HTMLResponse = document.querySelector("#app")
const tpl = document.createDocumentFragment()

fetch(`${API_URL}`)
.then((response)=> response.json())
.then((users)=>{


      const tpl= users.map((user) =>`<h3>  <p> Nombre: ${user.name}</p> <p> Genero: ${user.genre}</p> <p> Tipo: ${user.type}</p> <p> visualizaciones: ${user.views}</p> </h3>`)
    HTMLResponse.innerHTML = `<p>${tpl}</p>`
}) 


let refresh = document.getElementById('refresh');
refresh.addEventListener('click', _ => {
            location.reload();
})