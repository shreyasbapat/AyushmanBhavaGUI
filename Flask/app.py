from flask import Flask, request, url_for, render_template, jsonify
from flask_restful import Resource, Api
import requests
import json
import os
import subprocess
from openpyxl import load_workbook
import paypalrestsdk
import logging

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

os.environ['http_proxy'] = "http://10.8.0.1:8080" 
os.environ['https_proxy'] = "https://10.8.0.1:8080"

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

@app.route('/pay')
def pay():
   return render_template('pay.html')

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AR92SyiTyQfPWGs8bH2xAOncMsKiuTXWECm7aBODm62jYBwboMLyyaKmDGBckKT0oDFMpj47AwYOKLuR",
  "client_secret": "EHLV7tym7p9ZU3gr6SrNTwM5BTIWGhYPCZfVyI6J_XfV6kPPjQQ_YTjadR67UwV0DaUMJsIeQGL2x0dh"
  
#   "mode": "live", # sandbox or live
#   "client_id": "Aa1OvenQntqBU_APRyS-4Exd89f69l4_yQwlLHd7hn3Yq1TNoQph_XBgx_1d15YNuMiCPB9FAlYa0_jn",
#   "client_secret": "EPplWCfFfvJVaup1YQ05FRpSdfAPreLZUhrezdgpxRlZ4p8LL3NDd-_xYg-V5C45gLdUredMsCuhnMb0"
  
   })
  
total_amount_to_be_paid = 100
@app.route('/payment', methods=['POST'])
def payment():
    payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://localhost:5001",
        "cancel_url": "http://localhost:3000"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "Total Payable Amount",
                "sku": "item",
                "price": total_amount_to_be_paid,
                "currency": "INR",
                "quantity": 1}]},
        "amount": {
            "total": total_amount_to_be_paid,
            "currency": "INR"},
        "description": "This is the payment transaction description."}]})

    if payment.create():
        print("Payment created successfully")
    else:
        print(payment.error)
    return jsonify({'paymentID' : payment.id})

@app.route('/execute', methods=['POST'])
def execute():
    success = False
    payment = paypalrestsdk.Payment.find(request.form['paymentID'])

    if payment.execute({'payer_id':request.form['payerID']}):
        print ('Execute Success')
        success = True

    return jsonify({'success' : success})

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)