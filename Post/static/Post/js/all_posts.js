$(document).ready(function () {
    $.get('/post/api', function (data, status) {
        console.log(data);
    });
});