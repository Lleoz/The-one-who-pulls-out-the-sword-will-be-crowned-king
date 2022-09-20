import pyautogui
import keyboard
import time
import ctypes

def main():
    pyautogui.mouseDown()
    print("Start pulling the sword")

    for _ in range (10000):
        ctypes.windll.user32.mouse_event(
            0x0003, 0, -2000, 0, 0)
        if keyboard.is_pressed('f11'):
            break
        time.sleep(0.03)
    pyautogui.mouseUp()
    print("Stop pulling the sword")

keyboard.add_hotkey('f10', main)
