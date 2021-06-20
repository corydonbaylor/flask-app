from flask import render_template
from app import app

# visualization routes


@app.route('/statistics')
def statistics():
    deck = [
        {
            'name': 'Hypothesis Testing and p-values',
            'image': 'images/statistics/p_values/p-values.001.png',
            'link': 'p_value',
            'text': 'Measure how unsual an event is with p-values'
        },
        {
            'name': 'Linear Regression',
            'image': 'images/statistics/linear/regression.004.jpg',
            'link': 'linear',
            'text': 'Learn how to make predictions with a trend line'
        },
        {
            'name': 'K-Means Clustering',
            'image': 'images/statistics/kmeans/kmeans.005.png',
            'link': 'kmeans',
            'text': 'Learn how to complete a market segementation with k-means clustering.'
        },
        {
            'name': 'Classification Tree',
            'image': 'images/statistics/class_tree/tree.001.png',
            'link': 'class_tree',
            'text': 'Build a simple classification tree by hand and determine if someone is a likely emoji user!'
        }

    ]
    return render_template('pages/statistics/statistics.html', deck=deck, title='Statistics', color='purples', pad='p-0')


@app.route('/statistics/p_value')
def p_value():
    return render_template('/pages/statistics/p-values.html', title='p-values', color='purples')


@app.route('/statistics/kmeans')
def kmeans():
    return render_template('/pages/statistics/kmeans.html', title='k-means', color='purples')


@app.route('/statistics/linear')
def linear():
    return render_template('/pages/statistics/linear.html', title='k-means', color='purples')


@app.route('/statistics/classification_tree')
def class_tree():
    return render_template('/pages/statistics/class_tree.html', title='Classification Tree', color='purples')
