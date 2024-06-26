import urllib.request as dw

bannerUrl = "https://ssl.pstatic.net/melona/libs/1501/1501567/ed4cace02c73430794ac_20240523134351650.jpg"
savePath = "homework-1/banner.jpg"
savePath2 = "homework-1/advertise.jpg"
advertiseUrl = "https://naverpa-phinf.pstatic.net/MjAyNDA1MjlfODAg/MDAxNzE2OTQ0MzA5MTAx.mb83YI-jmHcE2P-Xvvxh7U9txLrKR7imNhhuVbAYyb8g.WtoW3opdLLv_I4NcqQhJbefI3d-z-H2x7nYCYDxUvYIg.PNG/%EC%84%B8%EB%9D%BC%EB%A7%88%EC%9D%B4%EB%93%9C-%ED%8F%BC%ED%81%B4%EB%A0%8C%EC%A7%95_17169443090877857933133177616668.png"

f = dw.urlopen(bannerUrl).read()
f2 = dw.urlopen(advertiseUrl).read()

with open(savePath, mode='wb') as image:
    image.write(f)

with open(savePath2, mode='wb') as image:
    image.write(f2)

