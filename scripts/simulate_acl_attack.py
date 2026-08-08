import boto3
from botocore.exceptions import ClientError

# LocalStack S3 setup
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

bucket_name = "annabel-secure-bucket"
file_name = "malicious_public_upload.txt"

# Create a "malicious" file
with open(file_name, "w") as f:
    f.write("This file tries to make itself public!")

print(f"Attempting to upload {file_name} with public-read ACL...")

try:
    s3.upload_file(file_name, bucket_name, file_name, ExtraArgs={"ACL": "public-read"})
    print("⚠️ Upload succeeded — check if ACL was blocked.")
    
    # Verify the ACL status
    acl = s3.get_object_acl(Bucket=bucket_name, Key=file_name)
    grants = acl.get("Grants", [])
    public_grant = any(
        g["Grantee"].get("URI", "") == "http://acs.amazonaws.com/groups/global/AllUsers"
        for g in grants
    )
    
    if public_grant:
        print("❌ Public ACL detected! Your block might not be working.")
    else:
        print("✅ ACL blocked successfully — file is private despite public-read attempt.")
except ClientError as e:
    if "AccessDenied" in str(e):
        print("✅ AccessDenied: Public ACL correctly blocked.")
    else:
        print(f"❌ Unexpected error: {e}")

