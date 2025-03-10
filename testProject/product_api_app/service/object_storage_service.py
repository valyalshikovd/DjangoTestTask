
import os
import boto3

def upload_file(bucket, key, data):
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url=os.getenv("OBJECT_STORAGE_URL"),
        region_name=os.getenv("OBJECT_STORAGE_REGION"),
        aws_access_key_id=os.getenv("OBJECT_STORAGE_KEY_ID"),
        aws_secret_access_key=os.getenv("OBJECT_STORAGE_SECRET_KEY"))
    s3.upload_fileobj(data, bucket, key)



def get_file(bucket, key):
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url=os.getenv("OBJECT_STORAGE_URL"),
        region_name=os.getenv("OBJECT_STORAGE_REGION"),
        aws_access_key_id=os.getenv("OBJECT_STORAGE_KEY_ID"),
        aws_secret_access_key=os.getenv("OBJECT_STORAGE_SECRET_KEY"))
    return s3.get_object(Bucket=bucket, Key=key)