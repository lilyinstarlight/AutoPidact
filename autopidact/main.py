from __future__ import print_function

from time import sleep

from __init__ import Camera, View
import opencv
import drive

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate as LCD

lcd = LCD()
lcd.begin(16, 1)
lcd.message('MAX!!!!!!!!!!')

camera = Camera(0)
print(camera.getFrame().shape)
view = View('Camera 0')
while True:
	if camera.isReady():
		frame = camera.getFrame()
		green = split(frame)[1]
		circles = opencv.getCircles(green)

		big_circle = (0, 0, 0)
		for circle in circles:
			if circle[2] > big_circle[2]:
				big_circle = circle
			opencv.drawCircle(frame, circle)

		view.update(frame)

		if lcd.buttons:
			if lcd.buttonPressed(lcd.SELECT):
				drive.shooter(127)
				drive.shoot(15)
				sleep(2)
				drive.shoot(0)
				drive.shooter(0)

			if lcd.buttonPressed(lcd.UP):
				drive.shoot(15)
			else:
				drive.shoot(0)

			if lcd.buttonPressed(lcd.DOWN):
				drive.shooter(127)
			else:
				drive.shooter(127)

			if lcd.buttonPressed(lcd.LEFT):
				drive.left(63)
			else:
				drive.left(0)

			if lcd.buttonPressed(lcd.RIGHT):
				drive.right(63)
			else:
				drive.right(0)
		elif len(circles) > 0:
			if big_circle[2] > 100:
				drive.shooter(127)
				drive.shoot(15)
				sleep(2)
				drive.shoot(0)
				drive.shooter(0)
			else:
				if big_circle[0] < frame.shape[0] - 60:
					drive.left(0)
					drive.right(63)
				elif big_circle[0] > frame.shape[0] + 60:
					drive.left(63)
					drive.right(0)
				else:
					drive.left(63)
					drive.right(63)
	else:
		print('Camera not ready')
		sleep(1)
