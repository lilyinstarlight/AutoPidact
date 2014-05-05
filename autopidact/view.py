from gi.repository import Gtk, GdkPixbuf, GLib
import cv2

class View(Gtk.Window):
	def __init__(self, title, camera, interval=200):
		Gtk.Window.__init__(self)
		self.set_title(title)
		self.set_size_request(640, 480)
		self.set_resizable(False)
		self.cam = camera
		self.img = Gtk.Image()
		self.add(self.img)
		GLib.timeout_add(interval, self.update)

	def update(self):
		if self.cam.isReady():
			frame = cv2.cvtColor(self.cam.getFrame(), cv2.COLOR_BGR2RGB)
			pixbuf = GdkPixbuf.Pixbuf.new_from_data(bytes(frame), GdkPixbuf.Colorspace.RGB, False, 8, frame.shape[1], frame.shape[0], frame.strides[1], None, None)
			self.img.set_from_pixbuf(pixbuf)
		else:
			print('Camera not ready')
