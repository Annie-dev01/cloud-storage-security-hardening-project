import boto3
from botocore.exceptions import ClientError

# --- LocalStack S3 Configuration ---
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

bucket_name = "annabel-secure-bucket"

print(f"🔐 Hardening bucket: {bucket_name} ...\n")

# Step 0 — Create bucket if it doesn't exist
try:
    s3.head_bucket(Bucket=bucket_name)
    print(f"📦 Bucket '{bucket_name}' already exists.\n")
except ClientError:
    s3.create_bucket(Bucket=bucket_name)
    print(f"🆕 Bucket '{bucket_name}' created successfully.\n")

# Step 1 — Block all public access
s3.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        "BlockPublicAcls": True,
        "IgnorePublicAcls": True,
        "BlockPublicPolicy": True,
        "RestrictPublicBuckets": True
    }
)
print("✅ Step 1: Public access blocked")

# Step 2 — Enforce default server-side encryption (AES256)
s3.put_bucket_encryption(
    Bucket=bucket_name,
    ServerSideEncryptionConfiguration={
        "Rules": [
            {
                "ApplyServerSideEncryptionByDefault": {
                    "SSEAlgorithm": "AES256"
                }
            }
        ]
    }
)
print("✅ Step 2: Default server-side encryption (AES256) enforced")

# Step 3 — Enable versioning
s3.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={"Status": "Enabled"}
)
print("✅ Step 3: Bucket versioning enabled")

# Step 4 — Verify settings
print("\n🧩 Verifying configuration...")

encryption_status = s3.get_bucket_encryption(Bucket=bucket_name)
versioning_status = s3.get_bucket_versioning(Bucket=bucket_name)
public_block = s3.get_public_access_block(Bucket=bucket_name)

print(f"🔒 Encryption: {encryption_status['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']}")
print(f"📜 Versioning: {versioning_status.get('Status', 'Not Enabled')}")
print(f"🚫 Public Access Blocked: {public_block['PublicAccessBlockConfiguration']}")

print("\n✅ Bucket successfully hardened!")

