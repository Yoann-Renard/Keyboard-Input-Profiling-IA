from pynput import keyboard
from modules.Timer import *


def on_press(key):
    try:
        print(key.char, end='')
        print(TIMER.step())
    except AttributeError:
        print(key, end='')
        print(TIMER.step())


def start_input_monitoring() -> None:
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()