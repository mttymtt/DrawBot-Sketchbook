txt = "Howdy!"
newtxt = ""

# for char in txt:
#     newPage(500, 500)
    
#     newtxt += char
#     font("Blanco", 80)
#     text(newtxt, (10, 250))

myText = "Wow, look how neat!"

for i, char in enumerate(txt):
    print(i, char)
    
    newPage(500, 500)
    
    newtxt += char
    f_txt = FormattedString()
    f_txt.append(newtxt, font="Blanco Italic", fontSize=80)
    
    text(f_txt, (10, 250))

saveImage("05_typewriter.gif")