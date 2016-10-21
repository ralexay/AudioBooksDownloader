import unittest
from tests.fetch_files_list import FetchFilesListTest

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    ts = unittest.TestSuite()
    ts.addTest(FetchFilesListTest("test_audioknigi_club"))
    ts.addTest(FetchFilesListTest("test_audioknigi_online_com"))
    ts.addTest(FetchFilesListTest("test_mp3tales_info"))

    runner.run(ts)
