# what are you doing bro 🤨
path = input('What is the path/string?\n>>> ')
try:
    readedfilepath = open(path, 'r').read()
except:
    readedfilepath = path
print("Original String:\n\n" + readedfilepath)
currenthexlinestr = 0
secondcurrenthexlinestr = 0
thirdcurrenthexlinestr = 0
currenthexstr = "000: "
currenthexchar = 0
for char in readedfilepath:
    currenthexchar += 1
    if currenthexchar != 8 and currenthexchar != 16:
        currenthexstr = currenthexstr + char.encode('utf-8').hex() + " "
    elif currenthexchar == 8:
        currenthexstr = currenthexstr + char.encode('utf-8').hex() + "  "
    else:
        currenthexlinestr += 1
        actualcurrenthexlinestr = ""
        actualsecondcurrenthexlinestr = ""
        actualthirdcurrenthexlinestr = ""
        if currenthexlinestr == 10:
            actualcurrenthexlinestr = "a"
        elif currenthexlinestr == 11:
            actualcurrenthexlinestr = "b"
        elif currenthexlinestr == 12:
            actualcurrenthexlinestr = "c"
        elif currenthexlinestr == 13:
            actualcurrenthexlinestr = "d"
        elif currenthexlinestr == 14:
            actualcurrenthexlinestr = "e"
        elif currenthexlinestr == 15:
            actualcurrenthexlinestr = "f"
        elif currenthexlinestr == 16:
            currenthexlinestr = 0
            secondcurrenthexlinestr += 1
            actualcurrenthexlinestr = "0"
        else:
            actualcurrenthexlinestr = currenthexlinestr
        
        if secondcurrenthexlinestr == 10:
            actualsecondcurrenthexlinestr = "a"
        elif secondcurrenthexlinestr == 11:
            actualsecondcurrenthexlinestr = "b"
        elif secondcurrenthexlinestr == 12:
            actualsecondcurrenthexlinestr = "c"
        elif secondcurrenthexlinestr == 13:
            actualsecondcurrenthexlinestr = "d"
        elif secondcurrenthexlinestr == 14:
            actualsecondcurrenthexlinestr = "e"
        elif secondcurrenthexlinestr == 15:
            actualsecondcurrenthexlinestr = "f"
        elif secondcurrenthexlinestr == 16:
            secondcurrenthexlinestr = 0
            thirdcurrenthexlinestr += 1
            actualsecondcurrenthexlinestr = "0"
        else:
            actualsecondcurrenthexlinestr = secondcurrenthexlinestr
        
        if thirdcurrenthexlinestr == 10:
            actualthirdcurrenthexlinestr = "a"
        elif thirdcurrenthexlinestr == 11:
            actualthirdcurrenthexlinestr = "b"
        elif thirdcurrenthexlinestr == 12:
            actualthirdcurrenthexlinestr = "c"
        elif thirdcurrenthexlinestr == 13:
            actualthirdcurrenthexlinestr = "d"
        elif thirdcurrenthexlinestr == 14:
            actualthirdcurrenthexlinestr = "e"
        elif thirdcurrenthexlinestr == 15:
            actualthirdcurrenthexlinestr = "f"
        else:
            actualthirdcurrenthexlinestr = thirdcurrenthexlinestr
        if thirdcurrenthexlinestr == 0:
            currenthexstr = currenthexstr + char.encode('utf-8').hex() + "\n" + str(actualsecondcurrenthexlinestr) + str(actualcurrenthexlinestr) + "0: "
        else:
            currenthexstr = currenthexstr + char.encode('utf-8').hex() + "\n" + str(actualthirdcurrenthexlinestr) + str(actualsecondcurrenthexlinestr) + str(actualcurrenthexlinestr) + "0: "
        currenthexchar = 0
print("\nConverted to Hex:\n\n" + currenthexstr)