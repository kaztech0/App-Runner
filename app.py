import atexit
import tkinter as tk
from tkinter import filedialog, Text, colorchooser
import os


root = tk.Tk()
root.title('App Runner')
apps = []

root.configure(background='#507868')


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
        label = tk.Label(frame, text=app, bg="#A8C0B0")
        label.configure(font=("Helvetica", 10))
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=500, width=550, bg="#507868", highlightthickness=0)
canvas.pack()

frame = tk.Frame(root, bg="#A8C0B0", borderwidth=1, highlightthickness=3)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

goodDay = tk.Button(root, text="Hello! :D", padx=60,
            pady=0.1, fg="white", bg="#507868", borderwidth=0)
goodDay.configure(font=("Helvetica", 18, "italic"))
goodDay.pack()

openFile = tk.Button(root, text="Add Executable", padx=38,
                     pady=2, fg="white", bg="#507868", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run All", padx=60,
                     pady=2, fg="white", bg="#507868", command=runApps)
runApps.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

