import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    return 'Hello, World!'


if __name__ == '__main__':
    app.run(None, int(os.environ.get('PORT', 5000)), debug=True)
