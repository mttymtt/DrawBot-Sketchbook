import os

imagePath = "/Users/Mattymatt/Dropbox/GitHub/DrawBot-Sketchbook/Classes/Andy-Clymer/2019-07-16/TextAndImage/Images/Amaryllis fulgida.jpg"

script_folder = os.path.split(__file__)[0]
directory_path = os.path.join(script_folder, "TextAndImage/Images")

directory = os.fsencode(directory_path)

for file in os.listdir(directory):
    file_list = []
    filename = os.fsdecode(file)
    filename_path = os.path.join(directory_path, filename)
    filename_plain, file_extension = os.path.splitext(filename)
    if filename.endswith(".jpg"):
        # print(filename_plain)
        file_list.append(filename_plain)
        print(file_list)

folder_path, file_name = os.path.split(imagePath)
flower_name, file_extension = os.path.splitext(file_name)

newPage("LetterLandscape")
inch = 72
margin = (3 / 4) * inch

image_width, image_height = imageSize(imagePath)
scale_factor = (height() - (margin * 2)) / image_height

flower_name = file_name[0:-4]

fontSize(30)
fill(1, 0, 0)
with savedState():
    translate(margin, margin)
    scale(scale_factor)
    image(imagePath, (0,0))
    rect(200, 200, 2000, 30)

caption_offset = ( image_width * scale_factor + margin )
text(flower_name, (caption_offset, margin))