import math
frames = 100

maximum = 400
minimum = 0

w, h = frames*20+10, maximum

sine_scale = (maximum-minimum)/2

size(w, h)

for i in range(frames):
    translate(20,0)
    phase = 2 * pi * i / frames
    amplitude = (sin(phase-(((0/3)-0.5)*pi))*sine_scale)+sine_scale
    fill(1,0,0)
    oval(0,amplitude,8,8)
    
    amplitude2 = (sin(phase-(((1/3)-0.5)*pi))*sine_scale)+sine_scale
    fill(0,1,0)
    oval(0,amplitude2,8,8)
    
    amplitude3 = (sin(phase-(((2/3)-0.5)*pi))*sine_scale)+sine_scale
    fill(0,0,1)
    oval(0,amplitude3,8,8)

# saveImage("offset-sine-wave.png")