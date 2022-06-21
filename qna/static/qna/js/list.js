document.querySelector("#form").addEventListener('click',function(){
    let account_info = document.querySelector(".right a").innerHTML
    if (account_info == "login"){
    window.location.href = "/account/login";
    //url 수정
    alert("로그인이 필요한 기능입니다.")
    return false
    }
    else{
    window.location.href = '/qna/editor';
    //url 수정
    }
    }, false);