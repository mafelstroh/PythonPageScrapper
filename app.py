# -*- coding: utf-8 -*-
# Code by Manuel F. Stroh S.
'''
Basic page scrapper that will generate stats about the most HTML used tags in
the given URL
'''

from classes import PageScraper
import sys
import urlparse

if __name__ == '__main__':
    # Checking for default UTF-8 encoding
    default_encoding = 'utf-8'
    if sys.getdefaultencoding() != default_encoding:
        reload(sys)
        sys.setdefaultencoding(default_encoding)

        if len(sys.argv) > 1:
            url = sys.argv[1]
            print url
            parsed_url = urlparse.urlparse(url)
            valid = bool(parsed_url.scheme)
            if not valid:
                print "Please provide a valid url as an input param"
            else:
                # Instantiate
                ps = PageScraper.PageScraper(url)
                ps.scrap()
                print '\n'
                print "Done"
        else:
            print "Please provide the url as an input param"
