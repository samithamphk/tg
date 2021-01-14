FROM python:3.7-slim-stretch

RUN apt update
RUN apt install -y python3-dev gcc

ADD requirements.txt requirements.txt
#ADD export.pkl export.pkl
ADD *.py .

# Install required libraries
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

# Run it once to trigger resnet download
#RUN python app.py

EXPOSE 8136

# Start the server
ENTRYPOINT ["python"]
CMD ["app.py"]