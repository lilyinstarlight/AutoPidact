from RPi import GPIO
import spi
import time

left = right = shooter = 0

def init():
	spi.openSPI(bits=24)
	GPIO.setup(4, GPIO.OUT)

def deinit():
	spi.closeSPI()

def transfer():
	spi.transfer((left, right, shooter))

def left(pwm):
	global left
	left = pwm
	transfer()

def right(pwm):
	global right
	right = pwm
	transfer()

def shooter(pwm):
	global shooter
	shooter = pwm
	transfer()

def shoot():
	GPIO.output(4, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(4, GPIO.LOW)
