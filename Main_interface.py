'''from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic
import sys
import os

class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        self.load_GUI()
    
    def load_GUI(self):
        
        uic.loadUi(f'{os.path.dirname(os.path.realpath("Main.ui"))}\interface\Main.ui')
        
        self.show()

def main():
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    '''

