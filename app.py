# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template ("index.html")

@app.route('/results', methods = ['GET','POST'])
def results():
    if request.method == "POST":
        q1 = request.form["q1"]
        q2 = request.form["q2"]
        q3 = request.form["q3"]
        q4 = request.form["q4"]
        q5 = request.form["q5"]
        q6 = request.form["q6"]
        characters_ranking = {"Peter": 0, "Brian": 0,"Lois": 0, "Stewie": 0, "Chris": 0, "Meg": 0}
        character_pics = {"Peter": "https://tinyurl.com/yb79au49", "Brian": "https://tinyurl.com/ybuma6cl","Lois": "https://tinyurl.com/y8e5j2wx", "Stewie": "https://tinyurl.com/yblrhd2l", "Chris": "https://tinyurl.com/yakjw98e", "Meg": "https://tinyurl.com/y79uze5t"}
        if q1.upper() == "Y":
            characters_ranking["Meg"] += 1
        if q2.upper() == "Y":
            characters_ranking["Stewie"] += 1
        if q3.upper() == "Y":
             characters_ranking["Peter"] += 1
        if q4.upper() == "Y":
             characters_ranking["Stewie"] += 1
        if q5.upper() == "Y":
             characters_ranking["Brian"] += 1
        if q6.upper() == "Y":
             characters_ranking["Chris"] += 1
        top_key = ""
        top_value = 0
        for i in characters_ranking:
            if top_value < characters_ranking[i]:
                top_value = characters_ranking[i]
                top_key = i
        character_pic = character_pics[top_key]
    return render_template('results.html', top_key = top_key, character_pic = character_pic)
    
