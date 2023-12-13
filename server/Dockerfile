# build stage
FROM python:3.11.5

# Install pdm
RUN pip install --upgrade pip
RUN pip install pdm

# Copy only the necessary files for dependency installation
COPY pyproject.toml pdm.lock /server/
COPY . /server/

WORKDIR /server

# Check if pyproject.toml exists, if not, run pdm init
RUN [ ! -f pyproject.toml ] && pdm init -n || true

# Remove existing pdm.lock
RUN rm -f pdm.lock

# Install project dependencies
RUN pdm install

#RUN pdm add uvicorn

# Expose the port your app runs on
EXPOSE 8000

# Command to run the application
CMD ["pdm run start", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
