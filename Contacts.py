Contacts = [{'Name':'Esmail', 'Phone':'771777777'}]

def Add():
    Name = input("Enter name: ")
    Phone = input("Enter phone number: ")
    Contacts.append({'Name':Name, 'Phone':Phone})
    print('Contact added successfully')

def Update():
    Index = int(input("Enter index: "))
    if (Index) <= len(Contacts) and (Index) > 0:
        Name = input("Enter name: ")
        Phone = input("Enter phone number: ")
        Contacts[(Index-1)] = {'Name':Name, 'Phone':Phone}
        print('Contact updated successfully')
    else:
        print('Wrong index!')

def Delete():
    Index = int(input("Enter index: "))
    if (Index) <= len(Contacts) and (Index) > 0:
        del Contacts[(Index-1)]
        print('Contact deleted successfully')
    else:
        print('Wrong index!')

def View():
    if Contacts:
        print('___________________________________________________________')
        for index, contact in enumerate(Contacts):
            print(f"({index+1}):")
            print("Name: " + contact['Name'])
            print("Phone: " + contact['Phone'])
            print('___________________________________________________________')
    else:
        print("No Contacts!")

View()
Add()
View()
Update()
View()
Delete()
View()