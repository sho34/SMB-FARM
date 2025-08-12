:: do not print the commands when executing them
@echo off 
:: the command to be executed
pyside6-rcc ../resource_files/resource.qrc -o ../resource_rc.py
@REM pyside6-uic splashscreen.ui -o UI_FILE_SPLASH_SCREEN.py
:: what is printed when done
echo "succes..!, press any key to exit"
:: wait for input
pause