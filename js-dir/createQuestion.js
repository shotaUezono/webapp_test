    var count = 0;
    var idcount = 4;

    var qcon = function(){
        if(!count){
            document.getElementById("content").innerHTML="";
            count++;
        }
    }

    var addBox =function(){
        idcount++;
        var findDiv1 = null
        var hoge = document.getElementById("selectItem");
        console.log(hoge)

        var id = "q"+String(idcount);
        var ind = String(idcount);

        var i2 =document.createElement("p")
        i2.setAttribute("id", ind)
        i2.innerHTML = ('<label for="'+ind+'">'+ind+',</label><textarea id='+id+' rows="1" cols="40"></textarea>');
        hoge.appendChild(i2);

    }
    var delBox =function(){
        var f = document.getElementById("selectItem")

        f.removeChild(document.getElementById(String(idcount)));
        idcount--;
    }