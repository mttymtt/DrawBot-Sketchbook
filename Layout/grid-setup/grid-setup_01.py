import os

# FILENAME
basename = os.path.splitext(os.path.basename(__file__))[0]
name_detail = "12-col_12-baseline"
version = "01"
format = ".pdf"
filename = basename + "_" + name_detail + "_" + version + format

# Document Setup
newPage('Letter')
inch = 72
margin = (1 / 2) * inch
height_live = height() - (margin * 2) # height of live area

# Columns
col_num = 9
col_gap = (1 / 4) * inch
col_width = ((( width() - (margin * 2) ) - ( col_gap * (col_num - 1) )) / col_num)

# Baseline Grid
baseline_unit = 10
print(height_live / baseline_unit) # check if baseline unit fits nicely into live height

def columns():
    with savedState():
        fill(1,0,0,0.2)
        translate( (margin + col_width), 0)
        for i in range((col_num - 1)):
            rect( (i * (col_width + col_gap)), margin, col_gap, (height() - (margin * 2)) )
        
def baseline():
    with savedState():
        stroke(0,0,1,0.2)
        strokeWidth(1)
        # shift baseline to start at the top of margin
        translate(0, (height() - margin))
                        # be specific in making it an integer rather than a float (float = # with decimal)
        for i in range(0, int(height() - (margin * 2)), baseline_unit):
            line( (margin, -i), ((width() - margin), -i) ) # Negative i value so that the baseline 
                                                           # starts from the top rather than the bottom
def new_page():
    with savedState():
        stroke(1,0,0)
        strokeWidth(1)
        fill(None)
        rect(margin, margin, (width() - (margin*2)), (height() - (margin * 2)) )
    
    # Draw columns on each page
    columns()
    
    # Draw baseline grid on each page
    baseline()
    
    font("Times-Italic", 100)
    text("Headline", (margin, margin))
    
new_page()

# saveImage(filename)