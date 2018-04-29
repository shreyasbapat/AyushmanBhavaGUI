import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs 
Motor1A = 24
Motor1B = 23
Motor1E = 25
 
def setup():
	GPIO.setmode(GPIO.BCM)				# GPIO Numbering
	GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)
 
def run():
	# Going forwards
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
 
	sleep(5)
	# Stop
	GPIO.output(Motor1E,GPIO.LOW)

def destroy():	
	GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
	setup()
	run()
	destroy()