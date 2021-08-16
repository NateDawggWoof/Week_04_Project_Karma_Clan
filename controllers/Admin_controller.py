from flask import Flask, render_template, request, redirect, Blueprint

import models.user 
import repositories.user_repository as user_repo
import repositories.deed_repository as deed_repo

admin_blueprint = Blueprint("admin", __name__)

@admin_blueprint.route('/admin')
def admin():
    return render_template("admin/index.html")


@admin_blueprint.route('/admin/usersa')
def users_a():
    # user_repo.order_surname()
    users = user_repo.select_all()
    return render_template("admin/show_users.html", all_users = users)

@admin_blueprint.route('/admin/usera/edit/<id>')
def user_a_edit(id):
    user = user_repo.select(id)
    return render_template("admin/show_user_a_edit.html", user = user)

@admin_blueprint.route("/admin/usersa/delete/<id>", methods=['POST'])
def user_delete(id):
    deed_repo.delete_all_user_deeds(id)
    user_repo.delete(id)
    return redirect('/admin/usersa')


@admin_blueprint.route("/admin/usera/edit/<id>", methods=['POST'])
def update_user(id):
    name_first = request.form['name_first']
    name_last     = request.form['name_last']
    goal_daily    = request.form['goal_daily']
    
    user = user_repo.select(id)
    
    user.name_first = name_first
    user.name_last = name_last
    user.goal_daily = goal_daily
    user_repo.update(user)
    
    return redirect('/admin/usersa')

