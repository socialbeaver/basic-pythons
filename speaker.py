import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()
print("")

pyttsx3.speak("Hello world!")

#opening google chrome
pyttsx3.speak("Opening GOOGLE CHROME. Opening GMAIL")
print(".")
print(".")

#opening a specific url on google chrome - the short way. Needs a window to be already open
#webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")

#For opening a new tab on google chrome
#webbrowser.open_new_tab("https://www.google.com")
webbrowser.open_new_tab("https://mail.google.com/")
