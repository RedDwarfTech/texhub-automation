import sqlite3
import pytest
import requests
from dotenv import dotenv_values

config = dotenv_values('.env')

class TestProject:

    def test_project_list(self):
        login_url = config.get("BASE_URL") + '/tex/project/list'
        session = requests.Session()
        access_token = self.get_config('access_token')
        pytest.set_trace()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': access_token
        }
        response = session.get(login_url, headers = headers)
        if response.status_code == 200:
            print("success")
        else:
            print("failed")

    def get_config(self, key: str):
        conn = sqlite3.connect('texhub.db')
        c = conn.cursor()  
        c.execute("SELECT * FROM texhub_config where name = '" + key +"'")
        result = c.fetchall()
        return result['value']



