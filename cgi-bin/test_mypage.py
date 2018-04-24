#! /usr/bin/env python
#  coding: utf-8
from httphandler import  Request, Response, jump_body, get_htmltemplate_mypage
from db_exe import db_exe
import os
from http.cookies import SimpleCookie
import cgitb
cgitb.enable()

html_="""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <link rel="stylesheet" type="text/css" href="../css-dir/mypage.css">
    <title>itc introduction,for IT Clerical workers</title>
</head>
<body>
    <div id="header" style="border-style:outset">
        <h1 style="font-size:40px">User page's</h1>
            <div class="welcome" style="padding: 5px 5px 5px 5px;">
                <p id="welcomeMsg">Welcome to ITC's Introduction Application.</p>
            </div>
    </div>
    <p></p>
    <div id="container">
        <div id="nav">
            <div class="profile" style="border-style:outset; border-color:yellow; padding:2px 2px 2px 2px;">
                familyname : <center><p id="familyname">%s</p></center>
                firstname : <center><p id="firstname">%s</p></center>
                username : <center><p id="username">%s</p></center>
            </div>

            <form id="pch" action="../cgi-bin/profile_change.py" method="POST" style="padding:5px 5px 2px 2px;">
            </form>
        </div>
        <div id="content">
            <form id="qGo" action="../cgi-bin/question_page.py" method="POST">
            </form>
        </div>
    </div>
    <script src="../js-dir/createInput.js">
    </script>
</body>
</html>
"""


cook = SimpleCookie()
cook.load(os.environ.get("HTTP_COOKIE", ""))
req = Request()
user=None
family=None
first=None
if "user" in cook.keys():
    user=str(cook.get("user")).split("=")[1]

if user is None:
    raise Exception("username is Bad")

db=db_exe()
info = db.account_get_check(user)

first=info[3]
family=info[2]


html=html_%(family,first,user)
res = Response()
res.set_body(html)
print(cook.output())
print(str(res))


