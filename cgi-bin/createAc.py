#! /usr/bin/env python
#  coding: utf-8
from httphandler import  Request, Response, get_htmltemplate
from db_exe import db_exe
import http.cookies as cookies
import cgitb
cgitb.enable()
html_body = ""
html_ = """
    <html>
    <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="../css-dir/csstest.css">
    </head>
    <body onLoad=setTimeout("location.href='../cgi-bin/test_mypage.py'",3000)>
        <h1>%s</h1>
        <p>jump to mypage 3sec ago</p>
        
    </body>
    </html>
    """
create_fail_body="""
<html>
    <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="../css-dir/csstest.css">
    </head>
    <body onLoad=setTimeout("location.href='../login.html'",3000)>
        <h1>%s</h1>
        <p>jump to login 3sec ago</p>
    </body>
    </html>
"""


req = Request()
cook=cookies.SimpleCookie()
content=""
username = ""
password = ""
usernameTag = False
passwordTag = False


if req.form["username"].value:
    username = req.form["username"].value
    usernameTag = True
if req.form["firstpass"].value == req.form["secondpass"].value:
    password = req.form["firstpass"].value
    passwordTag = True

if usernameTag and passwordTag:

    db = db_exe()
    db.account_table()
    res = db.account_data_insert(username, password)
    if (res == "This account created already") or (res == "Account create fail"):
        content = res
        html_body = (create_fail_body % content)
    else:
        cook.clear()
        cook["user"] = username
        cook["user"]["path"] = "/"
        content = res
        html_body = (html_ % (content))
else:
    content = "Create account Fail."
    html_body = (create_fail_body % content)

res=Response()
body=html_body
res.set_body(get_htmltemplate()%body)
print(cook.output())
print(str(res))

