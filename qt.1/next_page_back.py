from PyQt6.QtCore import Qt
from next_page_front import html_page
from PyQt6.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QWidget, )


class main_page(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set the window title and dimensions
        self.setWindowTitle("Log in")
        self.setGeometry(100, 100, 600, 400)
        self.setFixedSize(600, 400)

        # Create a button and connect its clicked signal to the go_to_next method
        self.button = QPushButton("login", self)
        self.button.clicked.connect(self.go_to_next)
        self.button.setFixedSize(200, 50)

        # Create a vertical layout and add the button to it, with the button centered
        layout = QVBoxLayout()
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Create a widget, set its layout, and set it as the central widget of the window
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def go_to_next(self):
        # Create an instance of the htmlPage class and show it
        self.html_page = html_page()
        self.html_page.show()
        self.html_page.setFixedSize(800, 600)
