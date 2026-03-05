from flask import Flask, render_template
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, world!"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

if __name__ == "__main__":
    app.run(debug=True)
