from machine import Pin, PWM, Signal
from time import sleep

led = Signal(Pin(2, Pin.OUT), invert=True)

def led_on():
    led.on()

def led_off():
    led.off()

button = Pin(5, Pin.IN, Pin.PULL_UP)

def wait_for_button_press():
    while button.value() == True:
        sleep(0.01)

SECONDS_PER_FOOT = 2.0
SECONDS_PER_DEGREE = 0.02

def drive_forward(dist = 1.0):
    """
    Moves forward the provided distance, in feet
    """
    set_left_motor(1.0)
    set_right_motor(1.0)
    sleep(dist * SECONDS_PER_FOOT)
    stop()

def turn_left(angle = 90):
    """
    Turns left the provided distance, in degrees
    """
    set_left_motor(-0.5)
    set_right_motor(0.5)
    sleep(angle * SECONDS_PER_DEGREE)
    stop()

def turn_right(angle = 90):
    """
    Turns right the provided distance, in degrees
    """
    set_left_motor(0.5)
    set_right_motor(-0.5)
    sleep(angle * SECONDS_PER_DEGREE)
    stop()
    
def stop():
    set_left_motor(0)
    set_right_motor(0)
    sleep(0.2)

left_motor = PWM(Pin(14), freq=50, duty=77)
right_motor = PWM(Pin(12), freq=50, duty=77)

def set_left_motor(power):
    """
    Sets the power of the left motor, on a scale of -1.0 to 1.0
    """
    _set_motor(left_motor, power)

def set_right_motor(power):
    """
    Sets the power of the right motor, on a scale of -1.0 to 1.0
    """
    _set_motor(right_motor, power)

def _set_motor(motor, power):
    if power > 1.0:
        power = 1.0
    if power < -1.0:
        power = -1.0

    duty_cycle = 77 + 37*power
    motor.duty(int(duty_cycle))