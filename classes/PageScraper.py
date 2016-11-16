import collections
import re
import urllib2

class PageScrapper(object):

    # Constructor
    def __init__(self, url):
        self.url = url

    def scrap(self):
        print "Starting scrapping process..."

        scrapped_data_array = []
        order_response = urllib2.urlopen(self.url)
        order_content = order_response.read()
        html_tags = re.findall(r'<(\w+)\s+\w+.*?>', order_content)

        # Append each item to an array, then convert it to a
        # collection.Counter in order to make easier some operations
        for p in html_tags:
            scrapped_data_array.append((str(p)))

        # Sort the array
        scrapped_data_array.sort()

        # Get the 5 most used tags and show the count of them
        counter_top_5 = collections.Counter(scrapped_data_array).most_common(5)

        # Get a general count of HTML tags
        counter_general = collections.Counter(scrapped_data_array)

        print '\n'
        print('### Written by Manuel F. Stroh S. ### \n')
        print '\n'
        print('Top 5 <HTML> tags and their counts is ', counter_top_5)
        print '\n'
        print('General <HTML> tags used tags with their respective count: ')

        print(collections.Counter(counter_general))
