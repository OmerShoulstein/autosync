import sqlite3


def execute_query(query, params):
    db = sqlite3.connect("users.db")
    result = list(db.execute(query, params))
    db.commit()
    db.close()
    return result
