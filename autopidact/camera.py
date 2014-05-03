import cv2

class Camera:
	def __init__(self, device):
		self.capture = cv2.VideoCapture(device=device)

	def isReady(self):
		return self.capture.isOpened()

	def getFrame(self):
		return self.capture.read()[1]
