from flask import render_template
from app import app

# visualization routes


@app.route('/viz')
def viz():
    deck = [
        {
            'name': 'The Day (Rock) Music Died',
            'image': 'images/viz/rock_small.png',
            'link': 'rock',
            'text': 'Rock music has been dying for decades but is now on life support',
            'tools': 'matplotlib',
            'tool_type': 'matplotlib'
        },
        {
            'name': 'Sentiment Analysis of Greek Plays',
            'image': 'images/viz/plays/rex.png',
            'link': 'plays',
            'text': 'Check out a poster I made that show a sentiment analysis of nine greek plays',
            'tools': 'ggplot2',
            'tool_type': 'ggplot'
        },
        {
            'name': 'Virginia Joy Plot',
            'image': 'images/viz/joy_plot/joy_plot.png',
            'link': 'joy_plot',
            'text': 'Learn how to make a joy plot of the topography of Virginia',
            'tools': 'ggplot2',
            'tool_type': 'ggplot'
        },
        {
            'name': 'Covid Dotmap',
            'image': 'images/viz/covid-still.PNG',
            'link': 'covid_dotmap',
            'text': 'Learn to make a dotmap with the maps package and gganimate',
            'tools': 'ggplot2',
            'tool_type': 'ggplot'
        },
        {
            'name': 'Sentiment Calendar',
            'image': 'images/viz/calendar.png',
            'link': 'calendar',
            'text': 'Scrape tweets and plot them as this cool sentiment calendar',
            'tools': 'ggplot2',
            'tool_type': 'ggplot'
        },
        {
            'name': 'Barchart Race',
            'image': 'images/viz/barchart.PNG',
            'link': 'barchart',
            'text': 'Create the popular barchart race using R',
            'tools': 'ggplot2',
            'tool_type': 'ggplot'
        }

    ]
    return render_template('/pages/viz/viz.html', deck=deck, title='Visualizations', color='greens', pad='p-0')


@app.route('/viz/rock')
def rock():
    return render_template('/pages/viz/rock.html', title='Rock', color='greens')


@app.route('/viz/plays')
def plays():
    return render_template('/pages/viz/plays.html', title='Greek Plays', color='greens')


@app.route('/viz/joy_plot')
def joy_plot():
    return render_template('/pages/viz/joy_plot.html', title='Joy Plot', color='greens')


@app.route('/viz/covid_dotmap')
def covid_dotmap():
    return render_template('/pages/viz/covid_dotmap.html', title='Dot Map', color='greens')


@app.route('/viz/calendar')
def calendar():
    return render_template('/pages/viz/twitter_viz.html', title='Sentiment Calendar', color='greens')


@app.route('/viz/barchart_race')
def barchart():
    return render_template('/pages/viz/barchart_race.html', title='Barchart Race', color='greens')
