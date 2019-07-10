newPage("Letter")

shapeWidth = 10

for x in range(0, width(), 30):
    for y in range(0, height(), 30):
        path = BezierPath()
        path.moveTo( (x, y) )
        path.curveTo( (x+shapeWidth, y), (x * 1.1, y+shapeWidth * 2), (x+shapeWidth, y+shapeWidth) )
        fill(None)
        stroke(1,0,0)
        drawPath(path)