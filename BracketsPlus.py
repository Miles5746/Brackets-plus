from pynput import keyboard
import pyautogui

def on_press(key):
    try:
        if key.char == '(':  # if the key pressed is '('
            pyautogui.write(')', interval=0.01)  # type ()
    except AttributeError:
        pass  # handles special keys like shift, ctrl, etc.

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
