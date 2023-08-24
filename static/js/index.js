async function makeRequest(url, method = 'GET') {
    let headers = {};
    let response;
    console.log(method)
    if (method !== "GET") {
        headers = {
            'Authorization': `Token ${getCookie("token")}`,
            "Content-Type": "application/json",
        }
    }
    console.log(headers)
    if (["POST", "PATCH", "PUT", "DELETE"].includes(method)) {
        response = await fetch(url, {
            "method": method,
            'Authorization': `Token ${getCookie("token")}`,
            "headers": headers
        });
    } else {
        response = await fetch(url, {
            "method": method,
            "headers": headers,
        });
    }

    if (response.ok) {
        return await response.json();
    } else {
        console.log(response.statusText)
        let error = new Error(response.statusText);
        throw error;
    }
}

async function onClick(event) {
    event.preventDefault();
    let target = event.target;
    let target_parent = target.parentElement
    let url = target_parent.href ;
    let publicationId = target_parent.dataset.publicationId

    let method = "POST"
    if (target.classList.value.includes("fa-solid")) {
        method = "DELETE"
    }
    let response = await makeRequest(url, method);
    if (target.classList.value.includes("fa-regular")){
        target.classList = "text-white fa-solid fa-heart fa-2xl";
        target_parent.href = `/api/v1/publications/${publicationId}/unlikes/`
    } else {
        target.classList = "text-white fa-regular fa-heart fa-2xl";
        target_parent.href = `/api/v1/publications/${publicationId}/likes/`
    }
    console.log(response)
    let spanCount = document.getElementById(`publication_likes_count_${publicationId}`)
    spanCount.innerText = response.likes;
    console.log(response)
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function onLoad() {
    let likes = document.getElementsByClassName("likes")
    for (let like of likes) {
        like.addEventListener("click", onClick)
    }
}

window.addEventListener('load', onLoad)