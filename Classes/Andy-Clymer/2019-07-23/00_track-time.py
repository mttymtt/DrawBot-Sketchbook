import time

now = time.time()

for pageNumber in range(1000):
    newPage("A5")
    
print( time.time() - now )