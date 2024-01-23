FROM python:3.10
WORKDIR test_task
COPY ./requirements.txt /test_task/requirements.txt
RUN pip install --no-cache-dir -r /test_task/requirements.txt
COPY ./app /test_task/app
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]