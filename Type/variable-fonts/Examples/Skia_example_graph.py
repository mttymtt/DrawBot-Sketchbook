# import math
frames = 100

maximum = 319.99
minimum = 47.99
default = 100
axis_range = maximum - minimum

w, h = frames*20+10, maximum

sine_scale = axis_range / 2
vertical_shift = minimum + sine_scale

start_min = 0.5 * pi
start_max = -0.5 * pi
start_default = asin((default - vertical_shift) / sine_scale) - pi

phase_shift = start_default
up = -1
down = 1
direction = down

size(w, h)

with savedState():
    for i in range(frames):
        passes = 1
        translate(20,0)
        phase =  2 * pi * i / frames
        amplitude = (sine_scale * sin( direction * phase - phase_shift )) + vertical_shift
        print("amplitute", amplitude)
        fill(1,0,0)
        oval(0,amplitude,8,8)
        