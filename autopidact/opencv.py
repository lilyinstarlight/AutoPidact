import cv2
import numpy

def getRegionByColor(image, lower, upper, contour_threshold=200, blur=False):
	color = cv2.inRange(image, numpy.array(lower), numpy.array(upper))
	if blur:
		color = cv2.blur(image, (3, 3))
	contours = cv2.findContours(cv2.Canny(color, contour_threshold, contour_threshold * 2), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	big_contour = None
	big_contour_area = 0
	for contour in contours[0]:
		area = cv2.contourArea(contour)
		if area > big_contour_area:
			big_contour = contour
			big_contour_area = area
	return big_contour

def getRegionData(region):
	rect = cv2.boundingRect(region)
	return ([rect[0] + rect[2] / 2, rect[1] + rect[3] / 2], rect[2] * rect[3])

def getCircles(image, circle_threshold=200, blur=True):
	if blur:
		image = cv2.blur(image, (3, 3))
	return cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT, 1, image.shape[1]/8, param1=160)

def drawCircle(image, circle):
	cv2.circle(image, (circle[0], circle[1]), circle[2], (63, 255, 255))

def drawCircles(image, circles):
	for circle in circles:
		drawCircle(image, circle)
