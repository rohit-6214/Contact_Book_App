
contacts = {}


    
while True:
        print ("\nContact Book App")
        print ("1. Add new contact")
        print ("2. view contact")
        print ("3. update contact")
        print ("4. Delete Contact")
        print ("5. Search Contact")
        print ("6. Count Contact")
        print ("7. Exit")
        
        choice =input("\nEnter your choice: ")
        if choice == "1":
            name =input("Enter your name: ")
            if name in contacts:
                    print (f"Contact name '{name}' is already exist in contact book.")
            else: 
                    age = input("Enter your age: ")
                    email = input("Enter your E-mail: ")
                    mobile =input("Enter your Mob.no: ")
                    contacts[name] = {"age":int(age) , "email":email , "mobile":int(mobile) } 
                    print (f"\nContact {name} has been saved successfully.")
        
        
        elif choice == "2":
                name = input("Enter contact name to view: ")
                if name in contacts:
                        contact = contacts[name]
                        print("-your contact details-")
                        print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile Number: {contact['mobile']}")
                else:
                        print ("Contact not found") 
                        
                        
                        
        elif choice == "3":
            name = input("Enter your name that you want to update: ")
            if name in contacts:
                    age = input("Enter your update age: ")
                    email = input("Enter your update E-mail: ")
                    mobile =input("Enter your update Mob.no: ")
                    contacts[name] = {"age":int(age) , "email":email , "mobile":int(mobile) }
                    print (f"\nContact {name} has been updated successfully.")
            else:
                    print ("Contact not found")
                        
                        
        elif choice == "4":
            name = input("Enter your name: ")
            if name in contacts:
                del contacts[name]
                print (f"\nContact {name} has been deleted successfully.")
            else:
                print("Contact not found")
                    
                    
        elif choice =="5":
            search = input("Enter name you want to search: ")
            found = False
            for name,contact in contacts.items():
                    if name == search:
                        print("-your contact details-")
                        print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile Number: {contact['mobile']}")
                        found = True
                    if not found:
                        print ("Contact not found")
                    
    
        elif choice =="6":
            print("Total contacts are: ",len(contacts))
                          
                    
        elif choice =="7":
            print("app closed")
            exit()
                        
        
    
