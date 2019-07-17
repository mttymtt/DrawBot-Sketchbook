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
    
    total_lines = 40
    
    color_step = 1 / total_lines
    
    for i in range(total_lines):
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
        
        # draw a rectangle at the half way point of the for loop
        if i == total_lines / 2:
            with savedState():
                blendMode("screen")
                cmykStroke(None)
                strokeWidth(None)
                cmykRadialGradient(
                    (center_horizontal, center_vertical),                         # startPoint
                    (center_horizontal, center_vertical),                         # endPoint
                    [(0, 0, 0, 0), (0, 0, 0, 1)],  # colors
                    [0.2, 0.5],                         # locations
                    0,                                  # startRadius
                    live_height-(margin*2)                                 # endRadius
                    )
                rotate(randint(-20, 20), center=(center_horizontal, center_vertical))
                rect( margin_left+margin, margin_bottom+margin, live_width-(margin*2), live_height-(margin*2) )

for page_number in range(6):
    matthew_smith()
    


if export == True:
    saveImage(filename)