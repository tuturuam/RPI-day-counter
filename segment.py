import RPi.GPIO as GPIO
import time
import date_from
GPIO.setmode(GPIO.BCM)
 
# GPIO ports for the 7seg pins
segments =  (1, 21, 6, 19, 26, 12, 5, 13)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline
  
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
               
# GPIO ports for the digit 0-3 pins 
digits = (7,16,20,0)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
                
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)
                             
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}

try:
    while True:
        s = str(date_from.d3.days).rjust(4)
        for digit in range(4):
            for loop in range(0, 7):
                GPIO.output(segments[loop], num[s[digit]][loop])
                GPIO.output(13, 0)
            GPIO.output(digits[digit], 0)
            time.sleep(0.001)
            GPIO.output(digits[digit], 1)

finally: 
    GPIO.cleanup()
