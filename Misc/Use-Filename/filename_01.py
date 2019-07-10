import os

# FILENAME
basename = os.path.splitext(os.path.basename(__file__))[0]
file_detail = "test"
version = "01"
format = ".pdf"
if file_detail != "":
    filename = basename + "_" + file_detail + "_" + version + format
else:
    filename = basename + "-" + version + format

print(filename)