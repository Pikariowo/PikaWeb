from PyQt6.QtWidgets import *
from PyQt6.QtCore import QEvent

def setUI(self):
    self.setStyleSheet("""
    QMainWindow {
        background-image: url('./imgs/Hikari_02.jpg');
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    """)
    """
    label = QLabel("歡迎", window)
    label.setGeometry(100, 100, 200, 50)
    label.setStyleSheet("color: white; font-size: 20px;")"""

def close():
    QApplication.quit()