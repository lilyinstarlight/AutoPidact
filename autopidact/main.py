from __future__ import print_function

from gi.repository import Gtk

from view import View

view = View()
view.connect('delete-event', Gtk.main_quit)
view.show_all()
Gtk.main()
