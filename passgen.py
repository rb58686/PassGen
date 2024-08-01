import tkinter as tk
from tkinter import ttk
import random

windowWidth = 500
windowHeight = 500
windowResolution = str(windowWidth) + "x" + str(windowHeight)
passLen = 5
passwordList = [0, 0, 0, 0, 0]
charSet = []
password = ""
times = 0
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*-+,.?%;"
for char in chars:
    charSet.append(char)

def generatePass():
    for i in range(passLen):
        genChar = charSet[random.randrange(0, (len(charSet)) - 1)]
        passwordList[i] = genChar
    #for x in range(passLen):
        #global password
        #password[x] = passwordList[x]
    return password

def buttonClicked():
    generatePass()
    global password
    global times
    label.configure(text=password)
    print(password)
    times += 1

window = tk.Tk()
window.title("PassGen")
window.anchor("center")
window.geometry(windowResolution)
#frame = ttk.Frame(window, padding=10, width=windowWidth-5, height=windowHeight-5)
label = tk.Label(text=password, width=100, font=("Arial", 14))
button = ttk.Button(text = "Generate password", width = 20, padding=5, command = buttonClicked)
button.pack(anchor = "sw", expand = 1, side = "bottom", padx = 2)
#frame.pack()
label.pack()
window.mainloop()