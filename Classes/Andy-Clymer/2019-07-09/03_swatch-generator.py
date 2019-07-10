newPage("Letter")

color = [0, 0, 0, 0]
# Redefine colors:
color[randint(0,1)] = randint(0,10)/100
color[randint(0,2)] = random()

boxSize = width() / 5
padding = 20

translate(padding, padding)
for x in range(0, width(), round(boxSize + padding)):
    for y in range(0, height(), round(boxSize + padding)):
        # Randomize color a little
        color[randint(0,2)] = random()
        # Set fill
        cmykFill(*color)
        oval(x, y, boxSize, boxSize)
        
        # Make a copy of the original color
        secondaryColor = color.copy() # A list knows how to copy itself
        secondaryColor[randint(0,2)] = randint(0,10)/100
        cmykFill(*secondaryColor)
        rect(x, y, boxSize/2, boxSize/2)
        # Show color value as text
        # Turn the color list into a string
        colorName = "C:" + str(round(color[0] * 100))
        colorName += " M:" + str(round(color[1] * 100))
        colorName += " Y:" + str(round(color[2] * 100))
        colorName += " K:" + str(round(color[3] * 100))
        colorName += "\r" + "C:" + str(round(secondaryColor[0] * 100))
        colorName += " M:" + str(round(secondaryColor[1] * 100))
        colorName += " Y:" + str(round(secondaryColor[2] * 100))
        colorName += " K:" + str(round(secondaryColor[3] * 100))
        fill(0)
        font("Obviously-Regular", padding/2)
        text(colorName, (x, y - 10))        
        # # Make a copy of the original color
        # thirdColor = color.copy()
        # thirdColor[randint(0,2)] = randint(0,10)/100
        # cmykFill(*thirdColor)
        # rect(x+(boxSize/2), y+(boxSize/2), boxSize/2, boxSize/2)