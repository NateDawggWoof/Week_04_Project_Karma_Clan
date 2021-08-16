from db.run_sql import run_sql

from models.deed import Deed

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
        deed = Deed(row['user_id'], row['action_id'], row['date'], row['id'])
        deeds.append(deed)
    return deeds


def select(id):
    deed = None

    sql = "SELECT * FROM actions WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        deed = Deed(result['user_id'], result['action_id'], result['date'], result['id'])
    
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

def update(deed):
    sql = "UPDATE deeds SET (user_id, action_id, date) = (%s,%s,%s) WHERE id = %s"
    values = [deed.user.id, deed.action.id, deed.date, deed.id]
    run_sql(sql, values)