FROM public.ecr.aws/lambda/python:3.12

WORKDIR /var/task

ENV PYTHONPATH="/var/task/src"
ENV PYTHONPATH="/var/task/lambda_handlers"

COPY pyproject.toml poetry.lock ./

RUN python3 -m pip install poetry
RUN poetry install --no-root --only main

COPY src/ ./src/
COPY lambda_handlers/ ./lambda_handlers/

CMD ["lambda_handlers.bronze_email_marketing_handler.lambda_handler"]
