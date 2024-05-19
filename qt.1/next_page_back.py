from next_page_html import html_page


def go_to_next(parent_window):
    # Create an instance of the htmlPage class and show it
    parent_window.html_page = html_page()
    parent_window.html_page.show()
    parent_window.html_page.setFixedSize(800, 600)
