import pyautogui, time

while True:

  time.sleep(5)

  f = open("farm1", 'r')

  for palavra in f:
    pyautogui.typewrite(palavra)
    time.sleep(2)
    pyautogui.press("enter")
  time.sleep(7260)  #executar a cada 2hrs e 1 minuto