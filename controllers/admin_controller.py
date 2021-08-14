from flask import Flask, render_template, request, redirect, Blueprint

home_blueprint = Blueprint("locations", __name__)

@home_blueprint.route('/home')
def home():
    render_template("home/index.html")
