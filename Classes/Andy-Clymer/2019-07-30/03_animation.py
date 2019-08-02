import math

total_frames = 40
speed = 1/15 # represented as a fraction of a second

newPage("A5")
for frame in range(total_frames):
    percent = frame / (total_frames - 1)
    print(percent)
    
    frameDuration(speed) # represented as a fraction of a second
    # fill(1)
    # rect(0, 0, width(), height())
    fill(None)
    stroke(1, 0, 0)
    rect(0, 0, width() * (percent), height() * (percent))
    stroke(0)
    oval(0, 0, width() * (percent ** 6), height() * (percent ** 6))
    
    
# saveImage("02_animation.gif")