import os
import random
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello, World!'

## Returns a random number
@app.route('/random')
def random_number():
    return str(random.random())


if __name__ == '__main__':
    app.run(None, int(os.environ.get('PORT', 5000)), debug=True)
