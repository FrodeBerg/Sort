from random import shuffle
from crypt import methods
from secrets import randbelow
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# The two sorting tables
number_of_elements = 20
table1 = list(range(1,number_of_elements))
table2 = list(range(1,number_of_elements))

@app.route("/")
def index():
    return render_template("/index.html", elements=number_of_elements)

@app.route("/run", methods=["GET", "POST"])
def run():
    if request.method == 'POST':
        return render_template("/index.html", algo1=request.form.get("Algorithm1"), algo2=request.form.get("Algorithm2"))
    else:
        return render_template("/index.html")
    
@app.route("/random", methods=["GET", "POST"])
def random():
    if request.method == 'POST':

        shuffle(table1)
        shuffle(table2)  
        
        return render_template("/index.html", table1=table1, table2=table2)
    else:
        return render_template("/index.html")