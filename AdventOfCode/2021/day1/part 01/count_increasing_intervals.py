

numbers_file = "numbers.txt"
numbers = open(numbers_file).readlines()

increasing_count = 0
with open(numbers_file, "r") as f:
    numbers_list = [int(number) for number in f.readlines()]
    for index, number in enumerate(numbers_list):
        if index>0 and number>numbers_list[index-1]:
            increasing_count += 1

print(increasing_count)
