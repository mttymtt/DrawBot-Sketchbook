import os

# FILENAME
basename = os.path.splitext(os.path.basename(__file__))[0]
version = "01"
format = ".py"
filename = basename + "_" + version + format

print(filename)