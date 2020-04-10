import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
def ledblink(): # Run forever
 i=0
 while i<=3:
  i=i+1    
  GPIO.output(8, GPIO.HIGH) # Turn on
  sleep(0.2) # Sleep for 1 second
  GPIO.output(8, GPIO.LOW) # Turn off
  sleep(0.2) # Sleep for 1 s
 
def ledh():
   GPIO.output(8, GPIO.HIGH)
def ledlow():
    GPIO.output(8, GPIO.LOW) #
    
   