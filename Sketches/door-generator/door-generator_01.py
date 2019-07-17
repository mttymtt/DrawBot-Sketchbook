import os

# FILENAME
basename = os.path.splitext(os.path.basename(__file__))[0]
file_detail = "single"
version = "01"
format = ".png"
if file_detail != "":
    filename = basename + "_" + file_detail + "_" + version + format
else:
    filename = basename + "-" + version + format

export = False

# START ACTUALLY DOING STUFF

newPage("Letter")
inch = 72

door_width = width() / 3
door_height = door_width * 2.25
door_margin = door_width / 8

# Colors
C, M, Y, K = 100, 100, 100, 100
color_gold = [10/C, 20/M, 80/Y, 17/K]
color_black = [0/C, 0/M, 0/Y, 100/K]
color_red = [0/C, 100/M, 100/Y, 20/K]

# Define colors
color_accent = color_gold
color_door = color_red

# Door background
with savedState():
    cmykFill(*color_door)
    rect(0, 0, door_width, door_height)

# Door handle
with savedState():
    cmykFill(*color_accent)
    handle_size = (door_width / 10)
    oval(door_margin - (handle_size / 2), ((door_height / 2) - handle_size - (door_margin / 2)), handle_size, handle_size)

# Door number
with savedState():
    font_options = ["Bayside", "Indicia", "Redbird", "Strasse", "Trafalgar", "ValutaSolid"]
    font_name = "Numbers " + str(choice(font_options))
    
    door_number = str(randint(100, 999))
    
    cmykFill(*color_accent)
    font(font_name, door_width / 12)
    tracking(2)
    text(door_number, (door_width / 2, door_height - 20), align="center")

# # Door window
# with savedState():
#     window_width = door_width - (door_margin * 2)
#     window_height = (door_height / 2) - (door_margin * 2)
#     cmykFill(*color_black)
#     rect( ((door_width - window_width) / 2), (door_height - window_height - (door_margin)), window_width, window_height)

# Door window
with savedState():
    window_gap = door_margin / 4
    number_of_windows_across = randint(1, 3)
    number_of_windows_down = randint(1, 4)
    print(number_of_windows_across)
    print(number_of_windows_down)
    window_width = ((door_width - (door_margin * 2) - (window_gap * (number_of_windows_across - 1))) / number_of_windows_across)
    window_height = ((door_height / 2) - (door_margin) - (window_gap * (number_of_windows_down - 1))) / number_of_windows_down
    
    translate(door_margin, door_height - ((door_height / 2) - (door_margin)) - door_margin )
    cmykFill(*color_black)
    for x in range(number_of_windows_across):
        for y in range(number_of_windows_down):
            rect( x * (window_width + window_gap), y * (window_height + window_gap), window_width, window_height)

# Door mailslot
with savedState():
    mail_width = door_width / 3.5
    mail_height = mail_width / 3
    cmykFill(*color_accent)
    rect( ((door_width - mail_width) / 2), ((door_height - (mail_height * 3)) / 2), mail_width, mail_height)
    
# Door bottom detail
with savedState():
    window_gap = door_margin / 4
    number_of_windows_across = randint(1, 3)
    number_of_windows_down = randint(1, 4)
    print(number_of_windows_across)
    print(number_of_windows_down)
    window_width = ((door_width - (door_margin * 2) - (window_gap * (number_of_windows_across - 1))) / number_of_windows_across)
    window_height = ((door_height / 2) - (door_margin * 3) - (window_gap * (number_of_windows_down - 1))) / number_of_windows_down
    
    translate(door_margin, door_margin )
    cmykFill(None)
    stroke(0, 0, 0, 0.1)
    strokeWidth(5)
    for x in range(number_of_windows_across):
        for y in range(number_of_windows_down):
            # rect( x * (window_width + window_gap), y * (window_height + window_gap), window_width, window_height)
            rect( x * (window_width + window_gap), y * (window_height + window_gap), window_width, window_height)
            
if export == True:
    saveImage(filename)