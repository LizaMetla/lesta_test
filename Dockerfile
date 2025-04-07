FROM python:3.9-slim

RUN mkdir lesta_test_project
WORKDIR /lesta_test_project

COPY . /lesta_test_project

RUN pip install -r requirements/requirements.txt

CMD ["python", "app.py"]