'''
Kyle Lee, Vedant Kothari, Suhana Kumar
Team Name: K^3
K18 - Serving Looks
2024-10-14
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def primary():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)