import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget


# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Flight Booker")
        self.setGeometry(100,100, 1000, 700)
        #self.showFullScreen()
        #self.showFullScreen()
        self.book_button = QPushButton("Book flight")
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.exit)
        layout = QVBoxLayout(self)
        layout.addWidget(self.book_button)
        layout.addWidget(self.exit_button)
        #self.exit_button.show()
    
    def exit(self):
        app.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(app)
    window.show()

    sys.exit(app.exec())