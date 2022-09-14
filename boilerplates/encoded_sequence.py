import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
import digitalio
import board
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


keyboard = Keyboard(usb_hid.devices)
k_util = KeyboardLayoutUS(keyboard)

def handle_sequence(array):
    for action in array:
        if isinstance(action, int):
            time.sleep(action / 1000)
        else:
            k_util.write(action)

def spin(text):
    k1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~! @#$%^&*()_-+={[}]|:;<,>.?/"
    k2 = "RM0uB%y-n&8{k+<=?W6w|r1c[h*jVJgK;z@C4SD> q(.bAtf3^_IFaYHp:$lPLv95GNTxmZ]7dO!~s}Qe/#2oEUX,)i"

    result = ""
    for letter in text:
        if letter in k2:
            result += k1[k2.index(letter)]
        else:
            result += letter
    return result

## Startup Sequence
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
for i in range(6):
    led.value = not led.value
    time.sleep(0.25)
led.value = True

handle_sequence([spin("encoded1"), "\t", 200, spin("encoded2"), "\n"])