# Please note, this file is set up for a variable font version of Montecatini Pro which is not available commercially at the moment. You can adopt this code for another variable font that you have purchased.

# DISCLAIMER: This code might not be written the best it can be. I've run into the problem where after exporting one gif or video, I have to restart DrawBot in order to run it again. You may also run into this problem, so this is just a heads up. If you know what the problem is which causes this, please let me know!

# True = Animated
# False = Static (Easier to set up the design before making the animation)
animated = True

# True = Makes frame speed longer and saves as a mp4 
# False = Makes frame speed shorter and saves as a gif
video = False

# True = Light Version
# False = Dark Version
light = False

#-----------------------------------

if animated:
    frames = 20
else: 
    frames = 1
    
# How long a single frame lasts (represented as a second)
# (Actually doesn't change frame speed in this animation, but I'm keeping it here anyway)
if video:
    frameSpeed = 0.08 
    GIF = False # Saves mp4
else:
    frameSpeed = 0.08
    GIF = True # Saves gif

# width and height of canvas
w, h = (1080, 1920)

# font stuff
f_name = "Montecatini VAR"
f_size = 150

copy = "TOMORROW"

# RGB
R = 255
G = 255
B = 255

# colors
white = [255/R, 255/G, 255/B]
black = [0/R, 0/G, 0/B]
red = [210/R, 101/G, 92/B]

# color assignments

if light:
    color_bg = white
    color_text = red
    saveLight = True
else:
    color_bg = black
    color_text = white
    saveLight = False

width_min = 100 + 0.01 # adjusting by 0.01 because it glitches when at the extremes

weight_max = 800 - 0.01 # adjusting by 0.01 because it glitches when at the extremes
weight_min = 400 + 0.01 # adjusting by 0.01 because it glitches when at the extremes

# this adjusts the sin wave so that the bottom is actually the weight_min
adj = weight_min + 200

# sin scale - cut the sin wave in half otherwise it'd be twice as large
scale = weight_min/2

letters = len(copy) # number of letters
# letters = len(copy) - copy.count(" ") # number of letters WITHOUT spaces

lines = 13 # number of lines

font(f_name)
fontSize(f_size)
margin = fontCapHeight() # set margin to font capheight, although you may want to change this to something more independently defined because it could be problematic if the cap height is massive (for a short word or if you have a long phrase with a small point size)

# Determine the space between each line based on the number of lines defined above
spacer = ((h - (margin * 2)) - (margin * lines)) / (lines - 1)


# take the number of lines and draw/distribute the text to fit within the margin of the canvas
def repeatType(text, f):
    for l in range(lines):
        offset = l / lines
        text(textLine(phase(f), offset), (w/2, margin + (margin+spacer)*l), align="center")
    
# take the number of lines and draw/distribute the text to fit within the margin of the canvas
def phase(f):
    phase = 2 * pi * f / frames
    return phase

# runs through your copy and offsets the weight 
def textLine(phase, offset):
    for c in range(len(copy)):
        txt = FormattedString()
        for c in range(len(copy)):
            amplitude = sin(phase-((((c)/letters)-(offset+0.5))*pi))*scale
            txt.append(copy[c], font=f_name, fontSize=f_size, fontVariations=dict(wdth=width_min, wght=(amplitude+adj)), openTypeFeatures=dict(calt=False, ss02=True), fill=(color_text))
        return txt
        
# this takes everything above and puts it together
def drawAnimation():
    for f in range(frames):
        newPage(w,h)
        frameDuration(0.08)

        fill(*color_bg)
        rect(0,0,w,h)

        #actually draw the type
        font(f_name)
        fontSize(f_size)
    
        repeatType(text, f) # where the magic happens
    
if saveLight:
    if GIF:
        drawAnimation()
        saveImage("Montecatini-Pro_Tomorrow_Light_01-00.gif")
    else:
        # repeat drawAnimation() so that it repeats more than once when saving out an mp4
        drawAnimation()
        drawAnimation()
        drawAnimation()
        drawAnimation()
        drawAnimation()
        saveImage("Montecatini-Pro_Tomorrow_Light_01-00.mp4")
else:
    if GIF:
        drawAnimation()
        saveImage("Montecatini-Pro_Tomorrow_Black_01-00.gif")
    else:
        # repeat drawAnimation() so that it repeats more than once when saving out an mp4
        drawAnimation()
        drawAnimation()
        drawAnimation()
        drawAnimation()
        drawAnimation() 
        saveImage("Montecatini-Pro_Tomorrow_Black_01-00.mp4")