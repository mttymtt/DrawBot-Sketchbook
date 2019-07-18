import os

# FILENAME
basename = os.path.splitext(os.path.basename(__file__))[0]
file_detail = ""
version = "01"
format = ".png"
if file_detail != "":
    filename = basename + "_" + file_detail + "_" + version + format
else:
    filename = basename + "-" + version + format

export = False

total_pages = 10

def matthew_smith():
    newPage(1080, 1080)
    
    inch = 72
    margin = (2) * inch
    
    live_width = width() - (margin * 2)
    live_height = height() - (margin * 2)
    
    margin_bottom = margin
    margin_left = margin * 2
    margin_top = height() - margin
    margin_right = width() - (margin * 2)
    
    center_horizontal = width() / 2
    center_vertical = height() / 2
    
    # determine size of circle mask
    # size is relative to width of document
    # or it'll max out at what is defined below
    relative_size = live_width - (margin * 4)
    max_size = 4 * inch
    
    fill(None)
    
    def clipping_mask():
        if relative_size > max_size:
            mask_width = max_size
        else:
            mask_width = relative_size
            
        mask_height = mask_width * 2.5
        
        rotate(randint(-20, 20), center=(center_horizontal, center_vertical))
        rect( (width() - mask_width) / 2, (height() - mask_height) / 2, mask_width, mask_height )
    
    total_lines = 40
    color_step = 1 / total_lines
    
    def stack():
        for i in range(total_lines):
            with savedState():
                # change color of lines
                cmykStroke(0, 0, 0, i * color_step)
                strokeWidth(width() / 75)
                # lineCap("round")
        
                # first point
                x1 = randint(margin_left, center_horizontal)
                y1 = randint(margin_bottom, margin_top)
    
                # second point
                x2 = randint(center_horizontal, margin_right)
                y2 = randint(margin_bottom, margin_top)
    
                # draw the line
                line((x1, y1), (x2, y2))
    
    with savedState():
        fill(1)
        rect(0,0,height(),width())
    
    # draw the lines in the background
    stack()
    
    # start to define the image object
    im = ImageObject()
    
    with im:
        stack()
    
    # apply some filters
    im.gaussianBlur(4)
    
    # this calculates the offset of the blur applied above (results in negative x & y)
    offset_x, offset_y = im.offset()
    
    # apply clipping mask to blurred image    
    cmykFill(0, 0, 0, 0)
    clipPath(clipping_mask())
    
    # draw the blurred image
    image(im, (offset_x, offset_y))
        
        
# Produce a drawing for each page
for page_number in range(total_pages):
    matthew_smith()
    


if export == True:
    saveImage(filename, multipage="True")