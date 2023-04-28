from tkinter import *

root = Tk()
root.title("Responsive Grid Example")

# Create some widgets
label1 = Label(root, text="Label 1", bg="red")
label2 = Label(root, text="Label 2", bg="green")
label3 = Label(root, text="Label 3", bg="blue")

# Place them in a grid
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)

# Configure the rows and columns
n_rows = 2
n_columns = 2
for i in range(n_rows):
    root.grid_rowconfigure(i, weight=1)
for i in range(n_columns):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()