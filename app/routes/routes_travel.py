from flask import render_template
from app import app

# travel


@app.route('/travel')
def travel():
    return render_template('pages/travel/travel.html', title='Travel')


@app.route('/travel/iceland')
def iceland():
    return render_template('pages/travel/iceland.html', title='Iceland')


@app.route('/travel/southwest')
def southwest():
    return render_template('pages/travel/southwest.html', title='Southwest')


@app.route('/travel/puerto_rico')
def puerto_rico():
    return render_template('pages/travel/puerto_rico.html', title='Puerto Rico')


@app.route('/travel/argentina')
def argentina():
    return render_template('pages/travel/argentina.html', title='Argentina')


@app.route('/travel/uruguay')
def uruguay():
    return render_template('pages/travel/uruguay.html', title='Uruguay')


@app.route('/travel/hungary')
def hungary():
    return render_template('pages/travel/hungary.html', title='Hungary')


@app.route('/travel/costa_rica')
def costa_rica():
    return render_template('pages/travel/costa_rica.html', title='Costa Rica')


@app.route('/travel/mediterranean')
def med():
    return render_template('pages/travel/med.html', title='Mediterranean')


@app.route('/megan')
def megan():
    return render_template('pages/travel/megan.html', title='For Megan')
