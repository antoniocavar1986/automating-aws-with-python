# Importing boto3 and click library #
import boto3
import click

# creating aws s3 session #
session =  boto3.Session(profile_name='AntonioAutomation')
s3 = session.resource('s3')

# Creating group for scripts #
@click.group()
def cli():
    pass

# Script for listing all s3 buckets #
@cli.command('list-s3-buckets')
def list_s3_buckets():
    for bucket in s3.buckets.all():
        print(bucket)
        "List of all s3 buckets"

# Script for listing objets in particulat s3 buckets #
@cli.command('list-s3-objects')
@click.argument('bucket')
def list_s3_objects(bucket):
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)
        "Listing objects from named s3 bucket"

if __name__ == '__main__':
    cli()
