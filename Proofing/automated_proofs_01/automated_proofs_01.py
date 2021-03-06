# IMPORTS
import string
import datetime

# --------------------------------------
# FONT INFORMATION

font_name = "Helvetica"
font_version = "0.001"

# --------------------------------------
# DATE & TIME

d = datetime.datetime.today()
current_date = d.strftime('%Y-%m-%d')
current_time = d.strftime('%H:%M')

# --------------------------------------
# PAGE INFORMATION

show_grid = True
show_labels = True

inch = 72

margin = (1/2) * inch
number_of_columns = 12
number_of_rows = 48

newPage("LetterLandscape")

live_width = width() - (margin * 2)
live_height = height() - (margin * 2)

col_width = live_width / number_of_columns
row_height = live_height / number_of_rows

edge_left = 0
edge_right = live_width
edge_top = live_height
edge_bottom = 0


# --------------------------------------
# BASE PAGE FUNCTION

def new_page(section):
    newPage("LetterLandscape")
    
    grid()
    
    metadata(section)
    
    translate(margin, margin)
    
# --------------------------------------
# BASE PAGE FUNCTION

def grid():
    if show_grid == True:
        draw_grid()
    if show_labels == True:
        label_grid()

# --------------------------------------
# META FUNCTIONS

def meta_style():
    fill(0)
    font("Helvetica", 8)

def metadata(section):
    with savedState():
        translate(margin, margin)
        with savedState():
            meta_style()
        
            translate(0, -fontCapHeight())
        
            text(font_name, (edge_left, edge_top), align="left" )
            text("v." + font_version, (x_cord["2"], edge_top), align="left" )
        
            text(section, (x_cord["4"], edge_top), align="left" )
        
            text(current_date, (x_cord[str(number_of_columns - 2)], edge_top), align="right" )
            text(current_time, (x_cord[str(number_of_columns - 1)], edge_top), align="right" )

# --------------------------------------
# DEFINE COORDINATES

x_cord_name_list = list()
x_cord_num_list = list()

y_cord_name_list = list()
y_cord_num_list = list()


x_cord_dict = dict(zip(x_cord_name_list, x_cord_num_list))
zip_x_cords = zip(x_cord_name_list, x_cord_num_list)

y_cord_dict = dict(zip(y_cord_name_list, y_cord_num_list))
zip_y_cords = zip(y_cord_name_list, y_cord_num_list)

with savedState():
    for x in range(number_of_columns + 1):
        
        col_name = str(x)
        x_cord = str(x * col_width)
        
        x_cord_name_list.append(col_name)
        x_cord_num_list.append(float(x_cord))
        
        for y in range(number_of_rows + 1):
            
            row_name = str(y)
            y_cord = str(y * row_height)
            
            y_cord_name_list.append(row_name)
            y_cord_num_list.append(float(y_cord))                
                
# Create a dictionary from zip object
x_cord = dict(zip_x_cords)
y_cord = dict(zip_y_cords)


# --------------------------------------
# DRAW THE GRID

def draw_grid():
    with savedState():
        translate(margin, margin)
        for x in range(number_of_columns):
            for y in range(number_of_rows):
                with savedState():
                    fill(None)
                    stroke(1, 0, 0, 0.1)
                    strokeWidth(0.25)
                    rect(x * col_width, y * row_height, col_width, row_height)
                
# --------------------------------------
# LABEL THE GRID

def label_grid():
    with savedState():
        translate(margin, margin)
    
        fill(1, 0, 0, 0.5)
        font("Helvetica", 8)
    
        for x in range(number_of_columns + 1):
            text(str(x), (x_cord[str(x)], margin / -2), align="center")
        
        translate(0, (-fontCapHeight() / 2))
        for y in range(number_of_rows + 1):
            text(str(y), (margin / -2, y_cord[str(y)]), align="center")

# --------------------------------------
# TITLE PAGE

def title_page(section=""):
    metadata(section)
    with savedState():
        translate(margin, margin)
        font(font_name, 100)
        text(font_name, (edge_left, y_cord["28"]))


# --------------------------------------
# ||||||||||||||||||||||||||||||||||||||
# --------------------------------------
# ||||||||||||||||||||||||||||||||||||||
# --------------------------------------
# ||||||||||||||||||||||||||||||||||||||
# --------------------------------------
# ||||||||||||||||||||||||||||||||||||||
# --------------------------------------
# ||||||||||||||||||||||||||||||||||||||
# --------------------------------------
# ||||||||||||||||||||||||||||||||||||||
# --------------------------------------
# START DRAWING


# --------------------------------------
# CHARACTER SET

# for i in range(3):
#     new_page("Character Set")
    
# --------------------------------------
# SPACING
    
new_page("Spacing")
modifier = 8
y_pos_1 = 40 + modifier
y_pos_2 = y_pos_1 - 2
for i in string.ascii_uppercase:
    while y_pos_2 > 0:
        y_pos_1 -= modifier
        y_pos_2 -= modifier
        
        if y_pos_2 < 0:
            break
        
        print(y_pos_1)
        print(y_pos_2)
        with savedState():
            fill(0)
            for k in range(2):
                txt = "HH" + str(i) + "HHOO" + str(i) + "OO"
                font_size = 48
                font(font_name, font_size)
                textWidth, textHeight = textSize(txt)
            
                text( txt + txt.lower(), (x_cord["0"], y_cord[str(y_pos_1)]) )
                meta_style()
                text( f"{font_size}pt", (x_cord["0"], y_cord[str(y_pos_2)]) )

# for i in range(3):
#     new_page("Spacing")
#     with savedState():
#         textbox_height = 4
#         x, y, w, h = x_cord["0"], y_cord[str(number_of_rows - 3 - textbox_height)], live_width, row_height * textbox_height
#         fill(1, 0, 0, 0.25)
#         rect(x, y, w, h)
#         fill(0)
#         font(font_name, 49)
        
#         txt = "This is a test"
        
#         baseline = textBoxBaselines(txt, (x, y, w, h))
        
#         with savedState():
#             translate(0, (baseline[0][-1] - y) / -2)
#             stroke(0, 0, 1, 0.5)
#             # draw cap height
#             line( (x, baseline[0][-1] + fontAscender()), (w, baseline[0][-1] + fontAscender()) )
#             # draw cap height
#             line( (x, baseline[0][-1] + fontCapHeight()), (w, baseline[0][-1] + fontCapHeight()) )
#             # draw x-height
#             line( (x, baseline[0][-1] + fontXHeight()), (w, baseline[0][-1] + fontXHeight()) )
#             # draw baseline
#             line( (x, baseline[0][-1]), (w, baseline[0][-1]) )
            
#             # draw descender
#             line( (x, baseline[0][-1] + fontDescender()), (w, baseline[0][-1] + fontDescender()) )

#         # baselineShift( y - baseline[0][-1] )
#         baselineShift((baseline[0][-1] - y) / -2)
#         textBox( txt, (x, y, w, h) )






# --------------------------------------
# ADD PAGE NUMBERS AFTER ALL PAGES HAVE BEEN DRAWN 
# (ALWAYS KEEP AT THE BOTTOM)

# get all pages
allPages = pages()

page_number = 0

for page in allPages:
    # each time it loops through, add 1 to the page number
    page_number += 1
    
    # set first page as current context
    if page_number == 1:
        # style first page
        with page:
            grid()
            title_page("")
    else:
        # set next page as current context & add page number
        with page:
            meta_style()
            translate(0, -fontCapHeight())
            text(str(page_number), (edge_right, edge_top), align="right" )
        
        