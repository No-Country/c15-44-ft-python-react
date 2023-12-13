FROM python:3.11.5

WORKDIR /server

# Copy only the necessary files for dependency installation
COPY . /server/
COPY pyproject.toml pdm.lock /server/

# Install pdm
RUN python -m pip install --upgrade pip && \
    python -m pip install pdm

# Install project dependencies
RUN pdm install

# Expose the port your app runs on
EXPOSE 8000

# Command to run the application
CMD ["sh", "-c", "cd /server && pdm run start uvicorn src.main:app --host 0.0.0.0 --port 8000"]