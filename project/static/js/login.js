$(function(){
	var error_name = false;
	var error_pwd = false;

	function check_user_name(){
		var len = $('#username').val().length;
		if(len<3||len>20)
		{
			$('#username').next().html('请输入3-20个字符的用户名');
			$('#username').next().show();
			error_name = false;
		}
		else
		{
            $.ajax({
                type:'get',
                url:'/user/login_pwd/?uname='+$('#username').val()+'&upwd='+$('#pwd').val(),
                async:false,//false代表等待ajax执行完毕
                success:function (data){
                    if(data.count>0){
                        error_name = true;
                        error_pwd = true;
                    }
                    else{
                        $('#pwd').next().html('用户名或密码错误').show();
                        error_name = false;
			            error_pwd = false;
                    }
                }
            });
		}
	}


	$('#form_login').submit(function() {
		check_user_name();

	    if(error_name == true && error_pwd == true)
            {
                return true;
            }
            else
            {
                return false;
            }
		});


})
