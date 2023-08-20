#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count >= 0:
        
        print(count)
        count = count - 1
            
        if count == 0:
            print("Happy New Year!")
            break
        
        
happy_new_year()
         
def square_integers(int_list):
    return [item ** 2 for item in int_list]

def fizzbuzz():
    # code goes here!
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
