#/usr/bin/env python3

import json
import os
from flask import Flask,abort,render_template

def filedict_from_json(filename):
    with open(filename,'r') as file:
        filedict = json.loads(file.read())
    return filedict
filename_list = os.listdir('../files')
file_dict_list = [ filedict_from_json('../files/'+filename) \
                  for filename in filename_list ]
title_list = [ file_dict.get('title')  for file_dict in file_dict_list ]


app = Flask(__name__)

@app.route('/')
def index():
    title_list
    return render_template('index.html',title=title)

@app.route('/files/<filename>')
def file(filename):
    pass
