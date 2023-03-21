from flask import Flask
from Server import routes

app = Flask(__name__)
app.debug = True
