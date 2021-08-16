from flask import Flask, render_template, request, redirect, Blueprint

from models.action import Action
from models.user import User
from models.deed import Deed 
import repositories.user_repository as user_repo
import repositories.deed_repository as deed_repo
import repositories.action_repository as action_repo

admin_deeds_blueprint = Blueprint("admin_deeds", __name__)

@admin_deeds_blueprint.route('/admin/deeds')
def admin():
    deeds = deed_repo.select_all()
    users = user_repo.select_all()
    actions = action_repo.select_all()
    return render_template("admin/deeds/index.html", all_deeds = deeds, all_users = users, all_actions = actions)