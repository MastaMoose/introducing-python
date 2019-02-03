# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 22:22:38 2019

@author: MastaMoose
"""

from bottle import route, run, static_file

@route('/')
def main():
    return static_file('index.html', root='.')

run(host = 'localhost', port = 9999)