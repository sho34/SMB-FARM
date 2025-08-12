import sys
from gui import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SplashScreen() 
    window.show()

    sys.exit(app.exec())
    