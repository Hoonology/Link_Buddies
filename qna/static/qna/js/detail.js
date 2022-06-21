document.querySelector(".go_list").addEventListener("click",function(){
    window.location.href = '/qna'
})

let del_btn = document.querySelector(".delete")
del_btn.addEventListener("click",function(){
    if (window.confirm("정말 삭제하시겠습니까?")){
        let id=del_btn.getAttribute("id")
        window.location.href = '/qna/delete/'+id
    }else{
    return false
    }
})

let mod_btn = document.querySelector(".modify")
mod_btn.addEventListener("click",function(){
    let id=mod_btn.getAttribute("id")
    window.location.href = '/qna/forms/'+id
})

