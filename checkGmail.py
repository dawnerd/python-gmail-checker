#! /usr/bin/env python
# encoding: utf-8
"""
checkGmail.py

Checks for new gmail messages and displays then via growl

Requires:
	growl python bindings
	feedparser

usage:

python checkGmail.py username@gmail.com password
"""
import sys
import os
import time
import feedparser
import Growl

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]
EMAIL_FEED = 'https://'+str(USERNAME)+':'+str(PASSWORD)+'@mail.google.com/mail/feed/atom'
GROWL_DELAY = 0

def grab_feed():
	return feedparser.parse(EMAIL_FEED)

def main():
	gnotify = Growl.GrowlNotifier('checkGmail',['email'])
	gnotify.register()
	gimage = Growl.Image.imageWithIconForApplication('mail.app')

	try:
		f = grab_feed()
								
		for node in f.entries:
			try:
				title = node.title
			except:
				title = '(No Subject)'

			try:
				summary = node.summary
			except:
				summary = '[blank message]'
			
			gnotify.notify('email',title,summary,icon=gimage)
			time.sleep(GROWL_DELAY)
							
	except:
		print 'error'
		raise
		
if __name__ == '__main__':
	main()