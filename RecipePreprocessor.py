import re
from html.parser import HTMLParser
from pint import UnitRegistry

REMOVE_BRACKET_CONTENT = True

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return self.fed

class RecipePreprocessor(object):
    def clean_html(self, html_input):
        s = MLStripper()
        s.feed(html_input)
        return s.get_data()

    def remove_brackets(self, string):
        """
        Helper method, simply removes {([ ])} brackets from a string
        """
        return re.sub('[\{\[\(!@#$\)\]\}]', '', string);

    def remove_bracket_content(self, _groups):
        """
        This method removes text embedded in brackets
        eg. 250 ml (1 cup) sour cream -> 250 ml sour cream
        """
        for idx, group in enumerate(_groups):
            _groups[idx] = re.sub('  ',' ', re.sub('\(.*?\)', '', group))
        return _groups

    def clean_units(self, _groups):
        Q_ = UnitRegistry().Quantity
        res = []
        for group in _groups:
            l = group.split(' ')
            for idx, term in enumerate(l):
                try:
                    q = Q_(term)
                    if q.units.dimensionless:
                        try:
                            # print(term + l[idx + 1])
                            q = Q_(term + l[idx + 1])
                            l[idx] = str(q)
                            l.pop(idx+1)
                        except:
                            pass
                    else:
                        l[idx] = str(q)
                except:
                    pass
            res.append(' '.join(map(str, l)))
        return res

    # todo: we could add new input formats here in future and transform them to same output format
    def preprocess(self, html_input):
        _groups = self.clean_html(html_input)
        if REMOVE_BRACKET_CONTENT:
            _groups = self.remove_bracket_content(_groups)
        return self.clean_units(_groups)