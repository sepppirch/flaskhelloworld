
import json
import flask
from flask import Flask
from flask import (Flask, jsonify, redirect, render_template, request, session,
                   url_for)

app = Flask(__name__)

@app.route("/")
def hello_meineliebe():
    return render_template("page1.html")


@app.route("/posting")
def posting():
    id = int(flask.request.args.get("id"))
    print(id)
    imagepath = ["/static/hund2.jpg","/static/hund1.jpg", "/static/axlotto.jpg"]
    text = ["reeeeee","ruuuu", "er war haesslich - trotzdem!"]
    return render_template("posting.html", image = imagepath[id], text = text[id])