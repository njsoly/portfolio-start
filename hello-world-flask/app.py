import os
import random
import json
from flask import Flask, render_template
import plotly
import plotly.graph_objects as go

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello, World!'


## Returns a random number
@app.route('/random')
def random_number():
    return str(random.random())


@app.route('/chart')
def chart():
    # Sample data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [random.randint(100, 500) for _ in range(6)]
    expenses = [random.randint(50, 300) for _ in range(6)]

    # Create a Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Sales', x=months, y=sales, marker_color='#2ecc71'))
    fig.add_trace(go.Bar(name='Expenses', x=months, y=expenses, marker_color='#e74c3c'))

    fig.update_layout(
        title='Monthly Sales vs Expenses',
        xaxis_title='Month',
        yaxis_title='Amount ($)',
        barmode='group'
    )

    # Convert to JSON for the template
    chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('chart.html', chart_json=chart_json)


if __name__ == '__main__':
    app.run(None, int(os.environ.get('PORT', 5000)), debug=True)
