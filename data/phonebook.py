def insert_phonebook():
    contact = {}
    while True:
        name = input("Name: ")
        if name =="":
            break
        number = input("Number: ")
        contact[name] = number
    return contact
def display_phonebook(contact):
    print("Contact List:-")
    for name,number in contact.items():
        print(str(name) + " -> " + str(number))

def lookup_phonebook(contact):
    while True:
        name = input("Enter you contact name: ")
        if name == "":
            break
        
        if name in contact:
                number = contact[name]
                print(str(name) + ' contact number is ' + str(number))
        else:
            print(str(name) + ' have no number')
        


def main():
    contact = insert_phonebook()
    display_phonebook(contact)
    lookup_phonebook(contact)

if __name__ == "__main__":
    main()