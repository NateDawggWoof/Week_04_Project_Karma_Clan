from flask import Flask, render_template, request, redirect, Blueprint

from models.action import Action
import repositories.user_repository as user_repo
import repositories.deed_repository as deed_repo
import repositories.action_repository as action_repo

admin_actions_blueprint = Blueprint("admin_actions", __name__)

@admin_actions_blueprint.route('/admin/actions')
def actions():
    actions = action_repo.select_all()
    return render_template("admin/actions/index.html", all_actions = actions)

@admin_actions_blueprint.route("/admin/actions/delete/<id>", methods=['POST'])
def delete_action(id):
    deed_repo.delete_all_action_deeds(id)
    action_repo.delete(id)
    return redirect('/admin/actions')


@admin_actions_blueprint.route("/admin/actions/new", methods=['POST'])
def new_action():
    action_name = request.form['action_name']
    action_description = request.form['action_description']
    action_type = request.form['action_type']
    action_value = request.form['action_value']
    
    action = Action(action_name, action_description,action_type, action_value)
    
    action_repo.save(action)
    
    return redirect('/admin/actions')

@admin_actions_blueprint.route('/admin/actions/edit/<id>')
def action_edit(id):
    action = action_repo.select(id)
    return render_template("admin/actions/edit.html", action = action) 

@admin_actions_blueprint.route("/admin/actions/edit/<id>", methods=['POST'])
def update_action(id):
    action_name = request.form['action_name']
    action_description = request.form['action_description']
    action_type = request.form['action_type']
    action_value = request.form['action_value']
    
    action = Action(action_name,action_description,action_type,action_value,id)
    
    action_repo.update(action)
    
    return redirect('/admin/actions')   