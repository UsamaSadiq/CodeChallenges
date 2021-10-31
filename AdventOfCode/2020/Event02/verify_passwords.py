"""
Program to parse passwords.

This program reads a file of passwords and verifies each password
according to the mentioned criteria for each password
"""
import re

passwords_file = "passwords.txt"

# solution for part 1
valid_passwords_count = 0
invalid_passwords_count = 0
password_lines = open(passwords_file, "r")

for line in password_lines:
    policy, password = line.split(": ")
    count, required_letter = policy.split(" ")
    min_count, max_count = count.split("-")
    letter_count = list(password).count(required_letter)
    if letter_count in range(int(min_count), int(max_count) + 1):
        valid_passwords_count += 1
    else:
        invalid_passwords_count += 1
print(valid_passwords_count)

# solution for part2
valid_passwords_count = 0
invalid_passwords_count = 0
password_lines = open(passwords_file, "r")

for line in password_lines:
    policy, password = line.split(": ")
    positions, required_letter = policy.split(" ")
    first_position, second_position = positions.split("-")
    locations = [
        i + 1 for i in range(0, len(password)) if password[i] == required_letter
    ]
    if bool(int(first_position) in locations) ^ bool(int(second_position) in locations):
        valid_passwords_count += 1
    else:
        invalid_passwords_count += 1

print(valid_passwords_count)
