$(document).ready(function () {
    var register = 0;
    $('#register_show').on('click',function () {
        if(register == 0) {
            register = 1;
            $('.login-box').css('transform', 'translate3d(0,-700px,0)');
            $('.register-box').css('transform', 'translate3d(0,0,0)');
            $('.register-button').html('Login');
        }else{
            register = 0;
            $('.login-box').css('transform', 'translate3d(0,0,0)');
            $('.register-box').css('transform', 'translate3d(0,900px,0)');
            $('.register-button').html('Register')
        }
    });
});