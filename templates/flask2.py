# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:24:51 2019

@author: MastaMoose
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/echo/<thing>')
def echo(thing):
    return render_template('flask2.html', thing=thing)

app.run(port=9999, debug=True)