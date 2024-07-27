FROM python

WORKDIR /usr/src/app

COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD [ "python", "./program.py" ]