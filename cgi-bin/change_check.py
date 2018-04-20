#! /usr/bin/env python
#  coding: utf-8
from httphandler import  Request, Response, jump_body, get_htmltemplate_mypage
from db_exe import db_exe
import cgitb
cgitb.enable()


html_body = """
"""

ignore_body=jump_body%"../mypage.html"
req = Request()
f = req.form
update_date = ""
if 'Post' in req.form:
    family = f.getvalue("familyname", "")
    first = f.getvalue("firstname", "")
    if family:
        update_date = "familyname="+family+" "
    if first:
        update_date += "firstname="+first+" "


db=db_exe()
db.account_info_update()

res=Response()
body=html_body
res.set_body(get_htmltemplate_mypage()%body)
print(str(res))
print(req.form)
