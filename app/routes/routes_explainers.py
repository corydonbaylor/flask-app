from flask import render_template
from app import app

# visualization routes
@app.route('/explainers')
def explainers():
    deck = [
        {
            'name': 'Hypothesis Testing and p-values',
            'image': 'images/explainers/p_values/p-values.001.png',
            'link': 'p_value',
            'text': 'Measure how unsual an event is with p-values'
        },
        {
            'name': 'Linear Regression',
            'image': 'images/explainers/linear/regression.004.jpg',
            'link': 'linear',
            'text': 'Learn how to make predictions with a trend line'
        },
        {
            'name': 'K-Means Clustering',
            'image': 'images/explainers/kmeans/kmeans.005.png',
            'link': 'kmeans',
            'text': 'Learn how to complete a market segementation with k-means clustering.'
        }

    ]
    return render_template('pages/explainers/explainers.html', deck=deck, title='Explainers', color='purples', pad='p-0')

@app.route('/explainers/p_value')
def p_value():
    return render_template('/pages/explainers/p-values.html', title='p-values', color='purples')

@app.route('/explainers/kmeans')
def kmeans():
    return render_template('/pages/explainers/kmeans.html', title='k-means', color='purples')

@app.route('/explainers/linear')
def linear():
    return render_template('/pages/explainers/linear.html', title='k-means', color='purples')
