#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "bs4>=0.0.2",
#     "requests>=2.34.2",
# ]
# ///
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('DOWNLOAD_PAGE_URL')
    return parser.parse_args()

def main():
    args = get_args()
    r = requests.get(args.DOWNLOAD_PAGE_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.main.find_all('a'):
        if link.string == 'Dat':
            print(urljoin(args.DOWNLOAD_PAGE_URL, link['href']))

if __name__ == '__main__':
    main()
