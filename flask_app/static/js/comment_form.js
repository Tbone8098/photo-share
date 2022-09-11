var commentForm = document.querySelectorAll('.comment-form')

for (let form of commentForm) {
    form.addEventListener('submit', function (event) {
        event.preventDefault()
        console.log('running js for comments');
        let formContent = new FormData(form)

        fetch('/api/comment/create', {
            method: 'post',
            body: formContent
        })
            .then(resp => resp.json())
            .then(data => {
                console.log(data)
                if (data.status == 200) {
                    let commentSection = document.querySelector(`#comment-section-${data.photo.id}`)
                    let child = document.createElement('div')
                    child.innerHTML = `
                    <div class="border shadow p-5 rounded-lg">
                    <div class="flex justify-between font-bold">
                    <span>${data.user.fullname}</span>
                    <span>${data.comment.updated_at}</span>
                    </div>
                    <p>${data.comment.content}</p>
                    <div class="my-1 flex justify-end">
                    <a class="btn btn-danger" href="/comment/${data.comment.id}/delete">Delete</a>
                    </div>
                    </div>
                    `
                    commentSection.prepend(child)
                    form.reset()
                }
                else {
                    for (const key in data.errors) {
                        let errEl = document.querySelector(`.${key}_${data.photo_id}`)
                        errEl.textContent = data.errors[key]
                    }
                }
            })
            .catch(err => console.log(err))
    })
}

var deleteBtns = document.querySelectorAll('.comment-delete-btn')
for (let btn of deleteBtns) {
    btn.addEventListener('click', function(){
        id = this.getAttribute('comment-id')
        container = btn.parentElement.parentElement
        deletePost(id, container)
    })
}

function deletePost(id, container){
    fetch(`/api/comment/${id}/delete`)
    .then(resp => resp.json())
    .then(data => {
        console.log(data);
        container.remove()
    })
}

