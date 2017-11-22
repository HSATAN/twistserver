url = ""

function load_document() {
    word = form.word.value
    var xmlhttp;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function () {
        if (xmlhttp.readyState==4)
        {
            if(xmlhttp.status==200)
            {
                $("#result").html("")
                data = JSON.parse(xmlhttp.responseText);
                $("#result").value = "";
                data.forEach(function (item,index,array) {

                    $("#result").append( "<a  class='item' href=" + item['url'] + ' target="_blank">' + item['url'] + "</a><br>");

                })



            }
        }
    };
    xmlhttp.open("GET","/search?word=" + word,true);
    xmlhttp.send(null);
}


