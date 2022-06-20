FROM python:3-alpine

RUN apk add --no-cache bash \
 && pip install --no-cache-dir jpconvert nbstripout

CMD "/bin/bash"
