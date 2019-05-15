import os

folderPath = os.path.split(__file__)[0]
directoryPath = os.path.join(folderPath, "_assets/")

directory = os.fsencode(directoryPath)

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".jpg") or filename.endswith(".png"): 
         print(os.path.join(directoryPath, filename))
         # print(filename) # excludes file path
     else:
         print("Fail")