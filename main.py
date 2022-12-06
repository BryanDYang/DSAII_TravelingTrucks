# Author:        Bryan Yang
# Student ID:    #001303738
# Major:         B.S. Computer Science. Started 10/1/22
# Email:         byang10@wgu.edu
# Date:          12/3/22

import re
from truck import *
import delivery

# Assignment of Initial Value for Data Object or Variable: Truck.
tk_1 = Truck(1)
tk_2 = Truck(2)
tk_3 = Truck(3)


# Initiate Delivery Application Program.
# Sets Delivery of Truck 1 & 2 based on the project assumptions.
# Truck 3 departs after the Truck 1 travel completion.
def run(time):

    tk_1.tk_departure_time = 480
    delivery.delivery(tk_1, time)

    tk_2.tk_departure_time = 545
    delivery.delivery(tk_2, time)

    tk_3.tk_departure_time = tk_1.travel
    delivery.delivery(tk_3, time)


# Package Status of User input times.
# Big-O Notation: O(n)
def pk_status(time):
    print('\n=================================================================\n\t\t\t\t\t '
          'Status of Packages at', time, '\n=================================================================')

    for i in delivery.delivered:
        i.lookup(time)


# Method for viewing delivery completed and print statement total miles traveled to terminal.
# Big-O Notation: O(n)
def lookup_all():
    print('\n=================================================================\n\t\t\t\t'
          'List of Completed Package Delivery'
          '\n=================================================================')

    for i in delivery.delivered:
        print('Package:', i.pk_id, '|', i.address, '|', i.deadline, '|', i.city, '|', i.state, '|', i.zip, '|',
              i.weight, '|', i.update_status)
    print('\n=================== Packages Delivered with Total Distance of', round(delivery.total_distance),
          'miles ======================')

    # print distance each truck traveled.
    print('Truck:', tk_1.tk_id, 'returned to the hub with', tk_1.total_cost, 'miles traveled.')
    print('Truck:', tk_2.tk_id, 'returned to the hub with', tk_2.total_cost, 'miles traveled.')
    print('Truck:', tk_3.tk_id, 'returned to the hub with', tk_3.total_cost, 'miles traveled.')


# Method for viewing each package after run.
# Big-O Notation: O(n)
def lookup_pk(op, pk_id, time):
    for i in delivery.delivered:
        if op == '1' and i.pk_id == int(pk_id):
            print('Package Address {}: {}'.format(pk_id, i.address))
        if op == '2' and i.pk_id == int(pk_id):
            print('Package City {}: {}'.format(pk_id, i.city))
        if op == '3' and i.pk_id == int(pk_id):
            print('Package State {}: {}'.format(pk_id, i.state))
        if op == '4' and i.pk_id == int(pk_id):
            print('Package Zip Code {}: {}'.format(pk_id, i.zip))
        if op == '5' and i.pk_id == int(pk_id):
            print('Package Deadline {}: {}'.format(pk_id, i.deadline))
        if op == '6' and i.pk_id == int(pk_id):
            print('Package Weight {}: {}'.format(pk_id, i.weight))
        if op == '7' and i.pk_id == int(pk_id):
            i.lookup(time)

    # Call menu with more options for user prior to exiting the program.
    menu(time)


# Menu to use lookup package with different options for the user.
# Big-O Notation: O(1)
def menu(time):
    print('\n===========================\n\t\t Menu \n===========================')
    select = input('1: Complete Delivery List\n'
                   '2: Search a Package\n'
                   '3: Exit Program\n: ')

    # Menu to remind user to select valid option between 1-3.
    while select not in ('1', '2', '3'):
        print('\n===========================\n\t\t Menu \n===========================')
        print('Select A Valid Option between 1-3')
        select = input('1: Complete Delivery List\n'
                       '2: Search a Package\n'
                       '3: Exit Program\n: ')

    # Lookup all when 1 is selected.
    if select == '1':
        lookup_all()
        print('\n===========================\n\t\t Menu \n===========================')
        print('Select A Valid Option between 1-3')


    # Display submenu when 2 is selected with more options for specific packages using the lookup package method.
    elif select == '2':
        print('\n=====================================\n\t\t Searching package at', time,
              '\n=====================================')
        op = input('Select one of the following Options:\n'
                   'Address [1]\n'
                   'City [2]\n'
                   'State [3]\n'
                   'Zip Code [4]\n'
                   'Deadline [5]\n'
                   'Weight [6]\n'
                   'Status [7]\n: ')
        id = input('Enter Package ID: ')

        lookup_pk(op, id, time)

    # Exit when 3 is selected.
    else:
        SystemExit


# Start of the package delivery program.
# User is prompted to select a time to run the delivery run.
# Delivery progress is viewed based on inputted time.
# After the time input, option is given to the user for delivery list with delivery times for all packages.
# Big-O: O(1)
def user_intf():
    print('===========================\n\t\t MAIN MENU \n===========================')
    print('Current Time: 8:00am')

    time = input('To start, select time after 8:00am in 24-Hour format, (i.e. "15:00" for 3:00pm): ')

    # Iterate loop until time selection matches 8:00am or later in 24-hour format.
    while not re.match("([1]{1}[0-9]|[0]?[8-9]|2[0-3]):[0-5][0-9]", time):
        time = input(
            'Select a time after 8:00am in a valid 24-Hour format to start the deliveries (i.e. "15:00" for 3:00PM): ')

    run(time)
    pk_status(time)
    menu(time)


# Call the interface function to start the program
user_intf()
