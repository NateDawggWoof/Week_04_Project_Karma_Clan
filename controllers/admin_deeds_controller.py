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

@admin_deeds_blueprint.route("/admin/edits/delete//<id>", methods=['POST'])
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

@admin_deeds_blueprint.route('/admin/deeds/edit/<id>')
def edit_deed(id):
    deed = deed_repo.select(id)
    return render_template("admin/deeds/edit.html", deed = deed) 

@admin_deeds_blueprint.route("/admin/deeds/edit/<id>", methods=['POST'])
def update_deed(id):
    deed_user_id = request.form['deed_user']
    deed_user = user_repo.select(deed_user_id)

    deed_action_id = request.form['deed_action']
    deed_action = action_repo.select(deed_action_id)
    deed_date = request.form['deed_date']
   
    
    deed = Deed(deed_user,deed_action,deed_date,id)
    
    deed_repo.update(deed)
    
    return redirect('/admin/deeds') 


@admin_deeds_blueprint.route('/admin/deeds/user/<id>')
def deeds_user(id):
    user = user_repo.select(id)
    deeds = deed_repo.select_all_by_user_date(id)
    daily_total = "Choose Date"


    return render_template("admin/deeds/user/index.html", all_deeds = deeds, user = user, daily_total = daily_total)

@admin_deeds_blueprint.route('/admin/deeds/user/view/<id>', methods=['POST'])
def deeds_user_view(id):
    user = user_repo.select(id)
    date = request.form['deed_user_date']
    deeds = deed_repo.select_all_by_user_and_date(id,date) 
    daily_total = deed_repo.sum_value_select_all_by_user_and_date(id,date)

    
    return render_template("admin/deeds/user/index.html", all_deeds = deeds, user = user, daily_total = daily_total)