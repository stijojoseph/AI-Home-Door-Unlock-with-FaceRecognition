import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.OUT)

p = GPIO.PWM(40, 50)

p.start(0)
x=180
d=(x/18)+2
def ser():
   i=4.5 
   
   while i<d :
      # p.ChangeDutyCycle(0)  # turn towards 90 degree
       #time.sleep(1) # sleep 1 second
#        p.ChangeDutyCycle(0)  # turn towards 0 degree
#        time.sleep(1) # sleep 1 second
      # turn towards 180 degree
       time.sleep(0.2) # sleep 1 second
       p.ChangeDutyCycle(i) # turn towards 180 degree
       i=i+0.7
  # while i>2.5:
   #    time.sleep(0.2) # sleep 1 second
    #   p.ChangeDutyCycle(i) # turn towards 180 degree
     #  i=i-0.3
       
    #p.stop()
def ser2():
 i=12.5   
 while i>4.5:
      time.sleep(0.2) # sleep 1 second
      p.ChangeDutyCycle(i) # turn towards 180 degree
      i=i-0.7

