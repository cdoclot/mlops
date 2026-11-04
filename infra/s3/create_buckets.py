import os
import time

import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

s3 = boto3.client("s3", endpoint_url=os.environ["MLFLOW_S3_ENDPOINT_URL"])

for _ in range(30):
    try:
        existing = {b["Name"] for b in s3.list_buckets().get("Buckets", [])}
        break
    except (EndpointConnectionError, ClientError) as exc:
        print(f"S3 not ready ({exc.__class__.__name__}), retrying...")
        time.sleep(2)
else:
    raise SystemExit("S3 unreachable")

for bucket in os.environ.get("BUCKETS", "mlflow,dvc").split(","):
    if bucket in existing:
        print(f"bucket {bucket} : already there")
    else:
        s3.create_bucket(Bucket=bucket)
        print(f"bucket {bucket} : created")
