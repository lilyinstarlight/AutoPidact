from __future__ import print_function

from gi.repository import Gtk

from autopidact import Camera, View

view = View('Camera 0', Camera(0))
view.connect('delete-event', Gtk.main_quit)
view.show_all()

Gtk.main()
