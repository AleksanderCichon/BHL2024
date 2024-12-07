import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel

class TitleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.book_button = QPushButton("Book flight")
        self.exit_button = QPushButton("Exit")
        #self.exit_button.clicked.connect(self.exit)
        layout = QVBoxLayout(self)
        layout.addWidget(self.book_button)
        layout.addWidget(self.exit_button)


class BookWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("BOOK NOW")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

class MainWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setGeometry(100,100, 1000, 700)

        self.main_widgets = QStackedWidget()
        self.title_widget = TitleWindow()
        self.book_widget = BookWindow()

        self.title_widget.exit_button.clicked.connect(self.exit)
        self.title_widget.book_button.clicked.connect(lambda: self.set_page(1))
        #self.exit_button.show()

        self.main_widgets.addWidget(self.title_widget)
        self.main_widgets.addWidget(self.book_widget)
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.main_widgets)

    
    def exit(self):
        app.exit()

    def set_page(self, n):
        self.main_widgets.setCurrentIndex(n)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(app)
    window.show()

    sys.exit(app.exec())