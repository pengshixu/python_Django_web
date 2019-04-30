$(function(){
    if( $('#username').text() != '未登录'){
        $('.login_info').css("display","block")
        $('.login_btn').css("display","none")
    }
})