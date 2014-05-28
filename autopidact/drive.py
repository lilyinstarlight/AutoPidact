from RPi import GPIO

left_io = [ 8, 10, 12 ]
right_io = [ 16, 18, 22 ]
shooter_io = [ 24, 26, 7 ]
shoot_io = [ 11 ]

io = left_io + right_io + shooter_io + shoot_io

def init():
	GPIO.setmode(GPIO.BOARD)
	for io_pin in io:
		GPIO.setup(io_pin, GPIO.OUT)

def motor(pwm, io):
	for i in range(len(io)):
		if pwm & (1 << i):
			GPIO.output(io[i], GPIO.HIGH)
		else:
			GPIO.output(io[i], GPIO.LOW)

def left(pwm):
	motor(pwm, left_io)

def right(pwm):
	motor(pwm, right_io)

def shooter(pwm):
	motor(pwm, shooter_io)

def shoot(pwm):
	motor(pwm, shoot_io)
