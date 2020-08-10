# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio


# >> this will count to 100 and write the number line for line on your keyboard<<

from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()

sleep(3)

for i in range (100):
    keyboard.type(str(i))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(0.05)
