newPage(100, 100)

fill(None)
stroke(0)
strokeWidth(1)
line((0, 0), (height()/4,width()/4))

stroke(1, 0, 0)
path = BezierPath()
path.moveTo( (50, 50) )
path.lineTo( (80, 80) )
path.curveTo( (50, 80), (10, 50), (15, 86) )
drawPath(path)