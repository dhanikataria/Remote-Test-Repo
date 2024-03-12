FROM python:latest

#Enter the path where your file is located
WORKDIR /app

#to COPY the remote file at working directory in container
COPY main.py ./
# Now the structure looks like this '/home/remnux/Downloads/local-repo/hello.py'


#CMD instruction should be used to run the software
#contained by your image, along with any argumentsss.

CMD [ "python3", "main.py"]
