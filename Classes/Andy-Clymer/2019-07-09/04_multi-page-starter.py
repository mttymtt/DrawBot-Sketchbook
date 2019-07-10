for pageNumber in range(5):
    newPage("Letter")
    with savedState():
        fill(1,0,0)
        font("Obviously-CompressedBlack", 100)
        if pageNumber == 0:
            text("Title Page", (0, 0))
        else:
            text(str(pageNumber), (0, 0))
    for x in range(0, width(), 50):
        for y in range(0, height(), 50):
            rect(x, y, 10*pageNumber, 10*pageNumber)