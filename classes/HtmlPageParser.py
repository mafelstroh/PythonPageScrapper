# Making use of HTMLParser instead of
# using re to find handle HTML parsing
from HTMLParser import HTMLParser


class HtmlPageParser(HTMLParser):

    def __init__(self):
        # initialize the base class
        HTMLParser.__init__(self)
        self.tag_data = []

    def handle_starttag(self, tag, attrs):
        # Append the scrapped tagas to an array
        self.tag_data.append((str(tag)))
