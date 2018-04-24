#! /usr/bin/env python
#  coding: utf-8
from httphandler import  Request, Response, jump_body, get_htmltemplate_mypage
from db_exe import db_exe
import os
import cookie_analyze
from http.cookies import SimpleCookie
import cgitb
cgitb.enable()


html_body = """
<body onLoad=setTimeout("location.href='../cgi-bin/test_mypage.py'",3000)>
<h1>profile update successfull</h1>
<p>jump to mypage 3sec ago</p>
</body>
"""

fail_body = """
<body onLoad=setTimeout("location.href='../cgi-bin/test_mypage.py'",3000)>
<h1>profile update fail</h1>
<p>jump to mypage 3sec ago</p>
</body>
"""

dont_body = """
<body onLoad=setTimeout("location.href='../cgi-bin/test_mypage.py'",3000)>
<h1>profile don't update</h1>
<p>jump to mypage 3sec ago</p>
</body>
"""


cook = SimpleCookie()
cook.load(os.environ.get("HTTP_COOKIE", ""))
req = Request()
f = req.form
update_date = None
family=None
first=None

cookieObj={}

cookieObj=cookie_analyze.analyze(cook)

cook["user"]["path"]="/"

if ('family' in req.form) or ('first' in req.form):
    family = f.getvalue("family", "")
    first = f.getvalue("first", "")
    if family:
        update_date = 'familyname="'+family+'", '
    if first:
        update_date += 'firstname="'+first+'" '



db=db_exe()
if update_date is not None:
    db.account_info_update(update_date,cookieObj['user'])
    if family is not None:
        cook["family"] = family
        cook["family"]["path"]="/"
    if first is not None:
        cook["first"]= first
        cook["first"]["path"] = "/"

else:
    html_body=dont_body


res=Response()
body=html_body
res.set_body(get_htmltemplate_mypage()%body)
print(cook.output())
print(str(res))

