$(document).ready(function () {
    var register = 0;
    $('#register_show').on('click', function () {
        if (register == 0) {
            register = 1;
            $('.login-box').css('transform', 'translate3d(0,-700px,0)');
            $('.register-box').css('transform', 'translate3d(0,0,0)');
            $('.register-button').html('Login');
        } else {
            register = 0;
            $('.login-box').css('transform', 'translate3d(0,0,0)');
            $('.register-box').css('transform', 'translate3d(0,900px,0)');
            $('.register-button').html('Register')
        }
    });

    $(document).on('submit', '#login-form', function (e) {
        var data = {};
        e.preventDefault();
        var url = $(this).attr('action');
        var method = $(this).attr('method');
        var username = $("[name = username]").val();
        var password = $("[name = password]").val();
        if (username.length < 1) {
            console.log("Username field can't be empty");
        } else if (password.length < 1) {
            console.log("Password field can't be empty");
        } else { /* Username and Password field is filled */
            var csrf = data['csrfmiddlewaretoken'] = new Token().getCookie('csrftoken');
            data['username'] = username;
            data['password'] = password;
            console.log(data);
            $.ajax({
                url: url,
                type: method,
                data: data,
                success: function (res) {
                    if (res.status = 200) {
                        console.log(res.response);
                        location.href = res.success_url;
                    }
                },
                error: function (res) {
                    console.log(res.response);
                }
            });
        }
    });

    $(document).on('submit', '#register-form', function (e) {
        e.preventDefault();
        var data = {};
        var url = $(this).attr('action');
        var method = $(this).attr('method');
        var username = data['username'] = $("[name = username-register]").val();
        var password = data['password'] = $("[name = password-register]").val();
        var first_name = data['first_name'] = $("[name = first_name]").val();
        var last_name = data['last_name'] = $("[name = last_name]").val();
        var email = data['email'] = $("[name = email]").val();
        var csrf = data['csrfmiddlewaretoken'] = new Token().getCookie('csrftoken');
        console.log(data);
        $.ajax({
            url: url,
            type: method,
            data: data,
            success: function (res) {
                if (res.success == 'true') {
                    register = 0;
                    $('.login-box').css('transform', 'translate3d(0,0,0)');
                    $('.register-box').css('transform', 'translate3d(0,900px,0)');
                    $('.register-button').html('Register');
                    console.log("Successfuly Registered");
                    $('#username').val(username);
                    $('#password').val(password);
                }
            },
            error: function (res) {
                console.log(res);
            }
        });
    });
});