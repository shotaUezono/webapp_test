import cgi
import os
import time
class Request(object):
    """
    HTTPリクエストをハンドリングするクラス
    CGI側でインスタンスを生成し利用する
    クエリデータや環境変数へのアクセス、主要ヘッダへの
    アクセス用メソッドを提供
    """

    def __init__(self, environ=os.environ):
        """
        インスタンスの初期化メソッド
        クエリ、環境変数をアトリビュートとして保存する。
        """
        self.form = cgi.FieldStorage()
        self.environ=environ

class Response(object):
    """
    HTTPレスポンスをハンドリングするクラス
    レスポンスを送る前にインスタンスを生成し利用
    レスポンスやヘッダの内容を保持、
    ヘッダを含めたレスポンスの送信を行う.
    """

    def __init__(self, charset="utf-8"):
        """
        インスタンスの初期化メソッド
        ヘッダ用の辞書,本文用の文字列などを初期化する
        """
        
        self.headers = {'content-type':'text/html;charset=%s' % charset}
        self.body=""
        self.status=200
        self.status_message=''

    def set_header(self, name, value):
        """
        レスポンスのヘッダを設定する
        """
        self.headers[name]=value

    def get_header(self, name):
        """
        設定済みのレスポンス用ヘッダを返す
        """
        return self.headers.get(name, None)

    def set_body(self, bodystr):
        """
        レスポンスとして出力する本文の文字列を返す
        """
        self.body=bodystr

    def make_output(self, timestamp=None):
        """
        ヘッダと本文を含めたレスポンス文字列を作る
        """
        if timestamp is None:
            timestamp = time.time()
            year, month, day, hh, mm, ss, wd, y, z = time.gmtime(timestamp)
            dtstr ="%s, %02d %3s %4d %02d:%02d:%02d GMT" % ( _weekdayname[wd], day, _monthname[month], year, hh, mm, ss)
            self.set_header("Last-Modified", dtstr)
            headers="\n".join(["%s: %s" % (k, v) for k,v in self.headers.items()])
        return headers+"\n\n"+self.body

    def __str__(self):
        """
        リクエストを文字列に変換する
        """

        return self.make_output()

def get_htmltemplate():
    """
    レスポンスとして返すHTMLのうちの定形部分のreturnメソッド
    """

    html_body = """
    <html>
    <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="../css-dir/csstest.css">
    </head>
    <body>
    %s
    </body>
    </html>
    """

    return html_body

def get_htmltemplate_mypage():
    html = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
        <link rel="stylesheet" type="text/css" href="../css-dir/mypage.css">
        <title>itc introduction,for IT Clerical workers</title>
    </head>
    %s
    </html>
    """
    return html

def jump_body():
    html_body = """
                <body onLoad=setTimeout("location.href='%s'",3000)>
                <h1>login successfull</h1>
                <p>jump to mypage 3sec ago</p>
                </body>"""
    return html_body


_weekdayname =["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
_monthname = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "July",
              "Aug", "Sep", "Oct", "Nov", "Dec"]


