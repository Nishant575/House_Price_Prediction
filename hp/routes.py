
import os
from hp import app, util
from hp.forms import InfoForm
from flask import render_template, url_for, flash, redirect, request, abort, jsonify


@app.route("/")
@app.route("/home")
def home():
     return render_template("home.html")

@app.route("/sell",methods=['POST', 'GET'])
def predict_price():
    form = InfoForm()
    #price = util.get_estimated_price()
    price=0 
    if form.validate_on_submit():
        price = util.get_estimated_price(form.location.data, form.area.data,form.bhk.data,form.bath.data)
        price = abs(price)
        print(price)

    return render_template("predict.html",form=form,price=price,title="sell")

@app.route("/buy")
def buy():
    return render_template("buy.html",title="buy")
    