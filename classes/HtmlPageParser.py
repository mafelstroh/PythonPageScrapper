import HTMLParser

class HtmlPageParser(HTMLParser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        tag