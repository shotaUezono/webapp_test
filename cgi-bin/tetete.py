#! /usr/bin/env python
#  coding: utf-8
from httphandler import Request,Response,get_htmltemplate_mypage
import cgitb
cgitb.enable()


html_body="""<!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
        <link rel="stylesheet" type="text/css" href="../css-dir/mypage.css">
        <title>itc introduction,for IT Clerical workers</title>
    </head>
    <body>
    %s
    </body>
    </html>
"""

req = Request()
a = req.form
res=Response()
body=(html_body%a)
res.set_body(body)

print(str(res))