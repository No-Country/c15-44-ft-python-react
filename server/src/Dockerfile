FROM python:3.11.5

WORKDIR /app

# Copy only the necessary files
COPY . /app

# Install dependencies
RUN pip install pdm
RUN pdm install

# Expose the port your app runs on
EXPOSE 8000

# Command to run the application
CMD ["pdm", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

