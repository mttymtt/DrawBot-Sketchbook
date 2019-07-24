import os

textName = "MobyDick.txt"

# fetch current folder path
folderPath = os.path.split(__file__)[0]
# specify path of assets
directoryPath = os.path.join(folderPath, "TextAndData/Text Processing/")
# string together text name and directory path
filePath = str(directoryPath + textName)

# open the text file
textFile = open(filePath, "r", encoding="utf-8")
# actually read the contents of that file
myText = textFile.read()
# and don't forget to close it
textFile.close()



formattedText = FormattedString()
for letter in myText:
    if letter != "o":
        formattedText.append(letter, fontSize=10, font="Times", fill=(0))
    else:
        formattedText.append(letter, fontSize=14, font="Helvetica", fill=(random(), random(), random()))


margin = 3/4 * 72
pageNumber = 0

# LOOP TO MAKE THE BOOK

while len(formattedText) > 0:
    newPage("A5")
    pageNumber += 1
    live_width = width() - (margin * 2)
    live_height = height() - (margin * 2)

    # actually draw/set the text
    formattedText = textBox(formattedText, (margin, margin, live_width, live_height) )
    
    # add a page number
    text(str(pageNumber), (width()/2, margin/2), align="center")

print(myText)