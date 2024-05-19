from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView


class html_page(QMainWindow):
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






