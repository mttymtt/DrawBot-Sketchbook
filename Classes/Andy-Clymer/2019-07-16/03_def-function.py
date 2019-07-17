def drawPage(size=100):
    newPage("Letter")
    fontSize(size)
    text("Hello World", (100, 100))
    
drawPage() # this defaults to 100 because I defined it above
drawPage(20)