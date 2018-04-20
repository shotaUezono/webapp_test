var url = window.location.search

var val = getUrlVars();

/**
* URL analyze and Return query
* @returns {Array} query string
*/

function getUrlVars(){
    var vars = [];
    var max = 0;
    var hash = "";
    var array = "";

    hash = url.slice(1).split('&');
    max = hash.length;
    for(var i = 0; i < max; i++){
        array = hash[i].split("=");
        vars[array[0]] = array[1];
    }
    return vars;
}

var user = val["user"];
f = document.getElementById("pch");
f2 = document.getElementById("qGo");
document.getElementById("username").innerHTML = user;

//add hidden + submit form
var i1 = document.createElement("input");
i1.setAttribute("type", "hidden");
i1.setAttribute("name", "user");
i1.setAttribute("value", user);
f.appendChild(i1);

var i2 = document.createElement("input");
i2.setAttribute("type", "submit");
i2.setAttribute("id", "chbtn");
i2.setAttribute("value", "profile change");
f.appendChild(i2);

var i3 = document.createElement("input");
i3.setAttribute("type", "hidden");
i3.setAttribute("name", "userG");
i3.setAttribute("value", user);
f2.appendChild(i3);

var p = document.createElement("p");
p.innerHTML = "IT Clerical worlers quiz, Let's try!";
f2.appendChild(p);

var i4 = document.createElement("input");
i4.setAttribute("type", "submit");
i4.setAttribute("id", "chbtn");
i4.setAttribute("value", "Go Question!");
f2.appendChild(i4);

//add p tag infomation
var family = val["familyname"];
document.getElementById("familyname").innerHTML = family;

var first = val["firstname"];
document.getElementById("firstname").innerHTML = first;

//cookie config
var a = 'user='+user+'; path=/; max-age=300';
document.cookie=a;

//session set
window.sessionStorage.setItem([user],[user])
console.log(window.sessionStorage.getItem([user]))

console.log(document.getElementsByName("user"));