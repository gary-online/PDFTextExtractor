import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)   
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(row=0, column=1)

#instructions
instructions = tk.Label(root, text="Please select a PDF file to extract text from.", font=("Arial Bold", 12))
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[('PDF File', '*.pdf')])
    if file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[0]
        page_content = page.extract_text()
        
        #text_box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font=("Arial Bold", 12), bg="#20bebe", fg="white", height=2, width=20)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)   
canvas.grid(columnspan=3)

root.mainloop()
