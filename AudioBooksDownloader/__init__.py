#!/usr/bin/python
# coding: utf-8


"""
**************************
supported sites:
**************************
http://a-booka.ru/
http://www.audioknigi-online.com/
https://audioknigi.club/
**************************
"""
import sys
import getopt
from .models import *


class BooksDownloader(object):

    @staticmethod
    def download_book(url, download_dir=None):
        """

        :param url:
        :param download_dir:
        :return:
        """
        from .models.book_utils import BookUtils

        book = BookUtils.get_book_downloader(url)
        if book is None:
            print "site not supported: %s" % (url)
        else:
            book.get_files_list()
            BookUtils.save_book(book, download_dir=download_dir)

    @staticmethod
    def main(argv):
        output_dir = "tmp"
        try:
            opts, args = getopt.getopt(argv, 'u:o')
        except getopt.GetoptError:
            print "No url specified. exiting with error"
            print "usage: download_book.py -u <download_url> -o <output_dir>"
            sys.exit(2)

        url = None
        for opt, arg in opts:
            if opt == "-h":
                print "usage: download_book.py -u <download_url> -o <output_dir>"
                sys.exit()
            if opt == "-o" and len(arg) > 0:
                output_dir = arg
            if opt == '-u':
                url = arg

        if url is None:
            print "no url defined"
            exit(1)
        if output_dir is None:
            print "no save directory defined"
            exit(1)
        BooksDownloader.download_book(url, output_dir)

