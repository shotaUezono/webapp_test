#! /usr/bin/env python
#  coding: utf-8
from httphandler import  Request, Response, get_htmltemplate
from db_exe import db_exe
import http.cookies as cookies
import cgitb
cgitb.enable()
cook = cookies.SimpleCookie()

html_body = """
    <html>
    <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="../css-dir/csstest.css">
    </head>
    %s
    </html>
    """

true_body="""
<body onLoad=setTimeout("location.href='test_mypage.py'",3000)>
<h1>login successfull</h1>
<p>jump to mypage 3sec ago</p>
</body>
"""

false_body="""
<body onLoad=setTimeout("location.href='../login.html'",3000)>
<h1>login Fail</h1>
<p>jump to login 3sec ago</p>
</body>
"""

req = Request()

db = db_exe()
db.account_table()
input_name = req.form["username"].value
input_pass = req.form["password"].value
content = ""
if db.account_check(input_name, input_pass):
    ac_info = db.account_get_check(input_name)
    familyname = str(ac_info[2])
    firstname = str(ac_info[3])
    age = str(ac_info[4])


    cook["user"] = input_name
    cook["user"]["path"] = "/"

    cook["family"] = familyname
    cook["family"]["path"] = "/"

    cook["first"] = firstname
    cook["first"]["path"] = "/"

    content=true_body

else:
    content = (html_body % false_body)

res=Response()
res.set_body(content)
print(cook.output())
print(str(res))


