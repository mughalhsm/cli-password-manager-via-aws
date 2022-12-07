import boto3    
import os

BUCKET = 'hm-nc-data-bucket'


s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET)
bucket.object_versions.delete()



os.remove("s3_contents.txt")