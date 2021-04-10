from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine


app = Flask(__name__)
# app.config["MONGODB_HOST"] = "mongodb://localhost:27017/project_4"
app.config["SECRET_KEY"] = "a"


# db = MongoEngine(app)

from . import routes