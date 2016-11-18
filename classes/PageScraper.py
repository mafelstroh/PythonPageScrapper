import collections
import re
import urllib2
import HtmlPageParser


class PageScraper(object):

    # Constructor
    def __init__(self, url):
        self.url = url
        self.counter_top_5 = 0
        self.counter_general = 0
        # Taken from Django's url regex validator
        self.valid_url_regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$',
            re.IGNORECASE)

    def validate_url(self):
        # Validate a well formed URL
        """

        :rtype: bool
        """
        if not re.match(self.valid_url_regex, self.url):
            print "ERROR: Malformed URL. Please provide a well formed \
                   URL (http://www.myDomain.com) "
            raise SystemExit
        else:
            return bool(1)

    def scrap(self):
        # Starting already with a parsed URL
        print("\n")
        print("Starting scrapping process...")

        order_response = urllib2.urlopen(self.url)
        order_content = order_response.read()

        hps = HtmlPageParser.HtmlPageParser()
        hps.feed(order_content)

        # Sort the array
        hps.tag_data.sort()

        # Get the 5 most used tags and show the count of them
        self.counter_top_5 = collections.Counter(hps.tag_data)\
            .most_common(5)

        # Get a general count of HTML tags
        self.counter_general = collections.Counter(hps.tag_data)

    def output(self, verbose=0):
        # Print output
        if bool(verbose):
            print("\n")
            print('### Written by Manuel F. Stroh S. ### \n')
            print('Page scrapping with Python...\n')

        print('Top 5 <HTML> tags and their counts is: ')
        print(self.counter_top_5)
        print("\n")

        print('General <HTML> tags used tags with their respective count: \n')
        print(collections.Counter(self.counter_general))
