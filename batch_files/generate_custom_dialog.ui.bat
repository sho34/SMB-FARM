:: do not print the commands when executing them
@echo off 
:: the command to be executed
pyside6-uic ../ui_files/edit_animal.ui -o ../UI_FILE_EDIT_ANIMAL.py
@REM pyside6-uic splashscreen.ui -o UI_FILE_SPLASH_SCREEN.py
:: what is printed when done
echo "python code for EDIT_ANIMAL.ui generated succesfully..!, press any key to exit"
:: wait for input
pause