import PIL
from PIL import Image

baseheight = 480
for i in range(9,12):
	i+=1
	img = Image.open(str(i)+".jpg")
	hpercent = (baseheight / float(img.size[1]))
	wsize = int((float(img.size[0]) * float(hpercent)))
	img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
	img.save(str(i)+".jpg")
