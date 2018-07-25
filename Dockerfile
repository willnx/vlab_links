FROM willnx/vlab-base
COPY dist/*.whl /tmp

RUN pip install /tmp/*.whl && rm /tmp/*.whl
RUN apk del gcc
WORKDIR /usr/lib/python3.6/site-packages/vlab_link_api
CMD uwsgi --ini ./app.ini
