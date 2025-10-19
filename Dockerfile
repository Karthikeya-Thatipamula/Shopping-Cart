# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY backend/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend and frontend code into the container
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Run the application with gunicorn, pointing to the app object in backend/app.py
CMD ["sh", "-c", "python backend/seed.py && gunicorn --bind 0.0.0.0:5001 --chdir backend app:app"]
