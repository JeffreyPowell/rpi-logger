#!/usr/bin/python



from PIL import Image, ImageDraw, ImageFont

# Graph defaults

pagewidth = 1024
pageheight = 512

gx = 32
gy = 32
gxx = pagewidth - 32
gyy = pageheight - 32


gtitle      = "Twin 85 Amp Hr"
gxaxistitle = "HOURS"
gyaxistitle = "VOLTS"

gxaxismin  = 00.0
gxaxismax  = 24.0

gyaxismin  = 10.0
gyaxismax  = 14.5

gxaxismajor = 1.0
gxaxisminor = 0.25

gyaxismajor = 1.0
gyaxisminor = 0.1



# Image defaults

white   = (255,255,255)
greylll = (224,224,224)
greyll  = (192,192,192)
greyl   = (160,160,160)
grey    = (128,128,128)
greyd   = ( 96, 96, 96) 
greydd  = ( 64, 64, 64)
greyddd = ( 32, 32, 32)
black   = (  0,  0,  0)

redllll = (255,204,204)
redll   = (255,102,102)
redl    = (255, 51, 51)
red     = (255,000,000)
redd    = (204,000,000)

orange  = (255,128,000)
yellow  = (255,255,000)

green   = (000,255,000)

bluell  = (102,102,255)
bluel   = ( 51, 51,255)
blue    = (  0,  0,255)

violet  = (255,  0,255)


imagemode = "RGB"
imagesize = ( pagewidth, pageheight )

im = Image.new(imagemode,imagesize,color=white)
draw  = ImageDraw.Draw(im)
#fnt18 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf',18)
#fnt14 = ImageFont.truetype('/usr/share/fonts/google-crosextra-carlito/Carlito-Regular.ttf',14)
#fnt10 = ImageFont.truetype('/usr/share/fonts/google-crosextra-carlito/Carlito-Regular.ttf',10)
#fnt8  = ImageFont.truetype('/usr/share/fonts/google-crosextra-carlito/Carlito-Regular.ttf',8)
fnt18  = ImageFont.load_default()
fnt14  = ImageFont.load_default()
fnt10  = ImageFont.load_default()
fnt8   = ImageFont.load_default()


# draw minor axix
xsteps = ( gxaxismax - gxaxismin ) / gxaxisminor
xstep = xsteps
while xstep >= 0:
    x = gx + (xstep*(gxx-gx)/xsteps)
    draw.line( ( x, gy, x, gyy ), fill=redllll )
    xstep -= 1

ysteps = ( gyaxismax - gyaxismin ) / gyaxisminor
ystep = ysteps
while ystep >= 0:
    y = gy + (ystep*(gyy-gy)/ysteps)
    draw.line( ( gx, y, gxx, y ), fill=redllll )
    #text = "%0.1f" % (gyaxismax - (ystep*gyaxisminor))
    #draw.text( ( gx+2, y-2), text, font=fnt8, fill=greyl)
    ystep -= 1


# draw major axix
xsteps = ( gxaxismax - gxaxismin ) / gxaxismajor
xstep = xsteps
while xstep >= 0:
    x = gx + (xstep*(gxx-gx)/xsteps)
    draw.line( ( x, gy, x, gyy ), fill=red )
    text = "%2.2f" % (gxaxismin+(xstep*gxaxismajor))
    draw.text( ( x-10, gyy+1), text, font=fnt10, fill=black)
    xstep -= 1

ysteps = ( gyaxismax - gyaxismin ) / gyaxismajor
ystep = ysteps
while ystep >= 0:
    y = gy + (ystep*(gyy-gy)/ysteps)
    draw.line( ( gx, y, gxx, y ), fill=red )
    text = "%2.0f" % (gyaxismax - (ystep*gyaxismajor))
    draw.text( ( gx-13, y-6), text, font=fnt10, fill=black)
    ystep -= 1


# draw border
draw.line( (gx,  gy,  gx, gyy), fill=black )
draw.line( (gx, gyy, gxx, gyy), fill=black )
draw.line( (gxx,gyy, gxx,  gy), fill=black )
draw.line( (gxx, gy,  gx,  gy), fill=black )


draw.text( (pagewidth/2,gyy+15), gxaxistitle, font=fnt10, fill=black )
draw.text( (1,pageheight/2), gyaxistitle, font=fnt10, fill=black )

# draw title
draw.text((((pagewidth-(len(gtitle)*8))/2),6), gtitle, font=fnt18, fill=black)


#draw.line( (gx,  gyy,  gxx, gy), fill=blue )


im.putpixel( (100,100), green )
im.putpixel( (101,101), green )
im.putpixel( (100,101), green )
im.putpixel( (101,100), green )

im.save("graphx.png")





