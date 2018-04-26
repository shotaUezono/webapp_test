#! /usr/bin/env python
#  coding: utf-8
from httphandler import  Request, Response, get_htmltemplate_mypage
from db_exe import db_exe
import http.cookies as cookies
import cgitb
cgitb.enable()
cook = cookies.SimpleCookie()

http_body="""
<body>
</body>
"""