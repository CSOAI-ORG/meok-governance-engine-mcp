FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -s /bin/bash appuser
WORKDIR /app
USER appuser

# Copy source code
COPY --chown=appuser:appuser . /app

# Install dependencies
RUN pip install --no-cache-dir -e .

# Expose port (if needed)
EXPOSE 8000

# Run the MCP server
CMD ["python", "server.py"]