#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return self.fed

class Tagger(object):
    def __init__(self):
        pass

    def clean(self, html_input):
	    s = MLStripper()
	    s.feed(html_input)
	    return s.get_data()

    def get_tags(self, html_input):
    	res = ""
    	l = self.clean(html_input)
    	for i in l:
    		res += '<span class=\"tag {}\"><a href="#">{}</a></span>'.format("green", i)
    	return res
    	# return ''.join(self.clean(html_input))
    	# res = ""
    	# l = self.clean(html_input)
    	# print l
    	# for term in self.clean(html_input):
    	# 	print term
	    # return ''.join(self.clean(html_input))

	# def get_tags(self, html_input):
	# 	res = ""
	# 	# for term in self.clean(html_input):
	# 	# 	res += '<span class=\"tag {}\">{}</span>'.format(term, "green")
	# 	return res