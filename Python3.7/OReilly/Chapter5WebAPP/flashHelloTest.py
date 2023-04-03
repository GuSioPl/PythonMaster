from flask import Flask, render_template
from vsearch import searchForLetters
app = Flask(__name__)

@app.route('/')
## @app.route('/JAKASSTRONA/')  http://127.0.0.1:5000/JAKASSTRONA/
def hello() ->str:
    return 'Hello Word'

@app.route('/letterschecj/')
def search4Letters() ->str:
    return searchForLetters("Mariusz Pudzian Pudzianowski")

@app.route('/entry/')
def entryPage():
    return render_template('entry.html',
                           the_title='Welcome')

app.run()