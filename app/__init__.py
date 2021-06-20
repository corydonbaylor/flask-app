from flask import Flask

app = Flask(__name__)

from app.routes import routes
from app.routes import routes_coding
from app.routes import routes_tutorials
from app.routes import routes_viz
from app.routes import routes_travel
from app.routes import routes_statistics
