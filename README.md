# texhub-automation

This project used to test the texhub rest api.

#### Run single api test

Switch to the project root folder and run:

```bash
# test login
pytest src/case/user/login/user_login_test.py
# test project list
pytest src/case/project/base/test_project.py
# print the content to console
pytest -s src/case/project/base/test_project.py
```

#### tracing the variable

add the tracing code in context:

```python
pytest.set_trace()
```

then you can print any variable in the code context.

#### Generate test report

use this command to run test and generate test report.

```bash
pytest --html=report.html --self-contained-html
```
