from flask import render_template
from app import app

# visualization routes
@app.route('/explainers')
def explainers():
    deck = [
        {
            'name': 'k-Means Clustering',
            'image': 'images/explainers/kmeans/kmeans.007.png',
            'link': 'kmeans',
            'text': 'Learn how to complete a market segementation with k-means clustering.'
        }

    ]
    return render_template('explainers.html', deck=deck, title='Explainers', color='purples', pad='p-0')

@app.route('/explainers/kmeans')
def kmeans():
    return render_template('/pages/explainers/kmeans.html', title='k-means', color='purples')

