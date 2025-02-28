import requests
import boto3
import os
import logging
from botocore.exception import ClientError

#make client
s3 = boto3.client('s3', region_name='us-east-1')

#upload file
bucket = 'ds2002-mst3k'
local_file = 'project/vuelta.jpg'



#make request
def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded to {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading: {e}")


#upload file
bucket = 'ds2002-mst3k'
local_file = 'project/vuelta.jpg'

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = local_file
    ACL='public read'



#presigned url
def create_presigned_url(bucket_name, object_name, expiration=3600):

    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    return response


download_file(image_url, path)
