inch = 72

newPage("Letter")

margin = (1) * inch
gutter = (1 / 8) * inch
window_count = 6
color_threshold = window_count / 0.25
print(color_threshold)
window_width = (width() - ((margin * 2) + gutter * (window_count - 1))) / window_count
window_height = (height() - (margin * 2))

translate(margin, margin)
for x in range(window_count):
    fill(None)
    cmykLinearGradient(
        ( (window_width * x), margin ),    # startPoint
        ( (window_width * x) + window_width, (height() - margin) ),    # endPoint
        [(x / (color_threshold * 2), 0.1 + x / (color_threshold * 2), x / (color_threshold), 0), (x / (color_threshold), 0, x / (color_threshold * 2), 0)],    # colors
        [0, 1]    # locations
        )
    rect(((window_width + gutter) * x), 0, window_width, window_height)
    
fill(1, 1, 1)
oval(randint(0, width() - margin), randint(0, height() - (margin*2)), 100, 100)