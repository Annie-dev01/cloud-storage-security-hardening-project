import boto3
import requests

# LocalStack S3 setup
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

bucket_name = "annabel-secure-bucket"
file_name = "secure_upload.txt"

# Create a test file
with open(file_name, "w") as f:
    f.write("Hello, this is a secure upload test!")

# Upload the file
s3.upload_file(file_name, bucket_name, file_name)
print("✅ File uploaded successfully.")

# Check if the file uses encryption in transit (HTTPS)
endpoint = "http://localhost:4566"
if endpoint.startswith("https://"):
    print("✅ Connection encrypted in transit (HTTPS).")
else:
    print("⚠️ Using HTTP (LocalStack runs locally, so this is fine).")

# Check server-side encryption status
response = s3.head_object(Bucket=bucket_name, Key=file_name)
encryption = response.get("ServerSideEncryption")

if encryption:
    print(f"✅ Server-side encryption enabled: {encryption}")
else:
    print("❌ Server-side encryption not enabled!")


