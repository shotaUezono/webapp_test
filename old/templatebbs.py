#! /usr/bin/env python
# coding: utf-8
import sqlite3
from string import Template
from os import path
from httphandler import Request, Response, get_htmltemplate
import cgitb
cgitb.enable()
con=sqlite3.connect("./bookmark.dat")
cur=con.cursor()
try:
    cur.execute("""CREATE TABLE bookmark (title text, url text);""")
except:
    pass

req=Request()
f=req.form
value_dic={'message':'', 'title':'', 'url':'', 'bookmarks':''}

if 'post' in req.form:
    if (not f.getvalue('title', '')) or (not f.getvalue('url', '')):
        value_dic['message']='You must input title and url.'
        value_dic['title']=f.getvalue('title', '', 'utf-8', 'ignore')
        value_dic['url']=f.getvalue('url', '')
    else:
        cur.execute("""INSERT INTO bookmark(title, url) VALUES(?, ?)""",
                    (f.getvalue('title', ''), f.getvalue('url', '')))
        con.commit()

#after add
listbody=''
cur.execute("SELECT title, url FROM bookmark")
for item in cur.fetchall():
    listbody+="""<dt>%s</dt><dd>%s</dd>¥n"""%(item)
listbody="""<ul>¥n%s</ul>"""%listbody
value_dic['bookmarks']=listbody
#

res=Response()
f=open(path.join(path.dirname(__file__), 'bookmarkform.html'))
t=Template(f.read())

body=t.substitute(value_dic)
res.set_body(body)
print(str(res))
