from flask import Flask
import pyautogui
import time

app = Flask(__name__)

@app.route("/press/<keys>")
def press(keys):
    # Example: keys = "ctrl+s" or "alt+f4"
    combo = keys.split("+")
    pyautogui.hotkey(*combo)
    return f"Pressed {keys}"

@app.route("/start_gspro")
def open_gspro():
    pyautogui.hotkey("win", "r")
    pyautogui.write("C:\\GSProV1\\Core\\GSP\\gspro.exe\n")
    time.sleep(15)
    pyautogui.hotkey("win","r")
    pyautogui.write("C:\\GSPro\\GSPro_Skytrak_1.98\\GSProDeviceInterface.exe\n")
    return "Running"

@app.route("/update_scripts")
def update_scripts():
    pyautogui.hotkey("win","r")
    pyautogui.write("C:\\GolfSimScripts\\update_scripts.bat\n")
    time.sleep(1)
    exit()

    return "Updated Scripts"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

