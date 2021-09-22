import time
import pyautogui

def SendMessage():
    time.sleep(1)
    text = open("messages.txt");
    for i in text:
        pyautogui.typewrite(i)
        pyautogui.press("enter")

SendMessage()