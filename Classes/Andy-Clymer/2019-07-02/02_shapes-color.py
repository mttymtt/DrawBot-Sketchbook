import os

filename = os.path.basename(__file__)

# Function
print("This is a function")


# New Page, 300pt x 200pt
# 72ppi
newPage(300, 200) #if no values are defined, the canvas defaults to 1000 x 1000

# Fill
# One Value: Gray scale
# Three Values: RGB
# Four Values: RGBA
fill(0, 1, 0.5, 0.25)

rect(10, 10, 100, 150) # x, y, height, width
# FUN FACT: select two values, hold command, and click and drag to freely change values

cmykFill(1, 1, 0, 0, 0.5) # c, m, y, k, alpha

oval(10, 10, 200, 150)

saveImage(filename + ".png")