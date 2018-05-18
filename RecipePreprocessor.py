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

class RecipePreprocessor(object):
    def clean_html(self, html_input):
        s = MLStripper()
        s.feed(html_input)
        return s.get_data()

    def clean_units(self, recipe_groups):
        for group in recipe_groups:
            pass
        return recipe_groups

    # todo: we could add new input formats here in future and transform them to same output format
    def preprocess(self, html_input):
        return self.clean_units(self.clean_html(html_input))