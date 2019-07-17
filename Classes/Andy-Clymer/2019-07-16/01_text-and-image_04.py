import os

def draw_page(image_path):
    newPage("LetterLandscape")
    inch = 72
    margin = (3 / 4) * inch

    image_width, image_height = imageSize(image_path)
    scale_factor = (height() - (margin * 2)) / image_height

    flower_name = filename_plain

    fontSize(30)
    with savedState():
        fill(0)
        translate(margin, margin)
        scale(scale_factor)
        
        # Make a clipping path
        # path = BezierPath()
        # path.moveTo( (100,100) )
        # path.lineTo( (2000, 300) )
        # # path.lineTo( (300, 3000) )
        # path.curveTo( (2000, 600), (150, 1500), (300, 3000) )
        # path.closePath()
        # clipPath(path)
        
        fill(None)
        circle = oval(300, 300, 1000, 1500)
        clipPath(circle)
        
        image(image_path, (0,0))
        
        rect(200, 200, 2000, 30)

    caption_offset = ( image_width * scale_factor + margin )
    fill(1, 0, 0)
    text(flower_name, (caption_offset, margin))

script_folder = os.path.split(__file__)[0]
directory_path = os.path.join(script_folder, "TextAndImage/Images")
directory = os.fsencode(directory_path)
file_list_plain = [] # rewrite this later when appending files to list
file_list_path = [] # rewrite this later when appending files to list
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # join directory path and filename
    filename_path = os.path.join(directory_path, filename)
    filename_plain, file_extension = os.path.splitext(filename)
    if file_extension in [".jpg", ".png", ".tiff"]:
        # take all of the plain file names and make a list
        file_list_plain.append(filename_plain)
        # take all of the path names and make a list
        file_list_path.append(filename_path)
        
        image_path = filename_path
        
        draw_page(image_path)
# print(file_list_plain)
# print(file_list_path)