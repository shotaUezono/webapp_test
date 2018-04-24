
def analyze(cook):
    cookieObj={}
    cookieList = str(cook).split("Set-Cookie:")
    for c in cookieList:
        if c:
            s = c.split(";")[0]
            v = s.split("=")
            cookieObj[v[0].strip()] = v[1].strip()

    return cookieObj