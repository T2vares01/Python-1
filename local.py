import pyautogui as py
from time import sleep

x = py.position()
print('sua posição sera informada em :')
for c in range(1,8):
    print(c,end=',')
    sleep(1)
print('8',x)