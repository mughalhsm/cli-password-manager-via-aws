# Using Python To Access AWS 

In this sprint, you will practice using the `boto3` library to manage interactions with AWS infrastructure.

## Task One - Warm Up
Create a Python script that:
1. Creates an S3 bucket.
1. Loads two text files to the bucket.
1. Prints a listing of the files, saving the filenames in a readable list.
1. Reads one of the files and prints it to the console.
1. Deletes the files in the bucket.
1. Deletes the bucket.
1. Checks that the bucket is deleted by listing the available buckets (should be none).

## Task Two - AWS-Powered Password Manager

In this task, you will create a simple command-line application to store and retrieve passwords. The passwords will be stored in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). Accessing your AWS account (with your Access Key Id and Secret Key) will be considered sufficient authorisation to retrieve the passwords.

The application should allow you to:
 - store a user id and password as a secret in `secretsmanager`
 - list all the stored secrets
 - retrieve a secret - the resulting user id and password should not be printed out but should be stored in a file.
 - delete a secret.

The basic workflow should look like this:
```bash
awsume sandbox # or whatever means you use to authenticate
[Sandbox]
python password_manager.py
> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
y
> Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
l
> 0 secret(s) available
> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
e
> Secret identifier: 
Missile_Launch_Codes
> UserId:
bidenj
> Password:
Pa55word
> Secret saved.
> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
l
> 1 secret(s) available
  Missile_Launch_Codes
> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
r
> Specify secret to retrieve:
Missile_Launch_Codes
> Secrets stored in local file secrets.txt
> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
d
> Specify secret to delete:
Missile_Launch_Codes
> Deleted
> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
x
> Thank you. Goodbye.

# In the shell:
cat secrets.txt
UserId: bidenj
Password: Pa55word
```

 - Ensure that your code is thoroughly unit-tested. Use mocks if you need to. (Use of the `moto` library to mock `secretsmanager` is encouraged but not required.)
 - Ensure that you use `try...except` to manage potential errors. Input errors or `boto3` client errors should be handled "gracefully" - ie the user should get some informative response and the application should continue running. For example:
 ```
> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
l
> 1 secret(s) available
  Missile_Launch_Codes
> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
r
> Specify secret to retrieve:
Fortnite_Password
> That is not a valid secret.
> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
...
```

 There are many enhancements you could make. Feel free to increase the sophistication of the interface.


