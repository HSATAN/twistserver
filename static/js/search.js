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
                    desc = (item['abstract']['metadata']==null)?item['abstract']['title']:item['abstract']['metadata']
                    var reg = new RegExp(word, "g")
                    desc = desc.replace(reg,"<span style=\"color:red\">"+word +"</span>")
                    var tempdata = "<div class='item'>" + "<a  href=" + item['url'] +
                        ' target="_blank">' + item['url'] + "</a><br>" + "" + desc + "</div>"

                    $("#result").append(tempdata);

                })



            }
        }
    };
    xmlhttp.open("GET","/search?word=" + word,true);
    xmlhttp.send(null);
}


