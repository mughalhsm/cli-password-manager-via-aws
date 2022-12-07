from password_manager import listing, entry, retrieve, deletion
import boto3
from moto import mock_secretsmanager

def test_correct_listing_function():
    with mock_secretsmanager():
        # No secrets have been.
        client = boto3.client('secretsmanager')
        response = client.list_secrets()
        assert listing() == (0, [])
        ## Add two secrets to the mock secretmanager
        client = boto3.client("secretsmanager")
        client.create_secret(
            Name="Mock_secret_1", 
            SecretString="mock-password_1"
        )
        client.create_secret(
            Name="Mock_secret_2", 
            SecretString="mock-password_2"
        )
        response = client.list_secrets()
        assert listing() == (2, ["Mock_secret_1", "Mock_secret_2"])
       

def test_entry_function():
    with mock_secretsmanager():
        unique_id_arn = entry('mock_secret', 'mock_user', 'mock_password')
        client = boto3.client('secretsmanager')
        response = client.list_secrets()
        secrets = response['SecretList'][0]
        mock_secret_arn = secrets['ARN']
        assert unique_id_arn == mock_secret_arn


def test_retrieve_function():
    with mock_secretsmanager():
        entry('mock_secret_1', 'mock_user123', '6793902')
        entry('mock_secret_2', 'mock_user', 'mock_password')
        entry('mock_secret_3', 'mock_user983', '1234442')
        assert retrieve('mock_secret_1') == ('mock_user123', '6793902')
        assert retrieve('mock_secret_3') == ('mock_user983', '1234442')

def test_deletion_function():
    with mock_secretsmanager():
        entry('mock_secret_1', 'mock_user123', '6793902')
        entry('mock_secret_2', 'mock_user', 'mock_password')
        entry('mock_secret_3', 'mock_user983', '1234442')
        assert deletion('mock_secret_1') == 'mock_secret_1'
        assert listing() == (2, ["mock_secret_2", "mock_secret_3"])







   






    

        

