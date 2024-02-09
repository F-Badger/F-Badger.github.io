# import libraries
import tkinter as gui

#import filedialog to allow selection of files
from tkinter import filedialog

def get_pdf():
    
    root = gui.Tk()
    root.withdraw() 

    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )

    return file_path

print (get_pdf())
        
