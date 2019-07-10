# Variables

things = ["book", "computer", "table"] # list
adverbs = ["a little", "very much", "not at all"]
adj = ["great", "awful", "boring"]

phrase = "The " + choice(things) + " is " + choice(adverbs) + " " + choice(adj)

newPage("A5Landscape")
font("Obviously-CompressedBlack", 120)
fill(1,0,0)
text(phrase, ( (width()/2), ((height()/2) - (fontCapHeight()/2)) ), align="center")