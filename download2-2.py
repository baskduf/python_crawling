import urllib.request as uw

imrUrl = "https://th.bing.com/th/id/OIP.SekACUba6VopDOvCQuvV6QHaGl?rs=1&pid=ImgDetMain"
savePath = "test.jpg"
htmlUrl = "http://google.com"
savePath2 = "index.html"

f = uw.urlopen(imrUrl).read()
r2 = uw.urlopen(htmlUrl).read()
saveFile1 = open(savePath, "wb") #w - 쓰기 r - 읽기 a - add, b- binary
saveFile1.write(f)
saveFile1.close()

with open(savePath, "wb") as saveFile2: #with python2.7 , with를 벗어나면 close를 자동으로 호출
    saveFile2.write(r2)

print("다운로드 완료")

#urlopen = 필요로 하는 파일을 파싱하기 위함 (변수할당->파싱->open) 쉽다. 중간에 파싱하기는
#urlretrieve = direct로 download함 (저장->open(r)->변수 할당 ->파싱->다시저장)