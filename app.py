# Importing flask module
from flask import Flask, render_template, request ,flash
from problem_1 import find_cdets
from problem_2 import find_build_num
from problem_3 import find_branch_and_commit_id
# Creating a Flask instance
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/problem1', methods=["GET","POST"])
def problem1():
    if request.method == "POST":
        b1 = request.form.get("b1")
        b2 = request.form.get("b2")
        file_name = request.form.get("file_name")
        if int(b1) > int(b2):
            flash(find_cdets(b1,b2,file_name))
        else:
            flash(find_cdets(b1,b2,file_name))
        
    return render_template('problem1.html')    
    
@app.route('/problem2', methods=["GET","POST"])
def problem2():
    if request.method == "POST":
        branch = request.form.get("bno")
        cdet = request.form.get("cdet")
        flash(find_build_num(cdet,branch))
    return render_template("problem2.html")

@app.route('/problem3', methods=["GET","POST"])
def problem3():
    if request.method == "POST":
        file_name = request.form.get("bno")
        dc,commits = find_branch_and_commit_id(file_name)
        flash(dc)
        flash(str(commits) + " Commits")
    return render_template("problem3.html")

@app.route('/problem4')
def problem4():
    return render_template("problem4.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
