from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', content='yo')

@app.route('/<name>')
def user(name):
    return render_template('index.html', content=name)

@app.route('/newpage')
def newpage():
    return render_template('newpage.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)