# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python source files
COPY code1.py .
COPY test_all.py .
COPY test_code1.py .

# Create a non-root user for security
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Default command to run the main application
CMD ["python", "test_code1.py"]

# Alternative commands you can use:
# To run pytest tests: docker run <image> python -m pytest test_code1.py -v
# To run interactive Python: docker run -it <image> python
# To run specific tests: docker run <image> python -m pytest test_code1.py::TestAdd::test_integer_addition -v 