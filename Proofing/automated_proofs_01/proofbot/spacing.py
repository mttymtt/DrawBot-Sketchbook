import string

# --------------------------------------
#    OHno()
#    Returns OHno, OH, no, OOHHnnoo, OOHH, or nnoo
#    Returns string or list
#    defaults to OHno as string

def OHno(arg="OHno", arg2="string"):
    OH_list = ["HHHOOO", "HHOHOO"]
    no_list = ["nnnooo", "nnonoo"]
    
    OHno_string = ""
    OH_string = ""
    no_string = ""

    OOHH_list = ["HHOHHOOHOO"]
    nnoo_list = ["nnonnoonoo"]
    
    OOHHnnoo_string = ""
    OOHH_string = ""
    nnoo_string = ""

    for letter in string.ascii_uppercase:
        OH_list.append("H" + letter + "HO" + letter + "O" )
        OOHH_list.append("HH" + letter + "HHOO" + letter + "OO" )

    for letter in string.ascii_lowercase:
        no_list.append("n" + letter + "no" + letter + "o" )
        nnoo_list.append("nn" + letter + "nnoo" + letter + "oo" )

    OHno_list = OH_list + no_list
    OOHHnnoo_list = OOHH_list + nnoo_list

    for OH_item in OH_list:
        OHno_string += OH_item + "\n"
        OH_string += OH_item + "\n"
    
    for no_item in no_list:
        OHno_string += no_item + "\n"
        no_string += no_item + "\n"
    
    for OOHH_item in OOHH_list:
        OOHHnnoo_string += OOHH_item + "\n"
        OOHH_string += OOHH_item + "\n"
    
    for nnoo_item in nnoo_list:
        OOHHnnoo_string += nnoo_item + "\n"
        nnoo_string += nnoo_item + "\n"

    if arg == "OHno":
        if arg2 == "string":
            return OHno_string
        else:
            return OHno_list
    if arg == "OH":
        if arg2 == "string":
            return OH_string
        else:
            return OH_list
    if arg == "no":
        if arg2 == "string":
            return no_string
        else:
            return no_list
            
    if arg == "OOHHnnoo":
        if arg2 == "string":
            return OOHHnnoo_string
        else:
            return OOHHnnoo_list
    if arg == "OOHH":
        if arg2 == "string":
            return OOHH_string
        else:
            return OOHH_list
    if arg == "nnoo":
        if arg2 == "string":
            return nnoo_string
        else:
            return nnoo_list