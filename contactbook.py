import os
contact = {"Name" : [],"Phone" : [],"Email" : [],"Address" : []}


def addContact():
    name = input("Enter a name : ")
    phonenumber = int(input("Enter a phone number : "))
    email = input("Enter a email : ")
    address = input("Enter a address : ")
    contact["Name"].append(name)    
    contact["Phone"].append(phonenumber)    
    contact["Email"].append(email)    
    contact["Address"].append(address)    

def deleteContact(num):
    del contact["Name"][num-1]
    del contact["Phone"][num-1]
    del contact["Email"][num-1]
    del contact["Address"][num-1]

def viewContact():
    for i in range(0,len(contact["Name"])):
        print(f"{i+1} - ContactInfo")
        print("Name : " ,contact["Name"][i])
        print("Phonenumber : " ,contact["Phone"][i])
        print("Email : " ,contact["Email"][i])
        print("Address : " ,contact["Address"][i])
        i += 1
        print("-"*30)

def searchContact(name):
    for i in range(0,len(contact["Name"])):
        if(contact["Name"][i] == name):
            print(f"{i+1} - ContactInfo")
            print("Name : " ,contact["Name"][i])
            print("Phonenumber : " ,contact["Phone"][i])
            print("Email : " ,contact["Email"][i])
            print("Address : " ,contact["Address"][i])
            break
        i += 1

def updateContact(num):
    name = input("Enter a new Name : ")
    phonenumber = int(input("Enter a new Phone Number : "))
    email = input("Enter a new email : ")
    address = input("Enter a new Address : ")

    contact["Name"][num-1] = name
    contact["Phone"][num-1] = phonenumber
    contact["Email"][num-1] = email
    contact["Address"][num-1] = address

    searchContact(contact["Name"][num-1])




while True:
    print("-"*30)
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. List Contact")
    print("6. Exit")
    print("-"*30)

    option = int(input("Enter a option from above : "))
    os.system('cls')

    if option == 1:
        print("Enter a values to add contact ")

        addContact()
        print("-"*30)

    if option == 2:
        viewContact()

        num = int(input("Enter a Sno. to remove: "))
        deleteContact(num)
        print("Delete sucessfully")
        print("-"*30)

    if option == 3:
        name = input("Enter a name to search : ")
        searchContact(name)    

    if option == 4:
        viewContact()
        num = int(input("Enter a Sno to update : "))
        updateContact(num)

    if option == 5:
        print("-"*30)
        viewContact()
        print("-"*30)


    if option == 6:
        break
    

