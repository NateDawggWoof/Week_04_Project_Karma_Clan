from flask import Flask, render_template, request, redirect, Blueprint

from models.user import User
import repositories.user_repository as user_repo
import repositories.deed_repository as deed_repo

admin_actions_blueprint = Blueprint("admin", __name__)