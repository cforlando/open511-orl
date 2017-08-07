"""
Open511 Orlando
"""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')

# Enable CORS for the entire app
cors = CORS(app, resources={
    r'/*': {'origins': '*'}
})

from open511.api import api
