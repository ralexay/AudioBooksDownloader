import abc
from bs4 import BeautifulSoup


class BookDownloader(object):
    def __init__(self, book_url):
        self.book_url = book_url
        self.book_title = None
        self.files_for_download = []

    @abc.abstractmethod
    def _get_book_title(self, soup):
        return

    @abc.abstractmethod
    def get_files_list(self):
        return

    def _get_html_soup(self):
        import book_utils
        html = book_utils.BookUtils.get_url(self.book_url)
        soup = BeautifulSoup(html, "html.parser")
        return (soup, html)

    def make_valid_url(self, url):
        url = url.replace(" ", "%20")
        return url
