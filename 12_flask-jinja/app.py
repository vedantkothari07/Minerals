# Aditya, Vedant, Ziyad
# Vicious Turkeys
# SoftDev
# Sep 2024
# Time Spent: .5

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
It would give an error if you tried to access /my_foist_template through
local_host:5000/my_foist_template
Q1:
local_host:5000/my_foist_template
Q2:
model_templt.html is the template to render
foo = "foooo" tells jinja that foo is "foooo" and should be rendered as that
collection = coll tells jinja that while rendering the page  collection refers to 
to the list coll = [0,1,1,2,3,5,8]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QCC:
1. It is interesting taht there is an "endfor" statement, as this is not the case in languages we have studied so far.
2. What is the purpose of the % signs?
    We think that it is a delimiter; the % signs signal the start and end of a function.
3. Why do some functions have one set of curly brackets but others have 2?
    It seems as though one set signals functions and 2 sets signals items.
4. Why do we use Jinja as opposed to just HTML?
    We concluded that Jinja is useful and convenient when we want our data to change upon refreshing and when we want to incorporate Python.




"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask#, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()
