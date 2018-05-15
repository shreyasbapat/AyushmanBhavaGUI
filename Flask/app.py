from flask import Flask, request, url_for, render_template
from flask_restful import Resource, Api
import requests
import json
import os
import subprocess
from openpyxl import load_workbook

wb1 = load_workbook('sheet.xlsx')
ws = wb1["Sheet1"]

a = ws['B1']
b = ws['B2']
c = ws['B3']
d = ws['B4']
e = ws['B5']
f = ws['B6']
g = ws['B7']
h = ws['B8']
i = ws['B9']
j = ws['B10']

items = [a,b,c,d,e,f,g,h,i,j]

def restart_trans():
	for i in range (1,11):
		ws.cell(row=i, column=2).value=0
	wb1.save('sheet.xlsx')

restart_trans()

os.environ['http_proxy'] = "http://10.7.0.1:8080" 
os.environ['https_proxy'] = "https://10.7.0.1:8080"

app = Flask(__name__)
api = Api(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def pag_not_found(e):
    return render_template('500.html'), 500

@app.route('/')
def hello():
    data = {
      'name' : 'Prabhakar'
      }
    return render_template('index.html', **data)

@app.route('/camera')
def camera():
   return render_template('camera.html')

@app.route('/motor1')
def run_m1():
   import motor1
   motor1.setup(Motor=1)
   motor1.run(Motor=1)
   return render_template('index.html', **data)

@app.route('/motor2')
def run_m1():
   import motor1
   motor1.setup(Motor=2)
   motor1.run(Motor=2)
   return render_template('index.html', **data)

@app.route('/motor3')
def run_m1():
   import motor1
   motor1.setup(Motor=3)
   motor1.run(Motor=3)
   return render_template('index.html', **data)

@app.route('/motor4')
def run_m1():
   import motor1
   motor1.setup(Motor=4)
   motor1.run(Motor=4)
   return render_template('index.html', **data)

@app.route('/motor5')
def run_m1():
   import motor1
   motor1.setup(Motor=5)
   motor1.run(Motor=5)
   return render_template('index.html', **data)

@app.route('/motor6')
def run_m1():
   import motor1
   motor1.setup(Motor=6)
   motor1.run(Motor=6)
   return render_template('index.html', **data)

@app.route('/motor7')
def run_m1():
   import motor1
   motor1.setup(Motor=7)
   motor1.run(Motor=7)
   return render_template('index.html', **data)

@app.route('/motor8')
def run_m1():
   import motor1
   motor1.setup(Motor=8)
   motor1.run(Motor=8)
   return render_template('index.html', **data)

@app.route('/motor9')
def run_m1():
   import motor1
   motor1.setup(Motor=9)
   motor1.run(Motor=9)
   return render_template('index.html', **data)

@app.route('/motor10')
def run_m1():
   import motor1
   motor1.setup(Motor=10)
   motor1.run(Motor=10)
   return render_template('index.html', **data)

@app.route('/test')
def test():
	ws.cell(row=6, column=2).value=5
	wb1.save('sheet.xlsx')
	return

@app.route('/about')
def about():
   return render_template('about.html')


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)