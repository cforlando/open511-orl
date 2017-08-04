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
    return """
<html>
<h1>Open511 Orlando Endpoints</h1>
<ul>
  <li><b>/jurisdiction</b> - City information</li>
  <li><b>/jurisdictiongeography</b> - City limits geometry</li>
</ul>
</html>
"""

from open511.api import api
