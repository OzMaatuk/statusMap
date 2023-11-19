FROM  mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

WORKDIR /statusmap

# copy files from host
COPY . .

# Install dependencies
RUN pip install pymongo flask python-dotenv

EXPOSE 5000

# Run server
CMD ["python", "server.py"]