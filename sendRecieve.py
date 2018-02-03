# Imports.
import RPi.GPIO as GPIO
import time

# Set pins.
outPin = 11
inPin = 35

def setup():    
    # Pin numbering system.
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    
    # Output Pin.
    GPIO.setup(outPin, GPIO.OUT)   # Set outPin's mode is output
    GPIO.output(outPin, GPIO.HIGH) # Set outPin high(+3.3V)

    # Input Pin.
    GPIO.setup(inPin, GPIO.IN)
  
def blink():
    delay = 0.1
    
    while True:
        # Turn on.
        GPIO.output(outPin, GPIO.HIGH)
        print(GPIO.input(inPin))
        time.sleep(delay)

        # Turn off.
        #GPIO.output(outPin, GPIO.LOW)
        print(GPIO.input(inPin))
        time.sleep(delay)
        
def destroy():
  GPIO.output(outPin, GPIO.LOW)   # led off
  GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    blink()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
