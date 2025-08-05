import json
import os

import boto3
from botocore.exceptions import ClientError


class S3:
    def __init__(self, bucket_name=None):
        self.s3_client = boto3.client("s3")
        self.bucket_name = bucket_name or os.getenv("ETL_MARKETING_BUCKET")

    def upload_file(self, data, folder, file_name):
        json_data = json.dumps(data, indent=4)
        file_path = f"{folder}/{file_name}"
        try:
            response = self.s3_client.put_object(
                Body=json_data,
                Key=file_path,
                Bucket=self.bucket_name,
                ContentType="application/json",
            )
        except ClientError:
            return response
        return True
