FROM python:3.13.4
# Set the working directory
WORKDIR /project
# Copy the requirements file into the container
COPY ../requirements.txt .
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code into the container
COPY . .
# Expose the port the app runs on
EXPOSE 8000
# Optionally add a default command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
