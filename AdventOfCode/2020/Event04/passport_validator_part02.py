"""
This program reads data of some passports from a file
and validates each field of each passport based on input criteria.
"""
from validations import validate_fields

data_file = "passports.txt"
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
allowed_missing_fields = ["cid"]


def parse_passports(passport_file):
    passports = []
    with open(passport_file, "r") as f:
        passport = {}
        while line := f.readline():
            fields = line.split()
            if fields:
                for field in fields:
                    key, value = field.split(":")
                    passport[key] = value
            else:  # empty line
                passports.append(passport)
                passport = {}
        passports.append(passport)  # handle the last entry from data file
    return passports


def validate_passports(passports, req_fields, allowed_fields):
    valid_count = 0
    for passport in passports:
        if set(req_fields).issubset(
            passport.keys()
        ):  # case A: where all fields are present
            if validate_fields(passport):
                valid_count += 1
        else:  # case B: where some keys are missing
            missing_filds = set(req_fields) - passport.keys()
            if missing_filds.issubset(
                allowed_fields
            ):  # case C: where only field 'cid' is missing
                if validate_fields(passport):
                    valid_count += 1
    return valid_count


input_passports = parse_passports(data_file)
print(
    f"Valid Passwords: {validate_passports(input_passports, required_fields, allowed_missing_fields)}"
)
