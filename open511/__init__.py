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

@app.route('/')
def index():
    return "Open511 Orlando Endpoints<br>/jurisdiction<br>/jurisdictiongeography"

from open511.api import api
