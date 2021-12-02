

commands_file = "commands.txt"
numbers = open(commands_file).readlines()

x = 0
y = 0
aim = 0

with open(commands_file, "r") as f:
    commands_list = [command for command in f.readlines()]
    for command in commands_list:
        direction, value = command.split(' ')
        if direction == 'forward':
            x += int(value)
            y += int(value)*aim
        elif direction == 'up':
            aim -= int(value)
        elif direction =='down':
            aim += int(value)
    
    final_position = x*y
    print(final_position)
