import personapi_options
import personapi_operations

operations = {
    1: personapi_operations.add_person,
    2: personapi_operations.edit_person,
    3: personapi_operations.delete_person,
    4: personapi_operations.add_address_to_person,
    5: personapi_operations.edit_address,
    6: personapi_operations.delete_address,
    7: personapi_operations.count_number_of_persons,
    8: personapi_operations.list_persons
}

selected_option = 0

def display_api_options():
    print('*********************************************************')
    print("\n::Please select an option NUMBER from the items below::\n")
    print('*********************************************************')
    personapi_options.display_options()
    print('\n*********************************************************')
    global selected_option
    selected_option = int(input("\nEnter an option:: "))
print('\n*********************************************************')
print("Hi! Welcome to the User API.")
display_api_options()


while True:
    if selected_option == 9:
        print("Bye!! See you later.")
        break
    elif selected_option == 1:
        operations[1]()
        display_api_options()
    elif selected_option == 2:
        operations[2]()
        display_api_options()
    elif selected_option == 3:
        operations[3]()
        display_api_options()
    elif selected_option == 4:
        operations[4]()
        display_api_options()
    elif selected_option == 5:
        operations[5]()
        display_api_options()
    elif selected_option == 6:
        operations[6]()
        display_api_options()
    elif selected_option == 7:
        operations[7]()
        display_api_options()
    elif selected_option == 8:
        operations[8]()
        display_api_options()
    else:
        print("!!!Invalid Input. Try Again!!!")
        display_api_options()

