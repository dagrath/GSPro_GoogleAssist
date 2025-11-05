 curl "https://raw.githubusercontent.com/dagrath/GSPro_GoogleAssist/refs/heads/main/ha_control.py" -o C:\GolfSimScripts\ha_control_new.py
 TIMEOUT /T 5
 cd C:\GolfSimScripts\
 move /y ha_control.py ha_control_old.py
 TIMEOUT /T 1
 move /y ha_control_new.py ha_control.py
 start start_ha.bat
