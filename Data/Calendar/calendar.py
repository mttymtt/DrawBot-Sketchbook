import csv

pt = 72

h = 4.5 * pt
w = 3.35 * pt

with open('data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # print(row['Year'], row['Month'], row['Day'])
        year = row[0]
        month = row[1].lower()
        date = row[2]
        day = row[3].lower()
        
        newPage(w, h)
        
        # Draw the month at the top
        cmykFill(0, 0, 0, 1)
        font('Braggadocio MT', 24)
        textWidth, textHeight = textSize(month)
        textBox(month, (0, (h - 42), w, textHeight), align="center")
        
        # Draw the day of the month
        cmykFill(0, 1, 1, .3)
        font('HWT Mardell', 200)
        textWidth, textHeight = textSize(date)
        text(date, (((w - textWidth) / 2), 100))
        
        # Draw the week day
        t = 8
        cmykFill(0, 0, 0, 1)
        font('Braggadocio MT', 24)
        tracking(t)
        textWidth, textHeight = textSize(day)
        text(day, (((w-textWidth)/2)+(t/2), 47))
        
        # Draw the line beneath the week day
        stroke(0, 0, 0, 1)
        strokeWidth(1)
        line((((w-203)/2), 39), (w-((w-203)/2), 39))
