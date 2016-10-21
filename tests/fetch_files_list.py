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
