import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
import digitalio
import board
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
k_util = KeyboardLayoutUS(keyboard)

def press(keycode_input):
    keyboard.press(keycode_input)
    time.sleep(0.15)
    keyboard.release(keycode_input)

def handle_sequence(array):
    for action in array:
        if isinstance(action, int):
            time.sleep(action / 1000)
        else:
            k_util.write(action)

## Startup Sequence
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
for i in range(6):
    led.value = not led.value
    time.sleep(0.5)
led.value = True


handle_sequence(["field1", 200, "\t\t\t\t", 300, "\n", 200, "field2", 200, "\n"])