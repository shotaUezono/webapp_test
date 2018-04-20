#!/usr/bin/env python
# coding: utf-8

import sqlite3
from old.simpletemplate import SimpleTemplate
from os import path
from httphandler import Request, Response
import cgitb; cgitb.enable()

con=sqlite3.connect('./bookmark.dat')
cur=con.cursor()
try:
    cur.execute("""CREATE TABLE bookmark (
                   title text, url text);""")
except:
    pass

req=Request()
f=req.form
value_dic={'message':'', 'title':'', 'url':'','bookmarks':''}

if 'post' in req.form:
    if f.getvalue('title', '') and f.getvalue('url', ''):
        cur.execute("""INSERT INTO bookmark(title, url) VALUES(?, ?)""",
                    (f.getvalue('title', ''), f.getvalue('url', '')))
        con.commit()
    else:
        value_dic['message']='タイトルとURLは必須項目です'
        value_dic['title']=f.getvalue('title', '')
        value_dic['url']=f.getvalue('url', '')

cur.execute("SELECT title, url FROM bookmark")               # (1)
value_dic['bookmarks']=tuple(cur.fetchall())

res=Response()
p=path.join(path.dirname(__file__), 'stbookmarkform.html')   # (2)
t=SimpleTemplate(file_path=p)
body=t.render(value_dic)
res.set_body(body)
print(str(res))