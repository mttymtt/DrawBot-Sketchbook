txt = "Howdy, Partner!"
newtxt = ""

# for char in txt:
#     newPage(500, 500)
    
#     newtxt += char
#     font("Blanco", 80)
#     text(newtxt, (10, 250))

for i, char in enumerate(txt):
    print(i, char)
    
    percent = i / (len(txt) - 1)
    
    newPage(800, 500)
    fill(1)
    rect(0, 0, width(), height())
    
    # append each character to a new txt variable
    newtxt += char
    # start to format that text collected
    f_txt = FormattedString()
    f_txt.append(
        newtxt, 
        font="Blanco Italic", 
        fontSize=80,
        baselineShift=randint(0, 10),
        cmykFill=(1, percent, 0, 0)
        )
    
    text(f_txt, (10, 250))

saveImage("06_typewriter.gif")