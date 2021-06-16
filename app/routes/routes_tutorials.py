from flask import render_template
from app import app

# web devlopment routes


@app.route('/tutorials')
def tutorials():
    return render_template('pages/tutorials/tutorials.html', title='Web Dev', pad='p-0')


@app.route('/tutorials/linux_git')
def linux_git():
    return render_template('pages/tutorials/build_website/linux_git.html', title='Linux and Git')


@app.route('/tutorials/html_css')
def html_css():
    return render_template('pages/tutorials/build_website/html_css.html', title='HTML and CSS')


@app.route('/tutorials/bootstrap')
def bootstrap():
    return render_template('pages/tutorials/build_website/bootstrap.html', title='Bootstrap')


@app.route('/tutorials/local_raspberry')
def local1():
    return render_template('pages/tutorials/build_website/using_raspberry.html', title='Hosting: Raspberry Pi')


@app.route('/tutorials/hello_flask')
def flask1():
    return render_template('pages/tutorials/build_website/Flask.html', title='Flask pt. I: Creating Your First Flask App')


@app.route('/tutorials/templates')
def flask2():
    return render_template('pages/tutorials/build_website/templates.html', title='Flask pt. II: Templating with Jinja2')


@app.route('/tutorials/local_host_2')
def local2():
    return render_template('pages/tutorials/build_website/local_hosting_2.html', title='Flask and Apache')


@app.route('/tutorials/port_forwarding')
def local3():
    return render_template('pages/tutorials/build_website/port_forwarding.html', title='Port Forwarding')
