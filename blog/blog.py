#!/usr/bin/env python
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, jsonify
from flask.ext.responses import json_response, xml_response, auto_response
from datetime import date
from datetime import datetime
from urlparse import urlparse, urlunparse

app = Flask(__name__)

@app.route('/year_count')
def year_count():
    return render_template('year_count.html')

@app.route('/')
def index():
    return render_template('index.html', hello="hello")

@app.route('/tutorial')
def tutorial():
    return redirect('http://178.79.163.43:5000', code=302)

@app.route('/hi.json')
def json_test():
    return json_response({'name': 'Alex', 'message': 'hi!'}, status_code=201)

@app.route('/select')
def select():
    return render_template('select.html')

@app.route('/_select')
def _select():
    selected = request.args.get('data')
    return jsonify(result=selected)

@app.route('/robots.txt')
def robots_txt():
    return app.send_static_file('robots.txt')

@app.route('/button', methods=['GET', 'POST'])
def button():
    if request.method == 'GET':
        return render_template('button.html')
    elif request.method == 'POST':
        button_state = 'Pressed' if request.form.get('button_state') == 'true' else 'Not Pressed'
        return render_template('button.html', button_state=button_state)

@app.route('/timestamp')
def timestamp_render():
    if request.args.get('value'):
        timestamp = int(request.args.get('value'))
        if len(str(timestamp)) == 13:
                timestamp = int(str(timestamp)[0:-3])
        result = str(datetime.fromtimestamp(timestamp))
        return render_template('timestamp.html', timestamp=timestamp, result=result)
    return render_template('timestamp.html')

@app.route('/static/<path:path>')
def send_static():
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host='::', port=8080, debug=True)
