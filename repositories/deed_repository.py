from db.run_sql import run_sql

from models.deed import Deed

import repositories.user_repository as user_repo
import repositories.action_repository as action_repo

def save(deed):
    sql = "INSERT INTO deeds (user_id, action_id, date) VALUES (%s,%s,%s) RETURNING id"
    values = [deed.user.id, deed.action.id, deed.date]
    results = run_sql( sql, values )
    
    deed.id = results[0]['id']
    return deed

def select_all():
    deeds = []

    sql = "SELECT * FROM deeds"
    results = run_sql(sql)

    for row in results:
        user = user_repo.select(row['user_id'])
        action = action_repo.select(row['action_id'])

        deed = Deed(user, action, row['date'], row['id'])
        deeds.append(deed)
    return deeds


def select(id):
    deed = None

    sql = "SELECT * FROM deeds WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        user = user_repo.select(result['user_id'])
        action = action_repo.select(result['action_id'])

        deed = Deed(user, action, result['date'], result['id'])
    
    return deed

def delete(id):
    sql = "DELETE FROM deeds WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM deeds"
    run_sql(sql)

def delete_all_user_deeds(id):
    sql = "DELETE FROM deeds WHERE user_id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all_action_deeds(id):
    sql = "DELETE FROM deeds WHERE action_id = %s"
    values = [id]
    run_sql(sql, values)

def update(deed):
    sql = "UPDATE deeds SET (user_id, action_id, date) = (%s,%s,%s) WHERE id = %s"
    values = [deed.user.id, deed.action.id, deed.date, deed.id]
    run_sql(sql, values)




def select_all_by_user_date(id):
    deeds = []

    sql = "SELECT * FROM deeds WHERE user_id = %s ORDER BY date"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        user = user_repo.select(row['user_id'])
        action = action_repo.select(row['action_id'])

        deed = Deed(user, action, row['date'], row['id'])
        deeds.append(deed)
    return deeds

def select_all_by_user_and_date(id,date):
    deeds = []
    date = str(date)

    sql = "SELECT * FROM deeds WHERE user_id = %s ORDER BY date"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        user = user_repo.select(row['user_id'])
        action = action_repo.select(row['action_id'])

        deed = Deed(user, action, row['date'], row['id'])
        deed.date = str(deed.date)
        
        if deed.date == date:
            deeds.append(deed)
    return deeds

def sum_value_select_all_by_user_and_date(id,date):
    deeds = []
    total_actions_value = 0
    date =str(date)

    sql = "SELECT * FROM deeds WHERE user_id = %s ORDER BY date"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        user = user_repo.select(row['user_id'])
        action = action_repo.select(row['action_id'])


        deed = Deed(user, action, row['date'], row['id'])

        deed.date = str(deed.date)
        if deed.date == date:
            deeds.append(deed)
            total_actions_value += action.value
    return total_actions_value