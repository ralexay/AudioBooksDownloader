#!/usr/bin/python
# coding: utf-8


import sys
from AudioBooksDownloader import BooksDownloader
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    # BooksDownloader.main(sys.argv[1:])
    BooksDownloader.download_book("http://abook.fm/book/%D0%9D%D0%B0%20%D0%B4%D0%B5%D1%81%D1%8F%D1%82%D0%BE%D0%BC%20%D0%BD%D0%B5%D0%B1%D0%B5")
