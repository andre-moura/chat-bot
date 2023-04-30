from flask import render_template, Blueprint


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', title='Home')


@main.route('/chat')
def chat():
    return render_template('chat.html', title='Chat')