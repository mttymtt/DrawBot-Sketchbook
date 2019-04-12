# Please note, this file is set up for a variable font version of Montecatini Pro which is not available commercially at the moment. You can adopt this code for another variable font that you have purchased.

# True = Animated
# False = Static(Easier to set up the design before making the animation)
animated = True

# True = Makes frame speed longer (mp4)
# False = Makes frame speed shorter (gif)
video = False

# True = Light Version
# False = Dark Version
light = False

# Only applicable in the light version
# True = Black line appears to "fill" the gray lines and is hidden in the gutters
# False = Black line moves over the gutters between columns
hide = False

#-----------------------------------

if animated:
    phaseDuration = 6
    pause = 12
else:
    phaseDuration = 1
    pause = 1
    
# How long a single frame lasts (represented as a second)
if video:
    frameSpeed = 0.075
    GIF = False # Saves mp4
else:
    frameSpeed = 0.01
    GIF = True # Saves gif

# width and height of canvas
w, h = (1080, 1080)

# margin of canvas
margin = 40

# stroke weight
strokeWeight = 2

#colors
R = 255
G = 255
B = 255

# red = [185/R, 24/G, 29/B] #deeper red
red = [208/R, 84/G, 69/B] #lighter red
white = [1, 1, 1]
gray = [0.7, 0.7, 0.7]
darkGray = [70/R, 70/G, 70/B]
black = [0, 0, 0]

if light:
    color_bg = white
    color_weights = red
    color_widths = darkGray
    color_underlineActive = darkGray
    color_underlineInactive = gray
    saveLight = True
else:
    color_bg = black
    color_weights = white
    color_widths = white
    color_underlineActive = white
    color_underlineInactive = black
    saveLight = False

# font stuff
f_name = "Montecatini VAR"
f_size = 160

stretto_max = 164
stretto_min = 100.01

normale_max = 261
normale_min = 164

ampio_max = 360
ampio_min = 261

largo_max = 360

stretto_scale = (stretto_max-stretto_min)/2
normale_scale = (normale_max-normale_min)/2
ampio_scale = (ampio_max-ampio_min)/2
largo_scale = (largo_max-stretto_min)/2

# calculate a scale factor to resize the font to fit 1/6th of the height
txt = 'TEST'
font(f_name)
fontSize(f_size)
textWidth, textHeight = textSize(txt)
f_scale = ((h-(7*margin))/6) / textHeight

def pagePresets():
    newPage(w,h)
    frameDuration(frameSpeed)
    
    fill(*color_bg)
    rect(0,0,w,h)

def drawWeights():
    # only declare once and recycle for text below
    textWidth, textHeight = textSize(light)

    #actually draw the type
    text(light, (margin, margin+(textHeight*5)), align="left")

    text(regular, (margin, margin+(textHeight*4)), align="left")

    text(medium, (margin, margin+(textHeight*3)), align="left")

    text(semibold, (margin, margin+(textHeight*2)), align="left")

    text(bold, (margin, margin+(textHeight)), align="left")

    text(ultra, (margin, margin), align="left")

def drawWidths():
    fill(*color_widths)
    font("Josefin Sans Semibold", 21)
    tracking(4)
    textWidth, textHeight = textSize("Stretto")
    text("STRETTO", (margin, h-(margin+(textHeight*1))), align="left")

    textWidth, textHeight = textSize("Stretto")
    text("NORMALE", (((w-margin)/4)*1+margin, h-(margin+(textHeight*1))), align="left")

    textWidth, textHeight = textSize("Stretto")
    text("AMPIO", (((w-margin)/4)*2+margin, h-(margin+(textHeight*1))), align="left")

    textWidth, textHeight = textSize("Stretto")
    text("LARGO", (((w-margin)/4)*3+margin, h-(margin+(textHeight*1))), align="left")

def drawUnderline():
    offset = ((w-(margin*2)-(margin*3))/4)+margin

    fill(*color_underlineInactive)
    rect(margin, h-(margin*2), ((w-(margin*2)-(margin*3))/4), strokeWeight)
    rect(margin+offset, h-(margin*2), ((w-(margin*2)-(margin*3))/4), strokeWeight)
    rect(margin+(offset*2), h-(margin*2), ((w-(margin*2)-(margin*3))/4), strokeWeight)
    rect(margin+(offset*3), h-(margin*2), ((w-(margin*2)-(margin*3))/4), strokeWeight)

    fill(*color_underlineActive)
    rect(margin+translate, h-(margin*2), ((w-(margin*2)-(margin*3))/4), strokeWeight)
    
    if hide:
        fill(*color_bg)
    else:
        fill(None)
    rect(offset, (h-(margin*2)-(strokeWeight/2)), margin, strokeWeight*2)
    rect(offset*2, h-(margin*2), margin, strokeWeight*2)
    rect(offset*3, h-(margin*2), margin, strokeWeight*2)



#-----------------------------------
# STRETTO -> NORMALE
#-----------------------------------

for i in range(phaseDuration):
    pagePresets()
    
    # format lines of type
    phase = 2 * pi/2 * i / phaseDuration
    amplitude = sin(phase-((-1.5)*pi))*stretto_scale
    light = FormattedString()
    light.append("Light", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((stretto_max-stretto_min)/2), wght=400.01), fill=(color_weights))

    regular = FormattedString()
    regular.append("Regular", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((stretto_max-stretto_min)/2), wght=470), fill=(color_weights))

    medium = FormattedString()
    medium.append("Medium", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((stretto_max-stretto_min)/2), wght=510), fill=(color_weights))

    semibold = FormattedString()
    semibold.append("SemiBold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((stretto_max-stretto_min)/2), wght=590), fill=(color_weights))

    bold = FormattedString()
    bold.append("Bold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((stretto_max-stretto_min)/2), wght=650), fill=(color_weights))

    ultra = FormattedString()
    ultra.append("Ultra", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((stretto_max-stretto_min)/2), wght=800), fill=(color_weights))
    
    translate = ( (((w-(margin*2)-(margin*3))/4)+margin) * ((amplitude+stretto_min+((stretto_max-stretto_min)/2))-stretto_min)/(stretto_max-stretto_min) )
        
    drawWeights()
    drawWidths()
    drawUnderline()
#-----------------------------------
# NORMALE PAUSE
#-----------------------------------
        
for i in range(pause):
    pagePresets()
    
    light = FormattedString()
    light.append("Light", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_max, wght=400.01), fill=(color_weights))

    regular = FormattedString()
    regular.append("Regular", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_max, wght=470), fill=(color_weights))

    medium = FormattedString()
    medium.append("Medium", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_max, wght=510), fill=(color_weights))

    semibold = FormattedString()
    semibold.append("SemiBold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_max, wght=590), fill=(color_weights))

    bold = FormattedString()
    bold.append("Bold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_max, wght=650), fill=(color_weights))

    ultra = FormattedString()
    ultra.append("Ultra", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_max, wght=800), fill=(color_weights))
    
    translate = ( (((w-(margin*2)-(margin*3))/4)+margin) * 1 )
    
    drawWeights()
    drawWidths()
    drawUnderline()
        
#-----------------------------------
# NORMALE -> AMPIO
#-----------------------------------
        
for i in range(phaseDuration):
    pagePresets()
    
    phase = 2 * pi/2 * i / phaseDuration
    amplitude = sin(phase-((-1.5)*pi))*normale_scale
    light = FormattedString()
    light.append("Light", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+normale_min+((normale_max-normale_min)/2), wght=400.01), fill=(color_weights))

    regular = FormattedString()
    regular.append("Regular", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+normale_min+((normale_max-normale_min)/2), wght=470), fill=(color_weights))

    medium = FormattedString()
    medium.append("Medium", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+normale_min+((normale_max-normale_min)/2), wght=510), fill=(color_weights))

    semibold = FormattedString()
    semibold.append("SemiBold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+normale_min+((normale_max-normale_min)/2), wght=590), fill=(color_weights))

    bold = FormattedString()
    bold.append("Bold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+normale_min+((normale_max-normale_min)/2), wght=650), fill=(color_weights))

    ultra = FormattedString()
    ultra.append("Ultra", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+normale_min+((normale_max-normale_min)/2), wght=800), fill=(color_weights))
    
    translate = (((w-(margin*2)-(margin*3))/4)+margin) + ( (((w-(margin*2)-(margin*3))/4)+margin) * ((amplitude+normale_min+((normale_max-normale_min)/2))-normale_min)/(normale_max-normale_min) )
    
    drawWeights()
    drawWidths()
    drawUnderline()
        
#-----------------------------------
# AMPIO PAUSE
#-----------------------------------
        
for i in range(pause):
    pagePresets()
        
    light = FormattedString()
    light.append("Light", font=f_name, fontSize=f_size, fontVariations=dict(wdth=normale_max, wght=400.01), fill=(color_weights))

    regular = FormattedString()
    regular.append("Regular", font=f_name, fontSize=f_size, fontVariations=dict(wdth=normale_max, wght=470), fill=(color_weights))

    medium = FormattedString()
    medium.append("Medium", font=f_name, fontSize=f_size, fontVariations=dict(wdth=normale_max, wght=510), fill=(color_weights))

    semibold = FormattedString()
    semibold.append("SemiBold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=normale_max, wght=590), fill=(color_weights))

    bold = FormattedString()
    bold.append("Bold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=normale_max, wght=650), fill=(color_weights))

    ultra = FormattedString()
    ultra.append("Ultra", font=f_name, fontSize=f_size, fontVariations=dict(wdth=normale_max, wght=800), fill=(color_weights))
    
    translate = ( ((((w-(margin*2)-(margin*3))/4)+margin)*2) )
    
    drawWeights()
    drawWidths()
    drawUnderline()
        
#-----------------------------------
# AMPIO -> LARGO
#-----------------------------------
        
for i in range(phaseDuration):
    pagePresets()
        
    phase = 2 * pi/2 * i / phaseDuration
    amplitude = sin(phase-((-1.5)*pi))*ampio_scale
    # print(amplitude+ampio_min+((ampio_max-ampio_min)/2))
    light = FormattedString()
    light.append("Light", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+ampio_min+((ampio_max-ampio_min)/2), wght=400.01), fill=(color_weights))

    regular = FormattedString()
    regular.append("Regular", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+ampio_min+((ampio_max-ampio_min)/2), wght=470), fill=(color_weights))

    medium = FormattedString()
    medium.append("Medium", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+ampio_min+((ampio_max-ampio_min)/2), wght=510), fill=(color_weights))

    semibold = FormattedString()
    semibold.append("SemiBold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+ampio_min+((ampio_max-ampio_min)/2), wght=590), fill=(color_weights))

    bold = FormattedString()
    bold.append("Bold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+ampio_min+((ampio_max-ampio_min)/2), wght=650), fill=(color_weights))

    ultra = FormattedString()
    ultra.append("Ultra", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+ampio_min+((ampio_max-ampio_min)/2), wght=800), fill=(color_weights))
    
    translate = (((w-(margin*2)-(margin*3))/4)+margin)*2 + ( (((w-(margin*2)-(margin*3))/4)+margin) * ((amplitude+ampio_min+((ampio_max-ampio_min)/2))-ampio_min)/(ampio_max-ampio_min) )
    
    drawWeights()
    drawWidths()
    drawUnderline()
        
#-----------------------------------
# LARGO PAUSE
#-----------------------------------
        
for i in range(pause):
    pagePresets()
        
    light = FormattedString()
    light.append("Light", font=f_name, fontSize=f_size, fontVariations=dict(wdth=ampio_max, wght=400.01), fill=(color_weights))

    regular = FormattedString()
    regular.append("Regular", font=f_name, fontSize=f_size, fontVariations=dict(wdth=ampio_max, wght=470), fill=(color_weights))

    medium = FormattedString()
    medium.append("Medium", font=f_name, fontSize=f_size, fontVariations=dict(wdth=ampio_max, wght=510), fill=(color_weights))

    semibold = FormattedString()
    semibold.append("SemiBold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=ampio_max, wght=590), fill=(color_weights))

    bold = FormattedString()
    bold.append("Bold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=ampio_max, wght=650), fill=(color_weights))

    ultra = FormattedString()
    ultra.append("Ultra", font=f_name, fontSize=f_size, fontVariations=dict(wdth=ampio_max, wght=800), fill=(color_weights))
    
    translate = ( ((((w-(margin*2)-(margin*3))/4)+margin)*3) )
    
    drawWeights()
    drawWidths()
    drawUnderline()
        
#-----------------------------------
# LARGO -> STRETTO
#-----------------------------------
        
for i in range(phaseDuration):
    pagePresets()
        
    phase = 2 * pi/2 * i / phaseDuration
    amplitude = sin(phase-((-0.5)*pi))*largo_scale
    light = FormattedString()
    light.append("Light", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((largo_max-stretto_min)/2), wght=400.01), fill=(color_weights))

    regular = FormattedString()
    regular.append("Regular", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((largo_max-stretto_min)/2), wght=470), fill=(color_weights))

    medium = FormattedString()
    medium.append("Medium", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((largo_max-stretto_min)/2), wght=510), fill=(color_weights))

    semibold = FormattedString()
    semibold.append("SemiBold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((largo_max-stretto_min)/2), wght=590), fill=(color_weights))

    bold = FormattedString()
    bold.append("Bold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((largo_max-stretto_min)/2), wght=650), fill=(color_weights))

    ultra = FormattedString()
    ultra.append("Ultra", font=f_name, fontSize=f_size, fontVariations=dict(wdth=amplitude+stretto_min+((largo_max-stretto_min)/2), wght=800), fill=(color_weights))
    
    translate = ((((w-(margin*2)-(margin*3))/4)+margin)*3) * (((amplitude+stretto_min+((largo_max-stretto_min)/2))-stretto_min)/(largo_max-stretto_min))
    
    drawWeights()
    drawWidths()
    drawUnderline()
        
#-----------------------------------
# STRETTO PAUSE
#-----------------------------------
        
for i in range(pause):
    pagePresets()
        
    light = FormattedString()
    light.append("Light", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_min, wght=400.01), fill=(color_weights))

    regular = FormattedString()
    regular.append("Regular", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_min, wght=470), fill=(color_weights))

    medium = FormattedString()
    medium.append("Medium", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_min, wght=510), fill=(color_weights))

    semibold = FormattedString()
    semibold.append("SemiBold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_min, wght=590), fill=(color_weights))

    bold = FormattedString()
    bold.append("Bold", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_min, wght=650), fill=(color_weights))

    ultra = FormattedString()
    ultra.append("Ultra", font=f_name, fontSize=f_size, fontVariations=dict(wdth=stretto_min, wght=800), fill=(color_weights))
    
    translate = ( (((w-(margin*2)-(margin*3))/4)+margin) * 0 )
    
    drawWeights()
    drawWidths()
    drawUnderline()

if saveLight:
    if GIF:
        saveImage("Montecatini-Pro_Widths-Slider_Light_01-00.gif")
    else:   
        saveImage("Montecatini-Pro_Widths-Slider_Light_01-00.mp4")
else:
    if GIF:
        saveImage("Montecatini-Pro_Widths-Slider_Black_01-00.gif")
    else:   
        saveImage("Montecatini-Pro_Widths-Slider_Black_01-00.mp4")