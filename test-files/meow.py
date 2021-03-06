#!/usr/bin/python

#
# from http://www.pythonforbeginners.com/feedparser/using-feedparser-in-python
# installed feedparser with `pip`, after installing pip with apt-get
#

import feedparser
import time
from subprocess import check_output

# ------
# uptime
# ------

uptime = check_output(['uptime'])
print "\n"
print '-------------------------------------------------------------'
print uptime.strip()
print '-------------------------------------------------------------'
print "\n"


# --------------------
# tribune (feedparser)
# --------------------

d = feedparser.parse('https://news.google.com/news/rss/search/section/q/thinksystem/thinksystem?hl=en-CA&gl=CA&ned=ca')

# print all posts
count = 1
blockcount = 1
for post in d.entries:
    if count % 5 == 1:
        print "\n" + time.strftime("%a, %b %d %I:%M %p") + '  ((( TRIBUNE - ' + str(blockcount) + ' )))'
        print "-----------------------------------------\n"
        blockcount += 1
    print post.title + "\n" + post.link
    count += 1
