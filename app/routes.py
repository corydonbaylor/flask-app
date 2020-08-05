from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/analytics')
def analytics():
    return render_template('analytics.html')


@app.route('/webdev')
def webdev():
    return render_template('webdev.html')


@app.route('/webdev/local_host_2')
def local2():
    return render_template('pages/webdev/local_hosting_2.html')


@app.route('/viz')
def viz():
    deck = [

        {
            'name': 'Covid Dotmap',
            'image': 'images/viz/covid-still.PNG',
            'link': 'covid_dotmap'
        },
        {
            'name': 'Sentiment Calendar',
            'image': 'images/viz/calendar.png',
            'link': 'calendar'
        },
        {
            'name': 'Barchart Race',
            'image': 'images/viz/barchart.PNG',
            'link': 'barchart'
        }

    ]
    return render_template('viz.html', deck=deck)


@app.route('/viz/covid_dotmap')
def covid_dotmap():
    return render_template('/pages/viz/covid_dotmap.html')


@app.route('/viz/calendar')
def calendar():
    return render_template('/pages/viz/twitter_viz.html')


@app.route('/viz/barchart_race')
def barchart():
    return render_template('/pages/viz/barchart_race.html')
