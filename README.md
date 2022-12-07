##AWS-Powered Password Manager

I created a simple command-line application to store and retrieve passwords. 

The passwords are stored in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). 

Accessing your AWS account (with your Access Key Id and Secret Key) will be considered sufficient authorisation to retrieve the passwords.

The application allows you to:
 - store a user id and password as a secret in `secretsmanager`
 - list all the stored secrets
 - retrieve a secret - the resulting user id and password will not be printed out but should be stored in a file.
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

 - The code is thoroughly unit-tested. I used the `moto` library to mock `secretsmanager`.




