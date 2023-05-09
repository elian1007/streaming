const API_URL = 'http://127.0.0.1:8000/api/mediarandom/';

function getMediaTemplate(media) {
    tempstr = `<h3>  <p> Nombre: ${media.name}</p> <p> Genero: ${media.genre}</p> <p> Tipo: ${media.type}</p> <p> visualizaciones: ${media.views}</p> <p>promedio: ${media.average}</p> <button onclick="markAsViewed('${media.id}')">Vista</button> </h3>`
    return tempstr
}
const HTMLResponse = document.querySelector("#app")
const tpl = document.createDocumentFragment()

fetch(`${API_URL}`)
    .then((response) => response.json())
    .then((users) => {
        const tpl = users.map((media) => getMediaTemplate(media))
        HTMLResponse.innerHTML = `<p>${tpl}</p>`
    })

let refresh = document.getElementById('refresh');
refresh.addEventListener('click', _ => {
    location.reload();
})


const MEDIA_URL = 'http://127.0.0.1:8000/api/mediaorder?';
const HTMLResponse2 = document.querySelector("#app2")
const select = document.querySelector("#select")
const tpl2 = document.createDocumentFragment()

showMedias()

function eventSelect() {
    showMedias(select.value)
}

function showMedias(orderingField) {
    fetch(`${MEDIA_URL}` + new URLSearchParams({
            ordering: orderingField,
        }))
        .then((response) => response.json())
        .then((users) => {
            const tpl = users.map((media) => getMediaTemplate(media))
            HTMLResponse2.innerHTML = `<p>${tpl}</p>`
        })
}

const FILTER_URL = 'http://127.0.0.1:8000/api/mediafilter?';
const HTMLResponseFilter = document.querySelector("#appFilter")
const inputName = document.querySelector("#name")
const inputGenre = document.querySelector("#genre")
const inputRate = document.querySelector("#rate")

const buttonFiltre = document.querySelector("#buttonFilter")
const tplFilter = document.createDocumentFragment()

showMediasFilter("", "", "")

function eventFilter() {
    showMediasFilter(inputName.value, inputGenre.value, inputRate.value)
}

function showMediasFilter(name, genre, type) {
    fetch(`${FILTER_URL}` + new URLSearchParams({
            name: name,
            genre: genre,
            type: type
        }))
        .then((response) => response.json())
        .then((users) => {
            const tpl = users.map((media) => getMediaTemplate(media))
            HTMLResponseFilter.innerHTML = `<p>${tpl}</p>`
        })
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csfr = document.getElementsByName("csrfmiddlewaretoken");
async function markAsViewed(mediaIdSelected) {
    console.log(mediaIdSelected)

    // const params = new URLSearchParams();
    // params.append('mediaId', mediaIdSelected);

    // const response = await fetch('http://127.0.0.1:8000/api/mediaview/', {
    //     method: 'post',
    //     body: params,
    //     credentials: 'same-origin',
    //     headers: {
    //         "X-CSRFToken": csfr.name
    //     }
    // });
    // const data = await response.json();
    const params = new URLSearchParams();
    params.append('mediaId', mediaIdSelected);
    // You have to download 3rd Cookies library
    // https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
    let csrftoken = getCookie('csrftoken');
    let response = fetch("http://127.0.0.1:8000/api/mediaview/", {
        method: 'POST',
        body: params,
        headers: { "X-CSRFToken": csrftoken },
    })

    console.log(response);

}