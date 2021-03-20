import sqlite3
import PIL
from PIL import Image, ImageDraw, ImageFont

conn = sqlite3.connect('reg.db')
curr = conn.cursor()

curr.execute("SELECT * FROM Registrations")

RGB = (0,0,0)

inFont = "GreatVibes-Regular.ttf"
inFonti = "Lora-Italic.ttf"
inFontib = "Lora-BoldItalic.ttf"

rows = curr.fetchall()
count=0
for row in rows:
    im = PIL.Image.open("template.png")
    draw = ImageDraw.Draw(im)

    i=99
    myFont = ImageFont.truetype(inFont, i)

    tempString= row[0].title()

    W,H = im.size

    w,h = draw.textsize(tempString,font=myFont)
    draw.text((((W/2)-(w/2)),(582)),row[0], RGB, font = myFont)

    tempString1= "of "

    tempString= row[1].upper()

    i=30
    myFonti = ImageFont.truetype(inFonti, i)
    w1,h1 = draw.textsize(tempString1,font=myFonti)
    myFontib = ImageFont.truetype(inFontib, i)
    w2,h2 = draw.textsize(tempString,font=myFontib)

    draw.text((((W/2)-((w1+w2)/2)),(701)),tempString1, RGB, font = myFonti)
    draw.text((((W/2)-((w1+w2)/2)+w1),(701)),tempString, RGB, font = myFontib)

    dest = 'output1/'+row[0]+str(count)+'.png'
    count = count+1
    im.save(dest)










