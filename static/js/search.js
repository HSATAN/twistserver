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
                data = JSON.parse(xmlhttp.responseText);
                data.forEach(function (item,index,array) {

                    $("#result").append( "<a href=" + item['url'] + ' target="_blank">' + item['url'] + "</a><br>");

                })



            }
        }
    };
    xmlhttp.open("GET","/search?word=" + word,false);
    xmlhttp.send(null);
}


