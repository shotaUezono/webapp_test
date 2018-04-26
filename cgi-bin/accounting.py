#! /usr/bin/env python
#  coding: utf-8
from httphandler import  Request, Response, get_htmltemplate
import http.cookies as cook
import cgitb
cgitb.enable()

login_form_body="""
<h1>itc introduction,for IT Clerical workers</h1>
    <form action="/cgi-bin/inChallenge.py" method="POST">
        <p>Username:
        <input type="text" name="username" required>
        *
        </p>
        <p>Password:
        <input type="password" name="password" minlength="8" required>
        *
        </p>
        <input type="submit" name="submit">
    </form>
"""

create_account_body="""
<h1>itc introduction,for IT Clerical workers</h1>
    <div style="border-style:solid; border-witdh: 2px;">
    <p a>Please input infomation of your new account.</p>
    <p>username is any string.</p>
    <p>You need to put more than 8 letters in the password and again password fields.</p>
    <p>Then you can press submit button.</p>
    <p>[[ ATTENTION ]]</p>
    <p>Here, you can use half-width alphanumeric characters, symbols ("_", "-", "#", "@").</p>
    <p>Do not use double-byte characters.</p>
    </div>
    <form action="/cgi-bin/createAc.py" name="create" method="POST">
        <p>Please your username :<input type="text" name="username" required></p>
        <p>Please your password :<input type="password" name="firstpass" minlength="8" required onkeyup="stringadd()"></p>
	    <p>Input password again :<input type="password" name="secondpass" minlength="8" required onkeyup="stringadd2()"></p>
        <input type="submit" id="submit" disabled>
        <div id="attention">password is missmatch</div>
    </form>
<script src="../js-dir/tejs.js" async>  
</script>

"""

content=""
c = cook.SimpleCookie()
c.clear()
def login_form():
    global content
    content+= login_form_body

def create_account_form():
    global content
    content+= create_account_body

req=Request()

if "Yes" == req.form["bool"].value:
    login_form()
else:
    create_account_form()

res=Response()
body=content
res.set_body(get_htmltemplate()%body)

print(str(res))
