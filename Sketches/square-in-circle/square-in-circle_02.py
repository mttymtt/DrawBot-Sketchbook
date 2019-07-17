margin = 100

newPage(1000, 1000)
# fill(None)
# stroke(1,0,0)
# strokeWidth(1)
diameter = width() - margin
for i in range(10):    
    if i > 0:
        diameter = (diameter * sqrt(2)) - ( diameter / sqrt(2) )
    linearGradient(
        ( ((width() + diameter) / 2), ((height() + diameter) / 2) ),    # startPoint
        ( ((width() - diameter) / 2), ((height() - diameter) / 2) ),    # endPoint
        [(1,1,1), (0,0,0)],    # colors
        [0, 1]    # locations
        )
    rect( ((width() - diameter) / 2), ((height() - diameter) / 2), diameter, diameter)
    linearGradient(
        ( ((width() - diameter) / 2), ((height() - diameter) / 2) ),    # startPoint
        ( ((width() + diameter) / 2), ((height() + diameter) / 2) ),    # endPoint
        [(1,1,1), (0,0,0)],    # colors
        [0, 1]    # locations
        )
    oval( ((width() - diameter) / 2), ((height() - diameter) / 2), diameter, diameter)
    
# saveImage("square-in-circle_02.png")