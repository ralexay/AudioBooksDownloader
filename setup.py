from distutils.core import setup

setup(
    name='AudioBooksDownloader',
    version='0.0.1',
    packages=['tests', 'AudioBooksDownloader', 'AudioBooksDownloader.models'],
    url='https://github.com/ralexay/AudioBooksDownloader',
    license='',
    author='ralexay',
    author_email='',
    description='', requires=['bs4', 'requests', 'demjson']
)
