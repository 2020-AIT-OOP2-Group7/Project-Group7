#!/usr/bin/env python
# coding:utf-8
from flask import Flask, request,render_template,send_from_directory  # Flaskは必須、requestはリクエストパラメータを処理する場合に使用します。
from werkzeug.utils import secure_filename
import glob
import os
app = Flask(__name__)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(host="localhost", port=8080, debug=True)
