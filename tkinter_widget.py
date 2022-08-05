import tkinter as tk

root=tk.Tk()
root.geometry("300x400")

entry1=tk.Entry(root)
entry1.insert('end','type your name')
entry1.pack()


root.mainloop()
