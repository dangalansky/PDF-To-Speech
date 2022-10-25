import PyPDF2
from gtts import gTTS
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from pygame import mixer


# FUNCTIONS
def open_pdf():
    filename = filedialog.askopenfilename(initialdir='/',
                                          title='Choose A File',
                                          filetypes=(('pdf files', '*.pdf'),))
    pdf_filepath.set(filename)


def pdf_to_txt(filepath):
    with open(filepath, 'rb') as pdf_obj:
        pdfreader = PyPDF2.PdfFileReader(pdf_obj)
        x = pdfreader.numPages

        with open("pdf.txt", 'w') as txt_file:
            for n in range(x):
                page = pdfreader.getPage(n)
                text = page.extractText()
                txt_file.writelines(text)

    messagebox.showinfo(title='Success!',
                        message='PDF Successfully converted to pdf.txt!')


def txt_to_mp3():
    filename = mp3_title.get()
    mp3_playback.set(filename)
    with open('pdf.txt', 'r') as file:
        text = file.read()
    speech = gTTS(text=text, lang='en', slow=False)
    speech.save(f'{filename}.mp3')
    messagebox.showinfo(title='Success!',
                        message=f'Text successfully saved as {filename}.mp3!')


def playback():
    filename = mp3_playback.get()
    mixer.init()
    mixer.music.load(f'{filename}.mp3')
    mixer.music.play()


# GUI
window = Tk()
window.geometry('800x800')
window.title("DON'T SAY IT...SPRAY IT!")

# BACKGROUND
canvas = Canvas(height=800, width=800, bg='#77BBC9', highlightthickness=0)
image = Image.open("bg.jpg")
image_rs = image.resize((780, 780), Image.ANTIALIAS)
background = ImageTk.PhotoImage(image_rs)
canvas.create_image(395, 385, image=background)
canvas.place(x=0, y=0)

# OPEN PDF
pdf_filepath = StringVar(None)
Entry(window, textvariable=pdf_filepath, width=30, highlightthickness=0).place(x=30, y=385)
Button(window, text='Open PDF', highlightbackground='#77BBC9', command=open_pdf).place(x=310, y=380)
Button(window, text='Convert to Text', highlightbackground='#77BBC9',
       command=lambda: pdf_to_txt(pdf_filepath.get())).place(x=90, y=432)

# CONVERT TO MP3
mp3_title = StringVar(None)
Entry(window, textvariable=mp3_title, width=15, highlightthickness=0).place(x=50, y=530)
Button(window, text='Save as MP3', highlightbackground='#77BBC9', command=txt_to_mp3).place(x=100, y=595)

# PLAYBACK
mp3_playback = StringVar(None)
Button(window, text='Play!!!', highlightbackground='#77BBC9', command=playback).place(x=280, y=683)

window.mainloop()
