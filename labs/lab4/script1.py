#!/bin/bash

LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION_TIME=$3


#upload file
aws s3 cp "$LOCAL_FILE" s3://"$BUCKET_NAME"/


#presigned url
aws s3 presign --expires-in "$EXPIRATION_TIME" s3://"$BUCKET_NAME"/"$LOCAL_FILE"

