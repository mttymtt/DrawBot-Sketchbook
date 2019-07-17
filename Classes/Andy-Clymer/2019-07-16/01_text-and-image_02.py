import os

folderPath = os.path.split(__file__)[0]
directoryPath = os.path.join(folderPath, "TextAndImage/Images")

directory = os.fsencode(directoryPath)

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     filename_path = os.path.join(directoryPath, filename)
     if filename.endswith(".jpg") or filename.endswith(".png"): 
         print(filename_path)
         # print(filename) # excludes file path
     else:
         print("Fail")

newPage("Letter")

imagePath = "/Users/Mattymatt/Dropbox/GitHub/DrawBot-Sketchbook/Classes/Andy-Clymer/2019-07-16/TextAndImage/Images/Amaryllis fulgida.jpg"

image(imagePath, (0,0))