master_pwd = input("What is the master password? ")

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
            print("Account:", account, "| Password:", password)


#funtion to add a new password onto the manager
def add():
    name = input("Account Name: ")
    password = input("Password: ")
    
    #open a txt file in append mode to add to the end of the file, or create the file if it doesnt exist 
    with open("passwords.txt", 'a') as file:
        file.write(name+ "|" + password + "\n")

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
    else: 
        print("Invalid mode.")
        continue