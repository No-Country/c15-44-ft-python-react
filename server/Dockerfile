FROM python:3.11.5

WORKDIR /server

# Copy only the necessary files for dependency installation
COPY pyproject.toml pdm.lock /server/
COPY . /server/

# Install pdm
RUN python -m pip install --upgrade pip && \
    python -m pip install pdm

# Check if pyproject.toml exists, if not, run pdm init
RUN [ ! -f pyproject.toml ] && pdm init -n || true

# Install project dependencies
RUN pdm install

# Expose the port your app runs on
EXPOSE 8000

# Command to run the application
CMD ["ls && ","pdm", "run start", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
