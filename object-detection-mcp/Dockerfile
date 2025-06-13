FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends libglib2.0-0 libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python - <<'PY'
import contextlib, sys, io
from ultralytics import YOLO

with contextlib.redirect_stdout(sys.stderr):
    YOLO("yolov8n.pt")
PY

COPY server.py .
EXPOSE 3333

CMD ["python", "server.py"]
