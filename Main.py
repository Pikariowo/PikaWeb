from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QEvent
from UI import *
from UI_Design.index import *
import sys, os, webbrowser

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        setUI(self)

        self.Button_1.clicked.connect(self.browser) #開啟瀏覽器(網頁)
        self.Button_3.clicked.connect(close) #關閉UI

    def browser(self):
        html_file = "./index.html"
        html_path = os.path.abspath(html_file)
        #開啟瀏覽器
        webbrowser.open_new_tab(f"file://{html_path}")

    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            if self.isMaximized():
                print("視窗最大化")
            elif self.isMinimized():
                print("視窗最小化")
            else:
                print("視窗恢復到普通大小")
        super().changeEvent(event)

    def closeEvent(self, event):
        print("視窗被關閉")
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())