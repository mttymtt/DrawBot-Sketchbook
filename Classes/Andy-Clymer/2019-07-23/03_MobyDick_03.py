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
formattedChapter = FormattedString()


for paragraph in myText.split("\n"):
    if "CHAPTER" in paragraph:
        chapterNumber, chapterHeading = paragraph.split(". ")
        # be sure to append a new line as well after paragraph
        formattedChapter.append(chapterNumber.split()[-1] + "\n", fontSize=10, font="Blanco", fill=(0), openTypeFeatures=dict(smcp=True), align="center")
        formattedChapter.append(chapterHeading + "\n", fontSize=18, font="Blanco Italic", fill=(0), openTypeFeatures=dict(smcp=False))
    else:
        formattedText.append(paragraph + "\n", fontSize=10, font="Blanco", openTypeFeatures=dict(smcp=False,liga=True), align="left")


margin = 3/4 * 72
pageNumber = 0

# LOOP TO MAKE THE BOOK

while len(formattedChapter) > 0:
    newPage("A5")
    live_width = width() - (margin * 2)
    live_height = height() - (margin * 2)
    
    formattedChapter = textBox(formattedChapter, (margin, margin, live_width, live_height) )

while len(formattedText) > 0:
    pageNumber += 1
    
    newPage("A5")
    live_width = width() - (margin * 2)
    live_height = height() - (margin * 2)

    # actually draw/set the text
    formattedText = textBox(formattedText, (margin, margin, live_width, live_height) )
    
    # add a page number
    font("Blanco", 8)
    text(str(pageNumber), (width()/2, margin/2), align="center")