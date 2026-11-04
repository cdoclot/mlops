# MLflow server image: pinned version + Postgres and S3 drivers.
# Same Python as the project (.python-version) to keep one version across the repo.
FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:0.13.5 /uv /bin/uv

RUN uv pip install --system --no-cache \
      mlflow==3.17.2 \
      "psycopg[binary]==3.3.6" \
      boto3==1.43.118

EXPOSE 5000
