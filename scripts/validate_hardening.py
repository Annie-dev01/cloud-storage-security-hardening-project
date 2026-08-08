import boto3
import json

# Connect to LocalStack S3
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

bucket_name = "annabel-secure-bucket"
file_name = "secure_upload.txt"

print("🔍 Validating bucket hardening...\n")

# Step 1: Upload a new file
with open(file_name, "w") as f:
    f.write("Version 1 of secure file")

s3.upload_file(file_name, bucket_name, file_name)
print("✅ Uploaded first version.")

# Step 2: Check encryption
obj_info = s3.head_object(Bucket=bucket_name, Key=file_name)
encryption = obj_info.get("ServerSideEncryption")

if encryption:
    print(f"🔒 Encryption in place: {encryption}")
else:
    print("❌ No server-side encryption detected!")

# Step 3: Upload a second version
with open(file_name, "w") as f:
    f.write("Version 2 of secure file")

s3.upload_file(file_name, bucket_name, file_name)
print("✅ Uploaded second version.")

# Step 4: List versions
response = s3.list_object_versions(Bucket=bucket_name)
versions = response.get("Versions", [])

print("\n📜 Object Versions:")
for v in versions:
    print(f"  • {v['Key']} — VersionId: {v['VersionId']} — IsLatest: {v['IsLatest']}")

if len(versions) > 1:
    print("\n✅ Versioning confirmed working.")
else:
    print("\n❌ Versioning not working as expected.")

print("\n🎯 Validation complete.")

