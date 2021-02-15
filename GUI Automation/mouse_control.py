import pyautogui
# Up is negative, down is positive
# Right is positive, left is negative
# (0, 0) is the top left corner
#   -
# -   +
#   +
pyautogui.moveRel(200, -1000, duration=2)  # Up and to the right
print(pyautogui.position())
# pyautogui.moveTo(10, 10)
# pyautogui.displayMousePosition()
# pyautogui.click(2998, -514)
