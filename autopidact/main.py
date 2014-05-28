from __future__ import print_function

from time import sleep
import os

import cv2

from __init__ import Camera, View
import opencv
import drive

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate as LCD

lcd = LCD()
lcd.begin(16, 1)

camera = Camera(0)

if 'DISPLAY' in os.environ:
	view = View('Camera 0')
else:
	view = None

drive.init()
while True:
	if camera.isReady():
		frame = camera.getFrame()
		region = opencv.getRegionByColor(frame, [148, 42, 235], [188, 82, 255])
		if region != None:
			(center, area) = opencv.getRegionData(region)

		lcd.clear()
		if lcd.buttons():
			if lcd.buttonPressed(lcd.SELECT):
				lcd.message('SELECT ')
				drive.shooter(7)
				sleep(1)
				drive.shoot(1)
				sleep(1)
				drive.shoot(0)
				sleep(1)
				drive.shooter(0)

			if lcd.buttonPressed(lcd.UP):
				lcd.message('UP ')
				drive.shoot(1)
			else:
				drive.shoot(0)

			if lcd.buttonPressed(lcd.DOWN):
				lcd.message('DOWN ')
				drive.shooter(7)
			else:
				drive.shooter(0)

			if lcd.buttonPressed(lcd.LEFT):
				lcd.message('LEFT ')
				drive.left(3)
			else:
				drive.left(0)

			if lcd.buttonPressed(lcd.RIGHT):
				lcd.message('RIGHT ')
				drive.right(3)
			else:
				drive.right(0)
		elif region != None:
			lcd.message('(' + str(center[0]) + ',' + str(center[1]) + ')-' + str(area))
			if area > 800:
				drive.shooter(7)
				drive.shoot(1)
				sleep(2)
				drive.shoot(0)
				drive.shooter(0)
			else:
				if center[0] < frame.shape[1] - 60:
					drive.left(0)
					drive.right(3)
				elif center[0] > frame.shape[1] + 60:
					drive.left(3)
					drive.right(0)
				else:
					drive.left(3)
					drive.right(3)
		else:
			drive.left(0)
			drive.right(0)
			drive.shooter(0)
			drive.shoot(0)

		if view:
			view.update(frame)
	else:
		camera = Camera(0)
		print('Camera not ready')
		sleep(1)
