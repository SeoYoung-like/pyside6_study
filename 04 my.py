# ---------------------------------
# PyQt6 용 module
# import sys
# import PyQt6.QtCore
# from PyQt6.QtWidgets import (QApplication, QWidget,
#                                QLabel)
# ---------------------------------
# PySide6 용 module
import sys
import PySide6.QtCore
from PySide6.QtCore import Slot
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (QApplication, QWidget,
                               QLabel, QPushButton)

# ================================
# define classes for this program


@Slot()
def say_hello():
    print("Button clicked, Hello!")

class Image_laundary(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(200, 200, 400, 200)
        self.setWindowIcon(QIcon("laundry_icon.webp"))
        self.setWindowTitle("이미지 세탁기 - 메타데이터 중복 해제")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        hello_label = QLabel(self)
        hello_label.setText('이미지 프로그램이다!')
        hello_label.setFont(QFont("맑은 고딕", 10))
        hello_label.move(150,90)

        hello02_label = QLabel(self)
        hello02_label.setText('안녕하세요')
        hello02_label.setFont(QFont("맑은 고딕", 10))
        hello02_label.move(50,90)

        button = QPushButton("Click me", self)
        button.clicked.connect(say_hello)
        button.move(10, 10)
        button.show()


# ===============================
# Run the program
if __name__ == '__main__':
    print(PySide6.__version__)
    print(PySide6.QtCore.__version__)

    # Event Loop 등을 위한 QApplication instance 생성.
    app = QApplication(sys.argv)
    window = Image_laundary()
    # Event Loop 시작.
    sys.exit(app.exec())