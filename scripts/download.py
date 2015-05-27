#!/usr/bin/env python

import requests
from pyquery import PyQuery as pq

PAGE_WITH_LINKS='http://thelegendofrandom.com/blog/sample-page'
EXPECTED_PREFIX='http://thelegendofrandom.com/files/tuts/'

def get_document():
    return pq(url=PAGE_WITH_LINKS)

def download_file(url, filepath, verbose=True):
    """ Download a single file """
    if(verbose): print("Downloading {0} to {1}".format(url, filepath))
    r = requests.get(url)
    with open(filepath, 'wb') as file:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                file.flush()

if __name__ == '__main__':
    d = get_document()
    for anchor in d.find('a'):
        e = pq(anchor)
        href = e.attr('href')
        if href and href.startswith(EXPECTED_PREFIX):
            filepath = href.replace(EXPECTED_PREFIX, '')
            download_file(href, filepath)
