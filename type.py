import pyperclip
import os

os.system("notepad")
pyperclip.copy('Please type this out')
s = pyperclip.paste()
with open("type.txt","w") as p:
    p.write(s)
