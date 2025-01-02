FROM python:3
ENV PORT=9000
ENV IN_CONTAINER=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY django_todo/ ./django_todo/
RUN chmod +x ./django_todo/start_server.sh
RUN mkdir files
CMD ./django_todo/start_server.sh ${PORT} ${IN_CONTAINER}