# IMPORTS
import string
import datetime
from proofbot import *

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

# page size
page_size = "LetterLandscape"
page_width, page_height = sizes(paperSize=page_size)

# unit of measurement
inch = 72

# margin
margin = (1/2) * inch

# safe area
live_width = page_width - (margin * 2)
live_height = page_height - (margin * 2)

# columns & rows
number_of_columns = 12
number_of_rows = 48

col_width = live_width / number_of_columns
row_height = live_height / number_of_rows

# edges
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
# TITLE PAGE

def title_page():
    with savedState():
        font(font_name, 100)
        text(font_name, (edge_left, y_cord["28"]))
    
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


# --------------------------------------
# TITLE PAGE

new_page("")
title_page()

# --------------------------------------
# CHARACTER SET

# for i in range(3):
#     new_page("Character Set")
    
# --------------------------------------
# SPACING
    
new_page("Spacing")
text(numbers.pi1000.pi1000(50), (0, 0))






# --------------------------------------
# ADD PAGE NUMBERS AFTER ALL PAGES HAVE BEEN DRAWN 
# (ALWAYS KEEP AT THE BOTTOM)

# get all pages
allPages = pages()

page_number = 0

for page in allPages:
    # each time it loops through, add 1 to the page number
    page_number += 1
    
    # set second page as current context
    if page_number != 1:
        # set next page as current context & add page number
        with page:
            meta_style()
            translate(0, -fontCapHeight())
            text("pg. " + str(page_number), (edge_right, edge_top), align="right" )
        
        