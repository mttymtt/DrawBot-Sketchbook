import os

textName = "Names.txt"

# fetch current folder path
folderPath = os.path.split(__file__)[0]
directoryPath = os.path.join(folderPath, "TextAndData/Text Processing/")
filePath = str(directoryPath + textName)

# open the text file
textFile = open(filePath, "r", encoding="utf-8")
data = textFile.read()
textFile.close()

nameList = data.split("\n")
# print(nameList)

w, h = 5 * 72, 3 * 72

for name in nameList:
    lastName, firstName = name.split(", ")
    print(firstName, lastName)
    
    newPage(w, h)
    
    with savedState():
        f_size = 100
        font("Obviously Black", f_size)
        text_width, text_height = textSize(firstName)
        scale_factor = w / text_width
        fontSize(f_size * scale_factor)
        text(firstName, (0, text_height))
        
    with savedState():
        f_size = 100
        font("Obviously Black", f_size)
        text_width, text_height = textSize(lastName)
        scale_factor = w / text_width
        fontSize(f_size * scale_factor)
        text(lastName, (0, 0))
    
    
    
    