import pyperclip
import os
import pyautogui as p

os.system("notepad")
pyperclip.copy('Please type this out')
s = pyperclip.paste()
#with open("type.txt","w") as p:
#    p.write(s)
    
#save and close a particular file
os.startfile(r"xyz.txt")
p.write("does this work?")
p.hotkey('ctrl', 's')
p.hotkey('alt', 'f4')
