import os

# FILENAME
basename = os.path.splitext(os.path.basename(__file__))[0]
file_detail = "single"
version = "01"
format = ".png"
if file_detail != "":
    filename = basename + "_" + file_detail + "_" + version + format
else:
    filename = basename + "-" + version + format
print(filename)

export = True # Save image(s)?

newPage("Letter")

# Define window (to make into a mask)
window_w, window_h = (width()/4), (height()/4)
fill(None) # remove fill from mask
window = rect( ((width()/2) - (window_w/2)), ((height()/2) - (window_h/2)), window_w, window_h )

sun_size = window_w/2

clipPath(window)
# set a gradient as the fill color
linearGradient(
    (((width()/2) - (window_w/2)), ((height()/2) + (window_h/2))),    # startPoint
    (((width()/2) - (window_w/2)), ((height()/2) - (window_h/2))),    # endPoint
    [(0.7, 0, 0.6), (1, 0, 0)],    # colors
    [0.25, 1]    # locations
    )
# draw a rectangle
rect( ((width()/2) - (window_w/2)), ((height()/2) - (window_h/2)), window_w, window_h )
fill(1)
oval( ((width()/2) - (sun_size/2)), ((height()/2) - (window_h/2) - (sun_size / 4)), sun_size, sun_size )

if export == True:
    saveImage(filename)