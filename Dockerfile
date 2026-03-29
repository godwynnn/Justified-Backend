RUN apt-get update


RUN pip install --upgrade pip
# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /app/
CMD [ "daphne","server.wsgi:application" ]