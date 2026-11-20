# BigMart Retail Sales Dashboard — container image
# Build:  docker build -t bigmart-dashboard .
# Run:    docker run -p 8501:8501 bigmart-dashboard

FROM python:3.11-slim

WORKDIR /app

# System deps kept minimal — Streamlit/Plotly/Pandas don't need build tools
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health')" || exit 1

ENTRYPOINT ["streamlit", "run", "app.py", \
            "--server.port=8501", \
            "--server.address=0.0.0.0"]
