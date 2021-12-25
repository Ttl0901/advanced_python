from flask import Flask
from flask import render_template, request
import pandas as pd
app = Flask(__name__)
df = pd.read_csv('advanced_python.csv', sep = ';')

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/tlu')
def tlu():
   return 'Thang Long University'
@app.route('/author')
def author():
   return render_template('author.html')

@app.route('/add')
def add():
    a = request.args.get('a', default = 0, type = int)
    b = request.args.get('b', default = 0, type = int)
    return f"{a} + {b} = {a+b}"

@app.route('/mul/<int:a>/<int:b>')
def mul(a,b):
    return f"{a} * {b} = {a*b}"

@app.route('/thread/<string:posttitle>')
def getpage(posttitle):
    return f"querying post via {posttitle}"

@app.route('/student/code/<string:studentcode>')
def getstudentviacode(studentcode):
    result = df[df['student code'] == studentcode].to_html()
    return result
### REQUIREMNTS:
"""
- create a routing which allow user to show author info: /author
- a routing which allow user get total of 2 numbers: /add
- implementing a list funcs for querying data in advanced_python.csv
"""
if __name__ == '__main__':
   app.run()
