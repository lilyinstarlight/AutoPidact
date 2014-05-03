from gi.repository import Gtk, GdkPixbuf, GLib
import cv2

class View(Gtk.Window):
	def __init__(self, title, camera, interval=200):
		Gtk.Window.__init__(self)
		self.set_title(title)
		self.cam = camera
		self.img = Gtk.Image()
		self.add(self.img)
		GLib.timeout_add(interval, self.update)

	def update(self):
		if self.cam.isReady():
			frame = cv2.cvtColor(self.cam.getFrame(), cv2.COLOR_BGR2RGB)
			self.img.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_data(frame.data, GdkPixbuf.Colorspace.RGB, False, 8, frame.shape[1], frame.shape[0], frame.strides[0], None, None))
		else:
			print('not ready')
