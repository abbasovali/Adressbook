FROM python:3.8

# create and set the working directory
RUN mkdir /app
WORKDIR /app

# copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the rest of the app code
COPY . .

# set the FLASK_APP environment variable
ENV FLASK_APP=app.py

# run the app
CMD ["flask", "run", "--host=0.0.0.0"]
