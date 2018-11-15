def drawEllipses(cx, cy, rx, ry, dx, dy, n):
    for i in range(n):
        fill(0, 0, 0, 0)
        stroke(218/255, 224/255, 227/255)
        strokeWidth(1)
        oval(cx - rx, cy - ry, 2 * rx, 2 * ry)
        rx -= dx
        ry -= dy

w = 800
h = 600
canvasSize = w,h
xPosition = randint(0, h)

if w < h:
    radius = h
    numEllipses = w
else:
    radius = w
    numEllipses = h
maxStep = 20
newPage(w, h)
frameDuration(1/20)
fill(1,1,1)
rect(0, 0, w, h)

drawEllipses((w - xPosition), h+100, radius, radius,
maxStep, maxStep, numEllipses)

drawEllipses(xPosition, -100, radius, radius,
maxStep, maxStep, numEllipses)
