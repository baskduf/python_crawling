import json
import urllib.request as req
from urllib.parse import urlencode

api = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

values = {
    'ctxCd' : '1012  '
}

print("before", values)
params = urlencode(values)
print("after", params)

url = api + "?" + params

print("요청 url", url)

urlopen = req.urlopen(url).read().decode('utf-8')
print(urlopen)