from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/tlu')
def tlu():
   return 'Thang Long University'
@app.route('/author')
def author():
   return render_template('author.html')

### REQUIREMNTS:
"""
- create a routing which allow user to show author info: /author
- a routing which allow user get total of 2 numbers: /add
"""
if __name__ == '__main__':
   app.run()
