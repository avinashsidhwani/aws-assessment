import logging
import boto3
from boto3.dynamodb.conditions import Key, Attr

# logging config
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

# getting table from db
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tbl = dynamodb.Table('av_games')

# reading entry where gid is 2
response = tbl.query(KeyConditionExpression=Key('gid').eq(2))

for i in response['Items']:
	logger.info("Game: " + str(i['gname']) + " Rating: " + str(i['rating']))
