$(document).ready(function () {
    var file;
    $('.upload').change(function (e) {
        file = e.target.files[0];
        //console.log(file)
    });
    $(document).on('submit', '#publish-post-form', function (e) {
        e.preventDefault();
        var title = $("[name = title]").val();
        var body = $("[name = body]").val();
        var method = $(this).attr('method');
        var url = $(this).attr('action');
        if (file == undefined) {
            console.log('A file must be uploaded')
        } else {
            console.log(file);
            var formData = new FormData($(this)[0]);
            formData.append('csrfmiddlewaretoken',new Token().getCookie('csrftoken'));
            formData.append('post_hero_pic',file);
            $.ajax({
                url: url,
                type: method,
                enctype: 'multipart/form-data',
                data: formData,
                success: function (res) {
                    console.log(res);
                },
                error: function (res) {
                    console.log(res);
                },
                cache: false,
                contentType: false,
                processData: false
            });
        }
    });
});