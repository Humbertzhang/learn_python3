from PIL import Image,ImageDraw,ImageFont
im = Image.open("images.png")
color="#ff0000"
width,height = im.size
draw = ImageDraw.Draw(im)
draw.text((width-20,0),'99',fill=color)
del draw
im.save('avater.png','png')
