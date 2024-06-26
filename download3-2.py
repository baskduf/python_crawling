import json
import urllib.request as req
from urllib.parse import urlencode

api = "https://api.ipify.org"

values = {
    'format' : 'json'
}

print("before", values)
params = urlencode(values)
print("after", params)

url = api + "?" + params

print("요청 url", url)

urlopen = req.urlopen(url).read().decode('utf-8')
print(urlopen)