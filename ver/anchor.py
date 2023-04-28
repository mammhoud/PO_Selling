
from tkinter import *

root = Tk()
root.title("Anchor Example")
root.geometry("400x300")

# Create a frame to hold the widgets
frame = Frame(root)
frame.pack(fill=BOTH, expand=1)

# Create a label with anchor=NW
label1 = Label(frame, text="This is a label with anchor=NW", bg="yellow")
label1.pack(anchor=NW)

# Create a label with anchor=CENTER
label2 = Label(frame, text="This is a label with anchor=CENTER", bg="green")
label2.pack(anchor=CENTER)

# Create a label with anchor=SE
label3 = Label(frame, text="This is a label with anchor=SE", bg="red")
label3.pack(anchor=SE)

root.mainloop()
