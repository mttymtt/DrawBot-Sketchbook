import string

myText = FormattedString("Hi", fill=(0, 0, 1), fontSize=50)
# add more text to the formatted string above
myText.append(" there", fill=(0, 1, 1), fontSize=25, baselineShift=25)

newPage("A5")
text(myText, (100, 100))

myText = "This is my text, there are a lot of words."
formattedText = FormattedString()
print(myText.split())
for word in myText.split():
    print(word)
    formattedText.append(word + " ", fontSize=randint(20, 100))
    
text(formattedText, (10, 200))

print(string.ascii_uppercase)