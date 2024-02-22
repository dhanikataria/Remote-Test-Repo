FROM python:latest

#Enter the path where your file is located
WORKDIR /home/remnux/Downloads/local-repo

#to COPY the remote file at working directory in container
COPY hello.py ./
# Now the structure looks like this '/home/remnux/Downloads/local-repo/hello.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "hello.py"]
