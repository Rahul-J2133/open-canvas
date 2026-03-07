# to be integrated later into care.py to move mouse cursor based on hand movements instead of drawing on the canvas.
# This will allow for more intuitive control of the cursor using hand gestures.

import pyautogui

# Move the mouse cursor to a specific position
pyautogui.moveTo(x=100, y=100, duration=1)  # Move to coordinates (100, 100) over 1 second

# You can also move relative to the current position
pyautogui.moveRel(xOffset=50, yOffset=50, duration=10)  # Move 50 pixels right and 50 pixels down over 1 second

# # Perform a left mouse button click at the current cursor position
# pyautogui.click()

# You can also specify the coordinates to click at
pyautogui.click(x=100, y=100, button="right")

# # You can specify the number of clicks and the interval between them
# pyautogui.click(clicks=2, interval=0.5)  # Double click with a 0.5-second interval

# # You can also specify which button to click (left, middle, right)
# pyautogui.click(button='right')  # Right-click
