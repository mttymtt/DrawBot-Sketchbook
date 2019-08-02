import math

print(e)

total_frames = 20
speed = 1/15 # represented as a fraction of a second

for frame in range(total_frames):
    percent = frame / (total_frames - 1)
    print(percent)
    
    newPage("A5")
    frameDuration(speed) # represented as a fraction of a second
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    oval(0, 0, width() * percent, height() * percent)
    
    
saveImage("01_animation.gif")