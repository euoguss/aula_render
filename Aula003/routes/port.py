from flask import Flask, render_template, Blueprint

port_route = Blueprint('port', __name__)

@port_route.route("/")
def form():
    return render_template("index.html")
    ...