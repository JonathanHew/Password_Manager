import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# function to create a key which will be used to encrypt the txt file
# this function should only be called once to create only a single key. 
# It should be commented out after it is called
# to comment in or out the code remove or add the ''' before and after 

'''
def write_key():
    #generate a key using the imported ferenet cryptgraphy package
    key = Fernet.generate_key()
    #open key file in write in bites mode
    with open("key.key", "wb") as k_file:
        k_file.write(key)

write_key() 
'''


#function to load key which was previously created
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#funtion to view paswords on manager
def view():
    print('\n')
    print("Your Passwords:")
    #open the txt file in read mode
    with open("passwords.txt", 'r') as file:
        #loop through the txt file and print out each line
        for line in file.readlines():
            data = line.rstrip()
            #split each line into 2 variables, one for account name, one for the password
            account, password = data.split("|")
            print("Account:", account, "| Password:", fer.decrypt(password.encode()).decode())


#funtion to add a new password onto the manager
def add():
    name = input("Account Name: ")
    password = input("Password: ")
    token = fer.encrypt(password.encode())
    
    #open a txt file in append mode to add to the end of the file, or create the file if it doesnt exist 
    with open("passwords.txt", 'a') as file:
        file.write(name+ "|" + token.decode() + "\n")


master_pwd = input("What is the master password? ")
b_master_pwd = master_pwd.encode()
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
)
key = base64.urlsafe_b64encode(kdf.derive(b_master_pwd))
fer = Fernet(key)

print("\n")
print("Welcome to the Password Manager App")

#while loop to keep asking user for a mode 
while True:
    print("\n")
    print("Please choose an option below")
    print("1. Add a new password.")
    print("2. View your passwords.")
    print("3. To quit.")
    mode = input("Mode : ")

    #if 3 is selected then break out the while loop and quit 
    if mode == '3':
        break
    
    #if 1 is selected then enter add() funtion
    if mode == '1':
        add()
    #if 2 is selected then enter view() function
    elif mode == '2':
        view()
    #if something else is entered reask the question
    else: 
        print("Invalid mode.")
        continue