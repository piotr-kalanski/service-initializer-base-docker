FROM python:3

WORKDIR /usr/src/app

COPY base_requirements.txt ./
RUN pip install --no-cache-dir -r base_requirements.txt

COPY . .

ENTRYPOINT [ "python", "./main.py" ]