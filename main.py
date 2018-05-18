#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import hashlib

from Recipe import Recipe
from RecipeStorage import RecipeStorage
from RecipeTagger import Tagger
from RecipePreprocessor import RecipePreprocessor

from flask import Flask, render_template, request, Markup

app = Flask(__name__)

@app.route('/snipped', methods=['POST'])
def submitted_form():
    recipe_title = request.form['title']
    recipe_origin = request.form['origin']
    recipe_content = request.form['content']

    # process raw input
    m = hashlib.md5()
    m.update(recipe_origin.encode('utf-8'))
    recipe_id = m.hexdigest()
    recipe_groups = RecipePreprocessor().preprocess(html_input=recipe_content)

    RecipeStorage().store(recipe=Recipe())

    return render_template(
        'submitted_recipe.html',
        title= f'{recipe_title} (id: {recipe_id})',
        origin=recipe_origin,
        content_html=recipe_content,
        content=Markup(Tagger().get_group_widget(recipe_groups)))

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')