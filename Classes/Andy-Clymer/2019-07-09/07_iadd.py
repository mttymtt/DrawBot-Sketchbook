color = [0, 0.23290921294379985, 0.26243082354374625, 0]

print( round(color[0] * 100) )
print( round(color[1] * 100) )
print( round(color[2] * 100) )
print( round(color[3] * 100) )

# C:0 M:23 Y:26 K:0

# x = a
# x = a + b
# x = a + b + c
# OR
# x = a
# x += b
# x += c

# Turn the color list into a string
colorName = "C:" + str(round(color[0] * 100))
colorName += " M:" + str(round(color[1] * 100))
colorName += " Y:" + str(round(color[2] * 100))
colorName += " K:" + str(round(color[3] * 100))


print( colorName )