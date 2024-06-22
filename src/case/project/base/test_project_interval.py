import pprint
import sqlite3
import pytest
import requests
from dotenv import dotenv_values
from datetime import datetime
import time

config = dotenv_values('.env')

class TestProjectInterval:

    def test_proj_interval(self):
        while True:
            login_url = config.get("BASE_URL") + '/tex/project/list'
            session = requests.Session()
            access_token = self.get_config('access_token')
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + access_token
            }
            response = session.get(login_url, headers = headers)
            current_time = datetime.now()
            if response.status_code == 200:
                pprint.pprint(response.json())
                print("success" + str(current_time))
            else:
                pprint.pprint(response.json())
                print("failed" + str(current_time))
            time.sleep(1)

    def get_config(self, key: str):
        conn = sqlite3.connect('texhub.db')
        c = conn.cursor()  
        c.execute("SELECT * FROM texhub_config where name = '" + key +"'")
        result = c.fetchall()
        
        return result[0][1]



