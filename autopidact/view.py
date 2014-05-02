from gi.repository import Gtk, Gdk
import cv2

class View(Gtk.Window):
	def __init__(self):
		self.cam = cv2.VideoCapture(device=0)
		self.img = Gtk.Image()
		self.add(self.img)
		while True:
			self.update()

	def update(self):
		frame = cv2.cvtColor(self.cam.read(), cv2.BGR2RGB)
		self.img.set(Gdk.pixbuf_from_data(frame.data, Gdk.COLORSPACE_RGB, false, 8, frame.cols, frame.rows, frame.step))
