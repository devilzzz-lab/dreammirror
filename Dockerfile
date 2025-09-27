FROM python:3.13-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Install spaCy explicitly
RUN pip install spacy

# Download spaCy English model
RUN python -m spacy download en_core_web_sm

# Copy the app code
COPY . .

# Ensure output directory exists
RUN mkdir -p /app/app/dream_outputs

# Expose port
EXPOSE 8000

# Run backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
