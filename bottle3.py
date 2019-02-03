# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 22:28:07 2019

@author: MastaMoose
"""

from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html',root='.')

@route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s!" % thing

run(host = 'localhost', port = 9999)