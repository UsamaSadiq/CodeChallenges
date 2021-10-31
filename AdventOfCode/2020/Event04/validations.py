import re


def validate_byr(value):
    if re.match("^[0-9]{4}", value):
        if 1920 <= int(value) <= 2002:
            return True
    return False


def validate_iyr(value):
    if re.match("^[0-9]{4}", value):
        if 2010 <= int(value) <= 2020:
            return True
    return False


def validate_eyr(value):
    if re.match("^[0-9]{4}", value):
        if 2020 <= int(value) <= 2030:
            return True
    return False


def validate_hgt(value):
    if re.match("^[0-9]+(cm|in)$", value):
        if "cm" in value:
            if 150 <= int(value.strip("cm")) <= 193:
                return True
        elif "in" in value:
            if 59 <= int(value.strip("in")) <= 76:
                return True
    return False


def validate_hcl(value):
    if re.match("^#([0-9]|[a-f]){6}", value):
        return True
    return False


def validate_ecl(value):
    if re.match("amb|blu|brn|gry|grn|hzl|oth", value):
        return True
    return False


def validate_pid(value):
    if re.match("^[0-9]{9}$", value):
        return True
    return False


def validate_fields(passport):
    if not validate_byr(passport["byr"]):
        return False
    if not validate_eyr(passport["eyr"]):
        return False
    if not validate_iyr(passport["iyr"]):
        return False
    if not validate_ecl(passport["ecl"]):
        return False
    if not validate_hcl(passport["hcl"]):
        return False
    if not validate_hgt(passport["hgt"]):
        return False
    if not validate_pid(passport["pid"]):
        return False
    return True
