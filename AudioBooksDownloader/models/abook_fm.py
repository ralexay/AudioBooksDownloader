import json
import re
import book_utils
from book_downloader import BookDownloader


class AbookFM(BookDownloader):
    def __init__(self, book_url):
        super(AbookFM, self).__init__(book_url)
        self.self_net_loc = 'abook.fm'

    def _get_book_title(self, soup):
        h1 = soup.find('div', {'class': 'page-header'}).find("h1")
        tmp = h1.text.decode('utf-8', "ignore").splitlines()
        self.book_title = ' '.join(tmp)
        self.book_title = book_utils.BookUtils.validate_utf8(self.book_title.strip(' \t\n\r'))

    def get_files_list(self):
        (soup, html) = self._get_html_soup()
        self._get_book_title(soup)

        regex = re.compile('AbookJPlayer\(([\d]+)', re.IGNORECASE | re.MULTILINE | re.UNICODE)
        book_id = regex.findall(html)[0]
        playlist_url = "http://abook.fm/rest/book/%s/chapters?format=json" % (book_id)
        # print "bookid", book_id, playlist_url

        playlist_json = json.loads(book_utils.BookUtils.get_url(playlist_url))
        for item in playlist_json:
            files = item['files']
            for f in files:
                file_url = "http://abook.fm%s" % (f['path'])
                self.files_for_download.append(file_url)
                #print file_url
