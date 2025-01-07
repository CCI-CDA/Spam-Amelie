FROM python:3.13.0

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3333

CMD [ "fastapi", "run", "--host", "0.0.0.0", "--port", "3333" ]
