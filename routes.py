from . import app
from flask import Flask, render_template, request, redirect, url_for

from flask_wtf import FlaskForm
from wtforms import StringField

class SearchForm(FlaskForm):
    search_field = StringField('Username:')
    
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    search_form = SearchForm()

    if search_form.validate_on_submit():
        search_data = search_form.search_field.data
        return redirect(url_for('profile', username=search_data))
    return render_template('base.html', title="Homepage", search_form=search_form)


@app.route('/about')
def about():
    return 'Welcome to my cool Bitcamp project!'


users = [
    {
        'name': 'Bitcamper',
        'email': 'hello@bit.camp',
        'description': 'I love going to Bitcamp!'
    },
    {
        'name': 'nikolay',
        'email': 'nikolay@bit.camp',
        'description': "I'm a CS student at UMD!"
    },
    {
        'name': 'Dhanvee',
        'email': 'dhanvee@umd.edu',
        'description': "I'm a CS & Math student at UMD!"
    }
]


@app.route('/user/<username>')
def profile(username):
    user = None
    for u in users:
        if u['name'] == username:
            user = u
    if not user:
        user = users[0]
    return render_template('profile.html', title="{}'s profile page".format(user['name']), user=user)


@app.route('/feed')
def feed():
    return ''