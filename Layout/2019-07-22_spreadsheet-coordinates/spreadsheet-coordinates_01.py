# IMPORTS
import datetime

# --------------------------------------
# FONT INFORMATION

font_name = "Font Name"
font_version = "0.001"

# --------------------------------------
# DATE & TIME

d = datetime.datetime.today()
current_date = d.strftime('%Y-%m-%d')
current_time = d.strftime('%H:%M')

# --------------------------------------
# PAGE INFORMATION

inch = 72

margin = (1/2) * inch
number_of_columns = 12
number_of_rows = 36

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

def new_page():
    newPage("LetterLandscape")
    
    # eventually make these toggle-able
    draw_grid()
    label_grid()
    
    metadata()

# --------------------------------------
# META FUNCTIONS

def meta_style():
    fill(0)
    font("Helvetica", 8)

def metadata():
    translate(margin, margin)
    with savedState():
        meta_style()
        
        translate(0, -fontCapHeight())
        
        text(font_name, (edge_left, edge_top), align="left" )
        text("Version: " + font_version, (x_cord["2"], edge_top), align="left" )
        
        text("Chapter", (x_cord["4"], edge_top), align="left" )
        
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

for i in range(3):
    new_page()








# --------------------------------------
# ADD PAGE NUMBERS AFTER (ALWAYS KEEP AT BOTTOM)

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
            draw_grid()
            label_grid()
    else:
        # set next page as current context & add page number
        with page:
            meta_style()
            translate(0, -fontCapHeight())
            text(str(page_number), (edge_right, edge_top), align="right" )
        
        