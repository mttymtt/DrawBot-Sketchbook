
def interpolate(percent, start, end):
    value = start + (end - start) * percent
    return value

def move(x_1, x_2, y_1, y_2, total_frames):
    for frame in range(total_frames):
        percent = frame / (total_frames - 1)
        print(frame, "-", percent)
    
        newPage(300, 300)

        new_x = interpolate(percent, x_1, x_2)
        new_y = interpolate(percent ** 4, y_1, y_2)

        oval(x_1, y_1, 5, 5)
        oval(x_2, y_2, 5, 5)
    
        oval(new_x, new_y, 5, 5)

        fontSize(100)
        text("3", (new_x, new_y))

move(x_1=50, x_2=250, y_1=220, y_2=20, total_frames=10)
move(x_1=250, x_2=50, y_1=20, y_2=220, total_frames=10)    

saveImage("08_interpolate.gif")