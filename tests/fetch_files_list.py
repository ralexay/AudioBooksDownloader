import unittest


class FetchFilesListTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_audioknigi_club(self):
        from AudioBooksDownloader.models.book_utils import BookUtils
        book = BookUtils.get_book_downloader('https://audioknigi.club/murkok-maykl-grezyaschiy-gorod')
        self.assertIsNotNone(book, "Book downloader not found")

        book.get_files_list()
        self.assertTrue(len(book.files_for_download) > 0, "no files found for download")

    def test_audioknigi_online_com(self):
        from AudioBooksDownloader.models.book_utils import BookUtils
        book = BookUtils.get_book_downloader('http://www.audioknigi-online.com/ghost-book.html')
        self.assertIsNotNone(book, "Book downloader not found")

        book.get_files_list()
        self.assertTrue(len(book.files_for_download) > 0, "no files found for download")

    def test_mp3tales_info(self):
        from AudioBooksDownloader.models.book_utils import BookUtils
        book = BookUtils.get_book_downloader('http://mp3tales.info/tales/?id=673')
        self.assertIsNotNone(book, "Book downloader not found")

        book.get_files_list()
        self.assertTrue(len(book.files_for_download) > 0, "no files found for download")
        
    def test_abook_fm(self):    
        from AudioBooksDownloader.models.book_utils import BookUtils
        book = BookUtils.get_book_downloader('http://abook.fm/book/%D0%9D%D0%B0%20%D0%B4%D0%B5%D1%81%D1%8F%D1%82%D0%BE%D0%BC%20%D0%BD%D0%B5%D0%B1%D0%B5')
        self.assertIsNotNone(book, "Book downloader not found")

        book.get_files_list()
        self.assertTrue(len(book.files_for_download) > 0, "no files found for download")
