from flask import render_template
from app import app

# travel
@app.route('/travel')
def travel():
    return render_template('travel.html', title='Travel')

@app.route('/travel/argentina')
def argentina():
    return render_template('pages/travel/argentina.html', title='Argentina')

@app.route('/travel/uruguay')
def uruguay():
    return render_template('pages/travel/uruguay.html', title='Uruguay')

@app.route('/travel/costa_rica')
def costa_rica():
    return render_template('pages/travel/costa_rica.html', title='Costa Rica')