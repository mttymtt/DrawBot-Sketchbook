# True = Animated
# False = Static (Easier to set up the design before making the animation)
animated = True

#-----------------------------------

if animated:
    frames = 30
else: 
    frames = 1
    
offset = 2
splices = 6
animationDuration = (frames-(offset*splices))/frames

# How long a single frame lasts (represented as a second)
# (Actually doesn't change frame speed in this animation, but I'm keeping it here anyway)
# if video:
#     frameSpeed = 0.05 
#     GIF = False # Saves mp4
# else:
#     frameSpeed = 0.05
#     GIF = True # Saves gif
    
frameSpeed = 0.04

# margin of canvas
margin = 40

# colors
R = 255
G = 255
B = 255

white = [1, 1, 1]
black = [0, 0, 0]
red = [1, 0, 0]

color_bg = white
color_text = black

# font name and size
f_name = "ThePyteFoundry--Epitome"
f_size = 100

# width and height of canvas
w = 1080

txt = 'SHORT PHRASE'
font(f_name)
fontSize(f_size)
textWidth, textHeight = textSize(txt)
f_scale = w / textWidth

font(f_name, f_size*f_scale)
h = fontCapHeight()

maximum = 100
minimum = 0

# sin wave scale
sine_scale = (maximum-minimum)/2

for i in range(frames):
    newPage(w,h)
    frameDuration(frameSpeed)
    
    fill(*color_bg)
    rect(0,0,w,h)
    
    phase = -1 * pi * i / frames
    
    font(f_name, f_size*f_scale)
    fill(*color_text)
    
    with savedState():
        amplitude = ((sin(phase-(((0)-1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)
        path = BezierPath()
        path.rect(0, (fontCapHeight()/6)*5, w, (fontCapHeight()/6))
        clipPath(path)
        if amplitude < 1:
            scale(x=amplitude,y=1)
        else:
            scale(x=1, y=1)
        text(txt, (0, 0))
        
    if i > offset:
        with savedState():
            amplitude = ((sin((phase)-(((offset*(-1)/frames)-1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)
            path = BezierPath()
            path.rect(0, (fontCapHeight()/6)*4, w, (fontCapHeight()/6))
            clipPath(path)
            if amplitude < 1:
                scale(x=amplitude,y=1)
            else:
                scale(x=1, y=1)
            text(txt, (0, 0))
    if i > offset * 2:
        with savedState():
            amplitude = ((sin((phase)-(((offset*-2/frames)-1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)
            path = BezierPath()
            path.rect(0, (fontCapHeight()/6)*3, w, (fontCapHeight()/6))
            clipPath(path)
            if amplitude < 1:
                scale(x=amplitude,y=1)
            else:
                scale(x=1, y=1)
            text(txt, (0, 0))
    if i > offset * 3:
        with savedState():
            amplitude = ((sin((phase)-(((offset*-3/frames)-1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)
            path = BezierPath()
            path.rect(0, (fontCapHeight()/6)*2, w, (fontCapHeight()/6))
            clipPath(path)
            if amplitude < 1:
                scale(x=amplitude,y=1)
            else:
                scale(x=1, y=1)
            text(txt, (0, 0))
    if i > offset * 4:
        with savedState():
            amplitude = ((sin((phase)-(((offset*-4/frames)-1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)
            path = BezierPath()
            path.rect(0, (fontCapHeight()/6)*1, w, (fontCapHeight()/6))
            clipPath(path)
            if amplitude < 1:
                scale(x=amplitude,y=1)
            else:
                scale(x=1, y=1)
            text(txt, (0, 0))
    if i > offset * 5:
        with savedState():
            amplitude = ((sin((phase)-(((offset*-5/frames)-1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)
            path = BezierPath()
            path.rect(0, (fontCapHeight()/6)*0, w, (fontCapHeight()/6))
            clipPath(path)
            if amplitude < 1:
                scale(x=amplitude,y=1)
            else:
                scale(x=1, y=1)
            text(txt, (0, 0))
            
for i in range(frames):
    newPage(w,h)
    frameDuration(frameSpeed)
    
    fill(*color_bg)
    rect(0,0,w,h)
    
    phase = -1 * pi * i / frames
    
    font(f_name, f_size*f_scale)
    fill(*color_text)
    
    with savedState():
        amplitude = (((sin(phase-(((0)+1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)) - (animationDuration)
        path = BezierPath()
        path.rect(0, (fontCapHeight()/6)*5, w, (fontCapHeight()/6))
        clipPath(path)
        if amplitude < 1:
            scale(x=amplitude,y=1, center=(w,0))
        if amplitude > 1:
            scale(x=1, y=1, center=(w,0))
        if amplitude < 0:
            scale(x=0, y=1, center=(w,0))
        text(txt, (0, 0))
    if i <= offset:
        with savedState():
            amplitude = (((sin(phase-(((0)+1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)) - (animationDuration)
            path = BezierPath()
            path.rect(0, 0, w, (fontCapHeight()/6)*5)
            clipPath(path)
            scale(x=1, y=1, center=(w,0))
            text(txt, (0, 0))
    if i >= offset:
        with savedState():
            amplitude = (((sin(phase-(((offset*(-1)/frames)+1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)) - (animationDuration)
            path = BezierPath()
            path.rect(0, (fontCapHeight()/6)*4, w, (fontCapHeight()/6))
            clipPath(path)
            if amplitude < 1:
                scale(x=amplitude,y=1, center=(w,0))
            if amplitude > 1:
                scale(x=1, y=1, center=(w,0))
            if amplitude < 0:
                scale(x=0, y=1, center=(w,0))
            text(txt, (0, 0))
    if i <= offset * 2:
        with savedState():
            amplitude = (((sin(phase-(((0)+1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)) - (animationDuration)
            path = BezierPath()
            path.rect(0, 0, w, (fontCapHeight()/6)*4)
            clipPath(path)
            scale(x=1, y=1, center=(w,0))
            text(txt, (0, 0))
    if i >= offset * 2:
        with savedState():
            amplitude = (((sin(phase-(((offset*(-2)/frames)+1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)) - (animationDuration)
            path = BezierPath()
            path.rect(0, (fontCapHeight()/6)*3, w, (fontCapHeight()/6))
            clipPath(path)
            if amplitude < 1:
                scale(x=amplitude,y=1, center=(w,0))
            if amplitude > 1:
                scale(x=1, y=1, center=(w,0))
            if amplitude < 0:
                scale(x=0, y=1, center=(w,0))
            text(txt, (0, 0))
    if i <= offset * 3:
        with savedState():
            amplitude = (((sin(phase-(((0)+1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)) - (animationDuration)
            path = BezierPath()
            path.rect(0, 0, w, (fontCapHeight()/6)*3)
            clipPath(path)
            scale(x=1, y=1, center=(w,0))
            text(txt, (0, 0))
    if i >= offset * 3:
        with savedState():
            amplitude = (((sin(phase-(((offset*(-3)/frames)+1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)) - (animationDuration)
            path = BezierPath()
            path.rect(0, (fontCapHeight()/6)*2, w, (fontCapHeight()/6))
            clipPath(path)
            if amplitude < 1:
                scale(x=amplitude,y=1, center=(w,0))
            if amplitude > 1:
                scale(x=1, y=1, center=(w,0))
            if amplitude < 0:
                scale(x=0, y=1, center=(w,0))
            text(txt, (0, 0))
    if i <= offset * 4:
        with savedState():
            amplitude = (((sin(phase-(((0)+1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)) - (animationDuration)
            path = BezierPath()
            path.rect(0, 0, w, (fontCapHeight()/6)*2)
            clipPath(path)
            scale(x=1, y=1, center=(w,0))
            text(txt, (0, 0))
    if i >= offset * 4:
        with savedState():
            amplitude = (((sin(phase-(((offset*(-4)/frames)+1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)) - (animationDuration)
            path = BezierPath()
            path.rect(0, (fontCapHeight()/6)*1, w, (fontCapHeight()/6))
            clipPath(path)
            if amplitude < 1:
                scale(x=amplitude,y=1, center=(w,0))
            if amplitude > 1:
                scale(x=1, y=1, center=(w,0))
            if amplitude < 0:
                scale(x=0, y=1, center=(w,0))
            text(txt, (0, 0))
    if i <= offset * 5:
        with savedState():
            amplitude = (((sin(phase-(((0)+1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)) - (animationDuration)
            path = BezierPath()
            path.rect(0, 0, w, (fontCapHeight()/6)*1)
            clipPath(path)
            scale(x=1, y=1, center=(w,0))
            text(txt, (0, 0))
    if i >= offset * 5:
        with savedState():
            amplitude = (((sin(phase-(((offset*(-5)/frames)+1.5)*pi))*sine_scale)+sine_scale) / (100 * animationDuration)) - (animationDuration)
            path = BezierPath()
            path.rect(0, (fontCapHeight()/6)*0, w, (fontCapHeight()/6))
            clipPath(path)
            if amplitude < 1:
                scale(x=amplitude,y=1, center=(w,0))
            if amplitude > 1:
                scale(x=1, y=1, center=(w,0))
            if amplitude < 0:
                scale(x=0, y=1, center=(w,0))
            text(txt, (0, 0))
                
saveImage("stretch-to-fill_01.gif")
