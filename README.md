# AudioBooksDownloader
Allows to download Audio Books websites

## Build Status 
[![CircleCI](https://circleci.com/gh/ralexay/AudioBooksDownloader/tree/master.svg?style=svg)](https://circleci.com/gh/ralexay/AudioBooksDownloader/tree/master)


##  Supported sites
*   http://abook.fm
*   http://audioknigi.club
*   http://www.audioknigi-online.com
*   http://mp3tales.info


## How to use
```python
from AudioBooksDownloader import BooksDownloader

if __name__ == "__main__":  
    BooksDownloader.download_book(book_url, download_dir=None)
```

