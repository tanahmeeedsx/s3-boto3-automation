import boto3

BUCKET_NAME = "tanjim-cloud-bucket"
S3_KEY = "test-boto3.txt"
DOWNLOAD_PATH = "files/downloaded-test.txt"

s3 = boto3.client("s3")

s3.download_file(
    BUCKET_NAME,
    S3_KEY,
    DOWNLOAD_PATH
)

print(f"{S3_KEY} downloaded successfully to {DOWNLOAD_PATH}.")
