from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explore')
def explore():
    return render_template('tools.html') #modificar html

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
