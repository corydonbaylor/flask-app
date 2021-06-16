from flask import render_template
from app import app

# coding routes


@app.route('/coding')
def coding():
    return render_template('pages/coding/coding.html', title='Analytics', color='greys', pad='p-0')


@app.route('/coding/getwiki')
def getwiki():
    return render_template('pages/coding/getwiki.html', title='getwiki', color='greys')
