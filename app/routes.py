from flask import render_template
from app import app

# home route


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', color='blues')

# analytics routes


@app.route('/analytics')
def analytics():
    return render_template('analytics.html', title='Analytics', color='greys')

@app.route('/analytics/getwiki')
def getwiki():
    return render_template('pages/analytics/getwiki.html', title='getwiki', color='greys')

# web devlopment routes


@app.route('/webdev')
def webdev():
    return render_template('webdev.html', title='Web Dev')
    
@app.route('/webdev/linux_git')
def linux_git():
    return render_template('pages/webdev/linux_git.html', title='Linux and Git')

@app.route('/webdev/html_css')
def html_css():
    return render_template('pages/webdev/html_css.html', title='HTML and CSS')

@app.route('/webdev/bootstrap')
def bootstrap():
    return render_template('pages/webdev/bootstrap.html', title='Bootstrap')

@app.route('/webdev/local_raspberry')
def local1():
    return render_template('pages/webdev/using_raspberry.html', title='Hosting: Raspberry Pi')

@app.route('/webdev/hello_flask')
def flask1():
    return render_template('pages/webdev/Flask.html', title='Flask pt. I: Creating Your First Flask App')

@app.route('/webdev/templates')
def flask2():
    return render_template('pages/webdev/templates.html', title='Flask pt. II: Templating with Jinja2')


@app.route('/webdev/local_host_2')
def local2():
    return render_template('pages/webdev/local_hosting_2.html', title='Flask and Apache')


@app.route('/webdev/port_forwarding')
def local3():
    return render_template('pages/webdev/port_forwarding.html', title='Port Forwarding')

# visualization routes


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
    return render_template('viz.html', deck=deck, title='Visualizations', color='greens')


@app.route('/viz/covid_dotmap')
def covid_dotmap():
    return render_template('/pages/viz/covid_dotmap.html', title='Dot Map', color='greens')


@app.route('/viz/calendar')
def calendar():
    return render_template('/pages/viz/twitter_viz.html', title='Sentiment Calendar', color='greens')


@app.route('/viz/barchart_race')
def barchart():
    return render_template('/pages/viz/barchart_race.html', title='Barchart Race', color='greens')

# travel
@app.route('/travel')
def travel():
    return render_template('travel.html', title='Travel')

@app.route('/travel/argentina')
def argentina():
    return render_template('pages/travel/argentina.html', title='Travel')