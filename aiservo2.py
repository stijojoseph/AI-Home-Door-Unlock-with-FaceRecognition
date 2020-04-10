import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)

p = GPIO.PWM(3, 50)

p.start(0)
x=180
d=(x/18)+2
def ser2():
   i=5.5 
   
   while i<d :
      # p.ChangeDutyCycle(0)  # turn towards 90 degree
       #time.sleep(1) # sleep 1 second
#        p.ChangeDutyCycle(0)  # turn towards 0 degree
#        time.sleep(1) # sleep 1 second
      # turn towards 180 degree
       time.sleep(0.2) # sleep 1 second
       p.ChangeDutyCycle(i) # turn towards 180 degree
       i=i+1.5
  # while i>2.5:
   #    time.sleep(0.2) # sleep 1 second
    #   p.ChangeDutyCycle(i) # turn towards 180 degree
     #  i=i-0.3
       
    #p.stop()
def ser():
 i=12.5   
 while i>5.5:
      time.sleep(0.2) # sleep 1 second
      p.ChangeDutyCycle(i) # turn towards 180 degree
      i=i-1.5
     