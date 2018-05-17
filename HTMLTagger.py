#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spacy
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return self.fed

class Tagger(object):
    def __init__(self):
        self.nlp = spacy.load('en')

    def clean(self, html_input):
	    s = MLStripper()
	    s.feed(html_input)
	    return s.get_data()

    def get_tags(self, html_input):
    	res = ""
    	l = self.clean(html_input)
    	for i in l:
    		res += '<span class=\"tag {}\"><a href="#">{}</a></span>'.format("green", i)

    	return '<span class=\"outline\">{}</span>'.format(res)

    def get_color(self, token):
        if any(char.isdigit() for char in token):
            return "blue"
        if all(char.isupper() for char in token) and len(token) > 1:
            return "red"
        return "green"

    def get_token_color(self, token):
        if token.pos_ == 'NOUN':
            return 'red'
        if token.pos_ == 'VERB':
            return 'blue'
        if token.pos_ == 'NUM':
            return 'green'
        return 'grey'


    def get_groups(self, html_input):
    	res = ""
    	for group in self.clean(html_input):
            doc = self.nlp(group)
            group_html = ""
            for token in doc:
                # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
                title_txt = f'text:{token.text} lemma:{token.lemma_} pos:{token.pos_} tag:{token.tag_} dep:{token.dep_}'
                group_html += '<span class=\"tag {}\"><a href="#" title="{}">{}</a></span>'.format(self.get_token_color(token), title_txt, token.text)

            # group_html = ""
            # for token in group.split(' '):
            #     group_html += '<span class=\"tag {}\"><a href="#">{}</a></span>'.format(self.get_color(token), token)
            res += '<span class=\"outline\">{}</span>'.format(group_html)

    	return res
