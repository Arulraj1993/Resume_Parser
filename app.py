# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:24:40 2020

@author: ELCOT
"""

from flask import Flask

#UPLOAD_FOLDER = 'C:/Users/ELCOT/Desktop/MINI_PROJECT_BACKUP/Uploads'
UPLOAD_FOLDER='F:/SEMESTER4/MINI_PROJECT/pdf_to_text/Uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024