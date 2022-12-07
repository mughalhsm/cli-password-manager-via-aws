import boto3
import os.path

BUCKET = 'hm-nc-data-bucket'

s3_client = boto3.client('s3')

create_bucket = s3_client.create_bucket(Bucket=BUCKET)
s3_client.upload_file("random.txt", BUCKET, "copy-randon.txt")
s3_client.upload_file("zen.txt", BUCKET, "python-zen.txt")

list_of_contents = ''

s3_contents_of_each_file = []


s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET)
print(bucket.objects.all())
for obj in bucket.objects.all():
    key = obj.key
    body = obj.get()['Body'].read()
    list_of_contents += key + "\n"
    s3_contents_of_each_file.append(body)

print(list_of_contents)
for content in s3_contents_of_each_file:
    print(content)
    print('\n')


if os.path.exists('s3_contents.txt') == False:
    with open("s3_contents.txt", "a") as file_object:
        file_object.write(list_of_contents)

