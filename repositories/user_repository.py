from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users (name, goal_daily, total_daily, total_overall) VALUES (%s,%s,%s,%s) RETURNING id"
    values =[user.name, user.goal_daily, user.total_daily, user.total_overall]

    results = run_sql(sql,values)

    user.id = results[0]['id']
    return user

