imagePath = "/Users/Mattymatt/Dropbox/GitHub/DrawBot-Sketchbook/Classes/Andy-Clymer/2019-07-16/TextAndImage/Images/Amaryllis fulgida.jpg"

print( imagePath.upper() )

splitPath = imagePath.split("/")
file_name = splitPath[-1]
print(file_name)

print( file_name[0:-4] )

print( file_name.replace(".jpg", "") )

# Playing with import os

import os
folder_path, file_name = os.path.split(imagePath)
# print(file_name + " lives in " + folder_path)

flower_name, file_extension = os.path.splitext(file_name)
print(flower_name)

