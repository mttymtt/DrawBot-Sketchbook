newPage("A5")

fill(1,0,0)
fontSize(100)
text("Hello", (100, 100))
text("Goodbye", (100, 200))

myText = FormattedString("Hi there", fill=(0, 0, 1), fontSize=50)

text(myText, (100, 300))