import cv2

class View:
	def __init__(self, title, delay=250):
		self.title = title
		self.delay = delay
		cv2.namedWindow(title)

	def update(self, image):
		cv2.imshow(self.title, image)
		cv2.waitKey(self.delay)
