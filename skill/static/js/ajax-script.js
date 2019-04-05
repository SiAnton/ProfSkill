
window.onload = function () {
    $("#form").submit(function (e) {
        e.preventDefault();

        var data = $("#category").val();
        console.log(data)

        $.ajax({
            url: '/service/',
            type: 'GET',
            data: $("#category").val(),
            cache: false,
            success: function () {
                console.log("yes");
            },
        });
    });
}
