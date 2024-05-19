import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QPushButton, QVBoxLayout,
                             QWidget, )
from PyQt6.QtWebEngineWidgets import QWebEngineView


class mainPage(QMainWindow):
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
        self.html_page = htmlPage()
        self.html_page.show()
        self.html_page.setFixedSize(800, 600)


class htmlPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and dimensions
        self.setWindowTitle("HTML Page")
        self.setGeometry(150, 150, 800, 600)
        self.setFixedSize(800, 600)

        # Create a QWebEngineView and set its HTML content
        self.browser = QWebEngineView()
        self.browser.setHtml(
            "<html>"
                    "<body>"
                             "<h1>"
                                    "Hello World"
                             "</h1>"
                    "</body>"
            "</html>"
        )

        # Set the QWebEngineView as the central widget of the window
        self.setCentralWidget(self.browser)


def main():
    # Create the QApplication and the mainPage instance, then show the mainPage and start the event loop
    app = QApplication(sys.argv)
    window = mainPage()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()