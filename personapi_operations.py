import json
import requests

error_message = 'Unexpected error!! Try again. If issue persiste contact support.\n'


def add_person():
    print("\n::Add a new person::\n")
    first_name = input("Enter the persons First name:: ")
    last_name = input("Enter the persons Last name:: ")
    person_json = {'firstName': first_name, 'lastName': last_name}
    response = requests.put('http://localhost:8080/persons', json=person_json)
    if response.status_code == 201:
        print('\nPerson Successfully Added with ID:: {}\n'.format(
            response.json()["id"]))
    else:
        print(error_message)


def edit_person():
    print("\n::Edit a person::\n")
    person_id = input("Enter the persons ID:: ")
    first_name = input("Enter the persons First name:: ")
    last_name = input("Enter the persons Last name:: ")
    person_json = {'id': person_id,
                   'firstName': first_name, 'lastName': last_name}
    response = requests.post('http://localhost:8080/persons', json=person_json)
    if response.status_code == 202:
        print('\nPerson Successfully Updated!\n')
    else:
        print(error_message)


def delete_person():
    print("\n::Delete a person::\n")
    person_id = input("Enter the ID of the Person to Delete:: ")
    response = requests.delete('http://localhost:8080/persons/' + person_id)
    if response.status_code == 202:
        print('\nPerson Successfully Deleted!\n')
    else:
        print(error_message)


def add_address_to_person():
    print("\n::Add an address to a person::\n")
    person_id = input("Enter the persons ID:: ")
    street = input("Enter the Street:: ")
    city = input("Enter the City:: ")
    state = input("Enter the State:: ")
    postal_code = input("Enter the Postal Code:: ")
    address_json = [{'street': street,
                     'city': city,
                     'state': state,
                     'postalCode': postal_code}]
    response = requests.post(
        'http://localhost:8080/persons/'+person_id+"/addresses", json=address_json)
    if response.status_code == 202:
        print('\nAddress Successfully Added!\n')
    else:
        print(error_message)


def edit_address():
    print("\n::Update a address::\n")
    address_id = input("Enter the ID of the Address to update:: ")
    street = input("Enter the New Street:: ")
    city = input("Enter the New City:: ")
    state = input("Enter the New  State:: ")
    postal_code = input("Enter the New Postal Code:: ")
    address_json = {'id': address_id,
                    'street': street,
                    'city': city,
                    'state': state,
                    'postalCode': postal_code}
    response = requests.post(
        'http://localhost:8080/addresses', json=address_json)
    if response.status_code == 202:
        print('\nAddress Successfully Updated!\n')
    else:
        print(error_message)


def delete_address():
    print("\n::Delete a Address::\n")
    address_id = input("Enter the ID of the Address to Delete:: ")
    response = requests.delete('http://localhost:8080/addresses/' + address_id)
    if response.status_code == 202:
        print('\nAddress Successfully Deleted!\n')
    else:
        print(error_message)


def count_number_of_persons():
    print("\n::Counting all Persons::\n")
    response = requests.get('http://localhost:8080/persons/count')
    if response.status_code == 200:
        print('Toal Number of Persons:: ' + str(response.json()) + '\n')
    else:
        print(error_message)


def list_persons():
    print("\n::Listing all persons::\n")
    response = requests.get('http://localhost:8080/persons')
    if response.status_code == 200:
        print(str(response.json()) + '\n')
    else:
        print(error_message)
