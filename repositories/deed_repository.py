from db.run_sql import run_sql

from models.deed import Deed

def save(deed):
    sql = "INSERT INTO deeds (user_id, action_id, date) VALUES (%s,%s,%s) RETURNING id"
    values = [deed.user.id, deed.action.id, deed.date]
    results = run_sql( sql, values )
    
    deed.id = results[0]['id']
    return deed