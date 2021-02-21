options = {
    1: "Add Person",
    2: "Edit Person",
    3: "Delete Person",
    4: "Add Address to person",
    5: "Edit Address",
    6: "Delete Address",
    7: "Count Number of Persons",
    8: "List Persons",
    9: "Exit"
}


def display_options():
    for option in options:
        print(str(option) + " :: " + options[option])
