import tkinter as tk
import os,glob

root=tk.Tk()

listbox=tk.Listbox(root)
listbox.pack()

mp4=glob.glob("*mp4")
for movie in mp4:
    listbox.insert(tk.END,movie)
listbox.bin("<Double-Button>","
root.mainloop()
