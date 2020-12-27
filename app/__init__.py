from flask import Flask

app = Flask(__name__)

from .routes import routes
from .routes import routes_web
from .routes import routes_analytics
from .routes import routes_viz
from .routes import routes_travel
