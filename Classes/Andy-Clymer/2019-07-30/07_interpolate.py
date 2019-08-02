
def interpolate(percent, start, end):
    value = start + (end - start) * percent
    return value

total_frames = 10

for frame in range(total_frames):
    percent = frame / (total_frames - 1)
    print(frame, "-", percent)
    
    newPage(300, 300)

    x_1, y_1 = 30, 200
    x_2, y_2 = 250, 19

    new_x = interpolate(percent, x_1, x_2)
    new_y = interpolate(percent, y_1, y_2)

    oval(x_1, y_1, 5, 5)
    oval(x_2, y_2, 5, 5)
    
    oval(new_x, new_y, 5, 5)

    fontSize(100)
    text("3", (new_x, new_y))