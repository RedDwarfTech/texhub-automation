from dotenv import load_dotenv
import pytest


if __name__ == '__main__':
    load_dotenv()
    print("Running")
    pytest.main(['-vs','./case/user/login/user_login_test.py'])