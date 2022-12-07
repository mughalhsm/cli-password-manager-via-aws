import boto3
from botocore.exceptions import ClientError
import json
import os.path

def ask():
    answer = input("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it: ")
    input_selection(answer)

list_of_options = ['e', 'l', 'd', 'x', 'r']

def input_selection(character):
    letter = character.lower()
    if letter == 'e':
        secret_identifier = input('Secret identifier: ')
        user_id = input('UserID: ')
        password_input = input('Password ')
        entry(secret_identifier, user_id, password_input)
        ask()
    if letter == 'l':
        listing()
        ask()
    if letter == 'd':
        secret_delete = input('Specify secret to delete: ')
        deletion(secret_delete)
        ask()
    if letter == 'r':
        passcode_required = input('Specify secret to retrieve: ')
        retrieve(passcode_required)
        ask()
    if letter == 'x':
        exit()
    if letter not in list_of_options:
        answer = input("Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it: ")
        input_selection(answer)


def listing():
    client = boto3.client('secretsmanager')
    try:
        response = client.list_secrets()
    except ClientError as error:
        print(error.response['Error']['Code'])
    else: 
        secrets = response['SecretList']
        number_secrets = len(secrets)
        if number_secrets == 0:
            print('0 secret(s) available')
            return 0, []
        else:
            print(f'{number_secrets} secret(s) available:')
            secrets_collected = []
            for secret in secrets:
                print(secret['Name'])
                secrets_collected.append(secret['Name'])
            return number_secrets, secrets_collected

def entry(secret_identifier, user_id, password_input):
    client = boto3.client('secretsmanager')
    try:
        response = client.create_secret(
            Name=f'{secret_identifier}', 
            SecretString=f'{{"username": "{user_id}", "password": "{password_input}"}}'
        )
        ARN = response['ARN']
    except ClientError as error:
        print(error.response['Error']['Code'])
    else: 
        print(f'Secret: "{secret_identifier}" created.')
        return ARN

    
def retrieve(secret_required):
    username = ''
    password = ''
    client = boto3.client('secretsmanager')

    try:
        secret_response = client.get_secret_value(
            SecretId=f'{secret_required}'
        )
    except ClientError as error:
        print(error.response['Error']['Code'])
        print('This secret does not exist.')
    else:
        database_secret = json.loads(secret_response['SecretString'])
        username_retrieved = database_secret['username']
        password_retireved = database_secret['password']
        with open("secrets.txt", "a") as file_object:
            file_object.write(f'\nSecret Name {secret_required} \nUsername: {username_retrieved} \nPassword: {password_retireved}\n')
        print(f'{secret_required} stored in secrets.txt file')
        return username_retrieved, password_retireved
    

def deletion(secret_required):
    client = boto3.client('secretsmanager')
    try:
        response = client.delete_secret(
            SecretId=f'{secret_required}',
            ForceDeleteWithoutRecovery=True
        )
    except ClientError as error:
        print(error.response['Error']['Code'])
    else:
        print(f'Secret: "{secret_required}" deleted.')
        return response['Name']
    
def exit():
    return print('Thank you. Goodbye.')


if __name__ == '__main__':
    ask()



