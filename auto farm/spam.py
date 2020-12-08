import pyautogui, time

time.sleep(5)

f = open("farm", 'r')

def xp():

  for palavra in f:
    pyautogui.typewrite(palavra)
    time.sleep(2)
    pyautogui.press("enter")

  time.sleep(1)
  xp()

xp()
  #executar a cada 2hrs e 1 minuto