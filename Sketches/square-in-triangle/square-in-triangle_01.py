newPage("TabloidLandscape")

# style the shapes
fill(None)
stroke(1,0,0)

inch = 72
margin = (2) * inch

# define the shape size
# if horizontal, base it off of the height - margin
if width() > height():
    shape_size = height() - (margin * 2)
# if vertical, base it off of the width - margin
else:
    shape_size = width() - (margin * 2)

# number of repeating shapes
steps_total = 6

# center drawing in canvas
# without this it'll start at 0, 0
translate( ((width() - shape_size) / 2), ((height() - shape_size) / 2) )

for step in range(steps_total):
    # draw the first square and triangle at the scale defined above (shape_size)
    # after the else: the shape_size is redefine, so this is important to isolate
    if step == 0:
        rect( 0, 0, shape_size, shape_size )
        polygon( (0,0), ( shape_size/2, shape_size ), (shape_size, 0) )
    else:
        # for every loop, let's redefine the shape_size. So it's kind of doing this:
        # shape_size = 1000 / 2 (1000 is the example start shape_size, and half of it will carry over with each loop)
        # shape_size = 500 / 2
        # shape_size = 250 / 2 and so on!
        shape_size = shape_size / (2)
        #with every loop, shift the shape over to center itself
        translate( shape_size / 2 )
        rect( 0, 0, shape_size, shape_size )
        polygon( (0,0), ( shape_size / 2, shape_size ), (shape_size, 0) )        
        