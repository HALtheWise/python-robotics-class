# This is your main script.

from time import sleep
from starter_code import led_on, led_off, wait_for_button_press, drive_forward, turn_left, turn_right

while True:
    led_off()
    sleep(1)
    led_on()
    sleep(1)

led_on()
wait_for_button_press()

led_off()
drive_forward()
turn_left()
drive_forward()
turn_right()
