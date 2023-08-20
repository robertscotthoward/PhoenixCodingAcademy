import sys
import os
from flask import Flask, Blueprint, render_template, request

site = Blueprint('PCA', __name__, template_folder='templates')

app = Flask(__name__)


@app.route('/info')
def info():
  return f'''
<pre>
PATH: {os.path.abspath('.')}
</pre>
'''
@app.route('/')
def hello():
  return render_template('main.html', user="Fred")

if __name__ == "__main__":
  app.run()