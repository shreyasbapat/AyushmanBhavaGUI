import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs 
# Motor1A = 24
# Motor1B = 23
# Motor1E = 25
 
def setup(Motor=1):
	GPIO.setmode(GPIO.BCM)				# GPIO Numbering
	GPIO.setup(Motor,GPIO.OUT)  # All pins as Outputs
	# GPIO.setup(Motor1B,GPIO.OUT)
	# GPIO.setup(Motor1E,GPIO.OUT)
 
def run(Motor=1):
	# Going forwards
	GPIO.output(Motor,GPIO.HIGH)
	# GPIO.output(Motor1B,GPIO.LOW)
	# GPIO.output(Motor1E,GPIO.HIGH)
 
	sleep(5)
	# Stop
	GPIO.output(Motor,GPIO.LOW)

def destroy():	
	GPIO.cleanup()

# if __name__ == '__main__':     # Program start from here
# 	setup()
# 	run()
# 	destroy()