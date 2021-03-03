from flask import render_template
from app import app

# analytics routes
@app.route('/analytics')
def analytics():
    return render_template('pages/analytics/analytics.html', title='Analytics', color='greys', pad='p-0')

@app.route('/analytics/getwiki')
def getwiki():
    return render_template('pages/analytics/getwiki.html', title='getwiki', color='greys')

