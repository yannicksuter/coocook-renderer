#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import hashlib

from LanguageDetect import detect_language
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

    basic_name, code, confidence, bytesize = detect_language(', '.join(recipe_groups))
    recipe_lang = basic_name
    recipe_lang_pred = float(confidence)

    tagger = Tagger(lang=code)

    RecipeStorage().store(recipe=Recipe(id=recipe_id, title=recipe_title, origin=recipe_origin, lang=recipe_lang))

    groups_widget, ingredients = tagger.get_group_widget(recipe_groups)

    return render_template(
        'submitted_recipe.html',
        title= f'{recipe_title} (id: {recipe_id})',
        origin=recipe_origin,
        language=recipe_lang,
        language_pred=recipe_lang_pred,
        content_html=recipe_content,
        content=Markup(groups_widget))

@app.route('/recipe/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = RecipeStorage().load(recipe_id)
    recipe_id = recipe['_id']
    recipe_title = recipe['_title']
    recipe_origin = recipe['_origin']
    recipe_lang = recipe['_lang']
    return render_template(
        'recipe.html',
        title=f'{recipe_title} (id: {recipe_id})',
        origin=recipe_origin,
        language=recipe_lang)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')