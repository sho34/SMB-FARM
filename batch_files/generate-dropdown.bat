:: do not print the commands when executing them
@echo off 
:: the command to be executed
pyside6-uic ../ui_files/dropdown.ui -o ../UI_FILE_DROPDOWN.py
@REM pyside6-uic splashscreen.ui -o UI_FILE_SPLASH_SCREEN.py
:: what is printed when done
echo "succes..!, press any key to exit"
:: wait for input
pause