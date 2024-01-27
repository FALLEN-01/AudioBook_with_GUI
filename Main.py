import tkinter as tk
from tkinter import *
from PyPDF2 import *
import pyttsx3
from tkinter import filedialog

root = Tk()
root.geometry('450x450')
root.title("AudioBook Creator")

Label(root, text="AudioBook Creator",font="Arial 15").pack() 
m=tk.IntVar()
f=tk.IntVar()

def browse():
    global PdfReader
    file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
    PdfReader = PdfReader(open(file, 'rb'))
    pathlabel.config(text=file)


def save():
    global speaker
    speaker = pyttsx3.init()
    for page_num in range(len(PdfReader.pages)):
        text =  PdfReader.pages[page_num].extract_text()
        speaker.runAndWait()
    speaker.stop()

    voices = speaker.getProperty('voices')
    if m.get() == 0:
        speaker.setProperty('voice', voices[0].id)
    elif f.get() == 1:
        speaker.setProperty('voice', voices[1].id)

    speaker.save_to_file(text,'audio.mp3')
    speaker.runAndWait()
    Label(root,text="The AudioBook is Saved").pack()
    tk.messagebox.showinfo("AudioBook Creator",  "AudioBook Is Saved") 

pathlabel = Label(root)
pathlabel.pack()

Button(root,text="Browse a File",command=browse).pack()
Button(root,text="Create and Save the Audio File ",command=save).pack()

Checkbutton(root,text="Male Voice",onvalue=0,offvalue=10,variable=m).pack()
Checkbutton(root,text="Female Voice",onvalue=1,offvalue=10,variable=f).pack()
root.mainloop()