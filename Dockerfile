FROM python:3.10-alpine3.21

WORKDIR /app

COPY ./dist/* /app/

RUN python -m venv venv \
    && . venv/bin/activate \
    && pip install /app/*.whl

CMD ["./venv/bin/python", "-m", "python_demo.app"]