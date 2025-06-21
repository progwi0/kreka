import os
import sys
import webbrowser

from tkinter import *
from tkinter import messagebox as dialogus
from tkinter import ttk

from tkinterweb import HtmlFrame

import sv_ttk
import darkdetect
import pywinstyles

app = Tk()
app.title("Kreka")

sv_ttk.set_theme(darkdetect.theme())

def titlus():
    version = sys.getwindowsversion()

    if version.major == 10 and version.build >= 22000:
        pywinstyles.change_header_color(app, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa")

def search():
    query = adress.get()
    web.load_website(f"https://www.google.com/search?q={query}")

def goto():
    query = adress.get()
    web.load_website(f"https://{query}")

def info():
    dialogus.showinfo("🍪", "Kreka 20.0\nBack again to Tk!\nCreated in 2025 by progwi0.\n(Sun Valley theme by rdbende. Check it out on GitHub!)")

top = ttk.Frame(app)
top.pack(fill="x", pady="4", padx= "2")

home = ttk.Button(top, text = "🏠", width=2 , command = lambda:web.load_website("https://progwi0.github.io/"))

home.pack(side="left", padx="2")

adress = ttk.Entry(top)
adress.pack(side="left", fill="both", expand=True)

search = ttk.Button(top, text = "🔍", width=2 , command=search)
search.pack(side="left", padx="2")

goto = ttk.Button(top, text = "➡️", width=2 , command=goto)
goto.pack(side="left", padx="2")

mps = ttk.Frame(app)
mps.pack(fill="x", pady="2", padx="2")

kreka = ttk.Button(mps, text = "🍪", width=2 , command = lambda:menu.post(app.winfo_pointerx(), app.winfo_pointery()))
kreka.pack(side="left", padx="2")

google = ttk.Button(mps, text = "Google", command = lambda:web.load_website("https://www.google.com/"))
google.pack(side="left", padx="2", fill="x", expand=True)

facebook = ttk.Button(mps, text = "Facebook", command = lambda:web.load_website("https://www.facebook.com/"))
facebook.pack(side="left", padx="2", fill="x", expand=True)

ddg = ttk.Button(mps, text = "DuckDuckGo", command = lambda:web.load_website("https://www.duckduckgo.com/"))
ddg.pack(side="left", padx="2", fill="x", expand=True)

wikipedia = ttk.Button(mps, text = "Wikipedia", command = lambda:web.load_website("https://en.wikipedia.org/wiki/Main_Page"))
wikipedia.pack(side="left", padx="2", fill="x", expand=True)

menu = Menu(app, tearoff = 0)

menu.add_separator()
menu.add_command(label="New window", command = lambda:os.system("kreka"))
menu.add_separator()
menu.add_command(label="My site", command = lambda:webbrowser.open("https://progwi0.github.io/"))
menu.add_command(label="About", command = info)
menu.add_separator()

web = HtmlFrame(app)
web.load_website("https://progwi0.github.io/")

web.pack(fill="both", expand=True)

titlus()
app.mainloop()
