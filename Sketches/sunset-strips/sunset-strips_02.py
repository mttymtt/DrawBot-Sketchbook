inch = 72

newPage("Letter")

margin = (1) * inch
window_count = 6
color_threshold = window_count / 0.25
print(color_threshold)
window_width = (width() - (margin * 2)) / window_count
window_height = (height() - (margin * 2))

translate(margin, margin)
for x in range(window_count):
    fill(None)
    cmykLinearGradient(
        ( (window_width * x), 0 ),    # startPoint
        ( (window_width * x) + window_width, 0 ),    # endPoint
        [(0.2 - (x / (color_threshold)), 0.1 + x / (color_threshold * 2), x / (color_threshold), 0), (x / (color_threshold), 0, x / (color_threshold * 6), 0)],    # colors
        [0, 1]    # locations
        )
    # cmykFill(x / 6, 0, 1, 0)
    rect((window_width * x), 0, window_width, window_height)