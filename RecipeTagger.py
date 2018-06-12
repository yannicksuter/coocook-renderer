import spacy
import textacy

class UnsupportedLanguage(Exception):
    """Raised if we can not detect the language of a text snippet."""

class Tagger(object):
    def __init__(self, lang='en', groups=None):
        if lang not in ['en']:
            raise UnsupportedLanguage(f'Language {lang} not supported.')

        self.lang = lang
        self.nlp = spacy.load(lang)

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
        if token.pos_ == 'ADJ':
            return 'yellow'
        return 'grey'

    def parse_group(self, group):
        doc = self.nlp(group)


    def get_group_widget(self, groups):
    	html_widget = ""
    	for group in groups:
            # print(group)
            doc = self.nlp(group)

            # _pattern = r'^<NUM>?<NOUN>$'
            # _pattern = r'<NUM><NOUN>'
            # _pattern = r'^<NUM>'
            # _pattern = r'<VERB>?<ADV>*<VERB>+'
            # _dod = textacy.Doc(group, lang=self.lang)
            # _lists = textacy.extract.pos_regex_matches(_dod, _pattern)
            # _lists = textacy.extract.pos_regex_matches(doc, _pattern)
            # for v in _lists:
            #     print(v.text)

            group_html = ""
            for token in doc:
                title_txt = f'text:{token.text} lemma:{token.lemma_} pos:{token.pos_} tag:{token.tag_} dep:{token.dep_}'
                group_html += '<span class=\"tag {}\"><a href="#" title="{}">{}</a></span>'.format(self.get_token_color(token), title_txt, token.text)

            html_widget += '<span class=\"outline\">{}</span>'.format(group_html)

    	return html_widget
