from crypt import methods
import os
from hp import app, util
from hp.forms import InfoForm
from flask import render_template, url_for, flash, redirect, request, abort, jsonify


@app.route("/",methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def predict_price():
    form = InfoForm()
    #price = util.get_estimated_price()
    price=0 
    if form.validate_on_submit():
        price = util.get_estimated_price(form.location.data, form.area.data,form.bhk.data,form.bath.data)
        print(price)

    return render_template("layout.html",form=form,price=price)
    