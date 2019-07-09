inch = 72
margin = (1 / 2) * inch * 2
grid_col = (1 / 4) * inch
grid_interval = 2

def grid():
    stroke(None)
    fill(1,0,0,0.2)
    for i in range(0, width(), grid_interval):
        rect((i*grid_col), margin/2, grid_col, height()-margin)

def new_page():
    size('Letter')
    stroke(1,0,0)
    strokeWidth(1)
    fill(None)
    rect(margin/2, margin/2, width()-margin, height()-margin)
    
    grid()
    
new_page()
print(sizes())