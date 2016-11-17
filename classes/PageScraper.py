import collections
import re
import urllib2
import urlparse


class PageScraper(object):

    # Constructor
    def __init__(self, url):
        self.url = url
        self.counter_top_5 = 0
        self.counter_general = 0
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
        if not re.match(self.valid_url_regex, self.url):
            print "ERROR: Malformed URL. Please provide a well formed \
                   URL (http://www.myDomain.com) "
            raise SystemExit

    def scrap(self):
        # Starting already with a parsed URL
        print "Starting scrapping process..."

        scrapped_data_array = []
        order_response = urllib2.urlopen(self.url)
        order_content = order_response.read()

        # Using basic regular expression to fetch HTML tags
        html_tags = re.findall(r'<(\w+)\s+\w+.*?>', order_content)

        # Append each item to an array, then convert it to a
        # collection.Counter in order to make easier some operations
        for p in html_tags:
            scrapped_data_array.append((str(p)))

        # Sort the array
        scrapped_data_array.sort()

        # Get the 5 most used tags and show the count of them
        self.counter_top_5 = collections.Counter(scrapped_data_array)\
            .most_common(5)

        # Get a general count of HTML tags
        self.counter_general = collections.Counter(scrapped_data_array)

    def output(self):
        print '\n'
        print('### Written by Manuel F. Stroh S. ### \n')
        print '\n'
        print('Top 5 <HTML> tags and their counts is ', self.counter_top_5)
        print '\n'
        print('General <HTML> tags used tags with their respective count: ')

        print(collections.Counter(self.counter_general))
