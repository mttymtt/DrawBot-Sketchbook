# width & height of the canvas as a tuple
w, h = 1080, 1080

# define how many frames the animation should be
total_frames = 40

# define the font name & font size
f_name = "Skia"
f_size = 100

# define the text that is actually drawn
txt = "VARIABLE"

# the values of the variable font
print( listFontVariations(f_name) ) # run this to print out what your font's values are

def ease(axis, start_pos, direction, passes):
    axis_min = listFontVariations(f_name)[axis]['minValue']
    axis_max = listFontVariations(f_name)[axis]['maxValue']
    axis_def = listFontVariations(f_name)[axis]['defaultValue']
    
    axis_range = axis_max - axis_min
    axis_scale = axis_range / 2
    vertical_shift = axis_min + axis_scale
    
    if start_pos == "start_min":
        phase_shift = 0.5 * pi
    if start_pos == "start_max":
        phase_shift = -0.5 * pi
    else:
        phase_shift = asin((axis_def - vertical_shift) / axis_scale) - pi
        
    if direction == "up":
        direction = -1
    else:
        direction = 1
        
    ease = (axis_scale * sin( direction * phase - phase_shift )) + vertical_shift
    return ease

# this is actually where all of the drawing happens
for frame in range(total_frames):
    phase = 2 * pi * frame / total_frames
    
    newPage(w, h)
    
    with savedState():
        fill(1)
        rect(0, 0, w, h)
    
    with savedState():
        fill(0)
        font(f_name, f_size)
        fontVariations(wght = ease("wght", "start_def", "up", 1), wdth = ease("wdth", "start_def", "up", 1))
        text(txt, (w / 2, (h / 2) - fontCapHeight()), align="center")
    print(ease("wght", "start_def", "up", 1))
    
# saveImage("Skia_example_01.gif")