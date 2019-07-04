# one value:    0 -> x
# two values:   x -> y
# three values: x -> y, but count every z
# for i in range(0, 20, 2):
#     print(i)

w, h = 300, 200
    
newPage(w, h)


# Ran can have three values:
    # start value, end value, interval size
for x in range(20, w, 20):
    for y in range(30, randint(0, h), randint(5, 25)):
        print(x)
        print(y)
        fill(x/255, y/255, 0)
        # Flip a coin
        decision = choice([True, False])
        if decision == True:
            stroke(None)
            rect(x-10, y-20, y/10, x/10)
        else:
            fill(0, 0, 1, 0.5)
            stroke(1, 0, 0)
            strokeWidth(randint(0,5))
            oval(x-10, y-20, 20, 20)
            strokeWidth(0.5)
            line(((x-10)+10, (y-20)+10), (y, 40))
        
# ========
        
# newPage(w, h*2)

# # Ran can have three values:
#     # start value, end value, interval size
# for x in range(20, w, 20):
#     for y in range(30, h, randint(5, 25)):
#         print(x)
#         print(y)
#         fill(x/255, y/255, 0)
#         rect(x, (h)+y-(x/2), x/2, 5)