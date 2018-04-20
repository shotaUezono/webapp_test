    var first = "";
    var second = "";

    function stringadd(){
        first = document.create.firstpass.value;
    }
    function stringadd2(){
        second = document.create.secondpass.value;
    }
    var check = function(){
        if((first.length >= 8 ) && (second.length >= 8)){
            document.getElementById("submit").disabled = false;
            if(first == second){
                document.getElementById("attention").innerHTML= "password is ok!!!!!!!";
            }else{
                document.getElementById("attention").innerHTML= "password is missmatch";
            }
        }else{
             document.getElementById("submit").disabled = true;
        }

        setTimeout(check, 100);
    }

    check();
