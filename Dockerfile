# Use python3.11
FROM python:3.11-slim

WORKDIR /app

# Copy project to the virtual machine
COPY . /app

# Install requirements libs
RUN pip install -r requirements.txt

#
EXPOSE 8000

# run project
CMD ["python3", "src"]