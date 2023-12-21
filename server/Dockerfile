# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set environment variables
#ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
#WORKDIR /server

WORKDIR /server/

# Install project dependencies using pip
COPY /requirements.txt /server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

# Expose the port your app runs on
#EXPOSE 8000

#ENV PATH="./server/:${PATH}"

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000" ,"--reload"]
#CMD ["uvicorn", "server.src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
