import boto3
from datetime import datetime
from hv_back import settings




S3_BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME
AWS_S3_REGION = settings.AWS_S3_REGION

def move_log_to_archive():
    from mainpage.models import AWSAuth
    aws_auth = AWSAuth.objects.first()
    if aws_auth:
        AWS_ACCESS_KEY = aws_auth.access_key_id
        AWS_SECRET_KEY = aws_auth.access_secret_key_id
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_S3_REGION)
    source_key = 'data/daily_log.csv'
    destination_key = f'data/log_{datetime.now().strftime("%y%m%d")}.csv'

    # 파일을 새 위치로 복사합니다.
    s3.copy_object(Bucket=S3_BUCKET_NAME, CopySource={'Bucket': S3_BUCKET_NAME, 'Key': source_key}, Key=destination_key)

    # 원본 파일을 삭제합니다.
    s3.delete_object(Bucket=S3_BUCKET_NAME, Key=source_key)