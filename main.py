import sys
from PyQt6.QtWidgets import QApplication
from gui import StoreGUI

def main():
    app = QApplication(sys.argv)
    window = StoreGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()