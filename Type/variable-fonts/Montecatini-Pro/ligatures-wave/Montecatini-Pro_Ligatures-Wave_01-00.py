# Please note, this file is set up for a variable font version of Montecatini Pro which is not available commercially at the moment. You can adopt this code for another variable font that you have purchased.

# True = Animated
# False = Static (Easier to set up the design before making the animation)
animated = True

# True = Makes frame speed longer and saves as a mp4 
# False = Makes frame speed shorter and saves as a gif
video = False

# True = Light Version
# False = Dark Version
light = True

#-----------------------------------

if animated:
    frames = 60
else: 
    frames = 1

# How long a single frame lasts (represented as a second)
# (Actually doesn't change frame speed in this animation, but I'm keeping it here anyway)
if video:
    frameSpeed = 0.05 
    GIF = False # Saves mp4
else:
    frameSpeed = 0.05
    GIF = True # Saves gif

# width and height of canvas
w, h = (1080, 1080)

# margin of canvas
margin = 40

# colors
R = 255
G = 255
B = 255

white = [1, 1, 1]
black = [0, 0, 0]
# red = [185/R, 24/G, 29/B] #deeper red
red = [208/R, 84/G, 69/B] #lighter red

if light:
    color_bg = white
    color_text = black
    color_highlight = red
    saveLight = True
else:
    color_bg = black
    color_text = white
    color_highlight = white
    saveLight = False

# font name and size
f_name = "Montecatini VAR"
f_size = 100


# calculate a scale factor to resize the font to fit 1/7th of the height
txt = 'TEST'
font(f_name)
fontSize(f_size)
textWidth, textHeight = textSize(txt)
f_scale = ((h - (9*margin)) / 7) / fontCapHeight()

# min and max weight interpolation values
weight_max = 800
weight_min = 400 + .01 # adding 0.01 because it glitches when at the minimum value

# min and max width interpolation values
width_max = 360
width_min = 100 + 0.01 # adding 0.01 because it glitches when at the minimum value

# sin wave scale
scale = (weight_max - weight_min) / 2

for i in range(frames):
    newPage(w,h)
    frameDuration(frameSpeed)
    
    fill(*color_bg)
    rect(0,0,w,h)
    
    font(f_name, f_size)
    
    phase = 2 * pi * i / frames
    
    amplitude1 = sin(phase-(((0/7)-0.5)*pi))*scale
    amplitude2 = sin(phase-(((1/7)-0.5)*pi))*scale
    amplitude3 = sin(phase-(((2/7)-0.5)*pi))*scale
    amplitude4 = sin(phase-(((3/7)-0.5)*pi))*scale
    amplitude5 = sin(phase-(((4/7)-0.5)*pi))*scale
    amplitude6 = sin(phase-(((5/7)-0.5)*pi))*scale
    amplitude7 = sin(phase-(((6/7)-0.5)*pi))*scale
    
    line1 = FormattedString()
    line1.append("MI", font=f_name, fontSize=f_size*f_scale, fontVariations=dict(wdth=width_min, wght=(amplitude1+weight_min+200)), fill=(color_text))
    line1.append("LA", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    line1.append("NO ", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line1.append("RO", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    line1.append("MA BA", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line1.append("RI", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    textWidth, textHeight = textSize(line1) # only declare once and recycle for text below
    text(line1, (margin, h-(textHeight)), align="left")
    
    line2 = FormattedString()
    line2.append("CA", font=f_name, fontSize=f_size*f_scale, fontVariations=dict(wdth=width_min, wght=(amplitude2+weight_min+200)), fill=(color_highlight))
    line2.append("TANIA BOL", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line2.append("OG", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    line2.append("NA", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    text(line2, (margin, h-(textHeight*2)), align="left")
    
    line3 = FormattedString()
    line3.append("RA", font=f_name, fontSize=f_size*f_scale, fontVariations=dict(wdth=width_min, wght=(amplitude3+weight_min+200)), fill=(color_highlight))
    line3.append("VE", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line3.append("NN", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    line3.append("A PA", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line3.append("DO", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    line3.append("VA", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    text(line3, (margin, h-(textHeight*3)), align="left")

    line4 = FormattedString()
    line4.append("LU", font=f_name, fontSize=f_size*f_scale, fontVariations=dict(wdth=width_min, wght=(amplitude4+weight_min+200)), fill=(color_text))
    line4.append("CC", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    line4.append("A ", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line4.append("TI", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    line4.append("VOLI ", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line4.append("CO", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    line4.append("MO", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    text(line4, (margin, h-(textHeight*4)), align="left")

    line5 = FormattedString()
    line5.append("TR", font=f_name, fontSize=f_size*f_scale, fontVariations=dict(wdth=width_min, wght=(amplitude5+weight_min+200)), fill=(color_text))
    line5.append("EV", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    line5.append("ISO ACIR", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line5.append("EALE", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    text(line5, (margin, h-(textHeight*5)), align="left")

    line6 = FormattedString()
    line6.append("CH", font=f_name, fontSize=f_size*f_scale, fontVariations=dict(wdth=width_min, wght=(amplitude6+weight_min+200)), fill=(color_highlight))
    line6.append("IETI ", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line6.append("A", font=f_name, fontSize=f_size*f_scale, openTypeFeatures=dict(ss03=True),fill=(color_highlight))
    line6.append("PRI", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line6.append("LI", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    line6.append("A ", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line6.append("P", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight), openTypeFeatures=dict(ss02=True))
    line6.append("ISA", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    text(line6, (margin, h-(textHeight*6)), align="left")

    line7 = FormattedString()
    line7.append("LU", font=f_name, fontSize=f_size*f_scale, fontVariations=dict(wdth=width_min, wght=(amplitude7+weight_min+200)), fill=(color_highlight))
    line7.append("CERNA & ME", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    line7.append("SS", font=f_name, fontSize=f_size*f_scale, fill=(color_highlight))
    line7.append("INA", font=f_name, fontSize=f_size*f_scale, fill=(color_text))
    text(line7, (margin, h-(textHeight*7)), align="left")
    
    # add a border around the canvas which "crops" the type the bleeds off the edge
    fill(None)
    stroke(*color_bg)
    strokeWidth(margin*2)
    rect(0,0,w,h)

if saveLight:
    if GIF:
        saveImage("Montecatini-Pro_Ligatures-Wave_Light_01-00.gif")
    else:   
        saveImage("Montecatini-Pro_Ligatures-Wave_Light_01-00.mp4")
else:
    if GIF:
        saveImage("Montecatini-Pro_Ligatures-Wave_Black_01-00.gif")
    else:   
        saveImage("Montecatini-Pro_Ligatures-Wave_Black_01-00.mp4")