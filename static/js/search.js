function load_document() {
    alert("-----------")
    var flag = false
    $(document).ready(function () {
        $("#su").click(function () {
            htmlobj = $.ajax({url: "/search",
                async: false,
            }).done(function () {
                flag = false
            });
        });
    });
    return flag;
}