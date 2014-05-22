import spi

left = right = shooter = shoot = 0

def init():
	spi.openSPI(bits=32)

def deinit():
	spi.closeSPI()

def transfer():
	spi.transfer((left, right, shooter, shoot))

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

def shoot(pwm):
	global shoot
	shoot = pwm
	transfer()
