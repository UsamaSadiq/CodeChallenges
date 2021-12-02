

commands_file = "commands.txt"
numbers = open(commands_file).readlines()

x = 0
y = 0

with open(commands_file, "r") as f:
    commands_list = [command for command in f.readlines()]
    for command in commands_list:
        direction, value = command.split(' ')
        if direction == 'forward':
            x += int(value)
        elif direction == 'up':
            y -= int(value)
        elif direction =='down':
            y += int(value)
    
    final_position = x*y
    print(final_position)
