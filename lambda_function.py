import os
import json
import boto3

from app.model import write_to_db


USER_ACCESS_KEY = os.environ['USER_ACCESS_KEY']
USER_SECRET_ACCESS_KEY = os.environ['USER_SECRET_ACCESS_KEY']

session = boto3.Session(
    aws_access_key_id=USER_ACCESS_KEY,
    aws_secret_access_key=USER_SECRET_ACCESS_KEY
)
s3 = session.resource('s3')


def lambda_handler(event, context):
    operation = event['httpMethod']

    if operation != 'GET':
        return {"error": f"Unsupported method: {operation}"}

    payload = event['queryStringParameters']

    bucket_name = payload.get('bucket_name')
    object_key = payload.get('object_key')

    try:
        obj = s3.Object(bucket_name, object_key)

        file_content = obj.get()['Body'].read().decode('utf-8').splitlines()

        success = write_to_db(file_content)

        if success:
            return {
                'statusCode': '200',
                'body': json.dumps({
                    'message': 'Sucesso ao inserir dados no banco!'
                }),
                'headers': {'Content-Type': 'application/json'},
            }
        else:
            return {
                'statusCode': '400',
                'body': json.dumps({
                    'message': 'Falha ao inserir dados no banco!'
                }),
                'headers': {'Content-Type': 'application/json'},
            }
    except Exception as e:
        print(e)
        print(
            f'Erro ao obter o objeto {object_key} do bucket {bucket_name}. Verifique que eles existam e que a função está na mesma região do bucket.')
        raise e
