import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget



class MainWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setGeometry(100,100, 1000, 700)

        self.main_widgets = QStackedWidget()
        self.title_widget = QWidget()
        #self.showFullScreen()
        #self.showFullScreen()
        self.title_widget.book_button = QPushButton("Book flight")
        self.title_widget.exit_button = QPushButton("Exit")
        self.title_widget.exit_button.clicked.connect(self.exit)
        layout = QVBoxLayout(self.title_widget)
        layout.addWidget(self.title_widget.book_button)
        layout.addWidget(self.title_widget.exit_button)
        #self.exit_button.show()

        self.main_widgets.addWidget(self.title_widget)
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.main_widgets)
    
    def exit(self):
        app.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(app)
    window.show()

    sys.exit(app.exec())