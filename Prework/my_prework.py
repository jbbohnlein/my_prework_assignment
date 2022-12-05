#       QUESTION #1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    #function prints back the user_name that user inputs
    print("\nHello " + user_name + "!\n")

hello_name("USERNAME")



#       QUESTION #2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    #function prints odd numbers from 1-100; returns nothing
    for x in range(100):
        x = int(x)
        if x % 2 == 1:
            print(x)
        else:
            x = x + 1

first_odds()



#       QUESTION #3
# Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    #function returns the max number of a given list
    print("\nThe highest number in the list is", max(a_list))

a_list = [1, 4, 809, 6, 191, 3]
max_num_in_list(a_list)



#       QUESTION #4
#Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    # Function answers whether a year is a leap year or not
    # Leap years are divisible by 4, but not 100 unless also divisible by 400
    a_year = int(a_year)
    if a_year % 4 == 0:
        if a_year % 4 == 0 and a_year % 100 != 0:
            return True
        elif a_year % 100 == 0 and a_year % 400 == 0:
            return True
        elif a_year % 100 == 0 and a_year % 400 != 0:
           return False
    elif a_year % 4 != 0:
        return False

print(is_leap_year(1900))
print(is_leap_year(1901))
print(is_leap_year(1904))
print(is_leap_year(2000))



#       QUESTION #5

def is_consecutive(a_list):
    # Function determines if the numbers in a list are consecutive or not
    x = len(a_list) - 1
    for i in range(0, x):
        if int(a_list[i]) != int(a_list[i + 1]) - 1:
            return False

    return True

a_list = [2, 3, 4, 5, 6, 7]
b_list = [1, 2, 4, 5, 6]
print(is_consecutive(a_list))
print(is_consecutive(b_list))