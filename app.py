# docstring- Emma Cox- Airplane database test
# imports
import sqlite3

# contents and variables
DATABASE = "fighters.db"


# functions
def print_all_aircraft():
    # print them nicely
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Print nicely (loop through all the results)
    print("Name                     Speed  Max_g Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<25}{fighter[2]:<7}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finishes
    db.close()


def print_all_aircraft_by_speed():
    # print by speed
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Print nicely (loop through all the results)
    print("Name                     Speed  Max_g Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<25}{fighter[2]:<7}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finishes
    db.close()


def print_all_aircraft_by_g():
    # print by max g
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY max_g DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Print nicely (loop through all the results)
    print("Name                     Speed  Max_g Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<25}{fighter[2]:<7}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finishes
    db.close()


def print_all_aircraft_by_climb():
    # print by climb rate
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY climb DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Print nicely (loop through all the results)
    print("Name                     Speed  Max_g Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<25}{fighter[2]:<7}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finishes
    db.close()


def print_all_aircraft_by_range():
    # print by range
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY range DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Print nicely (loop through all the results)
    print("Name                     Speed  Max_g Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<25}{fighter[2]:<7}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finishes
    db.close()


def print_all_aircraft_by_payload():
    # print by payload
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY payload DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Print nicely (loop through all the results)
    print("Name                     Speed  Max_g Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<25}{fighter[2]:<7}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finishes
    db.close()


# main code
while True:
    user_input = input(
"""
What would you like to do?
1. Print all aircraft
2. Print all aircraft by speed
3. Print all aircraft by max_g
4. Print all aircraft by climb 
5. Print all aircraft by range 
6. Print all aircraft by payload 
7. Exit
""")
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        print_all_aircraft_by_speed()
    elif user_input == "3":
        print_all_aircraft_by_g()
    elif user_input == "4":
        print_all_aircraft_by_climb()
    elif user_input == "5":
        print_all_aircraft_by_range()
    elif user_input == "6": 
        print_all_aircraft_by_payload()
    elif user_input == "7":
        break
    else:
        print("That was not an option\n")
