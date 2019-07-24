# This file prints a list of basic spacing strings
# using the OHno and OOHHnnoo format

import string

# =====================================================

OH_list = ["HHHOOO", "HHOHOO"]
no_list = ["nnnooo", "nnonoo"]

OOHH_list = ["HHOHHOOHOO"]
nnoo_list = ["nnonnoonoo"]

# =====================================================

for letter in string.ascii_uppercase:
    OH_list.append("H" + letter + "HO" + letter + "O" )
    OOHH_list.append("HH" + letter + "HHOO" + letter + "OO" )

for letter in string.ascii_lowercase:
    no_list.append("n" + letter + "no" + letter + "o" )
    nnoo_list.append("nn" + letter + "nnoo" + letter + "oo" )

# =====================================================
# OHno

for OH_item in OH_list:
    print(OH_item)
    
print("=" * 12)
    
for no_item in no_list:
    print(no_item)
    
print("=" * 12)

# =====================================================
# OOHHnnoo
    
for OOHH_item in OOHH_list:
    print(OOHH_item)
    
print("=" * 12)
    
for nnoo_item in nnoo_list:
    print(nnoo_item)
    
print("=" * 12)