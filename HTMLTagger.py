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

class HTMLCLeanup(object):
    def __init__(self):
        pass

    def clean(self, html_input):
	    s = MLStripper()
	    s.feed(html_input)
	    return ' '.join(s.get_data())