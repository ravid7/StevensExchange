from flask import Flask, Markup, render_template
import json

with open('./StevensEx/months.json') as data_file:    
    months = json.load(data_file)

with open('./StevensEx/values.json') as data_file:    
    valuesGraph = json.load(data_file)

app = Flask(__name__)

# labels = [
#     'JAN', 'FEB', 'MAR', 'APR',
#     'MAY', 'JUN', 'JUL', 'AUG',
#     'SEP', 'OCT', 'NOV', 'DEC'
# ]

labels = [
    months['months']['january'], months['months']['feburvary'], months['months']['march'], months['months']['april'],
    months['months']['may'], months['months']['june'], months['months']['july'], months['months']['august'],
    months['months']['september'], months['months']['october'], months['months']['november'], months['months']['december']
]

# values = [
#     967.67, 1190.89, 1079.75, 1349.19,
#     2328.91, 2504.28, 2873.83, 4764.87,
#     4349.29, 6458.30, 9907, 16297
# ]

values = valuesGraph['graph']["values"]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


@app.route('/bar')
def bar():
    bar_labels = labels
    bar_values = values
    return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD($)', max=17000, labels=bar_labels, values=bar_values)


@app.route('/line')
def line():
    line_labels = labels
    line_values = values
    return render_template('line_chart.html', title='Bitcoin Monthly Price in USD($)', max=17000, labels=line_labels, values=line_values)


@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Bitcoin Monthly Price in USD', max=17000, set=zip(values, labels, colors))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
