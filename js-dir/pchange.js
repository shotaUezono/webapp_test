
var r = document.cookie.split(";");
console.log(r);

cookieObj={}
r.forEach(function(value){
    var content = value.trim().split('=');
    cookieObj[content[0]] = content[1];
})

