import boto3
import click

session = boto3.Session(profile_name='AntonioAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to aws"
    pass

@cli.command('list_buckets')
def list_buckets():
    "List my S3 Buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List ALL s3 bucket objects"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == '__main__':
    cli()
