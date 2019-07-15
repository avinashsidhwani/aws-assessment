import boto3

dynamodb = boto3.resource('dynamodb' , region_name='us-east-1')

# creating Games table
tbl = dynamodb.create_table(
    TableName='av_games',
    KeySchema=[
        {
            'AttributeName': 'gid',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'gname',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'gid',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'gname',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# adding items
tbl = dynamodb.Table('av_games')
tbl.put_item(
   Item={
        'gid': 1,
        'gname': 'game1',
        'publisher': 'pub1',
        'rating': 4,
        'release_date': '15/6/2019',
        'genres': {
        	'gen1' : 'action',
        	'gen2' : 'space',
        },
    }
)
tbl.put_item(
   Item={
        'gid': 2,
        'gname': 'game2',
        'publisher': 'publisher2',
        'rating': 3,
        'release_date': '24/9/2018',
        'genres': {
        	'gen1' : 'sports',
        },
    }
)
