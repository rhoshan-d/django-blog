// document.addEventListener('DOMContentLoaded', function() {
//     document.querySelectorAll('.like-btn').forEach(button => {
//         button.addEventListener('click', function() {
//             const projectSlug = this.dataset.project
//             fetch(`/vehicles-projects/${projectSlug}/like/`, {
//                 method: 'POST',
//                 headers: {
//                     'X-CSRFToken': getCookie('csrftoken')
//                 }
//             })
//             .then(response => response.json())
//             .then(data => {
//                 this.classList.toggle('liked', data.liked);
//                 this.querySelector('.likes-count').textContent = data.likes_count
//             })
//             .catch(error => console.error('Error:', error))
//         })
//     })
// })

function getCookie(name) {
    let value = `; ${document.cookie}`
    let parts = value.split(`; ${name}=`)
    if (parts.length === 2) return parts.pop().split(';').shift()
}