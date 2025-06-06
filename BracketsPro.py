from pynput import keyboard
import pyautogui
import threading

waiting_for_close = False

def on_press(key):
    global waiting_for_close

    try:
        if hasattr(key, 'char'):
            char = key.char

            if char == '(':
                waiting_for_close = True

            elif waiting_for_close and char.isalpha():
                threading.Thread(target=insert_closing_bracket).start()
                waiting_for_close = False

    except Exception as e:
        print("Error:", e)

def insert_closing_bracket():
    pyautogui.write(')', interval=0)
    pyautogui.press('left')

# ✅ Use this pattern to keep it running forever
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
