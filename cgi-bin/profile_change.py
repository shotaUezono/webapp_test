#! /usr/bin/env python
#  coding: utf-8
from httphandler import  Request, Response, get_htmltemplate_mypage
from db_exe import db_exe
import cgitb
cgitb.enable()

html_body = """
<body>
<h1>profile change page</h1>
<p>What do you change infomation?</p>
<form action="change_check.py" method="POST">
    <p></p>
    <p>after familyname : <input id="family" type="text"></p>
    <p>after firstname : <input id="first" type="text"></p>
    <input id="username" type="hidden" value="%s">
    <input type="submit" name="submit" value="exe change">
</form>
<script src="../js-dir/pchange.js">
</script>
</body>
"""

html_bodytest = """
<body>
<h1>profile change page</h1>
<p>What do you change infomation?</p>
<form action="change_check.py" method="POST">
    <p></p>
    <p>after familyname : <input name="family" type="text"></p>
    <p>after firstname : <input name="first" type="text"></p>
    <input type="submit" name="submit" value="exe change">
</form>

</body>
"""

req = Request()

res=Response()
body=html_bodytest

res.set_body(get_htmltemplate_mypage()%body)
print(str(res))
