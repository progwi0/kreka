from tkinter import *
from tkinter import messagebox as dialogus
from tkinterweb import HtmlFrame

app = Tk()
app.title("Kreka (Tk)")

def search():
    query = adress.get()
    web.load_website(f"https://www.google.com/search?q={query}")

def goto():
    query = adress.get()
    web.load_website(f"https://{query}")

top = Frame(app)
top.pack(fill="x", pady="2", padx="2")

home = Button(top, text = "🏠", width=1, command = lambda:web.load_website("https://progwi0.github.io/"))
home.pack(side="left", padx="2")

back = Button(top, text = "←", width=1, command = lambda:web.back())
back.pack(side="left", padx="2")

forward = Button(top, text = "→", width=1, command = lambda:web.forward())
forward.pack(side="left", padx="2")

adress = Entry(top)
adress.pack(side="left", fill="both", expand=True)

refresh = Button(top, text = "🔄", width=1, command = lambda:web.reload())
refresh.pack(side="left", padx="2")

search = Button(top, text = "🔍", width=1, command=search)
search.pack(side="left", padx="2")

goto = Button(top, text = "➡️", width=1, command=goto)
goto.pack(side="left", padx="2")

mps = Frame(app)
mps.pack(fill="x", pady="2", padx="2")

kreka = Button(mps, text = "🍪", width=1, command = lambda:dialogus.showinfo("🍪", "Kreka 1.0\nCreated in 2025 by progwi0."))
kreka.pack(side="left", padx="2")

google = Button(mps, text = "Google", command = lambda:web.load_website("https://www.google.com/"))
google.pack(side="left", padx="2", fill="x", expand=True)

facebook = Button(mps, text = "Facebook", command = lambda:web.load_website("https://www.facebook.com/"))
facebook.pack(side="left", padx="2", fill="x", expand=True)

ddg = Button(mps, text = "DuckDuckGo", command = lambda:web.load_website("https://www.duckduckgo.com/"))
ddg.pack(side="left", padx="2", fill="x", expand=True)

youtube = Button(mps, text = "YouTube", command = lambda:web.load_website("https://www.youtube.com/"))
youtube.pack(side="left", padx="2", fill="x", expand=True)

web = HtmlFrame(app)
web.load_website("https://progwi0.github.io/")

web.pack(fill="both", expand=True)

app.mainloop()
