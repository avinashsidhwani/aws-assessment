import boto3

s3=boto3.resource("s3", region_name='us-east-1')
bucket = "av-training-q2"
obj_key = "q2.txt"

# getting a list of all the versions of our object
versions = list(s3.Bucket(bucket).object_versions.filter(Prefix=obj_key))

# downloading the second latest version
with open("q2_dl.txt", "wb") as f:
    f.write(versions[1].get()['Body'].read())
