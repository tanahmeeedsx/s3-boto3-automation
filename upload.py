import boto3

BUCKET_NAME = "tanjim-cloud-bucket"
FILE_PATH = "files/test-boto3.txt"
S3_KEY = "test-boto3.txt"

s3 = boto3.client("s3")

s3.upload_file(
    FILE_PATH,
    BUCKET_NAME,
    S3_KEY
)

print(f"{FILE_PATH} uploaded successfully to S3.")
