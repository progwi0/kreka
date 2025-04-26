import os
import webbrowser
import tk as tk
from tkinter import messagebox as dialogus
from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinterweb import HtmlFrame

app = Window(themename="litera")
app.title("Kreka")

homus = os.path.expanduser("~")
patus = os.path.join(homus, ".progwi0")
themepath = os.path.join(patus, "theme.txt")

simplus = "~/.progwi0/theme.txt"

if not os.path.exists(simplus):
    os.system("cd ~ && mkdir .progwi0 && cd .progwi0 && touch theme.txt")

def search():
    query = adress.get()
    web.load_website(f"https://www.google.com/search?q={query}")

def goto():
    query = adress.get()
    web.load_website(f"https://{query}")

def info():
    dialogus.showinfo("🍪", "Kreka 7.0\nCreated in 2025 by progwi0.")

def light():
    app.style.theme_use("litera")
    with open(themepath, "w") as file:
        file.write("litera")

def dark():
    app.style.theme_use("darkly")
    with open(themepath, "w") as file:
        file.write("darkly")

top = Frame(app)
top.pack(fill="x", pady="2", padx="2")

home = Button(top, text = "🏠", width=1.5, command = lambda:web.load_website("https://progwi0.github.io/"), bootstyle = SECONDARY)
home.pack(side="left", padx="2")

adress = Entry(top)
adress.pack(side="left", fill="both", expand=True)

search = Button(top, text = "🔍", width=1.5, command=search, bootstyle = SECONDARY)
search.pack(side="left", padx="2")

goto = Button(top, text = "➡️", width=1.5, command=goto, bootstyle = SECONDARY)
goto.pack(side="left", padx="2")

mps = Frame(app)
mps.pack(fill="x", pady="2", padx="2")

kreka = Button(mps, text = "🍪", width=1.5, command = lambda:menu.post(app.winfo_pointerx(), app.winfo_pointery()), bootstyle = SECONDARY)
kreka.pack(side="left", padx="2")

google = Button(mps, text = "Google", command = lambda:web.load_website("https://www.google.com/"), bootstyle = SUCCESS)
google.pack(side="left", padx="2", fill="x", expand=True)

facebook = Button(mps, text = "Facebook", command = lambda:web.load_website("https://www.facebook.com/"), bootstyle = PRIMARY)
facebook.pack(side="left", padx="2", fill="x", expand=True)

ddg = Button(mps, text = "DuckDuckGo", command = lambda:web.load_website("https://www.duckduckgo.com/"), bootstyle = WARNING)
ddg.pack(side="left", padx="2", fill="x", expand=True)

wikipedia = Button(mps, text = "Wikipedia", command = lambda:web.load_website("https://en.wikipedia.org/wiki/Main_Page"), bootstyle = DANGER)
wikipedia.pack(side="left", padx="2", fill="x", expand=True)

menu = Menu(app, tearoff = 0)

menu.add_separator()
menu.add_command(label="New window", command = lambda:os.system("kreka"))
menu.add_separator()
menu.add_command(label="Light theme", command = light)
menu.add_command(label="Dark theme", command = dark)
menu.add_separator()
menu.add_command(label="Update (Only for pix version)", command = lambda:os.system("pix reinstall kreka"))
menu.add_separator()
menu.add_command(label="My site", command = lambda:webbrowser.open("https://progwi0.github.io/"))
menu.add_command(label="About", command = info)
menu.add_separator()

web = HtmlFrame(app)
web.load_website("https://progwi0.github.io/")

web.pack(fill="both", expand=True)

with open(themepath, "r") as file:
        themus = file.read().strip()
        app.style.theme_use(themus)
        
app.mainloop()
