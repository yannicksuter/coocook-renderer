import spacy

class Tagger(object):
    def __init__(self, lang='en'):
        self.lang = lang
        self.nlp = spacy.load(lang)

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

    def get_group_widget(self, groups):
    	html_widget = ""
    	for group in groups:
            print(group)
            doc = self.nlp(group)
            group_html = ""
            for token in doc:
                title_txt = f'text:{token.text} lemma:{token.lemma_} pos:{token.pos_} tag:{token.tag_} dep:{token.dep_}'
                group_html += '<span class=\"tag {}\"><a href="#" title="{}">{}</a></span>'.format(self.get_token_color(token), title_txt, token.text)

            html_widget += '<span class=\"outline\">{}</span>'.format(group_html)

    	return html_widget