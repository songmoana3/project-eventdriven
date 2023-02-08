FROM python:3.9-alpine
RUN apk update && apk upgrade

WORKDIR /app
COPY ./ /app

CMD if [ ! -z ./venv/bin/ ]; then \
echo "[INFO]::Virtual environment not found in Docker container. Proceeding with virtual environment installation." && \
python3 -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
cd server && \
uvicorn main:app --host 0.0.0.0 --port 3001 --reload\
;else \
echo "[INFO]::Virtual environment is already installed. Installing required packages." && \
source venv/bin/activate && \ 
pip install -r requirements.txt && \
cd server && \
uvicorn main:app --host 0.0.0.0 --port 3001 --reload \
;fi 
