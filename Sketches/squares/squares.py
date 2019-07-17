w, h = 1000, 1000
box_size = w / 1.5
steps = 5

newPage(w, h)

color = [0, 1, 0, 0]

for i in range(steps):
    # Redefine colors:
    color[1] = 1 - (i * steps / 30)
    cmykFill(*color)
    if i == 0:
        rect( ((width() - box_size) / 2), ((height() - box_size) / 2), box_size, box_size)
    else:
        box_size = (box_size * sqrt(2)) - (box_size / sqrt(2))
        rect( ((width() - box_size) / 2), ((height() - box_size) / 2) - i * 20, box_size, box_size)