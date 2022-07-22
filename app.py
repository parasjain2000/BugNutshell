# Importing flask module
# An object of Flask class is the WSGI application
from flask import Flask, render_template, request

# Creating a Flask instance
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/problem1')
def problem1():
    return render_template("problem1.html")

@app.route('/problem2')
def problem2():
    return render_template("problem2.html")

@app.route('/problem3')
def problem3():
    return render_template("problem3.html")

@app.route('/problem4')
def problem4():
    return render_template("problem4.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
