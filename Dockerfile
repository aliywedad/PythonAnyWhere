FROM python:3.10

WORKDIR /backend

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --upgrade djongo pymongo



CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]