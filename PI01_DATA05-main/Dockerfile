FROM python:3.11.1
COPY . /carp1/carp2
WORKDIR /carp1/carp2
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0"]