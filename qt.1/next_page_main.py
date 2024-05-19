import sys
from PyQt6.QtWidgets import QApplication
from next_page_front import main_page


def next_page_main():
    # Create the QApplication and the mainPage instance, then show the mainPage and start the event loop
    app = QApplication(sys.argv)
    window = main_page()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    next_page_main()