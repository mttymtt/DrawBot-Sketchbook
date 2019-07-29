# IMPORTS
import string
import datetime
# from proofbot.numbers import pi1000
from proofbot import numbers
from proofbot import spacing

# --------------------------------------
#    FONT INFORMATION

font_name = "Helvetica"
font_version = "0.001"

# --------------------------------------
#    DATE & TIME

d = datetime.datetime.today()
current_date = d.strftime('%Y-%m-%d')
current_time = d.strftime('%H:%M')

# --------------------------------------
#    PAGE INFORMATION

show_grid = True
show_labels = True

# page size
page_size = "LetterLandscape"
page_width, page_height = sizes(paperSize=page_size)

# unit of measurement
inch = 72

# margin
margin = (1/2) * inch
half_margin = margin / 2

# general area
margin_width = page_width - (margin * 2)
margin_height = page_height - (margin * 2)

# safe area
live_width = margin_width
live_height = margin_height - margin


# columns & rows
number_of_columns = 12
number_of_rows = 48

gutter = (1/2) * inch

col_width = (live_width - (number_of_columns - 1) * gutter) / number_of_columns
row_height = live_height / number_of_rows

col_span = col_width + gutter # write (col_span * 2) to span two columns

# edges
edge_left = 0
edge_right = live_width
edge_top = margin_height
edge_bottom = 0

# live area top
live_top = live_height


# --------------------------------------
#    BASE PAGE FUNCTION

def new_page(section):
    newPage("LetterLandscape")
    
    grid()
    
    metadata(section)
    
    translate(margin, margin)
    
# --------------------------------------
#    TITLE PAGE

def title_page():
    with savedState():
        font(font_name, 100)
        text(font_name, (edge_left, y_cord["28"]))
    
# --------------------------------------
#    BASE PAGE FUNCTION

def grid():
    if show_grid == True:
        draw_grid()
    if show_labels == True:
        label_grid()

# --------------------------------------
#    META FUNCTIONS

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
        
            text(current_date, (x_cord[str(number_of_columns - 2)] - half_margin, edge_top), align="right" )
            text(current_time, (x_cord[str(number_of_columns - 1)] - half_margin, edge_top), align="right" )

# --------------------------------------
#    DEFINE COORDINATES

x_cord_name_list = list()
x_cord_num_list = list()

y_cord_name_list = list()
y_cord_num_list = list()


x_cord_dict = dict(zip(x_cord_name_list, x_cord_num_list))
zip_x_cords = zip(x_cord_name_list, x_cord_num_list)

y_cord_dict = dict(zip(y_cord_name_list, y_cord_num_list))
zip_y_cords = zip(y_cord_name_list, y_cord_num_list)

for x in range(number_of_columns):
    col_name = str(x)
    x_cord = str(x * col_width + (gutter * x))
    
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

print(x_cord)

# --------------------------------------
#    DEFINE COLUMN SPANS & OFFSETS
#    write col_span[4] to span four columns
#    write offset[4] to offset four columns

col_span = list()
for x in range(number_of_columns + 1):
    col_span_width = ((col_width + gutter) * x) - (gutter)
    col_span.append(int(col_span_width))


offset = list()
for x in range(number_of_columns + 1):
    offset_width = ((col_width + gutter) * x)
    offset.append(int(offset_width))


# --------------------------------------
#    DRAW THE GRID

def draw_grid():
    with savedState():
        translate(margin, margin)
        for x in range(number_of_columns):
            # for y in range(number_of_rows):
            with savedState():
                fill(None)
                fill(1, 0, 0, 0.05)
                rect(x * col_width + (gutter * x), edge_bottom, col_width, live_height)
                
# --------------------------------------
#    LABEL THE GRID

def label_grid():
    with savedState():
        translate(margin, margin)
    
        fill(1, 0, 0, 0.5)
        font("Helvetica", 8)
    
        for x in range(number_of_columns):
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
#    START DRAWING


# --------------------------------------
#    TITLE PAGE

new_page("")
title_page()

# --------------------------------------
#    CHARACTER SET

# for i in range(3):
#     new_page("Character Set")
    
# --------------------------------------
#    SPACING
    
section = "Spacing"
    
new_page(section)
with savedState():
    fontSize(24)
    textBox(spacing.OHno(), (0, 0, col_span[6], live_height))
    fontSize(36)
    textBox(spacing.OHno("no", "string"), (offset[6], 0, col_span[6], live_height))
    
# --------------------------------------
#    NUMBERS

section = "Numbers"

new_page(section)
with savedState():
    fontSize(48)
    textBox(numbers.pi1000(), (0, 0, col_span[6], live_height))
    textBox(numbers.n111(), (offset[6], 0, col_span[6], live_height))

flow = numbers.pi1000()
while len(flow) > 0:
    new_page(section)
    fontSize(36)
    flow = textBox(flow, (0, 0, col_span[6], live_height))
    flow = textBox(flow, (offset[6], 0, col_span[6], live_height))
    
# --------------------------------------
#    CONTEXT

section = "Context"

flow = numbers.pi1000()
while len(flow) > 0:
    new_page(section)
    fontSize(18)
    flow = textBox(flow, (offset[0], 0, col_span[4], live_height))
    flow = textBox(flow, (offset[4], 0, col_span[4], live_height))
    flow = textBox(flow, (offset[8], 0, col_span[4], live_height))



# --------------------------------------
#    ADD PAGE NUMBERS AFTER ALL PAGES HAVE BEEN DRAWN 
#    (ALWAYS KEEP AT THE BOTTOM)

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
        
         