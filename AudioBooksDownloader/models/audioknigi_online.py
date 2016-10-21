import json
import urllib2
from bs4 import BeautifulSoup
import demjson
import book_utils
from book_downloader import BookDownloader


class AudioknigiOnline(BookDownloader):

    def __init__(self, book_url):
        super(AudioknigiOnline, self).__init__(book_url)
        self.self_net_loc = 'audioknigi-online.com'

    def _get_book_title(self, soup):
        self.book_title = book_utils.BookUtils.validate_utf8(soup.find('h1', {'class': 'entry-title'}).text)


    def _get_playlist_file_url(self, soup):
        els = soup.find_all("script")
        for l in els:
            tmp = str(l)
            pos = tmp.find("var flashvars")
            if pos >= 0:
                tmp = tmp[pos:len(tmp)].replace("var flashvars =","")
                tmp = tmp.split(";")[0]
                invalidJsonPartLocation = tmp.find(",")
                tmp = "{" + tmp[invalidJsonPartLocation + 1:len(tmp)]

                tmp = urllib2.unquote(tmp).strip()
                pp = demjson.decode(tmp)
                if 'pl' in pp:
                    return pp['pl']
                if 'file' in pp:
                    return pp['file']
        return None

    def get_files_list(self):
        (soup,html) = self._get_html_soup()
        self._get_book_title(soup)
        playlist_url = self._get_playlist_file_url(soup)
        playlist_content = _BookUtils.get_url(playlist_url)

        if playlist_url.endswith(".xml"):
            # this file is ".xml"
            doc = BeautifulSoup(playlist_content, "xml")
            els = doc.find_all("location")
            for el in els:
                self.files_for_download.append(el)
        else:
            # this file ends as ".txt"
            data = json.loads(playlist_content) # json object
            for f in data['playlist']:
                file_name = f['file']
                self.files_for_download.append(file_name)