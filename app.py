import tkinter as tk
from tkinter import filedialog, Text, colorchooser
import os


root = tk.Tk()
root.title('App Runner')
apps = []

root.configure(background='#FF768F')


if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()
        # avoiding text vanishing after closing and opening

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="#FFAEBD")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


def removeFiles():
    if os.path.exists("save.txt"):
        os.remove("save.txt")


canvas = tk.Canvas(root, height=500, width=550, bg="#FF768F", highlightthickness=0)
canvas.pack()

frame = tk.Frame(root, bg="#FFAEBD")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


openFile = tk.Button(root, text="Add Executable", padx=38,
                     pady=1, fg="white", bg="#FF768F", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run All", padx=60,
                     pady=1, fg="white", bg="#FF768F", command=runApps)
runApps.pack()

removeFiles = tk.Button(root, text="Remove All", padx=49,
                        pady=1, fg="white", bg="#FF768F", command=removeFiles)
removeFiles.pack()




for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

