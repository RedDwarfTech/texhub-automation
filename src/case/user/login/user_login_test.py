import json
import os
import pprint
import sqlite3
import pytest
from rdpywheel.config.sysenv.env_reader import EnvReader
import requests
from dotenv import dotenv_values
config = dotenv_values('.env')

headers = {
    'Content-Type': 'application/json'
}

class TestUser:

    def test_login(self):
        username = config.get("USER_NAME")
        password = config.get("PASSWORD")
        self.do_login(username, password)

    def do_login(self,username, password):
        login_url = config.get("BASE_URL") + '/infra/user/login'
        session = requests.Session()
        data = {
            'phone': username, 
            'password': password,
            'appId': 'n29Pa29WS1',
            'deviceId': '73ba67a325d86e82b71689c42da593aa',
            'deviceName': '73ba67a325d86e82b71689c42da593aa',
            'deviceType': 4,
            'loginType': 1,
            'cfToken':''
        };
        response = session.post(login_url, data=json.dumps(data), headers = headers)
        if response.status_code == 200:
            login_resp = response.json()
            access_token = login_resp['result']['accessToken']
            refresh_token = login_resp['result']['refreshToken']
            conn = sqlite3.connect('texhub.db')
            c = conn.cursor()
            conn.commit()
            c.execute("INSERT OR REPLACE INTO texhub_config VALUES ('access_token', '" + access_token +"')")
            c.execute("INSERT OR REPLACE INTO texhub_config VALUES ('refresh_token', '" + refresh_token +"')")
            conn.commit()
            return session
        else:
            pprint.pprint(response.json())
            return None


