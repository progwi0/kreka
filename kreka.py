import gi
gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.1")
gi.require_version("GdkPixbuf", "2.0")
from gi.repository import Gtk, WebKit2, GdkPixbuf, Gdk
import os
import webbrowser

kreka = Gtk.Window(title = "Kreka")
kreka.set_default_size(1280, 960)
ui = Gtk.ScrolledWindow()

header = Gtk.HeaderBar()

krekacookie = Gtk.MenuButton()
krekacookie.connect("clicked", lambda krekacookie:exp.show_all())

home = Gtk.Button()
home.connect("clicked", lambda home:webview.load_uri("https://progwi0.github.io/"))

back = Gtk.Button()
back.connect("clicked", lambda back:webview.go_back())

entry = Gtk.SearchEntry()
entry.set_placeholder_text("https://progwi0.github.io/")
entry.set_alignment(0.5)
entry.set_hexpand(True)

forward = Gtk.Button()
forward.connect("clicked", lambda forward:webview.go_forward())

refresh = Gtk.Button()
refresh.connect("clicked", lambda refresh:webview.reload())

entry.connect("activate", lambda entry:webview.load_uri("https://www.qwant.com/?q=" + entry.get_text()))

header.set_custom_title(entry)

goto = Gtk.Button()
goto.connect("clicked", lambda goto:webview.load_uri(entry.get_text()))

closus = Gtk.Button()
closus.connect("clicked", Gtk.main_quit)

header.pack_start(home)
header.pack_start(back)
header.pack_start(forward)
header.pack_start(entry)
header.pack_end(closus)
header.pack_end(krekacookie)
header.pack_end(goto)
header.pack_end(refresh)

def distro():
    with open("/etc/os-release") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("ID="):
                    return line.strip().split("=")[1].strip('"')

def about(widget):
    dialogus = Gtk.AboutDialog()
    
    dialogus.set_program_name(f"Kreka")
    dialogus.set_version("19.2")
    dialogus.set_copyright("© 2025 progwi0")
    dialogus.set_comments(f"Simple web-browser on GTK3! (Running in {distro()})")

    dialogus.set_website("https://progwi0.github.io/")
    dialogus.set_authors(["progwi0", "chicken banana", "sigma"])
    
    dialogus.set_license_type(Gtk.License.GPL_3_0)
    
    dialogus.run()
    dialogus.destroy()

exp = Gtk.Popover()

menus = Gtk.Box(spacing=1, orientation=Gtk.Orientation.VERTICAL)

newwindows = Gtk.Button(label = "New window")
newwindows.connect("clicked", lambda newwindow:os.system("kreka"))
menus.pack_start(newwindows, True, True, 0)

mysite = Gtk.Button(label = "My site")
mysite.connect("clicked", lambda mysite:webbrowser.open("https://progwi0.github.io/"))
menus.pack_start(mysite, True, True, 0)

abouts = Gtk.Button(label = "About Kreka")
abouts.connect("clicked", about)
menus.pack_start(abouts, True, True, 0)

exp.add(menus)

krekacookie.set_popover(exp)

homeimg = Gtk.Image.new_from_icon_name("go-home-symbolic", Gtk.IconSize.BUTTON)
home.set_image(homeimg)

backimg = Gtk.Image.new_from_icon_name("go-previous-symbolic", Gtk.IconSize.BUTTON)
back.set_image(backimg)

forwardimg = Gtk.Image.new_from_icon_name("go-next-symbolic", Gtk.IconSize.BUTTON)
forward.set_image(forwardimg)

refreshimg = Gtk.Image.new_from_icon_name("view-refresh-symbolic", Gtk.IconSize.BUTTON)
refresh.set_image(refreshimg)

gotoimg = Gtk.Image.new_from_icon_name("mail-forward-symbolic", Gtk.IconSize.BUTTON)
goto.set_image(gotoimg)

closusimg = Gtk.Image.new_from_icon_name("window-close-symbolic", Gtk.IconSize.BUTTON)
closus.set_image(closusimg)

krekaimg = Gtk.Image.new_from_icon_name("emoji-symbols-symbolic", Gtk.IconSize.BUTTON)
krekacookie.set_image(krekaimg)

kreka.set_titlebar(header)

webview = WebKit2.WebView()
webview.load_uri("https://progwi0.github.io/")

def loadus(webview, load_event):
    if load_event == WebKit2.LoadEvent.FINISHED:
        entry.set_text(webview.get_uri())

webview.connect("load-changed", loadus)
ui.add(webview)

kreka.add(ui)

kreka.connect("destroy", Gtk.main_quit)
kreka.show_all()

Gtk.main()
kreka.show_all()

Gtk.main()
