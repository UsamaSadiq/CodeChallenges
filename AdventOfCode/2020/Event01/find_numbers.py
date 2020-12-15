"""
This program reads all numbers from a given input file.
Finds numbers whose sum is SUM and returns the product of numbers.
"""
from itertools import permutations
from math import prod


numbers_file = 'numbers.txt'
numbers = open(numbers_file).readlines()
required_sum = 2020

# base logic
with open(numbers_file, 'r') as f:
    numbers_list = [int(number) for number in f.readlines()]
    numbers_found = False
    for first_number in numbers_list:
        if not numbers_found:
            for second_number in numbers_list:
                if not numbers_found:
                    for third_number in numbers_list:
                        if not numbers_found and first_number+second_number+third_number==required_sum:
                            print(f'{first_number}+{second_number}+{third_number}={required_sum}, '
                                f'{first_number}*{second_number}*{third_number}='
                                f'{first_number*second_number*third_number}')
                            numbers_found = True


# using libraries
with open(numbers_file, 'r') as f:
    numbers_list = [int(number) for number in f.readlines()]
    
    candidate_numbers = 3 # total numbers to be found
    for pair in permutations(numbers_list, candidate_numbers):
        if sum(pair)==required_sum:
            print(f'Pair: {pair}, Required Product = {prod(pair)}')
            break
