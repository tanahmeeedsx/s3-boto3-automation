import boto3

BUCKET_NAME = "tanjim-cloud-bucket"

s3 = boto3.client("s3")

response = s3.list_objects_v2(Bucket=BUCKET_NAME)

print("Files in S3 bucket:")

for obj in response.get("Contents", []):
    print(obj["Key"])
