#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Code by Manuel F. Stroh S.
'''
Basic page scrapper that will generate stats about the most HTML used tags in
the given URL
'''

from classes import PageScraper
import sys
import argparse

if __name__ == '__main__':
    # Default URL to scrap if not provided by the user
    DEFAULT_URL = "http://ordergroove.com/company"
    # Checking for default UTF-8 encoding
    DEFAULT_ENCODING = 'utf-8'

    if sys.getdefaultencoding() != DEFAULT_ENCODING:
        reload(sys)
        sys.setdefaultencoding(DEFAULT_ENCODING)

        # Makes use of argparse.ArgumentParser() to handle
        # the arguments that the user has entered.
        parser = argparse.ArgumentParser()

        # Optional making it dynaming in a manner that the
        # user can specify another URL to be scrapped.
        parser.add_argument("-u", "--url",
                            help="Specifies the URL to be scrapped. If not provided "
                            "will use default page given for the exercise (" +
                            DEFAULT_URL + ")",
                            type=str,
                            default=DEFAULT_URL)

        # Action store_true will make this value boolean when received.
        parser.add_argument("-v",
                            "--verbose",
                            help="Displays output with more information",
                            action="store_true")

        # Parse the arguments
        args = parser.parse_args()

        if args.verbose:
            print "\n"
            print "Scrapping process...using the following URL: " + args.url
            print "\n"
            print "---------------------------------------"

        # Parse URL, start the process here
        ps = PageScraper.PageScraper(args.url)

        # Validation method before starting the process
        ps.validate_url()
        ps.scrap()
        ps.output(args.verbose)

        print "\nDone...!"
