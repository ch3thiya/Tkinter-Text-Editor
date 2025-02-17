from tkinter import *
from tkinter import filedialog

root = Tk("Text Editor")
root.geometry("600x400")

text = Text(root, wrap="word", font=("Helvetica", 12))
text.pack(expand=True, fill="both")

# Function to save the text content
def saveas():
    t = text.get("1.0", "end-1c")  # Get all text from the Text widget
    savelocation = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if savelocation:  # Check if the user provided a file location
        try:
            with open(savelocation, "w") as file1:
                file1.write(t)
        except Exception as e:
            print(f"Error saving file: {e}")

# Function to open a file
def openfile():
    filelocation = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if filelocation:  # Check if the user selected a file
        try:
            with open(filelocation, "r") as file1:
                content = file1.read()
                text.delete("1.0", END)  # Clear the current text
                text.insert("1.0", content)  # Insert the file content
        except Exception as e:
            print(f"Error opening file: {e}")

# Function to change the font
def change_font(font_name):
    text.config(font=(font_name, font_size.get()))

# Function to change the font size
def change_font_size():
    text.config(font=(font_var.get(), font_size.get()))

menubar = Menu(root)
root.config(menu=menubar)

# File menu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save As", command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Font menu
fontmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Font", menu=fontmenu)

# Font family options
font_var = StringVar(value="Helvetica")  # Default font
font_families = ["Helvetica", "Courier", "Times New Roman", "Arial"]
for family in font_families:
    fontmenu.add_radiobutton(label=family, variable=font_var, value=family, command=lambda f=family: change_font(f))

# Font size options
font_size = IntVar(value=12)  # Default font size
sizemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Size", menu=sizemenu)
sizes = [10, 12, 14, 16, 18, 20, 24, 28, 32]
for size in sizes:
    sizemenu.add_radiobutton(label=str(size), variable=font_size, value=size, command=change_font_size)

root.mainloop()