#! /usr/bin/env python
#  coding: utf-8
from httphandler import  Request, Response, get_htmltemplate
from db_exe import db_exe
import cgitb
cgitb.enable()

html_body = "<h1>question</h>"

req = Request()
res=Response()
body=html_body
res.set_body(get_htmltemplate()%body)
print(str(res))
