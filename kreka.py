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
header.set_show_close_button(True)

krekacookie = Gtk.Button()
krekacookie.connect("clicked", lambda krekacookie:menu.popup_at_pointer(None))

home = Gtk.Button()
home.connect("clicked", lambda home:webview.load_uri("https://progwi0.github.io/"))

back = Gtk.Button()
forward = Gtk.Button()

back.connect("clicked", lambda back:webview.go_back())
forward.connect("clicked", lambda forward:webview.go_forward())

entry = Gtk.SearchEntry()
entry.set_placeholder_text("https://progwi0.github.io/")
entry.set_alignment(0.5)
entry.set_hexpand(True)

entry.connect("activate", lambda entry:webview.load_uri("https://www.qwant.com/?q=" + entry.get_text()))

header.set_custom_title(entry)

goto = Gtk.Button()
goto.connect("clicked", lambda goto:webview.load_uri(entry.get_text()))

header.pack_start(home)
header.pack_start(back)
header.pack_start(forward)
header.pack_start(entry)
header.pack_end(goto)
header.pack_end(krekacookie)

menu = Gtk.Menu()

newwindow = Gtk.MenuItem(label = "New window")
newwindow.connect("activate", lambda newwindow:os.system("kreka"))
menu.append(newwindow)

mysite = Gtk.MenuItem(label = "My site")
mysite.connect("activate", lambda mysite:webbrowser.open("https://progwi0.github.io/"))
menu.append(mysite)

def about(widget):
    dialogus = Gtk.AboutDialog()
    
    dialogus.set_program_name("Kreka")
    dialogus.set_version("15.0")
    dialogus.set_copyright("© 2025 progwi0")
    dialogus.set_comments("Simple web-browser on GTK3!")
    
    iconus = GdkPixbuf.Pixbuf.new_from_file_at_size("/usr/share/icons/kreka.png", 64, 64)
    dialogus.set_logo(iconus)
    
    dialogus.set_website("https://progwi0.github.io/")
    dialogus.set_authors(["progwi0", "chicken banana", "sigma"])
    
    dialogus.set_license_type(Gtk.License.GPL_3_0)
    
    dialogus.run()
    dialogus.destroy()

abouts = Gtk.MenuItem(label = "About Kreka")
abouts.connect("activate", about)
menu.append(abouts)

menu.show_all()

homeimg = Gtk.Image.new_from_icon_name("go-home-symbolic", Gtk.IconSize.BUTTON)
home.set_image(homeimg)

backimg = Gtk.Image.new_from_icon_name("go-previous-symbolic", Gtk.IconSize.BUTTON)
back.set_image(backimg)

forwardimg = Gtk.Image.new_from_icon_name("go-next-symbolic", Gtk.IconSize.BUTTON)
forward.set_image(forwardimg)

gotoimg = Gtk.Image.new_from_icon_name("mail-forward-symbolic", Gtk.IconSize.BUTTON)
goto.set_image(gotoimg)

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
