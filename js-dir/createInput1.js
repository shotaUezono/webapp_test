
var r = document.cookie.split(";");
console.log(r);
cookieObj={}
r.forEach(function(value){
    var content = value.trim().split('=');
    cookieObj[content[0]] = content[1];
})
console.log(cookieObj)

var user = cookieObj["user"];
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
i2.setAttribute("class", "chbtn");
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
i4.setAttribute("class", "quesG");
i4.setAttribute("value", "Go Question!");
f2.appendChild(i4);

//add p tag infomation
var family = cookieObj["familyname"];
document.getElementById("familyname").innerHTML = family;

var first = cookieObj["firstname"];
document.getElementById("firstname").innerHTML = first;


//session set
window.sessionStorage.setItem([user],[user])
console.log(window.sessionStorage.getItem([user]))

console.log(document.getElementsByName("user"));