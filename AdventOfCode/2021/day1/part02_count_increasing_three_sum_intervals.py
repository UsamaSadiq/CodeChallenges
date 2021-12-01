

numbers_file = "numbers.txt"
numbers = open(numbers_file).readlines()

def sliding_window_sum(index, list):
    return list[index] + list[index-1] + list[index-2]

increasing_count = 0
with open(numbers_file, "r") as f:
    numbers_list = [int(number) for number in f.readlines()]
    for index, number in enumerate(numbers_list):
        if index>1 and sliding_window_sum(index, numbers_list) > sliding_window_sum(index-1, numbers_list):
            increasing_count += 1

print(increasing_count)
