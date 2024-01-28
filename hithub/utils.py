import boto3
from botocore.exceptions import NoCredentialsError
from environs import Env
env = Env()
env.read_env()
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")

# Allow a user to get an image asset from S3 via a signed URL
def generate_signed_url(filename, bucket_name=AWS_STORAGE_BUCKET_NAME, expiration=3600):
    try:
        # Create an S3 client
        s3 = boto3.client('s3')

        # Generate a signed URL that expires after 'expiration' seconds
        signed_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': filename},
            ExpiresIn=expiration
        )
        return signed_url
    
    except NoCredentialsError:
        return None  # Handle authentication error