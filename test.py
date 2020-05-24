import json
import boto3
import logging
import os
import datetime
import time


# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s - %(message)s')

# Suppress boto3 logging
logging.getLogger('boto3').setLevel(logging.WARNING)
logging.getLogger('botocore').setLevel(logging.WARNING)

def lambda_handler(event, context):
    # a function that is triggered by API Gateway and invokes the speaker-bot state machine

    # dump event
    logger.info(json.dumps(event))

    ec2 = boto3.client('ec2')

    # Retrieves all regions/endpoints that work with EC2
    response = ec2.describe_regions()
    print('Regions:', response['Regions'])

    # Retrieves availability zones only for region of the ec2 object
    response = ec2.describe_availability_zones()
    print('Availability Zones:', response['AvailabilityZones'])

    return 'success'