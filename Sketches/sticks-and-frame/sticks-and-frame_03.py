import os

# FILENAME
basename = os.path.splitext(os.path.basename(__file__))[0]
file_detail = ""
version = "01"
format = ".pdf"
if file_detail != "":
    filename = basename + "_" + file_detail + "_" + version + format
else:
    filename = basename + "-" + version + format

export = False

def matthew_smith():
    newPage("A5")
    
    inch = 72
    margin = (1) * inch
    
    live_width = width() - (margin * 2)
    live_height = height() - (margin * 2)
    
    margin_bottom = margin
    margin_left = margin
    margin_top = height() - margin
    margin_right = width() - margin
    
    center_horizontal = width() / 2
    center_vertical = height() / 2
    
    fill(None)
    # cmykStroke(0, 0, 0, 1)
    
    def clipping_mask():
        rotate(randint(-20, 20), center=(center_horizontal, center_vertical))
        rect( margin_left+margin, margin_bottom+margin, live_width-(margin*2), live_height-(margin*2) )
    
    total_lines = 40
    color_step = 1 / total_lines
    
    def stack():
        for i in range(total_lines):
            with savedState():
                # change color of lines
                cmykStroke(0, 0, 0, i * color_step)
                strokeWidth(5)
                # lineCap("round")
        
                # first point
                x1 = randint(margin_left, center_horizontal)
                y1 = randint(margin_bottom, margin_top)
    
                # second point
                x2 = randint(center_horizontal, margin_right)
                y2 = randint(margin_bottom, margin_top)
    
                # draw the line
                line((x1, y1), (x2, y2))
    
    im = ImageObject()
    
    with im:
        stack()
    
    stack()
    
    # apply some filters
    im.gaussianBlur(4)
    
    # this calculates the offset of the blur applied above (results in negative x & y)
    offset_x, offset_y = im.offset()
    
    # apply clipping mask to blurred image    
    cmykFill(0, 0, 0, 0)
    clipPath(clipping_mask())
    
    image(im, (offset_x, offset_y))
        
for page_number in range(6):
    matthew_smith()
    


if export == True:
    saveImage(filename)