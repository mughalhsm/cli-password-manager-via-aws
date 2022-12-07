import boto3

BUCKET = 'hm-nc-data-bucket'

s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET)
response = bucket.delete()

print(response)