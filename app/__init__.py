from flask import Flask

app = Flask(__name__)

from app.routes import routes
from app.routes import routes_web
from app.routes import routes_analytics
from app.routes import routes_viz
from app.routes import routes_travel
from app.routes import routes_explainers
