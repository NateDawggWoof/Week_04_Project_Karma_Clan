from db.run_sql import run_sql

from models.action import Action

def save(action):
    sql = "INSERT INTO actions (name, description, type, value ) VALUES ( %s,%s,%s,%s) RETURNING id"
    values = [action.name, action.description, action.type, action.value]
    results = run_sql( sql, values )
    
    action.id = results[0]['id']
    return action


def select_all():
    actions = []

    sql = "SELECT * FROM actions"
    results = run_sql(sql)

    for row in results:
        action = Action(row['name'], row['description'], row['type'], row['value'], row['id'])
        actions.append(action)
    return actions


def select(id):
    action = None

    sql = "SELECT * FROM actions WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        action = Action(result['name'], result['description'], result['type'], result['value'], result['id'])
    
    return action


def delete(id):
    sql = "DELETE FROM actions WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM actions"
    run_sql(sql)