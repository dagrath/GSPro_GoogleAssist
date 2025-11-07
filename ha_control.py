from flask import Flask
import pyautogui
import time
import sys

app = Flask(__name__)

@app.route("/press/<keys>")
def press(keys):
    # Example: keys = "ctrl+s" or "alt+f4"
    combo = keys.split("+")
    pyautogui.hotkey(*combo)
    return f"Pressed {keys}"
    
@app.route("/pressmore/<keys>")
def pressmore(keys):
    # Example: keys = "ctrl+s" or "alt+f4"
    combo = keys.split("+")
   # Press the 'a' key down
    pyautogui.keyDown(*combo)
    
    # Wait for half a second
    time.sleep(0.4)
    
    # Release the 'a' key
    pyautogui.keyUp(*combo)
    return f"Pressed {keys}"
    
@app.route("/start_gspro")
def open_gspro():
    pyautogui.hotkey("win", "r")
    pyautogui.write("C:\\GSProV1\\Core\\GSP\\gspro.exe\n")
    time.sleep(15)
    pyautogui.hotkey("win","r")
    pyautogui.write("C:\\GSPro\\GSPro_Skytrak_1.98\\GSProDeviceInterface.exe\n")
    return "Running"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





