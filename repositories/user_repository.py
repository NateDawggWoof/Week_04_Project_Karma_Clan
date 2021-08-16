from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users (name_first, name_last, goal_daily, total_daily, total_overall) VALUES (%s,%s,%s,%s,%s) RETURNING id"
    values =[user.name_first, user.name_last, user.goal_daily, user.total_daily, user.total_overall]

    results = run_sql(sql,values)

    user.id = results[0]['id']
    return user


def select_all():
    users = []

    sql = "SELECT * FROM users ORDER BY name_last"
    results = run_sql(sql)

    for row in results:
        user = User(row['name_first'],row['name_last'], row['goal_daily'], row['id'])
        user.total_daily = row['total_daily']
        user.total_overall = row['total_overall']
        users.append(user)
    return users


def select(id):
    user = None

    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        user = User(result['name_first'], result['name_last'] ,result['goal_daily'], result['id'])
        user.total_daily = result['total_daily']
        user.total_overall = result['total_overall']
    
    return user


def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def update(user):
    sql = "UPDATE users SET (name_first, name_last, goal_daily, total_daily, total_overall) = (%s,%s,%s,%s, %s) WHERE id = %s"
    values = [user.name_first, user.name_last , user.goal_daily, user.total_daily, user.total_overall, user.id]
    run_sql(sql, values)

# def order_surname():
#     sql = "SELECT * FROM users ORDER BY name_last"
#     run_sql(sql)
