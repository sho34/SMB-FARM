:: do not print the commands when executing them
@echo off 
:: the command to be executed
pyside6-uic ../ui_files/main.ui -o ../UI_FILE.py
@REM pyside6-uic splashscreen.ui -o UI_FILE_SPLASH_SCREEN.py
:: what is printed when done
echo "python code for main.ui generated succesfully..!, press any key to exit"
:: wait for input
pause
