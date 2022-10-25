from gtts import gTTS
from tkinter import *
from pygame import mixer


# FUNCTIONS
def convert_text():
    speech = gTTS(text=text_type.get(), lang='en', slow=False)
    speech.save('voice.mp3')


def play():
    mixer.init()
    mixer.music.load('voice.mp3')
    mixer.music.play()


# GUI
window = Tk()
window.geometry('600x300')
window.title("SAY IT LITE!")
Canvas(height=600, width=600, bg='#000000', highlightthickness=0).place(x=0, y=0)

# ENTRIES
Label(window, text="SAY IT lite!", font=('Draconian Typewriter', 30), bg='#000000', fg="#FFFFFF").pack(pady=20)
Label(window, text="enter yr text hurrrr:", font=('Draconian Typewriter', 20), bg='#000000', fg="#FFFFFF").pack(pady=30)

text_type = StringVar()
Entry(window, textvariable=text_type, width=70, font=('Arial', 12)).pack()

# BUTTONS
Button(window, text="Convert to Speech", highlightbackground='#000000', command=convert_text).pack(pady=10)
Button(window, text="Say IT!", highlightbackground='#000000', command=play).pack(pady=10)

window.mainloop()
