#! /usr/bin/env python
#  coding: utf-8
from httphandler import  Request, Response, get_htmltemplate
from db_exe import db_exe
import cgitb
cgitb.enable()
html_body = ""
html_ = """
    <html>
    <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="../css-dir/csstest.css">
    </head>
    <body onLoad=setTimeout("location.href='../html-dir/mypage.html?user=%s'",3000)>
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
    db.account_data_insert(username, password)
    if db.account_create_check(username):
        content = "This username is egistrating to database already."
        html_body = create_fail_body
    else:
        content = "Create account successfull."
        html_body = (html_ % (username, content))
else:
    content = "Create account Fail."
    html_body = create_fail_body

res=Response()
body=html_body
res.set_body(get_htmltemplate()%body)
print(str(res))
print(req.form["username"].value)
