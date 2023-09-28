# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim

# Working directory
WORKDIR /code

# Warning: A port below 1024 has been exposed. This requires the image to run as a root user which is not a best practice.
# For more information, please refer to https://aka.ms/vscode-docker-python-user-rights`
EXPOSE 8000


# Copy requirements.txt to /code and Install pip requirements
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY ./app /code/app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
