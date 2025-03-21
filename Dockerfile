FROM python:3.9-slim-buster

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/. .

# Set environment variables (Render will override these if set in dashboard)
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PORT=10000

# Expose the port Render expects
EXPOSE 10000

# Use Flask's production-ready server
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "10000"]
