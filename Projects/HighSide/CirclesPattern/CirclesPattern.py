# Draws two series of concentric circles which start on the outer edges of the canvas, both of whose origin positions are randomized and slightly inverse from one another.

# Adopted from Just van Rossum's Ellipses.py which can be found here: https://gist.github.com/justvanrossum/ff716d82a2b3345c3c84255761fc44a4

def drawEllipses(cx, cy, rx, ry, dx, dy, n):
    for i in range(n):
        fill(0, 0, 0, 0)
        stroke(218/255, 224/255, 227/255)
        strokeWidth(1)
        oval(cx - rx, cy - ry, 2 * rx, 2 * ry)
        rx -= dx
        ry -= dy

w = 1200
h = 600
canvasSize = w,h

yPositionTop = randint(h-(h // 4), h+100)
yPositionBottom = randint(-100, (h // 4))

if yPositionTop < h+20:
    xPositionTop = w+100
else:
    xPositionTop = randint((w-(w // 3)), (w+100))

if yPositionBottom > -20:
    xPositionBottom = -100
else:
    xPositionBottom = randint(0, w // 3)

if w < h:
    radius = h
    numEllipses = w // 2
else:
    radius = w
    numEllipses = ((w + 100) // 10)
maxStep = 20
newPage(w, h)
frameDuration(1/20)
fill(1,1,1)
rect(0, 0, w, h)

drawEllipses(xPositionTop, yPositionTop, radius, radius,
maxStep, maxStep, numEllipses)

drawEllipses(xPositionBottom, yPositionBottom, radius, radius,
maxStep, maxStep, numEllipses)

# saveImage("HighSide_CirclesPattern_01.pdf")
