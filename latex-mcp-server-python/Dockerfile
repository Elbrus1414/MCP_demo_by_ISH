FROM python:3.11-slim            

ENV PYTHONUNBUFFERED=1           

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive-latex-recommended \
        texlive-latex-extra \
        texlive-xetex \
        texlive-fonts-recommended \
        texlive-lang-cyrillic \
        pandoc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

ENTRYPOINT ["python", "/app/server.py"]
