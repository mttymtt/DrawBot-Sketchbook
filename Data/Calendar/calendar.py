import csv

size(300,300)

with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Year'], row['Month'], row['Day'])
        textbox('Year', 10, 10, 280, 280)