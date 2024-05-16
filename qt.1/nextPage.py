import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QPushButton, QVBoxLayout,
                             QWidget, )
from PyQt6.QtWebEngineWidgets import QWebEngineView


class mainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log in")
        self.setGeometry(100, 100, 600, 400)
        self.setFixedSize(600, 400)

        self.button = QPushButton("login", self)
        self.button.clicked.connect(self.go_to_next)
        self.button.setFixedSize(200, 50)

        layout = QVBoxLayout()
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def go_to_next(self):
        self.html_page = htmlPage()
        self.html_page.show()
        self.html_page.setFixedSize(800, 600)


class htmlPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HTML Page")
        self.setGeometry(150, 150, 800, 600)
        self.setFixedSize(800, 600)

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

        self.setCentralWidget(self.browser)


def main():
    app = QApplication(sys.argv)
    window = mainPage()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
