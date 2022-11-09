#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Nov 2022
# This program adds two numbers

import random


def main():
    # this is a number guessing game
    loop_counter = 0
    answer = 1

    # input
    print("This program calculates factorials.")
    string_integer = input("Enter any integer: ")

    # process
    try:
        int_integer = int(string_integer)
        while loop_counter < int_integer:
            loop_counter = loop_counter + 1
            answer = answer * loop_counter
        print("The answer is {0}".format(answer))
    except ValueError:
        print("Invalid integer")
    finally:
        print("Thanks for playing")
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
