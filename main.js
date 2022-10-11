
$(document).ready(function() {
    $("#render").click(() => {
        let settings = {
            "async": true,
            "crossDomain": true,
            "url": "http://127.0.0.1:5000/" + $("#biti_text").val(),
            "method": "GET",
            "headers": {
                "Content-Type": "application/json"
            },
            "processData": false,
            "data": "",
            "Access-Control-Allow-Origin": "*"
        };
        $("#main").attr("src", "https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif")
        $.ajax(settings).done(function (response) {
            $("#main").attr("src", response.url);
        });
    })
});
