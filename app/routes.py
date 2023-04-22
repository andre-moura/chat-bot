from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/chat')
def chat():
    return render_template('chat.html', title='Chat')