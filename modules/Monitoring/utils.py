from pynput import keyboard
from modules.Timer import *
from modules.Logging import *
from modules.Utils import *

chain_buffer = []
intervals_buffer = []


def writeln() -> None:
    global chain_buffer
    global intervals_buffer
    if chain_buffer and intervals_buffer:
        writer.info(msg=f'"{str(chain_buffer)}","{str(intervals_buffer)}"')
        chain_buffer = []
        intervals_buffer = []


def on_press(key) -> None:
    step = TIMER.step()
    if str(type(key)) != "<enum 'Key'>":
        if key.char == "'":
            return None
    if step == 0.0:
        writeln()
    else:
        intervals_buffer.append(step)
    if str(type(key)) == "<enum 'Key'>":
        chain_buffer.append(str(key))
    else:
        chain_buffer.append(key)


def start_input_monitoring() -> None:
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()
