import os

fileName = "WeatherData.csv"

# construct file path
folderPath = os.path.split(__file__)[0]
directoryPath = os.path.join(folderPath, "TextAndData/Data/")
filePath = str(directoryPath + fileName)

# open file
csvFile = open(filePath, "r", encoding="utf-8")
data = csvFile.read()
csvFile.close()

data_lines = data.split("\n")

# if you write a #: then it'll start at the number specified and go until empty
# print( data_lines[1:] )

newPage("LetterLandscape")

counter = 0
for data_line in data_lines[1:]:
    line_split = data_line.split(",")
    print(line_split)
    
    counter += 1
    
    date = line_split[0]
    temp = int(line_split[1])
    humidity = int(line_split[2])

    translate(5, 0)
    
    if "2019-06-18" in date: 
        fill(1, 0, 0)
        rect(0, 0, 3, temp)