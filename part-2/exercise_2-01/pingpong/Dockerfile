FROM python:3
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY pingpong.py .
CMD [ "python", "./pingpong.py" ]