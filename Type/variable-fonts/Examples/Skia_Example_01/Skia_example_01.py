import os
from time import strftime

# width & height of the canvas as a tuple
w, h = 1080, 1080

# define how many frames the animation should be
total_frames = 40

# define the font name & font size
font_name = "Skia"
font_size = 100

# define the text that is actually drawn
txt = "VARIABLE"

# the values of the variable font
print( listFontVariations(font_name) ) # run this to print out what your font's values are

#    ========================================
#    ========================================
#    
#    EASE FUNCTION
#    
#    This is a re-usable function, that we
#    can use to progressively change the
#    value of an axis (of our choosing)
#
#    ease(axis, start_pos, direction, passes)
#
#    axis:      4 letter string ("wght", "wdth", etc.)
#    start_pos: options are ("start_at_min", "start_at_max", or "start_at_default")
#    direction: options are ("up" or "down") and only applies to when you "start_at_default"
#    passes:    the number of times you'd like to cycle through the axis range
#    
#    ========================================
#    ========================================

def ease(axis, start_pos, direction, passes):
    axis_min = listFontVariations(font_name)[axis]['minValue']
    axis_max = listFontVariations(font_name)[axis]['maxValue']
    axis_def = listFontVariations(font_name)[axis]['defaultValue']
    
    axis_range = axis_max - axis_min
    axis_scale = axis_range / 2
    vertical_shift = axis_min + axis_scale
    
    if start_pos == "start_at_min":
        phase_shift = 0.5 * pi
    if start_pos == "start_at_max":
        phase_shift = -0.5 * pi
    else:
        phase_shift = asin((axis_def - vertical_shift) / axis_scale) - pi
        
    if direction == "up":
        direction = -1
    else:
        direction = 1
        
    ease = (axis_scale * sin( direction * phase - phase_shift )) + vertical_shift
    return ease

#    ========================================
#    ========================================
#    
#    WHERE THE DRAWING HAPPENS
#    
#    ========================================
#    ========================================

for frame in range(total_frames):
    phase = 2 * pi * frame / total_frames # determine where in the phase we are (starts at 0 and goes to 2pi)
    
    # for each frame, create a new page that we can draw on
    newPage(w, h)
    
    # draw a white rectangle in the background (a transparent background makes for a rough animation) 
    with savedState():
        fill(1) # if you want to change the colors, read up on them here: http://www.drawbot.com/content/color.html
        rect(0, 0, w, h)
    
    # this is where we start to draw the type
    with savedState():
        fill(0) # if you want to change the colors, read up on them here: http://www.drawbot.com/content/color.html
        font(font_name, font_size)
        
        # EASE FUNCTION
        # This is where we reuse that ease function from above
        fontVariations(wght = ease("wght", "start_at_default", "up", 1), wdth = ease("wdth", "start_at_default", "up", 1))
        
        # for more on drawing text: http://www.drawbot.com/content/text/drawingText.html
        text(txt, (w / 2, (h / 2) - fontCapHeight()), align="center")
        
    # let's just print that ease function so we can make sure all of the values are looking correct
    print(ease("wght", "start_def", "up", 1))

#    ========================================
#    ========================================
#    
#    SAVE THE DOCUMENT
#
#    The bottom most line saves out the image
#    but the other information gives us more
#    control over how we save the image.
#    
#    ========================================
#    ========================================
export = False # True: save your drawing; False: don't save! (Good for testing)

directory = 'Exports' # This is the folder where all of the images/videos will be saved
file_format = ".gif" # This is the format of the file you want to save out

# True: append file name with date and time of export
# False: don't append file name & overwrite each time you save (if filename & format remains same)
use_file_time = True
file_time = strftime("%Y-%m-%d_at_%H-%M-%S") # append date and time of export to filename

# The name of this python file
# We'll re-use this to name our exported files
basename = os.path.splitext(os.path.basename(__file__))[0]

if export == True:
    # Automatically create a folder to save the proofs into (if it doesn't exist already)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    if use_file_time == True:
        filename = basename + "_" + file_time + file_format
    else:
        filename = basename + file_format

    # Export the drawing!
    saveImage(directory + "/" + filename)