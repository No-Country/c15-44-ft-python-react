FROM python:3.11.5

WORKDIR /server

# Copy only the necessary files for dependency installation
COPY pyproject.toml pdm.lock* /server/

# Install pdm
RUN python -m pip install --upgrade pip && \
    python -m pip install pdm

# Install project dependencies
RUN pdm install

# Copy the rest of the application code
COPY . /server/

# Expose the port your app runs on
EXPOSE 8000

# Command to run the application
CMD ["pdm", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
