from flask import Flask, render_template, request, redirect, Blueprint

from models.user import User
import repositories.user_repository as user_repo
import repositories.deed_repository as deed_repo

admin_actions_blueprint = Blueprint("admin_actions", __name__)

@admin_actions_blueprint.route('/admin/actions')
def admin():
    return render_template("admin/actions/index.html")