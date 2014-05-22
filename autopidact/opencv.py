import cv2

def getCircles(image, circle_threshold=200):
	return cv2.HoughCircles(cv2.blur(image, (3, 3)), cv2.HOUGH_GRADIENT, 1, image.shape[0]/8, 160)

def drawCircle(image, circle):
	cv2.circle(image, (circle[0], circle[1]), circle[2], (63, 255,255))

def drawCircles(image, circles):
	for circle in circles:
		drawCircle(image, circle)
