from flask import render_template
from app import app

# web devlopment routes
@app.route('/webdev')
def webdev():
    return render_template('webdev.html', title='Web Dev', pad ='p-0')

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
