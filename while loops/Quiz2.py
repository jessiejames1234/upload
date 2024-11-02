name_list = []
def header_string(header):
    print("----------------------------------")
    print(header)
    print("----------------------------------")

def display_list():
    header_string("DISPLAY LIST")
    for list in name_list:
      print(str(name_list.index(list)) + " = "+ list)

def add_list():
    header_string("ADD LIST")
    add_list = input("Enter name to add: ")
    name_list.append(add_list)
    print(add_list , "DONE ADDED")

def update_list():
    display_list()
    header_string("UPDATE LIST")
    remove = int(input("Enter your number: "))
    add = input("Enter student name: ")
    name_list[remove] = add
    print("DONE UPDATED")

def delete_list():
    display_list()
    header_string("DELETE LIST")
    remove = int(input("Enter number to remove"))
    d_list = name_list.pop(remove)
    print(d_list, "DONE REMOVE")

def insert_list():
    display_list()
    header_string("INSERT LIST")
    number = int(input("number to insert: "))
    name = input("Enter the name to insert: ")
    name_list.insert(number, name)
    print(name, "INSERTED TO", number)

while True:
    print("\n1 = add list")
    print("2 = update list")
    print("3 = delete list")
    print("4 = display list")
    print("5 = insert list")
    print("6 = Exit program\n")

    enter_index = int(input("Enter your number: "))
    if enter_index == 1:
        add_list()
    elif enter_index == 2:
        update_list()
    elif enter_index == 3:
        delete_list()
    elif enter_index == 4:
        display_list()
    elif enter_index == 5:
        insert_list()
    elif enter_index == 6:
      break
print("Goodbye World!")