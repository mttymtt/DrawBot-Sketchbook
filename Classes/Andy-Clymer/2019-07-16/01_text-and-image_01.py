newPage("Letter")

# w, h = width(), height()

imagePath = "/Users/Mattymatt/Dropbox/GitHub/DrawBot-Sketchbook/Classes/Andy-Clymer/2019-07-16/TextAndImage/Images/Amaryllis fulgida.jpg"

image_width, image_height = imageSize(imagePath)
scale_factor = height() * 0.5 / image_height

fontSize(100)
fill(1, 0, 0)

with savedState():
    # translate((width() - w) / 2, (height() - h) / 2)
    # translate(100, 100)
    # rotate(20)
    scale(scale_factor)
    rotate(20, center=( image_width*scale_factor, image_height*scale_factor ))
    image(imagePath, (0,0))
    rect(200, 200, 2000, 30)

text("This is some text", (10, 10))