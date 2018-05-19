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
	GPIO.output(Motor,GPIO.LOW)
	# GPIO.output(Motor1B,GPIO.LOW)
	# GPIO.output(Motor1E,GPIO.HIGH)
 
	sleep(2)
	# Stop
	GPIO.output(Motor,GPIO.HIGH)

def destroy():	
	GPIO.cleanup()

gpiopin =[5,6,13,19,26,7,12,16,20,21]
#if __name__ == '__main__':
#	for i in gpiopin:
#		print (i)
#		setup(Motor=i)
#		run(Motor=i)
#		sleep(2)
#	destroy()

#if __name__ == '__main__':
#	i=100000000
#	while(i>0):
#		i=i-1
#		GPIO.setmode(GPIO.BCM)				# GPIO Numbering
#		GPIO.setup(5,GPIO.OUT)
#		GPIO.output(5,GPIO.HIGH)
#	destroy()

if __name__ == '__main__':			# GPIO Numbering
	setup(Motor=5)
	run(Motor=5)
	destroy()