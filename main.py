import logging
from HTMLTagger import Tagger
from flask import Flask, render_template, request, Markup

app = Flask(__name__)

@app.route('/')
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/snipped', methods=['POST'])
def submitted_form():
    title = request.form['title']
    origin = request.form['origin']
    content = request.form['content']

    return render_template(
        'submitted_recipe.html',
        title=title,
        origin=origin,
        content_html=content,
        content=Markup(Tagger().get_tags(content)))
        # content=HTMLCLeanup().get_tags(content))

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
