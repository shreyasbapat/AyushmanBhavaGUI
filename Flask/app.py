from flask import Flask, request, url_for, render_template
from flask_restful import Resource, Api
from data import *
import requests
import json
from bs4 import BeautifulSoup
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
Articles=Articles()
Url_for_camera = "http://localhost:8081"

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
   return render_template('camera.html',url_for_camera=Url_for_camera)

@app.route('/cam_off')
def cam_off():
   off = "sudo service motor stop"
   ll = "ls -l"
   subprocess.call(ll)
   return

@app.route('/motor1')
def run_m1():
   # run = "python3 motor1.py"
   # subprocess.call(run)
   # return
   import motor1
   motor1.setup(Motor=1)
   motor1.run(Motor=1)
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
    ar=requests.get('http://localhost:5001/article')
    return render_template('home.html', rest_data=ar.text)


@app.route('/articles')
def articles():
   return render_template('articles.html', articles=Articles)

@app.route('/article')
def article():
   return render_template('article.html', articles=Articles)

@app.route('/suggestions',methods=['GET', 'POST'])
def suggestions():
    return render_template('suggestions.html')

@app.route('/suggestion')
def suggestion():
    text = request.args.get('jsdata')

    suggestions_list = []

    if text:
        r = requests.get('http://suggestqueries.google.com/complete/search?output=toolbar&hl=en&q={}&gl=in'.format(text))

        # r = requests.get('https://www.google.com/search?num=30&source=hp&q={}'.format(text))

        soup = BeautifulSoup(r.content, 'lxml')
        # soup = BeautifulSoup(html)
        suggestions = soup.find_all('suggestion')
        # suggestions = soup.find_all('h3')

        for suggestion in suggestions:
            suggestions_list.append(suggestion.attrs['data'])
        # print (suggestions)
    return render_template('suggestion.html',suggestions=suggestions_list)

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

api.add_resource(Employees, '/employees') # Route_1



if __name__ == '__main__':
    app.run(port=5001, debug=True)