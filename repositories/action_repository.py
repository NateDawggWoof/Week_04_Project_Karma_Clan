from db.run_sql import run_sql

from models.action import Action

def save(action):
    sql = "INSERT INTO actions (name, description, type, value ) VALUES ( %s,%s,%s,%s) RETURNING id"
    values = [action.name, action.description, action.type, action.value]
    results = run_sql( sql, values )
    
    action.id = results[0]['id']
    return action