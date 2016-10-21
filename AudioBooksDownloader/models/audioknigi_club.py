import re
import book_utils
from book_downloader import BookDownloader


class AudioknigiClub(BookDownloader):
    def __init__(self, book_url):
        super(AudioknigiClub, self).__init__(book_url)
        self.self_net_loc = 'audioknigi.club'

    def _get_book_title(self, soup):
        el = soup.find_all("h1", {"class": "topic-title"})
        self.book_title = book_utils.BookUtils.validate_utf8(el[0].text.strip('\n').strip())

    def get_files_list(self):
        (soup, html) = self._get_html_soup()
        self._get_book_title(soup)
        scripts = soup.find_all("script")
        for script in scripts:
            if str(script).find(".audioPlayer(") > 0:
                s = unicode(str(script), 'utf-8')
                arr = re.findall("([\d+]{2,})", s, flags=re.UNICODE | re.IGNORECASE)
                from book_utils import BookUtils
                json_file = BookUtils.get_url("http://audioknigi.club/rest/bid/" + arr[0]).replace("\/","/")

                # import HTMLParser
                # h = HTMLParser.HTMLParser()
                # json_file = h.unescape(json_file)

                s = unicode(str(json_file), 'utf-8')
                #pattern = '([mp3:\"?]http:\/\/[\w\s\.\/\-\,\(\)]*\"?.mp3)'
                pattern = '(http:\/\/[\w\s\.\/\-\,\(\)]*\"?.mp3)'
                array = re.findall(pattern, s, flags=re.UNICODE | re.IGNORECASE)
                for item in array:
                    # item = self.make_valid_url(item)
                    item = item.strip('"')
                    #self.files_for_download.append(item.replace("\"",""))
                    self.files_for_download.append(item)
                    print item