import gi
gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.1")
from gi.repository import Gtk, WebKit2
import os
import webbrowser

kreka = Gtk.Window(title = "Kreka")
kreka.set_default_size(1280, 960)
kreka.set_icon_from_file("/usr/share/icons/kreka.png")
ui = Gtk.ScrolledWindow()

header = Gtk.HeaderBar()
header.set_show_close_button(True)

krekacookie = Gtk.Button(label = "🍪")
krekacookie.connect("clicked", lambda krekacookie:menu.popup(None, None, None, None, 0, Gtk.get_current_event_time()))

home = Gtk.Button(label = "🏠")
home.connect("clicked", lambda home:webview.load_uri("https://progwi0.github.io/"))

back = Gtk.Button(label = "⬅️")
forward = Gtk.Button(label = "➡️")

back.connect("clicked", lambda back:webview.go_back())
forward.connect("clicked", lambda forward:webview.go_forward())

entry = Gtk.Entry()
entry.set_hexpand(True)

entry.connect("activate", lambda entry:webview.load_uri("https://www.google.com/search?q=" + entry.get_text()))

header.set_custom_title(entry)

goto = Gtk.Button(label = "➡️")
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

update = Gtk.MenuItem(label = "Update (only for pix version)")
update.connect("activate", lambda update:os.system("pix reinstall kreka"))
menu.append(update)

mysite = Gtk.MenuItem(label = "My site")
mysite.connect("activate", lambda mysite:webbrowser.open("https://progwi0.github.io/"))
menu.append(mysite)

def about(widget):
    dialogus = Gtk.AboutDialog()
    
    dialogus.set_name("Kreka")
    dialogus.set_version("8.0")
    dialogus.set_copyright("© 2025 progwi0")
    dialogus.set_comments("Simple web-browser on GTK3!")
    dialogus.set_website("https://progwi0.github.io/")
    dialogus.set_license_type(Gtk.License.GPL_3_0)
    
    dialogus.run()
    dialogus.destroy()

abouts = Gtk.MenuItem(label = "About Kreka")
abouts.connect("activate", about)
menu.append(abouts)

menu.show_all()

kreka.set_titlebar(header)

webview = WebKit2.WebView()
webview.load_uri("https://progwi0.github.io/")
ui.add(webview)

kreka.add(ui)

kreka.connect("destroy", Gtk.main_quit)
kreka.show_all()

Gtk.main()
