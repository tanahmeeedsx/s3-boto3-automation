import boto3

BUCKET_NAME = "tanjim-cloud-bucket"
S3_KEY = "test-boto3.txt"

s3 = boto3.client("s3")

s3.delete_object(
    Bucket=BUCKET_NAME,
    Key=S3_KEY
)

print(f"{S3_KEY} deleted successfully from S3.")
