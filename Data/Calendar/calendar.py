import csv

pt = 72

h = 3 * pt
w = 3 * pt

with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row['Year'], row['Month'], row['Day'])
        year = row['Year']
        date = row['Day']
        newPage(h, w)
        text(year, (10, 10))
        fontSize(72)
        textWidth, textHeight = textSize(date)
        textBox(date, (0, ((w+(textHeight/-2))/-2), w, w), align="center")
        
        print(textHeight)
