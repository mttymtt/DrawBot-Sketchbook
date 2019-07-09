size('Letter')
inch = 72
margin = (1 / 2) * inch
col_num = 12
col_gap = (1 / 4) * inch
col_width = ((( width() - (margin * 2) ) - ( col_gap * (col_num - 1) )) / col_num)

def columns():
    stroke(None)
    fill(1,0,0,0.2)
    translate( (margin + col_width), 0)
    for i in range((col_num - 1)):
        rect( (i * (col_width + col_gap)), margin, col_gap, (height() - (margin * 2)) )

def new_page():
    stroke(1,0,0)
    strokeWidth(1)
    fill(None)
    rect(margin, margin, (width() - (margin*2)), (height() - (margin * 2)) )
    
    #Draw columns on each page
    columns()
    
new_page()