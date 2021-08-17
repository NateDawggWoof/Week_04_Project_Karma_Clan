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
    # user = user_repo.select(deed.user)
    actions = action_repo.select_all()
    return render_template("admin/deeds/index.html", all_deeds = deeds, all_users = users, all_actions = actions)

@admin_deeds_blueprint.route("/admin/deeds/delete/<id>", methods=['POST'])
def delete_deed(id):
    deed_repo.delete(id)
    return redirect('/admin/deeds')


@admin_deeds_blueprint.route("/admin/deeds/new", methods=['POST'])
def new_action():
    deed_user_id = request.form['deed_user']
    deed_user = user_repo.select(deed_user_id)

    deed_action_id = request.form['deed_action']
    deed_action = action_repo.select(deed_action_id)
    deed_date = request.form['deed_date']
   
    
    deed = Deed(deed_user,deed_action,deed_date)
    
    deed_repo.save(deed)
    
    return redirect('/admin/deeds')