import random
import os
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
a = input("How many to generate?\n>>> ")
try:
    int(a)
    b = input("Open link everytime?\n>>> ")
    for i in range(int(a)):
        link = "https://discord.gift/"
        for i in range(16):
            randomletter = letters[random.randint(0, len(letters) - 1)]
            link = link + randomletter
        print(link)
        if b == "Y" or b == "y":
            os.system('start "chrome.exe" "' + link + '"')
        link = "https://discord.gift/"
except Exception as e:
    print("Error: Can't generate " + a + " nitros.")
    print(e)