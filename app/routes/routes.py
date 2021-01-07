from flask import render_template
from app import app

# home route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', color='blues', pad='p-0')

# javascript
@app.route("/toggle_js")
def toggle_js():
    return render_template("/javascript/toggles.js")