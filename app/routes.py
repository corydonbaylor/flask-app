from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bitch Boi'}
    posts = [
        {
            'authors': {'username': 'john'},
            'body': 'Its lit out here'
        },
        {
            'authors': {'username': 'caitlin'},
            'body': 'I am caitlin'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
