'''
@author:      Manuel F. Stroh S.
@description: Basic page scrapper that will
              generate stats about the most used tags in the
              indicated URL (http://ordergroove.com/company)
'''

# Importing re for Regular Expressions, urllib2 to fetch the URL contents
# and collections to have a smarter way to get statistics about the most used
# HTML tags.

# For regular expressions, find the most used tags
import re

import urllib2

import collections

# Start
array = []

order_groove_page = 'http://ordergroove.com/company'

order_groove_response = urllib2.urlopen(order_groove_page)

order_groove_content = order_groove_response.read()

html_tags = re.findall(r'<(\w+)\s+\w+.*?>', order_groove_content)

# Append each item to an array, then convert it to a
# collection.Counter in order to make easier some operations

for p in html_tags:
    array.append((str(p)))

# Sort the array
array.sort()

# Get the 5 most used tags and show the count of them
counter_top_5 = collections.Counter(array).most_common(5)

#Get a general count of HTML tags
counter_general = collections.Counter(array)

print '\n'
print('### Written by Manuel F. Stroh S. ### \n')
print '\n'
print('Top 5 <HTML> tags and their counts is ', counter_top_5)
print '\n'
print('General <HTML> tags used tags with their respective count: ')

print(collections.Counter(counter_general))