import keyboard
import pyautogui


while True:
    if keyboard.is_pressed('w'):
        pyautogui.press('up', presses=1)

    elif keyboard.is_pressed('s'):
        pyautogui.press('down', presses=1)

    elif keyboard.is_pressed('a'):
        pyautogui.press('left', presses=1)

    elif keyboard.is_pressed('0'):
        pyautogui.press('space', presses=1)

    elif keyboard.is_pressed('d'):
        pyautogui.press('right', presses=1)

