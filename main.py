import keyboard as keyb
import time 
import pyautogui

score = 0
shorts = int(input("Enter how many shorts you want to see: "))
seconds = int(input("Because you want to view seconds: "))

keyb.wait("s")
for i in range(shorts):
    pyautogui.scroll(-100)
    time.sleep(seconds)
    score += 1
    print(f"All that's left is to view the shorts: {shorts - score}")