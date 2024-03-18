# turn user input into command and arguments
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):

    # the only correct numbers in args is 2
    if not args or len(args) != 2:
        return "Please enter the name and phone. Format: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args

    # throwing an error if contact already exists
    if name in contacts:
        raise ValueError("Contact")
    contacts[name] = phone
    return "Contact updated successfully"

def show_contact(args, contacts):
    if args:
        name = args[0] # tne name is always the first argument
        return contacts[args[0]] if name in contacts else 'No such name'
    else:
        return "Please enter the name as agrument. Format: phone [name]"

def show_all(contacts):
    if not contacts:
        return "No contacts"
    all_contacts = []

    # preparing data for printing as single text
    for name in contacts:
        all_contacts.append(f'{name}: {contacts[name]}')
        
    return '\n'.join(all_contacts)
    

# main function of the bot
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    # infinite loop to handle users requests
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_contact(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command")


if __name__ == "__main__":
    main()