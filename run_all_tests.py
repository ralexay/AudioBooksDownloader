import unittest
from tests.fetch_files_list import FetchFilesListTest
import sys

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    runner = unittest.TextTestRunner()
    ts = unittest.TestSuite()
    ts.addTest(FetchFilesListTest("test_audioknigi_club"))
    ts.addTest(FetchFilesListTest("test_audioknigi_online_com"))
    ts.addTest(FetchFilesListTest("test_mp3tales_info"))
    ts.addTest(FetchFilesListTest("test_abook_fm"))

    runner.run(ts)
