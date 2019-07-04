# random number between 0 and 1
print(random())

# random integer within a range
print(randint(1, 5))

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
print( choice(months) )

print( choice(["a", "b", "c"]) )

# True, False, None
# these are logical values
# print( choice([True, False]) )

newPage(300, 200)

decision = choice([True, False])

if decision == True:
    print("It was true!")
    rect(10, 20, 50, 100)
else:
    print("Sucker!")
    oval(10, 20, 50, 100)
    