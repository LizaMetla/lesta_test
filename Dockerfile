FROM python:3.9-slim

RUN mkdir lesta_test_project
WORKDIR /lesta_test_project

COPY ./requirements/requirements.txt .
RUN pip install -r requirements.txt

COPY . /lesta_test_project
CMD ["python", "app.py"]