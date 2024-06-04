
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/basics')
def basics():
    return render_template('basics.html')

@app.route('/success-stories')
def success_stories():
    return render_template('success_stories.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
