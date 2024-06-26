import urllib.request as uw

imrUrl = "https://th.bing.com/th/id/OIP.SekACUba6VopDOvCQuvV6QHaGl?rs=1&pid=ImgDetMain"
savePath = ".test.jpg"
htmlUrl = "http://google.com"
savePath2 = "index.html"
uw.urlretrieve(imrUrl, savePath)
uw.urlretrieve(htmlUrl,savePath2)
print("다운로드 완료")