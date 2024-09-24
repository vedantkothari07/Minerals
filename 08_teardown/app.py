# your heading here

'''
DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0. I believe I have seen similar syntax in Java, where you call a function name (Flask in this case), and enter a parameter inside for what you want to run the function with. 
1. A point of reference I have for the meaning of '/' is new line, where we use '/n'. I've also seen it in the terminal, where we use it to travel to different directories. 
2. 
3. 
4. 
5. 
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?


