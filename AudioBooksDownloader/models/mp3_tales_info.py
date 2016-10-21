from .book_downloader import BookDownloader


class MP3TalesInfo(BookDownloader):
    def __init__(self, book_url):
        super(MP3TalesInfo, self).__init__(book_url)
        self.self_net_loc = 'mp3tales.info'

    def _get_book_title(self, soup):
        h1 = soup.find('h1', {'itemprop': 'name'})
        tmp = h1.text
        self.book_title = tmp


    def get_files_list(self):
        (soup, html) = self._get_html_soup()
        self._get_book_title(soup)

        a = soup.find('span', {'class': 'mini'}).find("a")
        file_url = "http://%s%s" % (self.self_net_loc, a.attrs['href'])
        self.files_for_download.append(file_url)

        # download also book cover image
        img = soup.find('img', {'class': 'saturate'})
        file_url = "http://%s%s" % (self.self_net_loc, img.attrs['src'])
        self.files_for_download.append(file_url)
        print file_url