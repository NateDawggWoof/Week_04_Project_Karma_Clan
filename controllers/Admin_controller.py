from flask import Flask, render_template, request, redirect, Blueprint

admin_blueprint = Blueprint("admin", __name__)

@admin_blueprint.route('/admin')
def admin():
    render_template("admin/index.html")
