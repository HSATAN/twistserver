function load_document() {
    alert("--------------------------------")
    var xmlhttp;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function () {
        if (xmlhttp.readyState==4)
        {
            if(xmlhttp.status==200)
            {
                alert("加载完成")
                        document.getElementById("result").innerText="ceshi"

            }
        }
    };
    xmlhttp.open("GET","/search?word=huagnkaijie",false);
    xmlhttp.send(null);
}
