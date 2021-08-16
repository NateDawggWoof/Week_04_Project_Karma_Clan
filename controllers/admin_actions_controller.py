from flask import Flask, render_template, request, redirect, Blueprint

from models.user import User
import repositories.user_repository as user_repo
import repositories.deed_repository as deed_repo
import repositories.action_repository as action_repo

admin_actions_blueprint = Blueprint("admin_actions", __name__)

@admin_actions_blueprint.route('/admin/actions')
def admin():
    actions = action_repo.select_all()
    return render_template("admin/actions/index.html", all_actions = actions)

@admin_actions_blueprint.route("/admin/actions/delete/<id>", methods=['POST'])
def user_delete(id):
    deed_repo.delete_all_action_deeds(id)
    action_repo.delete(id)
    return redirect('/admin/actions')    