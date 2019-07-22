# ADMIN

import string
 
# Date & Time
import datetime
d = datetime.datetime.today()
current_date = d.strftime('%Y-%m-%d')
current_time = d.strftime('%H:%M')

# --------------------------------------

metadata = current_date + " " + current_time

# --------------------------------------

inch = 72

margin = (1) * inch

def metadata(x_cord, y_cord):
    with savedState():
        font("Blanco", 10)
        text(current_date, (x_cord, y_cord))
        # text(current_time, (y_cord, y_cord))

newPage("LetterLandscape")

live_width = width() - (margin * 2)
live_height = height() - (margin * 2)

col_width = live_width / 12
row_height = live_height / 20

def col_letters(num):
    letters = ""
    while num:
        mod = (num - 1) % 26
        letters += chr(mod + 65)
        num = (num - 1) // 26
    return "".join(reversed(letters))

cord_name_list = list()
cord_num_list = list()

cord_dict = dict(zip(cord_name_list, cord_num_list))

zip_cords = zip(cord_name_list, cord_num_list)

with savedState():
    translate(margin, margin)
    # for col_letter in list(string.ascii_lowercase):
    for x in range(int(live_width / col_width)):
        
        col_num = str(col_letters(x+1))
        x_cord = str(x * col_width)
        
        for y in range(int(live_height / row_height)):
            
            row_num = str(y)
            y_cord = str(y * row_height)
            
            with savedState():
                fill(None)
                stroke(1,0,0)
                strokeWidth(1)
                rect(x * col_width, y * row_height, col_width, row_height)
                
                cord_name = col_num + row_num
                print(cord_name)
                cord_num = float(x_cord), float(y_cord)
                print(cord_num)
                
                cord_name_list.append(cord_name)
                cord_num_list.append(cord_num)
                
# Create a dictionary from zip object
cord = dict(zip_cords)

print(cord["A1"])

translate(margin, margin)
fill(0, 0, 1)
text("Hello", cord["A12"] )