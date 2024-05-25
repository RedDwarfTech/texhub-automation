
import sqlite3


class CachedUtil:

    @staticmethod
    def get_config(key: str):
        conn = sqlite3.connect('texhub.db')
        c = conn.cursor()  
        c.execute("SELECT * FROM texhub_config where name = '" + key +"'")
        result = c.fetchall()
        return result['value']





