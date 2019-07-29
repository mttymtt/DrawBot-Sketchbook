# --------------------------------------
#    display()
#    Returns string
#    defualts to 1000 digits

def en(*argv):
    dict = {
        "Fox": "The quick brown fox jumps over the lazy dog.",
        "Wizards": "Grumpy wizards make toxic brew for the evil Queen and Jack.",
        "Waltz": "Jived fox nymph grabs quick waltz.",
        "Dwarf": "Glib jocks quiz nymph to vex dwarf.",
        "Sphinx": "Sphinx of black quartz, judge my vow.",
        "Zebras": "How vexingly quick daft zebras jump!",
        "Boxing": "The five boxing wizards jump quickly.",
        "Jackdaws": "Jackdaws love my big sphinx of quartz.",
        "Liquor": "Pack my box with five dozen liquor jugs."
        }
    Fox = "The quick brown fox jumps over the lazy dog."
    Wizards = "Grumpy wizards make toxic brew for the evil Queen and Jack."
    return argv
    
print(en(Fox))

# def myFun(arg1, *argv): 
#     print ("First argument :", arg1)
#     print("Next argument through *argv :", argv) 
  
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 