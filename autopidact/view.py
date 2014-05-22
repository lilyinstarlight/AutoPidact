import cv2

class View:
	def __init__(self, title):
		self.title = title
		cv2.namedWindow(title)

	def update(self, image):
		cv2.imshow(image)
		cv2.waitKey(250)
