import time
import pyautogui 
import pyperclip

time.sleep(3) 
p = pyautogui.locateOnScreen("login.png",confidence=.5)
if p: 
    x, y = pyautogui.center(p) 
    print(p)
    pyautogui.click(x, y)
    
    # 入力した文字列をクリップボードにコピー
    pyperclip.copy('こんにちは、世界！')

    # Ctrl+vで貼り付け
    pyautogui.hotkey('ctrl', 'v')