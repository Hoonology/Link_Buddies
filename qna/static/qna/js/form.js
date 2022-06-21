if(document.querySelector("#loginrequired")){
    alert("로그인이 필요한 기능입니다.")
    window.location.href = '/accounts/login';
}

document.querySelector("#question").addEventListener("keypress",function(e){
    let account_info = document.querySelector(".right a").innerHTML
    if (account_info == "login"){
        document.querySelector("#question").value=null
        alert("로그인이 필요한 기능입니다.")
        window.location.href = 'accounts/login';
        return false
    }
    else{
     document.querySelector("#textlen").innerHTML=Number(document.querySelector("#question").value.length)+1;    }
    },false)

document.querySelector(".go_list").addEventListener("click",function(){
    window.location.href = '/qna'
})