# A work in progress

import csv

inch = 72

h = 4.5 * inch
w = 3.35 * inch

margin = 0.25 * inch

with open('data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # print(row['Year'], row['Month'], row['Day'])
        year = row[0]
        month = str.upper(row[1].lower())
        date = row[2]
        day = str.upper(row[3].lower())
        person = str.upper(row[4].upper())
        title = row[5].lower()
        birth = row[6].lower()
        
        textWidth, textHeight = textSize(person)
        personHeight = fontCapHeight()
        
        newPage(w, h)
        
        # Draw the month at the top
        cmykFill(0, 0, 0, 1)
        font('Helvetica', 24)
        textWidth, textHeight = textSize(month)
        textBox(month, (0, (h - (margin+textHeight)), w, textHeight), align="center")
        
        # Draw the day of the month
        cmykFill(0, 1, 1, .3)
        font('Helvetica', 200)
        textWidth, textHeight = textSize(date)
        text(date, (((w - textWidth) / 2), 100))
        
        # Draw the week day
        t = 8
        cmykFill(0, 0, 0, 1)
        font('Helvetica', 24)
        tracking(t)
        textWidth, textHeight = textSize(day)
        text(day, (((w-textWidth)/2)+(t/2), margin+(personHeight*3)))
        
        # Draw the line beneath the week day
        stroke(0, 0, 0, 1)
        strokeWidth(1)
        line((margin, margin+(personHeight*2)), (w-margin, margin+(personHeight*2)))
        
        # Draw person's title
        cmykFill(0, 0, 0, 1)
        tracking(0.25)
        strokeWidth(0)
        font('Helvetica', 11)
        textWidth, textHeight = textSize(title)
        text(title, (margin, margin))

        # Draw person's name
        cmykFill(0, 1, 1, .3)
        font('Helvetica', 11)
        textWidth, textHeight = textSize(person)
        text(person, (((w-textWidth)/2), margin))
        
        # Draw person's birth year
        cmykFill(0, 0, 0, 1)
        font('Helvetica', 11)
        textWidth, textHeight = textSize("nel " + birth)
        text("nel " + birth, ((w-textWidth)-margin, margin))
        
#saveImage("Daily-Calendar_01-00.pdf")