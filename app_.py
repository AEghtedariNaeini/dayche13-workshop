from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Dayche!'


@app.route('/bye')
def bye_dayche():
    return 'Bye, Dayche!'

@app.route('/peyman')
def peyman():
    return 'Hello from Peyman!'


@app.route('/sobhan')
def sobhan():
    return 'Hello from Sobhan!'

@app.route('/Atefe')
def atefe():
    return 'Hello from Atefe!'

