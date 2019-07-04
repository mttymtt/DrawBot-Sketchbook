# PYTHON DATA TYPES:

# String

name = "Matthew"
statement = 'DrawBot is "Fun"' #strings can have single or double quotes

# Numbers

date = 2

# List
#         0    1      2      3...
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#       -12  -11    -10     -9...

# Print entire list
print(months)

# Print single month
print(months[-9])

# for loop
# loops through all items in the list
for month_name in months:
    print("-" * 20)
    print(month_name)
    print(500)
    print("Hello")