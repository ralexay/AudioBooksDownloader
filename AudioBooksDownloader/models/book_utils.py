import os
import urllib
import urlparse
import requests


class BookUtils(object):
    @staticmethod
    def _save_file(url, fname):
        print "downloading ", url
        r = requests.get(url, stream=True)
        with open(fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
                    # print "done", fname

    @staticmethod
    def save_book(book, download_dir=None):
        # create directory if not exists
        dir_name = book.book_title

        if download_dir is not None:
            dir_name = os.path.join(download_dir, dir_name)

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        # download all files
        counter = 1
        print "files for download " + str(len(book.files_for_download))
        for f in book.files_for_download:
            fname_tmp = os.path.basename(f)
            file, extension = os.path.splitext(fname_tmp)

            if extension in [".mp3"]:
                file_name = str(counter).zfill(3) + ".mp3"
            else:
                file_name = fname_tmp
            save_to_file = os.path.join(dir_name, file_name)
            BookUtils._save_file(f, save_to_file)
            counter += 1

        # leave comment file with download source
        f = open(os.path.join(dir_name, 'readme.txt'), 'w')
        f.write("This book was downloaded from " + book.book_url)
        f.close()

    @staticmethod
    def get_book_downloader(url):
        from .abook_fm import AbookFM
        from .audioknigi_club import AudioknigiClub
        from .audioknigi_online import AudioknigiOnline
        from .mp3_tales_info import MP3TalesInfo

        o = urlparse.urlparse(url)
        netloc = o.netloc.replace('www.', '')

        def f(netloc):
            return {
                'audioknigi.club': AudioknigiClub,
                'audioknigi-online.com': AudioknigiOnline,
                'abook.fm': AbookFM,
                'mp3tales.info': MP3TalesInfo
            }.get(netloc)

        try:
            return f(netloc)(url)
        except Exception, e:
            return None

    @staticmethod
    def get_url(url, data=None):
        try:
            if data is not None:
                data = urllib.urlencode(data)

            headers = {
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip,deflate,sdch',
                'Referer': '',
                'Accept-Language': 'en-US,en;q=0.8,he;q=0.6,ru;q=0.4',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
            }
            r = requests.get(url, headers=headers)
            return r.text
        except Exception, e:
            print e
            return None

    @staticmethod
    def validate_utf8(text):
        if type(text) != unicode:
            return unicode(text, 'utf8')
        return text
