from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()

sleep(3)

for i in range (100):
    keyboard.type(str(i))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(0.05)
