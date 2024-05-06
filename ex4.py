def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid input data."
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Missing name or phone")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_contact(args, contacts):
    if len(args) != 1:
        raise IndexError("Invalid number of arguments")
    name = args[0]
    if name not in contacts:
        raise KeyError("Contact not found")
    return f"{name}: {contacts[name]}"

@input_error
def show_all_contacts(args, contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts available"


contacts = {}
while True:
    command = input("Enter a command: ").strip().lower()
    if command == "add":
        args = input("Enter name and phone: ").split()
        print(add_contact(args, contacts))
    elif command == "phone":
        args = input("Enter name: ").split()
        print(show_contact(args, contacts))
    elif command == "all":
        print(show_all_contacts([], contacts))
    elif command == "exit":
        break
